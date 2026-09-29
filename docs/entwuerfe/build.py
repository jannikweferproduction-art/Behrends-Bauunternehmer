# Erzeugt die drei Hero-Entwürfe aus einer gemeinsamen Vorlage.
from pathlib import Path
here = Path(__file__).parent

def logo(ink="#141414", paper="#fff", mark_only=False, cls="logo"):
    mark = f'''
    <polyline points="48,398 48,152 160,38 478,242 478,332" fill="none" stroke="#FF1828" stroke-width="26" stroke-linejoin="miter"/>
    <path d="M172 190 C200 140 230 108 262 98 C290 92 322 110 342 138 C300 150 240 170 172 190Z" fill="{ink}"/>
    <line x1="300" y1="112" x2="350" y2="78" stroke="{ink}" stroke-width="11" stroke-linecap="round"/>
    <line x1="350" y1="76" x2="500" y2="50" stroke="{ink}" stroke-width="34" stroke-linecap="round"/>
    <rect x="80" y="214" width="76" height="52" rx="4" fill="{ink}"/>
    <rect x="80" y="278" width="13" height="50" rx="3" fill="{ink}"/>
    <rect x="105" y="278" width="118" height="50" rx="4" fill="{ink}"/>
    <rect x="80" y="340" width="66" height="50" rx="4" fill="{ink}"/>
    <rect x="160" y="340" width="118" height="50" rx="4" fill="{ink}"/>'''
    if mark_only:
        return f'<svg class="{cls}" viewBox="30 20 500 385" role="img" aria-label="Besser bauen Behrends">{mark}</svg>'
    text = f'''
    <g font-family="'Source Sans 3', sans-serif" font-weight="600" fill="{ink}">
      <text x="176" y="264" font-size="74" letter-spacing="-1">besser</text>
      <text x="243" y="326" font-size="74" letter-spacing="-1">bauen</text>
      <text x="296" y="388" font-size="76" letter-spacing="-1.5">BEHRENDS</text>
      <rect x="47" y="410" width="643" height="106" fill="{paper}" stroke="#FF1828" stroke-width="12"/>
      <text x="368" y="492" font-size="82" text-anchor="middle" letter-spacing="-1">Bauunternehmen</text>
    </g>'''
    return f'<svg class="{cls}" viewBox="30 20 680 505" role="img" aria-label="Besser bauen Behrends – Bauunternehmen">{mark}{text}</svg>'

FONTS = '''
@font-face{font-family:"Archivo";src:url(fonts/archivo.woff2) format("woff2");font-weight:100 900;font-stretch:62% 125%}
@font-face{font-family:"Source Sans 3";src:url(fonts/source-sans-3-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:"Source Sans 3";src:url(fonts/source-sans-3-latin-600-normal.woff2);font-weight:600}
@font-face{font-family:"IBM Plex Sans Condensed";src:url(fonts/ibm-plex-sans-condensed-latin-500-normal.woff2);font-weight:500}
@font-face{font-family:"IBM Plex Sans Condensed";src:url(fonts/ibm-plex-sans-condensed-latin-700-normal.woff2);font-weight:700}
@font-face{font-family:"IBM Plex Mono";src:url(fonts/ibm-plex-mono-latin-400-normal.woff2);font-weight:400}
@font-face{font-family:"IBM Plex Mono";src:url(fonts/ibm-plex-mono-latin-500-normal.woff2);font-weight:500}
@font-face{font-family:"Source Serif 4";src:url(fonts/source-serif-4.woff2) format("woff2");font-weight:200 900}
*{box-sizing:border-box;margin:0;padding:0}
img{display:block;max-width:100%}
a{color:inherit;text-decoration:none}
'''

WA = '<svg viewBox="0 0 24 24" aria-hidden="true" width="18" height="18"><path fill="currentColor" d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.8 4.4 3.9 1.6.7 2.3.8 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3Z"/></svg>'
PHONE = '<svg viewBox="0 0 24 24" aria-hidden="true" width="18" height="18"><path fill="currentColor" d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1l-2.3 2.2Z"/></svg>'

H1 = "Besser bauen heißt: sauber bis zur letzten Fuge."
SUB = "Umbau, Sanierung, Rohbau und Außenanlagen in Wittmund und Umgebung – vom Maurer, der selbst auf der Baustelle steht."
NAV = '<nav aria-label="Hauptnavigation"><a href="#">Leistungen</a><a href="#">Projekte</a><a href="#">Über uns</a><a href="#">Kontakt</a></nav>'

