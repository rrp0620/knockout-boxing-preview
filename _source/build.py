import json,html
OUT='/workspace/sites/knockout-boxing/'
BASE='https://rrp0620.github.io/knockout-boxing-preview/'
BW='https://bookwhen.com/knockoutboxing'
PTFORM='https://docs.google.com/forms/d/e/1FAIpQLScfvxdpHq0AM4tD8510DZvXHnU0EHVj2sc_S2oTith9ul8ZZg/viewform'
TEL='tel:+13022008714'
NAP={"@type":"PostalAddress","streetAddress":"1244 Capitol Trl","addressLocality":"Newark","addressRegion":"DE","postalCode":"19711","addressCountry":"US"}
HOURS=[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday"],"opens":"08:00","closes":"19:30"},
 {"@type":"OpeningHoursSpecification","dayOfWeek":"Saturday","opens":"09:00","closes":"12:30"},
 {"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"08:00","closes":"11:30"}]
BIZ={"@context":"https://schema.org","@type":["SportsActivityLocation","ExerciseGym"],"@id":BASE+"#gym","name":"Knockout Boxing & Fitness",
 "description":"USA Boxing-certified, family-owned boxing and fitness gym in Newark, DE offering cardio kickboxing, youth and adult skilled boxing, and private training.",
 "url":BASE,"telephone":"+1-302-200-8714","image":BASE+"img/hero.webp","logo":BASE+"img/icon-512.png","address":NAP,
 "geo":{"@type":"GeoCoordinates","latitude":39.69671,"longitude":-75.71032},"openingHoursSpecification":HOURS,"foundingDate":"2017",
 "areaServed":"Newark, DE","knowsLanguage":["en","es"],"sameAs":["https://www.facebook.com/Knockout007","https://www.instagram.com/knockoutboxing","https://bookwhen.com/knockoutboxing"],
 "hasMap":"https://maps.google.com/?q=1244+Capitol+Trl+Newark+DE+19711"}
NAV=[('index.html','Home'),('programs.html','Programs'),('schedule.html','Schedule'),('memberships.html','Memberships'),('about.html','About'),('faq.html','FAQs'),('contact.html','Contact')]

def page(fn,title,desc,body,crumb=None,extra_ld=(),hero=False):
  canon=BASE+('' if fn=='index.html' else fn)
  ld=[BIZ]+list(extra_ld)
  if crumb: ld.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
     {"@type":"ListItem","position":1,"name":"Home","item":BASE},{"@type":"ListItem","position":2,"name":crumb,"item":canon}]})
  nav=''.join(f'<a href="{u}"{" aria-current=\"page\"" if u==fn else ""}>{t}</a>' for u,t in NAV[1:])
  pre='<link rel="preload" as="image" href="img/seq/poster.webp" fetchpriority="high">' if hero else ''
  gsap='<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script><script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script><script src="main.js" defer></script>'
  bc=f'<p class="crumbs"><a href="index.html">Home</a> / <span>{crumb}</span></p>' if crumb else ''
  h=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{canon}">
