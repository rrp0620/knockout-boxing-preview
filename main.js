/* Knockout scene system. Tune the look in CONFIG; each [data-scene] section "arrives as a hit". */
const CONFIG={shake:14,flashOpacity:.35,impactDuration:.55,revealStagger:.08,frames:145,seqPath:i=>`img/seq/f${String(i).padStart(3,'0')}.webp`,pinLength:'+=180%',hitFrame:38};
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(window.gsap&&!reduce){
 gsap.registerPlugin(ScrollTrigger);
 const flash=document.querySelector('.flash');
 
 // --- canvas image-sequence hero (scrubbed, reversible) ---
 const cv=document.getElementById('seq'),ctx=cv.getContext('2d'),imgs=[],st={f:0};let loaded=0;
 const draw=()=>{const im=imgs[Math.round(st.f)];if(!im||!im.complete||!im.naturalWidth)return;
  const W=cv.width=cv.clientWidth*devicePixelRatio,H=cv.height=cv.clientHeight*devicePixelRatio;
  ctx.fillStyle='#050505';ctx.fillRect(0,0,W,H);
  const r=im.naturalWidth/im.naturalHeight;let w,h,x,y;
  if(W/H>1){h=H;w=h*r;x=W-w-W*.06;y=0;}            // desktop: bag on right
  else{const s=Math.max(W/im.naturalWidth,H/im.naturalHeight);w=im.naturalWidth*s;h=im.naturalHeight*s;x=(W-w)*.6;y=(H-h)/2;}
  ctx.drawImage(im,x,y,w,h);
  if(W/H>1){const g=ctx.createLinearGradient(x,0,x+w*.08,0);g.addColorStop(0,'#050505');g.addColorStop(1,'#05050500');ctx.fillStyle=g;ctx.fillRect(x,0,w*.08,H);}};
 for(let i=0;i<CONFIG.frames;i++){const im=new Image();im.src=CONFIG.seqPath(i);im.onload=()=>{if(++loaded===1||i===0)draw();if(loaded===CONFIG.frames){document.body.classList.add('ready');draw();}};imgs.push(im);}
 addEventListener('resize',draw);
 const htl=gsap.timeline({scrollTrigger:{trigger:'.hero',start:'top top',end:CONFIG.pinLength,pin:true,scrub:.5,anticipatePin:1}});
 htl.to(st,{f:CONFIG.frames-1,ease:'none',duration:1,onUpdate:draw},0)
    .to('.hero-copy',{y:-60,opacity:0,duration:.25},.08)
    .to('.scroll-hint',{opacity:0,duration:.05},0)
    .call(()=>{const fl=document.querySelector('.flash');gsap.fromTo(fl,{opacity:.25},{opacity:0,duration:.3})},null,CONFIG.hitFrame/CONFIG.frames);
const impact=(sec)=>{
  gsap.fromTo(flash,{opacity:CONFIG.flashOpacity},{opacity:0,duration:.4});
  gsap.fromTo(sec,{x:CONFIG.shake},{x:0,duration:CONFIG.impactDuration,ease:'elastic.out(1,.3)'});
  const w=sec.querySelector('.hit-word');
  if(w)gsap.fromTo(w,{scale:1.6,opacity:0},{scale:1,opacity:1,duration:.5,ease:'power4.out'});
 };
 document.querySelectorAll('[data-scene]:not(.hero)').forEach(sec=>{
  gsap.from(sec,{clipPath:'inset(12% 6% 12% 6% round 24px)',ease:'none',scrollTrigger:{trigger:sec,start:'top bottom',end:'top 30%',scrub:true}});
  ScrollTrigger.create({trigger:sec,start:'top 55%',once:true,onEnter:()=>{
   impact(sec);
   gsap.from(sec.querySelectorAll('.reveal'),{y:60,opacity:0,rotation:()=>gsap.utils.random(-3,3),stagger:CONFIG.revealStagger,duration:.7,ease:'back.out(1.7)'});
  }});
  const w=sec.querySelector('.hit-word');
  if(w)gsap.to(w,{xPercent:-20,ease:'none',scrollTrigger:{trigger:sec,scrub:true}});
 });
}
