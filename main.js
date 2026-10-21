/* Knockout scene system. Tune the look in CONFIG; each [data-scene] section "arrives as a hit". */
const CONFIG={shake:14,flashOpacity:.35,impactDuration:.55,revealStagger:.08,frames:145,seqPath:i=>`img/seq/f${String(i).padStart(3,'0')}.webp`,pinLength:'+=180%',hitFrame:38};
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(window.gsap&&!reduce){
 gsap.registerPlugin(ScrollTrigger);
 const flash=document.querySelector('.flash'),mob=()=>innerWidth<800;
 const cv=document.getElementById('seq');
 if(cv){ // canvas image-sequence hero (scrubbed, reversible). Frames load after first paint to keep LCP light.
  const ctx=cv.getContext('2d'),imgs=[],st={f:0};let loaded=0;
  const draw=()=>{const im=imgs[Math.round(st.f)];if(!im||!im.complete||!im.naturalWidth)return;
   const W=cv.width=cv.clientWidth*devicePixelRatio,H=cv.height=cv.clientHeight*devicePixelRatio;
   ctx.fillStyle='#050505';ctx.fillRect(0,0,W,H);
   const r=im.naturalWidth/im.naturalHeight;let w,h,x,y;
   if(W/H>1){h=H;w=h*r;x=W-w-W*.06;y=0;}
   else{const s=Math.max(W/im.naturalWidth,H/im.naturalHeight);w=im.naturalWidth*s;h=im.naturalHeight*s;x=(W-w)*.15;y=(H-h)/2;}
   ctx.drawImage(im,x,y,w,h);
   if(W/H>1){const g=ctx.createLinearGradient(x,0,x+w*.08,0);g.addColorStop(0,'#050505');g.addColorStop(1,'#05050500');ctx.fillStyle=g;ctx.fillRect(x,0,w*.08,H);}};
  const load=()=>{for(let i=0;i<CONFIG.frames;i++){const im=new Image();im.decoding='async';im.src=CONFIG.seqPath(i);im.onload=()=>{if(++loaded===CONFIG.frames){document.body.classList.add('ready');draw();}};imgs.push(im);}};
  (window.requestIdleCallback||setTimeout)(load,{timeout:1200});
  addEventListener('resize',draw);
  gsap.timeline({scrollTrigger:{trigger:'.hero',start:'top top',end:CONFIG.pinLength,pin:true,scrub:.5,anticipatePin:1}})
   .to(st,{f:CONFIG.frames-1,ease:'none',duration:1,onUpdate:draw},0)
   .to('.hero-copy',{y:-60,opacity:0,duration:.25},.08)
   .to('.scroll-hint',{opacity:0,duration:.05},0)
   .call(()=>gsap.fromTo(flash,{opacity:.25},{opacity:0,duration:.3}),null,CONFIG.hitFrame/CONFIG.frames);
 }
 const impact=sec=>{
  gsap.fromTo(flash,{opacity:CONFIG.flashOpacity},{opacity:0,duration:.4});
  gsap.fromTo(sec,{x:mob()?CONFIG.shake/2:CONFIG.shake},{x:0,duration:CONFIG.impactDuration,ease:'elastic.out(1,.3)',clearProps:'transform'});
  const w=sec.querySelector('.hit-word');if(w)gsap.fromTo(w,{scale:1.6,opacity:0},{scale:1,opacity:1,duration:.5,ease:'power4.out'});
 };
 document.querySelectorAll('[data-scene]').forEach(sec=>{
  gsap.from(sec,{clipPath:'inset(12% 6% 12% 6% round 24px)',ease:'none',scrollTrigger:{trigger:sec,start:'top bottom',end:'top 30%',scrub:true}});
  ScrollTrigger.create({trigger:sec,start:'top 55%',once:true,onEnter:()=>{impact(sec);
   const m=mob();gsap.fromTo(sec.querySelectorAll('.reveal'),{y:m?30:60,opacity:0,rotation:()=>gsap.utils.random(-1,1)*(m?1:2.5)},{y:0,opacity:1,rotation:0,stagger:CONFIG.revealStagger,duration:.7,ease:'back.out(1.4)',clearProps:'transform,opacity'});}});
  const w=sec.querySelector('.hit-word');if(w)gsap.to(w,{xPercent:-20,ease:'none',scrollTrigger:{trigger:sec,scrub:true}});
 });
}