<meta name="theme-color" content="#0b0b0c"><meta name="robots" content="index,follow">
<meta property="og:type" content="website"><meta property="og:site_name" content="Knockout Boxing &amp; Fitness"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{BASE}img/hero.webp"><meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{desc}"><meta name="twitter:image" content="{BASE}img/hero.webp">
<link rel="icon" type="image/png" sizes="32x32" href="img/icon-32.png"><link rel="apple-touch-icon" href="img/icon-180.png"><link rel="manifest" href="site.webmanifest">
<link rel="preload" href="fonts/graduate-400.woff2" as="font" type="font/woff2" crossorigin><link rel="preload" href="fonts/inter-400.woff2" as="font" type="font/woff2" crossorigin>{pre}
<link rel="stylesheet" href="style.css">
{''.join('<script type="application/ld+json">'+json.dumps(x)+'</script>' for x in ld)}
</head><body>
<a class="skip" href="#main">Skip to content</a>
<header class="nav"><a href="index.html" class="brand"><img src="img/logo.webp" alt="Knockout Boxing &amp; Fitness logo" width="44" height="44"><span>KNOCKOUT</span></a>
<nav aria-label="Main">{nav}</nav><a class="btn sm" href="{BW}" target="_blank" rel="noopener">Book</a></header>
<div class="flash" aria-hidden="true"></div>
<main id="main">{'' if hero else f'<section class="subhero"><div class="wrap">{bc}'}{body}</main>
<footer><nav class="foot-links" aria-label="Footer">{''.join(f'<a href="{u}">{t}</a>' for u,t in NAV)}<a href="{BW}" target="_blank" rel="noopener">Book on Bookwhen</a><a href="https://www.facebook.com/Knockout007" target="_blank" rel="noopener">Facebook</a><a href="https://www.instagram.com/knockoutboxing" target="_blank" rel="noopener">Instagram</a></nav>
<p>Knockout Boxing &amp; Fitness · 1244 Capitol Trl, Newark, DE 19711 · <a href="{TEL}">(302) 200-8714</a></p><p>Spec concept by WebSage</p></footer>
<div class="sticky-bar"><a class="sticky-call" href="{BW}" target="_blank" rel="noopener">Book a class</a><a class="sticky-tel" href="{TEL}" aria-label="Call (302) 200-8714">Call</a></div>
{gsap}</body></html>'''
  open(OUT+fn,'w').write(h)

def sec(id,word,inner,cls='scene'):
  return f'<section class="{cls}" id="{id}" data-scene><span class="hit-word" aria-hidden="true">{word}</span><div class="wrap">{inner}</div></section>'
def ul(items): return '<ul>'+''.join(f'<li>{i}</li>' for i in items)+'</ul>'

# ---------- schedule (from Bookwhen, week of Oct 26 – Nov 1, 2026) ----------
SCHED=[('Monday',[('9:00 am','Cardio Boxing/Kickboxing'),('9:00 am','Teen and Adult Skilled Boxing'),('10:00 am','Private Home School Boxing and Conditioning'),('4:30 pm','Cardio Boxing/Kickboxing'),('5:30 pm','Cardio Boxing/Kickboxing (2 classes)'),('5:30 pm','Kids Skilled Boxing 5yrs-12yrs old'),('6:30 pm','Cardio Boxing/Kickboxing'),('6:30 pm','Teen and Adult Skilled Boxing')]),
('Tuesday',[('10:30 am','Cardio Boxing/Kickboxing'),('4:30 pm','Cardio Boxing/Kickboxing'),('5:30 pm','Cardio Boxing/Kickboxing')]),
('Wednesday',[('9:00 am','Cardio Boxing/Kickboxing'),('9:00 am','Teen and Adult Skilled Boxing'),('4:30 pm','Cardio Boxing/Kickboxing'),('5:30 pm','Cardio Boxing/Kickboxing (2 classes)'),('5:30 pm','Kids Skilled Boxing 5yrs-12yrs old'),('6:30 pm','Cardio Boxing/Kickboxing'),('6:30 pm','Teen and Adult Skilled Boxing')]),
('Thursday',[('10:30 am','Cardio Boxing/Kickboxing'),('4:30 pm','Cardio Boxing/Kickboxing'),('5:30 pm','Cardio Boxing/Kickboxing (2 classes)'),('6:30 pm','Cardio Boxing/Kickboxing'),('6:30 pm','Teen and Adult Skilled Boxing')]),
('Friday',[('9:00 am','Cardio Boxing/Kickboxing'),('9:00 am','Teen and Adult Skilled Boxing'),('4:30 pm','Cardio Boxing/Kickboxing'),('5:30 pm','Cardio Boxing/Kickboxing'),('5:30 pm','Kids Skilled Boxing 5yrs-12yrs old')]),
('Saturday',[('9:00 am','Cardio Boxing/Kickboxing'),('9:00 am','Teen and Adult Skilled Boxing'),('10:30 am','Kids Skilled Boxing 5yrs-12yrs old')]),
('Sunday',[('9:00 am','Cardio Boxing/Kickboxing'),('9:30 am','Teen and Adult Skilled Boxing')])]
sched_html='<div class="sched">'+''.join(f'<div class="day card reveal"><h2 class="h3">{d}</h2><ul>'+''.join(f'<li><span>{t}</span>{c}</li>' for t,c in cls)+'</ul></div>' for d,cls in SCHED)+'</div>'
SRC=f'<p class="src">Schedule from Knockout\'s <a href="{BW}" target="_blank" rel="noopener">Bookwhen booking page</a> (week of Oct 26, 2026). Times can change, so check Bookwhen for the live schedule.</p>'
BOOKCTA=f'<div class="ctas"><a class="btn" href="{BW}" target="_blank" rel="noopener">Book a class</a><a class="btn ghost" href="{TEL}">Call (302) 200-8714</a></div>'

# ---------- HOME ----------
home=f'''<section class="hero" id="top">
 <canvas id="seq" aria-hidden="true"></canvas>
 <img class="hero-poster" src="img/seq/poster.webp" alt="" aria-hidden="true" width="600" height="800" fetchpriority="high">
 <div class="hero-shade"></div>
 <div class="hero-copy">
  <p class="kicker">Newark, DE · USA Boxing-certified · Since 2017</p>
  <h1><span class="line">Boxing &amp; Fitness Gym</span><span class="line red">in Newark, DE</span></h1>
  <p class="lede">Cardio kickboxing, youth and adult skilled boxing, and private training. Open 7 days a week. No experience needed.</p>
  {BOOKCTA}
 </div>
 <p class="scroll-hint" aria-hidden="true">Scroll to throw the first punch ↓</p>