def page(title, css, body):
    return f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><style>{FONTS}{css}</style></head><body>{body}</body></html>'''

# ---------- Richtung 1: Verband ----------
css1 = '''
:root{--kalk:#F4F1EC;--moertel:#D6D0C6;--anthrazit:#1E1C1A;--klinker:#8B3A2B;--signal:#E3161F}
body{background:var(--kalk);color:var(--anthrazit);font-family:"Source Sans 3",sans-serif}
header{display:flex;align-items:center;gap:40px;padding:14px 48px;background:var(--kalk);border-bottom:1px solid var(--moertel)}
header .logo{height:84px;width:auto}
header .logo.mark{display:none}
nav{display:flex;gap:32px;margin-left:auto;font-family:Archivo;font-weight:600;font-size:16px;font-stretch:105%}
.tel{display:inline-flex;align-items:center;gap:10px;background:var(--anthrazit);color:var(--kalk);padding:12px 18px;font-family:Archivo;font-weight:700;font-size:16px;letter-spacing:.01em}
.hero{position:relative;height:calc(100vh - 95px);min-height:640px}
.hero .foto{position:absolute;inset:0 0 0 22%;overflow:hidden}
.hero .foto img{width:100%;height:100%;object-fit:cover;object-position:50% 60%}
.cap{position:absolute;right:20px;bottom:18px;color:#fff;font-size:14px;background:rgba(20,18,16,.55);padding:6px 10px}
/* Rollschicht-Band */
.band{position:absolute;left:48px;bottom:56px;width:min(760px,60%);background:var(--kalk);padding:0 48px 44px}
.band::before{content:"";display:block;height:22px;margin:0 -48px 36px;
  background:repeating-linear-gradient(90deg,var(--klinker) 0 22px,var(--kalk) 22px 25px);border-bottom:3px solid var(--kalk);box-shadow:0 3px 0 var(--moertel)}
.schicht{display:flex;gap:14px;align-items:baseline;font-family:Archivo;font-weight:600;font-size:14px;letter-spacing:.14em;text-transform:uppercase;color:var(--klinker);margin-bottom:18px}
.schicht b{font-stretch:125%;font-weight:800;color:var(--anthrazit);letter-spacing:0}
h1{font-family:Archivo;font-weight:800;font-stretch:112%;font-size:clamp(34px,4.1vw,60px);line-height:1.02;letter-spacing:-.02em;max-width:14ch}
h1 em{font-style:normal;color:var(--klinker)}
.sub{margin-top:20px;font-size:20px;line-height:1.45;max-width:36ch}
.cta{display:flex;gap:12px;margin-top:28px;flex-wrap:wrap}
.btn{display:inline-flex;align-items:center;gap:10px;padding:15px 22px;font-family:Archivo;font-weight:700;font-size:17px;border:2px solid var(--klinker)}
.btn.p{background:var(--klinker);color:#fff}
.btn.s{color:var(--anthrazit);border-color:var(--anthrazit)}
.mass{position:absolute;left:calc(22% + 24px);top:28px;display:flex;align-items:center;gap:10px;color:#fff;font-family:"IBM Plex Mono";font-size:13px}
.mass i{display:block;width:90px;height:9px;border:1.5px solid #fff;border-top:0;border-bottom:0;position:relative}
.mass i::after{content:"";position:absolute;left:0;right:0;top:3px;border-top:1.5px solid #fff}
.leiste{display:none}
@media (max-width:760px){
  header{padding:10px 16px;gap:12px}
  header .logo.full{display:none} header .logo.mark{display:block;height:44px}
  header .name{font-family:Archivo;font-weight:800;font-size:17px;line-height:1.05;font-stretch:108%}
  header .name small{display:block;font-weight:500;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--klinker);font-stretch:100%}
  nav{display:none} .tel{margin-left:auto;padding:10px 12px;font-size:0} .tel svg{width:20px;height:20px}
  .hero{height:auto;min-height:0}
  .hero .foto{position:relative;inset:auto;height:300px}
  .mass{left:16px;top:16px}
  .cap{bottom:44px;right:12px;font-size:12px}
  .band{position:relative;left:auto;bottom:auto;width:auto;margin:-30px 16px 0;padding:0 20px 28px}
  .band::before{margin:0 -20px 24px;height:16px;background:repeating-linear-gradient(90deg,var(--klinker) 0 16px,var(--kalk) 16px 18px)}
  h1{font-size:33px}
  .sub{font-size:18px}
  .cta{display:none}
  .leiste{display:grid;grid-template-columns:1fr 1fr;position:fixed;left:0;right:0;bottom:0;border-top:1px solid var(--moertel)}
  .leiste a{display:flex;justify-content:center;align-items:center;gap:8px;padding:16px;font-family:Archivo;font-weight:700;font-size:16px}
  .leiste a:first-child{background:var(--klinker);color:#fff} .leiste a:last-child{background:var(--kalk)}
}
'''
body1 = f'''<header><a href="#">{logo(cls="logo full")}</a><a href="#" style="display:flex;gap:10px;align-items:center">{logo(mark_only=True, cls="logo mark")}<span class="name" hidden>Besser bauen Behrends<small>Bauunternehmen</small></span></a>{NAV}<a class="tel" href="#">{PHONE}0172 4300736</a></header>
<main><section class="hero">
<div class="foto"><img src="../../material/projekte/aussen-03-klinkermauer-abend.jpg" alt="Klinkermauer mit Pfeilern und Beleuchtung am Abend"></div>
<p class="cap">Klinkermauer mit Pfeilern und Rollschicht</p>
<div class="band">
<p class="schicht"><b>01</b>Maurerbetrieb in Wittmund</p>
<h1>Besser bauen heißt: sauber bis zur <em>letzten Fuge.</em></h1>
<p class="sub">{SUB}</p>
<div class="cta"><a class="btn p" href="#">{PHONE}0172 4300736 anrufen</a><a class="btn s" href="#">{WA}Foto per WhatsApp schicken</a></div>
</div></section></main>
<div class="leiste"><a href="#">{PHONE}Anrufen</a><a href="#">{WA}WhatsApp</a></div>
<style>@media (max-width:760px){{header .name{{display:block!important}}}}</style>'''
(here/"richtung-1-verband.html").write_text(page("Entwurf Richtung 1 – Verband", css1, body1))

# ---------- Richtung 2: Werkplan ----------
css2 = '''
:root{--plan:#FAFAF7;--raster:#E4E4DF;--tusche:#141414;--rot:#C8141D}
body{background:var(--plan);color:var(--tusche);font-family:"IBM Plex Sans Condensed",sans-serif;
 background-image:linear-gradient(var(--raster) 1px,transparent 1px),linear-gradient(90deg,var(--raster) 1px,transparent 1px);background-size:32px 32px}
.mono{font-family:"IBM Plex Mono",monospace}
header{display:flex;align-items:center;gap:40px;padding:12px 48px;border-bottom:1.5px solid var(--tusche);background:var(--plan)}
header .logo{height:80px;width:auto}
header .logo.mark{display:none}
nav{display:flex;gap:28px;margin-left:auto;font-family:"IBM Plex Mono";font-size:14px;text-transform:uppercase;letter-spacing:.06em}
.tel{display:inline-flex;align-items:center;gap:10px;border:1.5px solid var(--tusche);padding:10px 16px;font-family:"IBM Plex Mono";font-weight:500;font-size:15px;background:var(--plan)}
.achsen{display:flex;justify-content:space-around;padding:6px 48px 0 96px;font-family:"IBM Plex Mono";font-size:12px;color:#777}
.hero{display:grid;grid-template-columns:1.15fr .85fr;gap:56px;padding:18px 48px 40px 96px;position:relative;min-height:calc(100vh - 110px)}
.hero::before{content:"1\\A \\A \\A \\A \\A \\A 2\\A \\A \\A \\A \\A \\A 3";white-space:pre;position:absolute;left:48px;top:40px;font-family:"IBM Plex Mono";font-size:12px;line-height:1.6;color:#777}
.txt{display:flex;flex-direction:column;justify-content:center}
.pos{font-family:"IBM Plex Mono";font-size:13px;color:var(--rot);letter-spacing:.04em;margin-bottom:22px}
h1{font-weight:700;font-size:clamp(40px,5vw,74px);line-height:.98;letter-spacing:-.015em;text-transform:none;max-width:13ch}
.sub{font-family:"IBM Plex Sans Condensed";font-weight:500;font-size:21px;line-height:1.4;margin-top:22px;max-width:38ch}
.cta{display:flex;gap:12px;margin-top:30px}
.btn{display:inline-flex;gap:10px;align-items:center;padding:14px 20px;border:1.5px solid var(--tusche);font-family:"IBM Plex Mono";font-weight:500;font-size:15px}
.btn.p{background:var(--tusche);color:var(--plan)} .btn.s{background:var(--plan)}
.plankopf{margin-top:40px;display:grid;grid-template-columns:repeat(4,auto);border:1.5px solid var(--tusche);background:var(--plan);font-family:"IBM Plex Mono";font-size:12px;width:max-content}
.plankopf div{padding:8px 14px;border-right:1px solid var(--tusche)} .plankopf div:last-child{border:0}
.plankopf span{display:block;color:#777;font-size:10px;text-transform:uppercase;letter-spacing:.08em}
.bild{position:relative;align-self:center}
.bild img{width:100%;aspect-ratio:3/4;object-fit:cover;border:1.5px solid var(--tusche);filter:saturate(.85)}
.call{position:absolute;display:flex;align-items:center;font-family:"IBM Plex Mono";font-size:12px;color:var(--rot);white-space:nowrap}
.call::before{content:"";width:10px;height:10px;border:2px solid var(--rot);border-radius:50%;background:rgba(255,255,255,.6)}
.call span{background:var(--plan);border:1px solid var(--rot);padding:3px 7px;margin-left:var(--l,70px);position:relative}
.call span::before{content:"";position:absolute;right:100%;top:50%;width:var(--l,70px);border-top:1.5px solid var(--rot)}
.masskette{position:absolute;left:-30px;top:0;bottom:0;width:14px;border-left:1.5px solid var(--tusche)}
.masskette::before,.masskette::after{content:"";position:absolute;left:-7px;width:14px;border-top:1.5px solid var(--tusche)}
.masskette::before{top:0}.masskette::after{bottom:0}
.masskette b{position:absolute;top:50%;left:-16px;transform:translateY(-50%) rotate(-90deg);transform-origin:center;font:500 11px "IBM Plex Mono";background:var(--plan);padding:0 4px;white-space:nowrap}
.leiste{display:none}
@media (max-width:760px){
 header{padding:10px 16px;gap:12px} header .logo.full{display:none} header .logo.mark{display:block;height:42px}
 nav,.achsen{display:none} .tel{margin-left:auto;font-size:0;padding:10px}
 .hero{grid-template-columns:1fr;padding:22px 16px 90px;gap:28px;min-height:0}
 .hero::before{display:none}
 h1{font-size:40px} .sub{font-size:18px} .cta{display:none}
 .plankopf{grid-template-columns:1fr 1fr;width:auto;margin-top:24px} .plankopf div:nth-child(2){border-right:0} .plankopf div:nth-child(-n+2){border-bottom:1px solid var(--tusche)}
 .bild{margin-left:26px}
 .call{font-size:11px} .call span{--l:18px!important}
 .call:nth-of-type(1){left:30%!important} .call:nth-of-type(2){left:6%!important}
 .leiste{display:grid;grid-template-columns:1fr 1fr;position:fixed;left:0;right:0;bottom:0;border-top:1.5px solid var(--tusche)}
 .leiste a{display:flex;justify-content:center;gap:8px;align-items:center;padding:16px;font-family:"IBM Plex Mono";font-weight:500;font-size:15px}
 .leiste a:first-child{background:var(--tusche);color:var(--plan)} .leiste a:last-child{background:var(--plan)}
}
'''
body2 = f'''<header><a href="#">{logo(cls="logo full")}</a><a href="#">{logo(mark_only=True, cls="logo mark")}</a>{NAV}<a class="tel" href="#">{PHONE}0172 4300736</a></header>
<div class="achsen" aria-hidden="true"><span>A</span><span>B</span><span>C</span><span>D</span><span>E</span></div>
<main><section class="hero">
<div class="txt">
<p class="pos">BLATT 01 · MAURERBETRIEB WITTMUND</p>
<h1>{H1}</h1>
<p class="sub">{SUB}</p>
<div class="cta"><a class="btn p" href="#">{PHONE}Anrufen</a><a class="btn s" href="#">{WA}Foto per WhatsApp</a></div>
<div class="plankopf"><div><span>Bauherr</span>Sie</div><div><span>Ausführung</span>J. Behrends, Maurer</div><div><span>Ort</span>Wittmund + 40 km</div><div><span>Leistung</span>Umbau · Rohbau · Außen</div></div>
</div>
<figure class="bild">
<div class="masskette"><b>Verblendmauerwerk</b></div>
<img src="../../material/projekte/mauerwerk-01-klinkerfassade.jpg" alt="Klinker-Verblendmauerwerk mit Rollschicht über dem Fenster, Bockgerüst davor">
<p class="call" style="left:44%;top:39%;--l:60px"><span>Pos. 1 · Rollschicht</span></p>
<p class="call" style="left:18%;top:62%;--l:40px"><span>Pos. 2 · Klinker-Verblendung</span></p>
</figure>
</section></main>
<div class="leiste"><a href="#">{PHONE}Anrufen</a><a href="#">{WA}WhatsApp</a></div>'''
(here/"richtung-2-werkplan.html").write_text(page("Entwurf Richtung 2 – Werkplan", css2, body2))

# ---------- Richtung 3: Blaue Stunde ----------
css3 = '''
:root{--nacht:#15171A;--schiefer:#22262B;--warm:#F2EDE6;--licht:#E9B872}
body{background:var(--nacht);color:var(--warm);font-family:Archivo,sans-serif}
.hero{position:relative;height:100vh;min-height:640px;overflow:hidden}
.hero>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:60% 55%}
.hero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(21,23,26,.92) 0%,rgba(21,23,26,.7) 36%,rgba(21,23,26,0) 66%),linear-gradient(0deg,rgba(21,23,26,.6),transparent 30%)}
header{position:absolute;z-index:2;left:0;right:0;top:0;display:flex;align-items:center;gap:40px;padding:24px 56px}
header .logo{height:88px;width:auto} header .logo.mark{display:none}
nav{display:flex;gap:34px;margin-left:auto;font-size:15px;font-weight:500;letter-spacing:.02em}
.tel{display:inline-flex;align-items:center;gap:10px;font-weight:600;font-size:15px;border-bottom:1px solid var(--licht);padding:6px 0;color:var(--licht)}
.inhalt{position:absolute;z-index:2;left:56px;bottom:88px;max-width:620px}
.kicker{font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--licht);margin-bottom:22px}
h1{font-family:"Source Serif 4",serif;font-weight:400;font-size:clamp(40px,5.2vw,80px);line-height:1.02;letter-spacing:-.02em}
h1 em{font-style:italic;color:var(--licht)}
.sub{margin-top:24px;font-size:19px;line-height:1.5;max-width:40ch;color:#D9D3CA}
.cta{display:flex;gap:14px;margin-top:34px}
.btn{display:inline-flex;align-items:center;gap:10px;padding:16px 24px;font-weight:600;font-size:16px;border:1px solid var(--licht)}
.btn.p{background:var(--licht);color:var(--nacht)} .btn.s{color:var(--warm);border-color:rgba(242,237,230,.5)}
.leiste{display:none}
@media (max-width:760px){
 header{padding:14px 16px;gap:12px} header .logo.full{display:none} header .logo.mark{display:block;height:44px}
 nav{display:none} .tel{margin-left:auto;font-size:0;border:1px solid var(--licht);padding:10px}
 .hero{height:100vh;min-height:0}
 .hero::after{background:linear-gradient(0deg,rgba(21,23,26,.96) 0%,rgba(21,23,26,.85) 45%,rgba(21,23,26,.1) 75%)}
 .hero>img{object-position:62% 50%}
 .inhalt{left:16px;right:16px;bottom:78px}
 h1{font-size:38px} .sub{font-size:17px} .cta{display:none}
 .leiste{display:grid;grid-template-columns:1fr 1fr;position:fixed;left:0;right:0;bottom:0;z-index:3}
 .leiste a{display:flex;justify-content:center;align-items:center;gap:8px;padding:16px;font-weight:600;font-size:16px}
 .leiste a:first-child{background:var(--licht);color:var(--nacht)} .leiste a:last-child{background:var(--schiefer)}
}
'''
body3 = f'''<section class="hero">
<img src="../../material/projekte/aussen-03-klinkermauer-abend.jpg" alt="Klinkermauer mit beleuchteten Pfeilern vor einem Klinkerhaus am Abend">
<header><a href="#">{logo(ink="#F2EDE6", paper="#15171A", cls="logo full")}</a><a href="#">{logo(ink="#F2EDE6", mark_only=True, cls="logo mark")}</a>{NAV}<a class="tel" href="#">{PHONE}0172 4300736</a></header>
<div class="inhalt">
<p class="kicker">Maurerbetrieb · Wittmund</p>
<h1>Besser bauen heißt: sauber bis zur <em>letzten Fuge.</em></h1>
<p class="sub">{SUB}</p>
<div class="cta"><a class="btn p" href="#">{PHONE}0172 4300736 anrufen</a><a class="btn s" href="#">{WA}Foto per WhatsApp</a></div>
</div></section>
<div class="leiste"><a href="#">{PHONE}Anrufen</a><a href="#">{WA}WhatsApp</a></div>'''
(here/"richtung-3-blaue-stunde.html").write_text(page("Entwurf Richtung 3 – Blaue Stunde", css3, body3))
print("ok")