</section>
'''+sec('about','JAB',f'''<div class="split"><div><h2 class="reveal">Family-owned. <span class="red">Built to train.</span></h2>
 <p class="reveal">Knockout Boxing &amp; Fitness is the premier destination for those seeking to transform their bodies and minds through the art of boxing. We're a USA Boxing-certified facility as well as a local, family-owned business that has helped countless individuals get in shape since 2017.</p>
 <ul class="chips reveal"><li>Open 7 days a week</li><li>Flexible scheduling</li><li>Family plans</li><li>Yearly, monthly &amp; drop-in</li><li>Se habla español</li><li>20+ years of experience</li></ul>
 <p class="reveal"><a class="link" href="about.html">Meet the coaches →</a></p></div>
 <img class="reveal photo" src="img/home1.webp" alt="Cardio kickboxing class working the heavy bags at Knockout Boxing in Newark, DE" width="570" height="428" loading="lazy"></div>''')+\
sec('programs','CROSS',f'''<h2 class="reveal">Programs</h2><div class="cards">
 <a class="card reveal" href="programs.html#cardio-kickboxing"><span class="num">01</span><h3>Cardio Kickboxing</h3><p>45-55 minute group classes, seven days a week. Burn 500-1,000 calories. No experience needed.</p></a>
 <a class="card reveal" href="programs.html#youth-boxing"><span class="num">02</span><h3>Youth Skilled Boxing</h3><p>Ages 5 to 12. Fundamentals, footwork, pad and bag work, and self-defense skills.</p></a>
 <a class="card reveal" href="programs.html#adult-boxing"><span class="num">03</span><h3>Adult Skilled Boxing</h3><p>Beginner to advanced, optional live sparring, and an active amateur team.</p></a>
 <a class="card reveal" href="programs.html#private-training"><span class="num">04</span><h3>Private Training</h3><p>30- or 60-minute one-on-one sessions, in person or online.</p></a>
 </div><p class="reveal"><a class="link" href="schedule.html">See the weekly class schedule →</a></p>''')+\
sec('discounts','HOOK',f'''<h2 class="reveal">Discounts for those <span class="red">who serve</span></h2>
 <div class="cards four"><div class="card reveal"><h3>Military</h3><p>All active and veteran U.S. military members.</p></div><div class="card reveal"><h3>First Responders</h3><p>Local first responders.</p></div><div class="card reveal"><h3>Nurses &amp; Health Care</h3><p>Local nurses and health care professionals.</p></div><div class="card reveal"><h3>Teachers &amp; Students</h3><p>Local teachers and college students.</p></div></div>
 <p class="reveal">Contact us for details: <a class="link" href="{TEL}">(302) 200-8714</a> · <a class="link" href="memberships.html">Membership options →</a></p>''')+\
sec('gym','UPPERCUT','''<h2 class="reveal">Our Facility</h2><div class="gallery">
 <img class="reveal" src="img/g1.webp" alt="Rows of heavy bags on the training floor at Knockout Boxing &amp; Fitness" width="1000" height="667" loading="lazy">
 <img class="reveal" src="img/g2.webp" alt="Two boxers in headgear sparring in the ring" width="1000" height="903" loading="lazy">
 <img class="reveal" src="img/g3.webp" alt="Coach holding focus mitts for a young boxer" width="1000" height="667" loading="lazy">
 <img class="reveal" src="img/g4.webp" alt="Cardio kickboxing class on the heavy bags" width="1000" height="667" loading="lazy">
 <img class="reveal" src="img/g5.webp" alt="Coach and boxer drilling with pads beside the ring" width="1000" height="667" loading="lazy">
 <img class="reveal" src="img/g6.webp" alt="Young boxer training on the heavy bag" width="1000" height="667" loading="lazy"></div>
 <p class="note">[PLACEHOLDER – add real Google reviews with the owner's permission]</p>''')+\
sec('visit','K.O.',f'''<div class="split"><div><h2 class="reveal">Step in <span class="red">the ring.</span></h2><p class="reveal">Book a class online or call with questions.</p>
 <a class="btn big reveal" href="{TEL}">(302) 200-8714</a>
 <address class="reveal">1244 Capitol Trl<br>Newark, DE 19711</address>
 <a class="reveal link" href="contact.html">Directions &amp; map →</a></div>
 <table class="hours reveal"><caption>Hours</caption><tr><th scope="row">Mon–Fri</th><td>8:00 am – 7:30 pm</td></tr><tr><th scope="row">Saturday</th><td>9:00 am – 12:30 pm</td></tr><tr><th scope="row">Sunday</th><td>8:00 am – 11:30 am</td></tr></table></div>''','scene ko')
page('index.html','Boxing Gym in Newark, DE | Knockout Boxing & Fitness','USA Boxing-certified boxing & kickboxing gym in Newark, DE. Cardio kickboxing, youth & adult boxing, private training. Open 7 days. Book a class or call (302) 200-8714.',home,hero=True)

# ---------- PROGRAMS ----------
svc=lambda n,d:{"@context":"https://schema.org","@type":"Service","name":n,"description":d,"provider":{"@id":BASE+"#gym"},"areaServed":"Newark, DE"}
WHY=ul(['Supportive staff and experienced trainers','Clean, comfortable atmosphere','Flexible scheduling options','Competitive pricing with flexible payment plans','USA Boxing-certified facility','Open seven days a week','English and Spanish spoken','Established in 2017 with over 20 years of experience','Locally and family-owned business','Discounts and family plans available'])
prog=f'''<h1>Boxing &amp; Kickboxing Programs in Newark, DE</h1><p class="lede">Cardio kickboxing, youth skilled boxing, adult skilled boxing and private training at Knockout Boxing &amp; Fitness.</p>{BOOKCTA}</div></section>
<section class="block" id="cardio-kickboxing"><div class="wrap prose"><h2>Cardio Kickboxing Group Classes</h2>
<p>Experience the ultimate fitness challenge with our cardio kickboxing group classes at Knockout Boxing &amp; Fitness. Our 45-55 minute sessions are meticulously designed to help you burn between 500-1,000 calories, combining strength training, toning exercises, and intense cardio for maximum fat loss. Whether you're a seasoned athlete or new to fitness, our classes cater to all skill levels.</p>
<p>No prior boxing or kickboxing experience is needed and our expert trainers guide you through every movement. These classes include:</p>{ul(['10-minute warm-up','Four-minute rounds on heavy bags','New combinations every 1-2 minutes','Active rest intervals','Final circuit plus core work'])}
<p>Classes are offered seven days a week, with drop-ins, monthly memberships, and discounted annual plans available. Gloves and wraps are included with enrollment.</p>
<h3>Benefits of Cardio Kickboxing</h3>{ul(['Boost cardiovascular endurance','Enhance full-body strength','Improve coordination and balance','Increase flexibility and agility','Burn calories efficiently','Reduce stress and improve mental focus','Build self-confidence through skill development'])}
<h3>What to bring</h3><p>From the Bookwhen class listing: "Please wear fitness attire and bring a water bottle with you to class." We recommend you show up to class 15 minutes early, so you have enough time to stretch, put on your equipment and sign our waiver.</p></div></section>
<section class="block" id="youth-boxing"><div class="wrap prose"><h2>Youth Skilled Boxing (Ages 5–12)</h2>
<p>At Knockout Boxing &amp; Fitness, we're passionate about nurturing the next generation of boxers. Our youth skilled boxing program is tailored for children aged 5 to 12, welcoming both beginners and those with prior experience. We've designed this program to introduce kids to the exciting world of boxing while fostering personal growth, discipline, and confidence.</p>
<p>Our comprehensive program covers:</p>{ul(['Boxing fundamentals','Footwork techniques','Pad and bag work','Optional ring time','Offensive strategies','Defensive maneuvers','Self-defense skills'])}
<h3>Why Youth Boxing?</h3>{ul(['Builds confidence and self-esteem','Teaches discipline and respect','Improves physical fitness and coordination','Provides a positive outlet for energy','Develops focus and concentration','Offers an alternative to traditional team sports','Instills valuable self-defense skills'])}
<p>Our patient, experienced coaches create a supportive environment where your child can thrive. Classes are held four days a week, with month-to-month or annual membership plans. We provide all the necessary equipment, including gloves, wraps, and a mouthpiece.</p></div></section>
<section class="block" id="adult-boxing"><div class="wrap prose"><h2>Adult Skilled Boxing Classes</h2>
<p>Elevate your boxing skills with our comprehensive adult skilled boxing program. Whether you're a beginner looking to learn the ropes or an experienced boxer aiming to refine your technique, our program caters to all skill levels. We offer a progressive curriculum that starts with fundamental techniques and advances to complex strategies.</p>
<p>Our program includes:</p>{ul(['Offensive and defensive tactics','Intense conditioning','Optional live sparring','Fundamentals for beginners','Advanced techniques for experienced boxers','Instruction from national champions and professional contenders','Competitive opportunities','Path to professional boxing'])}
<p>For those interested in competing, Knockout Boxing &amp; Fitness hosts local shows twice a year and supports an active amateur team. Options include month-to-month or annual memberships, with no contract required. We provide all the necessary equipment, including gloves, wraps, and a mouthpiece.</p>
<h3>Benefits of Adult Skilled Boxing</h3>{ul(['Comprehensive physical workout','Stress relief','Self-defense skills','Improved coordination and reflexes','Mental toughness and discipline','Opportunity for competition','Supportive community'])}</div></section>
<section class="block" id="private-training"><div class="wrap prose"><h2>Private Boxing &amp; Fitness Training</h2>
<p>We offer private training programs tailored to your individual goals. Whether you're aiming for weight loss, muscle building, toning, conditioning, or honing your boxing skills, our experienced trainers are here to guide you. Our boxing and fitness program includes:</p>
{ul(['30- or 60-minute training sessions','Flexible scheduling options','In-person and online training (structured four-week remote training blocks available)','Access to cardio and skilled boxing classes','Tailored programs for weight loss, muscle building, and boxing skills'])}
<p class="price">From $199/month</p><p>Pricing starts at just $199/month for 30-minute sessions or $260/month for 60-minute sessions. Trial sessions are also available. As a private training client, you'll also gain access to our cardio and skilled boxing classes at no extra cost.</p>
<div class="ctas"><a class="btn" href="{PTFORM}" target="_blank" rel="noopener">Private Training Interest Form</a><a class="btn ghost" href="{TEL}">Call (302) 200-8714</a></div></div></section>
<section class="block"><div class="wrap prose"><h2>Why Choose Knockout Boxing &amp; Fitness</h2>{WHY}<p><a class="link" href="schedule.html">Class schedule →</a> · <a class="link" href="memberships.html">Memberships →</a> · <a class="link" href="faq.html">FAQs →</a></p></div></section>'''
page('programs.html','Kickboxing & Boxing Classes in Newark, DE | Knockout Boxing','Cardio kickboxing, youth boxing (ages 5-12), adult skilled boxing and private training in Newark, DE. All levels welcome. Book a class at Knockout Boxing & Fitness.',prog,'Programs',
 [svc('Cardio Kickboxing Group Classes','45-55 minute cardio kickboxing group classes, seven days a week, all skill levels.'),svc('Youth Skilled Boxing','Boxing program for children aged 5 to 12.'),svc('Adult Skilled Boxing','Progressive skilled boxing curriculum for adults, beginner to advanced.'),
  {**svc('Private Boxing & Fitness Training','30- or 60-minute private training sessions, in person or online.'),"offers":[{"@type":"Offer","name":"30-minute sessions","price":"199","priceCurrency":"USD","description":"Starting price per month"},{"@type":"Offer","name":"60-minute sessions","price":"260","priceCurrency":"USD","description":"Starting price per month"}]}])

# ---------- SCHEDULE ----------
sch=f'''<h1>Boxing &amp; Kickboxing Class Schedule – Newark, DE</h1><p class="lede">Cardio Boxing/Kickboxing, Kids Skilled Boxing and Teen and Adult Skilled Boxing classes, seven days a week.</p>{BOOKCTA}</div></section>
<section class="block"><div class="wrap">{sched_html}{SRC}
<div class="prose"><h2>Drop-in class prices</h2><p>On Bookwhen, single classes are listed at <strong>$25.00</strong> each for Cardio Boxing/Kickboxing, Kids Boxing and Teen/Adult Boxing. A 2.9% + $0.30 booking fee applies to bookings with a cost. Bookwhen refund policy: "No refunds upon payment".</p>
<h3>Before your first class</h3><p>"We recommend you show up to class 15 minutes early, so you have enough time to stretch and put on your equipment and sign our waiver." Please wear fitness attire and bring a water bottle. For skilled boxing: fitness attire and shoes required. For kids: all equipment needed for class will be provided at the gym.</p>
<p>Private Home School Boxing and Conditioning runs Mondays at 10:00 am. <span class="note">[PLACEHOLDER – description not listed]</span></p></div></div></section>'''
page('schedule.html','Class Schedule | Boxing & Kickboxing Newark, DE | Knockout','Weekly cardio kickboxing, kids boxing and teen & adult boxing class times at Knockout Boxing & Fitness in Newark, DE. Drop-in classes $25. Book online.',sch,'Schedule')

# ---------- MEMBERSHIPS ----------
mem=f'''<h1>Membership Options &amp; Discounts</h1><p class="lede">Sign up for one of our membership options available at Knockout Boxing &amp; Fitness. Give us a call if you have any questions. Family plans are also available!</p>{BOOKCTA}</div></section>
<section class="block"><div class="wrap"><div class="cards">
<div class="card"><h2 class="h3">Cardio Boxing/Kickboxing</h2>{ul(['Classes 7 days a week, no experience needed','Monthly, no-contract, and package memberships available','Boxing-based','HIT-style training','Engaging workouts','Boxing atmosphere','The most effective way to burn body fat and tone'])}<a class="link" href="{BW}" target="_blank" rel="noopener">Schedule your trial →</a></div>
<div class="card"><h2 class="h3">Private Training</h2>{ul(['Flexible membership options available','30-minute and 60-minute sessions available','One-on-one training with a personal trainer','Create your own schedule (we are open 7 days a week)','Training is focused on your private boxing and fitness needs'])}<p class="price">From $199/mo</p><p>$199/month for 30-minute sessions or $260/month for 60-minute sessions.</p><a class="link" href="{PTFORM}" target="_blank" rel="noopener">Private Training Interest Form →</a></div>
<div class="card"><h2 class="h3">Kids, teen, and adult boxing</h2>{ul(['Youth program (5-12) and adult classes available','Classes focused around the fundamentals of boxing','Real ring time and sparring'])}<a class="link" href="programs.html#youth-boxing">Learn more →</a></div>
<div class="card"><h2 class="h3">Drop-in classes</h2><p>Single classes are $25.00 on Bookwhen (plus a 2.9% + $0.30 booking fee).</p><p class="note">[PLACEHOLDER – monthly and annual membership prices not published]</p></div>
</div></div></section>
<section class="block" id="discounts"><div class="wrap"><h2>Discounts</h2><div class="cards four">
<div class="card"><h3>Military Discounts</h3><p>All active and veteran U.S. military members get a discount on our fitness and boxing classes.</p></div>
<div class="card"><h3>First Responder Discounts</h3><p>Local first responders get a discount on our fitness and boxing classes.</p></div>
<div class="card"><h3>Nurses &amp; Health Care Professionals</h3><p>Local nurses and health care professionals get a discount on our fitness and boxing classes.</p></div>
<div class="card"><h3>Teachers &amp; College Students</h3><p>Local teachers and college students get a discount on our fitness and boxing classes.</p></div></div>
<p>Contact us for details: <a class="link" href="{TEL}">(302) 200-8714</a></p></div></section>'''
page('memberships.html','Boxing Gym Memberships & Discounts | Newark, DE | Knockout','Monthly, annual and drop-in boxing and kickboxing memberships in Newark, DE. Private training from $199/month. Military, first responder, nurse, teacher and student discounts.',mem,'Memberships')

# ---------- ABOUT ----------
ab=f'''<h1>About Knockout Boxing &amp; Fitness</h1><p class="lede">A USA Boxing-certified, locally and family-owned boxing gym in Newark, DE.</p></div></section>
<section class="block"><div class="wrap split"><div class="prose"><h2>Who We Are</h2>
<p>We utilize boxing and kickboxing style training to deliver to the client what other fitness establishments cannot. We know getting in shape and staying healthy can be challenging, so we offer a variety of programs and classes to fit every personality. Regardless of where you are in your fitness journey, we'll have something just right for you. Whether your goals include getting in shape, training for professional boxing, or anything in between, Knockout Boxing &amp; Fitness is the place to be! Our classes include:</p>
{ul(['Cardio kickboxing','Youth boxing','Collegiate and sport conditioning','Private training','Adult skilled boxing'])}
<h3>Why Knockout Boxing &amp; Fitness?</h3><p>There are many gyms to choose from, but none do it quite like us! From our enthusiastic trainers, to the upscale facility and gym equipment, to the dedication to our clientele, we strive to make sure your experience at Knockout Boxing &amp; Fitness is second to none!</p>
{ul(['Exciting programs with experienced trainers and coaches','Flexibility for all types of schedules','Competitive pricing with flexible payment options','Gym is cleaned and sanitized multiple times daily','Military, police, nurse, fire, and college student discounts'])}</div>
<img class="photo" src="img/g5.webp" alt="Coach working pads with a boxer at Knockout Boxing in Newark" width="1000" height="667" loading="lazy"></div></section>
<section class="block" id="coaches"><div class="wrap"><h2>Our Coaches</h2><div class="cards four">
<div class="card"><h3>Coach Jon</h3><p>21 Years of Experience</p></div><div class="card"><h3>Coach Brody</h3><p>13 Years of Experience</p></div><div class="card"><h3>Coach Cameron</h3><p>12 Years of Experience</p></div></div>
<p class="note">[PLACEHOLDER – coach photos and full bios]</p></div></section>'''
page('about.html','About Us & Coaches | Knockout Boxing & Fitness, Newark DE','Family-owned, USA Boxing-certified boxing gym in Newark, DE since 2017. Meet Coach Jon, Coach Brody and Coach Cameron. Se habla español.',ab,'About')

# ---------- FAQ ----------
FAQ=[('Do I need prior boxing experience to join a class?','Prior experience is not required. Our classes are designed to accommodate individuals of all skill levels, including beginners. Each session is structured to be accessible and beneficial for participants with varying degrees of fitness and boxing knowledge.'),
('Can I try a class before committing to a membership?','We offer the option to book a single drop-in class. This allows prospective members to experience our gym environment and training style before making a decision about membership.'),
('What membership options are available?','We provide several membership options: annual memberships, month-to-month plans, and single class drop-in options.'),
('Are your classes suitable for kids?','Yes! We offer youth boxing programs specifically designed for children aged 5 and above. These classes focus on teaching boxing fundamentals and improving fitness in a safe, enjoyable environment tailored for younger participants.'),
('Can I participate in amateur/professional boxing?','We support amateur and professional boxing aspirations. Our gym hosts local shows twice annually and participates in regional tri-state competitions with our amateur team. For those interested in professional boxing, we provide comprehensive training and support to facilitate this transition, including an intensified training regimen and higher performance expectations.'),
('Why cardio kickboxing?','Our cardio kickboxing program offers a comprehensive fitness experience, combining strength training, muscle toning, and high-intensity cardio. Participants can expect to burn between 500-800 calories per session for women and 800-1,000 for men.'),
('What should I bring to class?','Please wear fitness attire and bring a water bottle. We recommend you show up to class 15 minutes early, so you have enough time to stretch, put on your equipment and sign our waiver.')]
fq='<h1>Boxing &amp; Kickboxing FAQs</h1><p class="lede">Answers to common questions about classes at Knockout Boxing &amp; Fitness in Newark, DE.</p></div></section><section class="block"><div class="wrap prose">'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in FAQ)+f'<p>Still have a question? Call <a class="link" href="{TEL}">(302) 200-8714</a>.</p></div></section>'
page('faq.html','FAQs | Boxing Classes in Newark, DE | Knockout Boxing & Fitness','Do I need experience? Are classes good for kids? Can I try a drop-in class? Answers about boxing and kickboxing classes at Knockout Boxing & Fitness, Newark DE.',fq,'FAQs',
 [{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}])

# ---------- CONTACT ----------
ct=f'''<h1>Contact &amp; Directions – Knockout Boxing, Newark DE</h1><p class="lede">Call to sign up, or book a class online.</p>{BOOKCTA}</div></section>
<section class="block"><div class="wrap split"><div><h2>Visit us</h2><address>Knockout Boxing &amp; Fitness<br>1244 Capitol Trl<br>Newark, DE 19711</address><p>Mailing address: 1248 Capitol Trl, Newark, DE 19711</p>
<p><a class="btn big" href="{TEL}">(302) 200-8714</a></p>
<p><a class="link" href="https://maps.google.com/?q=1244+Capitol+Trl+Newark+DE+19711" target="_blank" rel="noopener">Open in Google Maps →</a></p>
<p>Follow us: <a class="link" href="https://www.facebook.com/Knockout007" target="_blank" rel="noopener">Facebook</a> · <a class="link" href="https://www.instagram.com/knockoutboxing" target="_blank" rel="noopener">Instagram</a></p>
<table class="hours"><caption>Business hours</caption><tr><th scope="row">Mon–Fri</th><td>8:00 am – 7:30 pm</td></tr><tr><th scope="row">Saturday</th><td>9:00 am – 12:30 pm</td></tr><tr><th scope="row">Sunday</th><td>8:00 am – 11:30 am</td></tr></table></div>
<iframe class="map" title="Map to Knockout Boxing &amp; Fitness, 1244 Capitol Trl, Newark, DE" src="https://maps.google.com/maps?q=1244%20Capitol%20Trl%2C%20Newark%2C%20DE%2019711&z=15&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></section>'''
page('contact.html','Contact & Directions | Knockout Boxing & Fitness, Newark DE','Knockout Boxing & Fitness, 1244 Capitol Trl, Newark, DE 19711. Call (302) 200-8714. Open Mon-Fri 8-7:30, Sat 9-12:30, Sun 8-11:30. Map and directions.',ct,'Contact')

pages=['']+[u for u,_ in NAV[1:]]
open(OUT+'sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{BASE}{p}</loc><lastmod>2026-10-21</lastmod></url>' for p in pages)+'</urlset>\n')
open(OUT+'robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
open(OUT+'site.webmanifest','w').write(json.dumps({"name":"Knockout Boxing & Fitness","short_name":"Knockout","start_url":"./","display":"standalone","background_color":"#0b0b0c","theme_color":"#0b0b0c","icons":[{"src":"img/icon-192.png","sizes":"192x192","type":"image/png"},{"src":"img/icon-512.png","sizes":"512x512","type":"image/png"}]}))
print('built')
