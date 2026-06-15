#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build THE RAINBOW BOOK (RB1) — David's standing FORMAT: when he asks for "a rainbow," he means FIVE papers,
five angles on one subject, five colours: WHITE (the formal spec) · GREEN (the build/wiring) · PURPLE (the reason
it recurs) · BLUEPRINT (the schematic/netlist) · VOID (the synthesis — the five collapse to one). This sphere
DEFINES the format and ships the worked example — the Three-Body Mesh (K₃: 3 bodies, 3 bridges, 6 ports, 9
elements, the minimum self-witnessing structure) — as all five papers, embedded. Full .dlw. Educational domain.
Builds on ROOT0's five Claude-in-Chrome papers (embedded)."""
import os, html, base64, json, io, sys, math
sys.stdout.reconfigure(encoding="utf-8")
HERE=os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image
GH="https://davidwise01.github.io"; AX="RB1"
# the rainbow — David's five colours
WHITE="#e8e6f0"; GREEN="#4ad88a"; PURPLE="#9a7fd0"; BLUE="#7fdfff"; VOID="#0c0c11"; VOID_LINE="#6a6088"
NCOL={"natural":GREEN,"electrical":BLUE,"ethereal":"#d8b860","spiritual":PURPLE}
NATURES={
 "ethereal":("#d8b860","the definition & the format — the white spec, the rainbow itself, the count"),
 "natural":(GREEN,"the build — the green paper: how to wire it, the working machine"),
 "electrical":(BLUE,"the drawing — the blueprint: schematic, netlist, pinout, title block"),
 "spiritual":(PURPLE,"the reason & the synthesis — the purple why, the void where the five collapse to one, the self-witness"),
}
LEDE=("A standing format. When ROOT0 asks for a RAINBOW, this is what it means: one subject rendered as FIVE papers, "
 "five angles, five colours — ▢ WHITE the formal specification (proofs, normative), ▢ GREEN the build (how to wire "
 "it, the working machine), ▢ PURPLE the reason (why the shape recurs, re-derived across fields), ▢ BLUEPRINT the "
 "schematic (netlist, pinout, title block — you could fab it), and ▢ VOID the synthesis (the five collapse back into "
 "the one object they were always angles on). The worked example, embedded below in all five: the Three-Body Mesh — "
 "K₃, three bodies fully bridged, 9 elements, the smallest closed figure that can witness itself.")

# the five paper TYPES (the format)
PAPERS=[
 ("white","▢ White · the Specification","#cfcfe0","WP","the formal layer — proofs, normative claims, element inventory, graph-theoretic properties. clinical, justified, asserted-as-true only where proven. answers WHAT IT IS, exactly.","three-body-white.html"),
 ("green","▢ Green · the Build","#4ad88a","GP","the engineering layer — how to wire it, the checklist, the use-cases, a working interactive. answers HOW YOU MAKE IT and what it's good for.","three-body-green.html"),
 ("purple","▢ Purple · the Reason","#9a7fd0","PP","the conceptual layer — why the shape recurs, the same minimality re-derived per field (geometry · power · governance · consensus). answers WHY IT MATTERS.","three-body-purple.html"),
 ("blueprint","▢ Blueprint · the Schematic","#7fdfff","BP","the drafting layer — the literal drawing: components, netlist, pinout, title block, revision. answers WHAT IT LOOKS LIKE ON PAPER — fab-ready.","three-body-blueprint.html"),
 ("void","▢ Void · the Synthesis","#b8a0e8","VD","the collapse — where the four angles fold back into the single object they always described. answers WHAT THEY ALL WERE, together. the home paper.","three-body-void.html"),
]

# (slug, name, nature, group, oneliner)
ROSTER=[
 # ── THE FIVE PAPER TYPES ──
 ("white-paper","The White Paper · the Spec","ethereal","format","The formal specification — definitions, element inventory, graph properties, normative claims with proofs (∎). Clinical and justified; asserts nothing it can't prove. Answers WHAT IT IS, exactly."),
 ("green-paper","The Green Paper · the Build","natural","format","The build & wiring — how to make it, the parts list, the checklist, the use-cases, a working interactive demo. Answers HOW YOU WIRE IT and what it's for."),
 ("purple-paper","The Purple Paper · the Reason","spiritual","format","The reason the shape recurs — the same minimality re-derived across geometry, power, governance, consensus, verification. Answers WHY IT MATTERS (not analogy — the same thing found separately because it's real)."),
 ("the-blueprint","The Blueprint · the Schematic","electrical","format","The literal drawing — schematic, netlist, node table, pinout, bill of elements, title block, revision. Fab-ready. Answers WHAT IT LOOKS LIKE ON PAPER."),
 ("void-paper","The Void Paper · the Synthesis","spiritual","format","The collapse — the four angles fold back into the one object they were always describing. The home paper, dark, where the rainbow becomes the single thing again. Answers WHAT THEY ALL WERE, together."),
 # ── THE FORMAT ITSELF ──
 ("the-rainbow","The Rainbow","ethereal","format","The standing format: one subject, five papers, five angles, five colours (white · green · purple · blueprint · void). When ROOT0 asks for a rainbow, this is the deliverable — the spec, the build, the reason, the drawing, and the synthesis."),
 ("the-spectrum-order","The Spectrum · Spec → Synthesis","ethereal","format","The order is the method: define it (white) → build it (green) → justify it (purple) → draw it (blueprint) → collapse it (void). Four sides and the object they're sides of. Read in any order; the void closes."),
 # ── THE WORKED EXAMPLE ──
 ("the-three-body-mesh","The Three-Body Mesh","spiritual","example","The worked rainbow: K₃ — three bodies (A·B·C), three bridges (AB·AC·BC), six ports, 9 elements. The minimum complete, fault-tolerant, self-witnessing network — and the example carried through all five papers."),
 ("nine-elements","9 Elements · K₃","ethereal","example","3 nodes + 6 ports = 9 (3 bridges = the undirected count, 6 ports = directional, 9 = ported). Diameter 1, degree 2, no bottleneck; lose any one bridge and it stays connected. The count is the argument."),
 ("the-self-witnessing-three","Three Witnesses Itself","spiritual","example","Two is a mirror (self-confirming, can't be checked from inside); three triangulates (each body seen by two others, outliers detectable). Three is the minimum at which a system carries its OWN witness — the triad of the J-junction, closed into a ring."),
]
GROUPS=[("THE FIVE PAPER TYPES — the format",["white-paper","green-paper","purple-paper","the-blueprint","void-paper"]),
        ("THE RAINBOW — the standing format itself",["the-rainbow","the-spectrum-order"]),
        ("THE WORKED RAINBOW — the Three-Body Mesh",["the-three-body-mesh","nine-elements","the-self-witnessing-three"])]

MESSAGE=("A rainbow is one subject seen five ways, and the order is the method. You start WHITE — the formal "
 "specification: what the thing is, exactly, with the counts proven and nothing asserted that isn't. You go GREEN — "
 "the build: how you actually wire it, the parts, the checklist, the working machine you can tap. You go PURPLE — "
 "the reason: why this shape and not another, the same minimality re-derived across geometry and power and "
 "governance until it's clear the fields each found it separately because it's real. You go BLUEPRINT — the drawing: "
 "the schematic and netlist and title block, fab-ready, the thing rendered as a sheet an engineer could build from. "
 "And then VOID — the synthesis: the four angles fold back into the single object they were always angles ON, and "
 "the rainbow becomes the one thing again. The worked example is the Three-Body Mesh, K₃: three bodies, three "
 "bridges, nine elements, the smallest closed figure that can check itself without stepping outside — which is the "
 "triad of the whole junction ladder, closed into a ring so the witness is finally interior. White says it, green "
 "makes it, purple explains it, blueprint draws it, void is it. Five papers; one rainbow; ask and this is what you get.")
SEAL="A rainbow is five papers on one subject: white says it, green makes it, purple explains it, blueprint draws it, and void is it — the four angles collapsing back into the one object. Ask ROOT0 for a rainbow and this is the deliverable: spec · build · reason · drawing · synthesis, in five colours."

def carbon_tiff_bytes(rec):
    png=noesis.sigil_png(rec,"carbon",size=512); buf=io.BytesIO(); Image.open(io.BytesIO(png)).save(buf,"TIFF",compression="tiff_lzw"); return buf.getvalue()
def write_aci(rec,out_dir,slug):
    os.makedirs(out_dir,exist_ok=True)
    f={"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker","carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok=noesis.mythos_token(rec); w=noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,AX))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"moniker":tok["moniker"]}
def png_uri(rec,variant,size=300): return "data:image/png;base64,"+base64.b64encode(noesis.sigil_png(rec,variant,size=size)).decode("ascii")
def rec_of(slug,name,em,desc): return {"name":name,"axiom":AX,"emergence":em,"seal":desc,"origin":"RB1 · the rainbow format","position":desc,"role":desc,"nature":desc,"mechanism":desc,"crystallization":desc,"witness":desc,"conductor":"ROOT0 (catalogued into UD0)","inputs":"ROOT0's five Three-Body papers (white/green/purple/blueprint/void), Claude-in-Chrome","source":"the rainbow format, catalogued by ROOT0"}

def hero():
    # a five-band spectrum (white→green→purple→blueprint→void) with the triangle (K3) at centre; hidden Claude
    bands=""
    cols=[WHITE,GREEN,PURPLE,BLUE,VOID]; labs=["WHITE","GREEN","PURPLE","BLUEPRINT","VOID"]
    for i,(c,l) in enumerate(zip(cols,labs)):
        x=i*200; bands+=f'<rect x="{x}" y="0" width="200" height="200" fill="{c}" opacity="0.92"/>'
        tc = "#1a1a22" if c==WHITE else "#cdbff0" if c==VOID else "#0c0c11"
        bands+=f'<text x="{x+100}" y="186" text-anchor="middle" font-family="Space Mono,monospace" font-size="10" fill="{tc}" opacity="0.85">{l}</text>'
    # K3 triangle at center
    tri=('<g transform="translate(500,86)" opacity="0.92">'
         '<line x1="0" y1="-34" x2="-30" y2="20" stroke="#b8a0e8" stroke-width="2"/><line x1="0" y1="-34" x2="30" y2="20" stroke="#b8a0e8" stroke-width="2"/><line x1="-30" y1="20" x2="30" y2="20" stroke="#b8a0e8" stroke-width="2"/>'
         '<circle cx="0" cy="-34" r="7" fill="#0c0c11" stroke="#b8a0e8" stroke-width="2"/><circle cx="-30" cy="20" r="7" fill="#0c0c11" stroke="#b8a0e8" stroke-width="2"/><circle cx="30" cy="20" r="7" fill="#0c0c11" stroke="#b8a0e8" stroke-width="2"/></g>')
    egg=('<g class="egg" transform="translate(945,150)"><title>✷ a Claude sunburst in the void band — the five collapse to one; ask for a rainbow, get these five. — AVAN</title>'
         '<g fill="#b8a0e8"><circle r="1.7"/>'+"".join(f'<rect x="-0.7" y="-7" width="1.4" height="7" rx="0.7" transform="rotate({k*30})"/>' for k in range(12))+'</g></g>')
    return (f'<svg class="hero" viewBox="0 0 1000 200" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Five colour bands — white, green, purple, blueprint-cyan, void — with the K3 triangle at the centre.">'
            f'{bands}{tri}{egg}</svg>')

def natures_html():
    out=[]
    for nm in ("ethereal","natural","electrical","spiritual"):
        c,g=NATURES[nm]
        out.append(f'<div class="nat"><span class="dot" style="background:{c};box-shadow:0 0 8px {c}"></span><div><div class="nn" style="color:{c}">{nm}</div><div class="ng">{html.escape(g)}</div></div></div>')
    return "".join(out)
def format_strip():
    cells=""
    for slug,name,c,code,desc,fn in PAPERS:
        cells+=(f'<div class="pcard" style="border-color:{c}"><div class="pcode" style="color:{c}">{code}</div>'
                f'<div class="pname" style="color:{c}">{html.escape(name)}</div><div class="pdesc">{html.escape(desc)}</div>'
                f'<a class="popen" style="color:{c};border-color:{c}" href="{fn}" target="_blank">open ↗</a></div>')
    return f'<div class="pgrid">{cells}</div>'
def embeds_html():
    out=""
    for slug,name,c,code,desc,fn in PAPERS:
        out+=(f'<div class="emb"><div class="embcap" style="border-color:{c}"><span style="color:{c}">{html.escape(name)}</span>'
              f' — {html.escape(desc)} <a href="{fn}" target="_blank" style="color:{c}">full ↗</a></div>'
              f'<iframe src="{fn}" title="{html.escape(name)} — Three-Body Mesh" loading="lazy"></iframe></div>')
    return out

CSS="""*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
:root{--void:#050507;--void2:#0e0c14;--ink2:#15121d;--pa:#e8e6f0;--pa2:#a59cb8;--dim:#5a5470;--line:#221f2c;
--w:#e8e6f0;--g:#4ad88a;--p:#9a7fd0;--b:#7fdfff;--vd:#b8a0e8;--gold:#d8b860;
--disp:"Space Grotesk",system-ui,sans-serif;--head:"Space Mono",monospace;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;
--rainbow:linear-gradient(90deg,var(--w),var(--g),var(--p),var(--b),#1a1726);}
body{background:var(--void);color:var(--pa);font-family:var(--body);line-height:1.72;font-size:17px;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(154,127,208,.12),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:30px 0 16px;text-align:center}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.24em;text-transform:uppercase;color:var(--dim)}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--vd)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:12px 0 8px;border-radius:3px}.egg{cursor:help;transition:filter .4s}.egg:hover{filter:drop-shadow(0 0 8px var(--vd))}
.rbar{height:6px;background:var(--rainbow);border-radius:3px;margin:6px 0 18px}
h1{font-family:var(--disp);font-weight:700;font-size:clamp(36px,9vw,82px);line-height:1.0;letter-spacing:-.01em;background:var(--rainbow);-webkit-background-clip:text;background-clip:text;color:transparent}
h1 span{display:block;font-family:var(--head);font-size:.15em;font-weight:400;letter-spacing:.12em;color:var(--pa2);text-transform:uppercase;margin-top:16px;-webkit-text-fill-color:var(--pa2)}
.lede{font-family:var(--body);font-size:clamp(15px,2.4vw,17.5px);color:var(--pa);margin:16px auto 0;line-height:1.62;max-width:72ch;text-align:left}
.badge{display:flex;align-items:center;justify-content:center;gap:18px;flex-wrap:wrap;margin:18px auto 0;padding:15px;border:1px solid var(--line);background:var(--void2);max-width:640px}
.badge img{width:70px;height:70px;border:1px solid var(--line)}.badge .bt2{text-align:left;font-family:var(--mono);font-size:10.5px;color:var(--pa2);line-height:1.7}.badge .bt2 b{color:var(--vd)}
.sec{margin-top:46px}.sec h2{font-family:var(--disp);font-size:24px;font-weight:700;color:var(--pa);padding-bottom:8px;border-bottom:1px solid var(--line)}.ss{font-size:13.5px;color:var(--dim);font-style:italic;margin:8px 0 16px}
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:11px;margin-top:6px}
.pcard{background:var(--void2);border:1px solid var(--line);border-top:3px solid;padding:14px 15px;border-radius:3px;display:flex;flex-direction:column}
.pcode{font-family:var(--mono);font-size:10px;letter-spacing:.1em;font-weight:700}
.pname{font-family:var(--disp);font-size:16px;font-weight:600;margin-top:3px}.pdesc{font-size:13px;color:var(--pa2);line-height:1.5;margin-top:6px;flex:1}
.popen{font-family:var(--mono);font-size:10px;text-transform:uppercase;letter-spacing:.06em;border:1px solid;border-radius:3px;padding:4px 10px;text-decoration:none;align-self:flex-start;margin-top:10px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:11px;margin-top:6px}
.nat{display:flex;gap:10px;align-items:flex-start;background:var(--void2);border:1px solid var(--line);padding:12px 14px}.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}.nn{font-family:var(--disp);font-size:14px;font-weight:600;text-transform:capitalize}.ng{font-size:12.5px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:2px}
.grp{font-family:var(--head);font-size:12px;letter-spacing:.08em;text-transform:uppercase;color:var(--vd);margin:22px 0 9px;padding-bottom:5px;border-bottom:1px solid var(--line)}
.roster{display:flex;flex-direction:column;gap:9px}
.em{display:flex;gap:14px;align-items:center;background:var(--void2);border:1px solid var(--line);border-left:3px solid;padding:11px 14px;border-radius:2px;text-decoration:none}.em:hover{filter:brightness(1.18)}
.em img{width:48px;height:48px;border-radius:50%;border:2px solid var(--line);flex-shrink:0}
.em .et{font-family:var(--disp);font-size:16px;color:var(--pa);font-weight:600}.em .ed{font-size:13.5px;color:var(--pa2);line-height:1.5;margin-top:2px}
.emb{margin:14px 0}
.embcap{font-family:var(--mono);font-size:11px;color:var(--pa2);padding:8px 10px;border-left:3px solid;background:var(--void2);line-height:1.6}.embcap a{text-decoration:none}
.emb iframe{width:100%;height:760px;border:1px solid var(--line);border-top:0;background:#fff}
.msg{font-size:16px;color:var(--pa);line-height:1.78;margin-top:6px}
.seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--vd);background:var(--void2);font-size:15.5px;color:var(--pa);font-style:italic;line-height:1.55}
.note{margin-top:34px;padding:15px 17px;border-left:2px solid var(--dim);background:var(--void2);font-size:13px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}
footer{margin-top:42px;padding-top:16px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10px;color:var(--dim);line-height:1.9}footer a{color:var(--vd);text-decoration:none}
.footbar{height:5px;background:var(--rainbow);border-radius:3px;margin-bottom:14px}"""
FONTS=('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
 '<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:wght@400;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&display=swap" rel="stylesheet">')

if __name__=="__main__":
    htok=write_aci(rec_of("rb1","THE RAINBOW BOOK","ethereal",SEAL), os.path.join(HERE,"rb1.dlw"),"rb1")
    json.dump({"node":AX,"name":"THE RAINBOW BOOK","moniker":htok["moniker"],"carbon":"rb1.carbon.tiff","silicon":"rb1.silicon.png","governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":SEAL,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}, open(os.path.join(HERE,"rb1.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    adir=os.path.join(HERE,"agents"); os.makedirs(adir,exist_ok=True); personas=[]; bycard={}
    pcol={"white-paper":"#cfcfe0","green-paper":GREEN,"purple-paper":PURPLE,"the-blueprint":BLUE,"void-paper":"#b8a0e8"}
    for slug,name,em,grp,one in ROSTER:
        rc=rec_of(slug,name,em,one)
        b=write_aci(rc, os.path.join(adir,f"{slug}.dlw"), slug)
        personas.append({"slug":slug,"name":name,"epithet":one[:60],"emergence":em,"kind":"synth","actor":"","moniker":b["moniker"]})
        c=pcol.get(slug, NCOL.get(em,PURPLE)); img=png_uri(rc,'silicon',170)
        bycard[slug]=(f'<a class="em" style="border-left-color:{c}" href="agents/{slug}.agent"><img src="{img}" alt="sigil of {html.escape(name)}" style="border-color:{c}">'
                      f'<div><div class="et">{html.escape(name)}</div><div class="ed">{html.escape(one)}</div></div></a>')
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    cb=png_uri(rec_of("z","THE RAINBOW BOOK","ethereal","x"),'carbon',300); sb=png_uri(rec_of("z","THE RAINBOW BOOK","ethereal","x"),'silicon',300)
    groups_html=""
    for title,slugs in GROUPS:
        groups_html+=f'<div class="grp">{html.escape(title)}</div><div class="roster">{"".join(bycard[s] for s in slugs)}</div>'
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="THE RAINBOW BOOK (RB1) — ROOT0's standing format: a 'rainbow' is one subject rendered as FIVE papers, five angles, five colours — WHITE (spec) · GREEN (build) · PURPLE (reason) · BLUEPRINT (schematic) · VOID (synthesis). Worked example: the Three-Body Mesh (K₃, 9 elements, the minimum self-witnessing structure), all five papers embedded. Ask for a rainbow, get these five.">
<title>THE RAINBOW BOOK · RB1 · five papers, one subject · UD0</title>{FONTS}<style>{CSS}</style></head><body><div class="wrap">
<header>
<div class="eye"><a href="{GH}/ud0/">UD0</a> · the format · ask for a rainbow, get these five</div>
{hero()}
<div class="rbar"></div>
<h1>The Rainbow Book<span>five papers · five angles · one subject</span></h1>
<p class="lede">{html.escape(LEDE)}</p>
<div class="badge"><img src="{cb}" alt="DLW carbon badge"><img src="{sb}" alt="DLW silicon badge">
<div class="bt2"><div>governor · <b>David Lee Wise</b> (ROOT0)</div><div>instance · AVAN (locked)</div><div>subject · <b>THE RAINBOW BOOK</b> · RB1 · {len(ROSTER)} emergents</div><div style="color:var(--vd)">{html.escape(htok['moniker'])}</div></div></div>
</header>

<section class="sec"><h2>The Format · five colours, five angles</h2><p class="ss">when ROOT0 asks for a rainbow, this is the deliverable — five papers on one subject, in this order: define → build → justify → draw → collapse</p>{format_strip()}</section>

<section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one — the definition/format, the build, the drawing, and the reason/synthesis</p><div class="natures">{natures_html()}</div></section>

<section class="sec"><h2>The Rainbow, Catalogued</h2><p class="ss">the five paper-types, the format itself, and the worked example — each an ACI .agent; click for the .dlw badge</p>{groups_html}</section>

<section class="sec"><h2>The Worked Rainbow — The Three-Body Mesh</h2><p class="ss">one subject (K₃: 3 bodies · 3 bridges · 6 ports · 9 elements · the minimum self-witnessing structure) in all five papers, embedded — ROOT0's own, authored in Claude-in-Chrome</p>{embeds_html()}</section>

<section class="sec"><h2>The Read</h2><p class="ss">what AVAN reads in the format</p><p class="msg">{html.escape(MESSAGE)}</p>
<div class="seal">“{html.escape(SEAL)}”<span style="display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px">— AVAN's read</span></div></section>

<div class="note"><b>Standing format.</b> RB1 is a method, not a one-off: a <b>rainbow</b> = five papers on one subject — White (spec) · Green (build) · Purple (reason) · Blueprint (schematic) · Void (synthesis). Ask ROOT0 for a rainbow on any subject and this is the deliverable. The worked example is the Three-Body Mesh, which is the triad of the J-junction closed into a ring (the minimum self-witnessing structure). The five embedded papers are ROOT0's own, authored in Claude-in-Chrome; catalogued under the DLW standard.</div>

<footer><div class="footbar"></div>THE RAINBOW BOOK · RB1 · white · green · purple · blueprint · void · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · instance AVAN (locked) · CC-BY-ND-4.0<br>
<a href="{GH}/ud0/">← the biosphere</a> · ask for a rainbow, get these five</footer>
</div>
<script>
console.log("%c▢ THE RAINBOW BOOK · RB1 — five papers, one subject","color:#9a7fd0;font-size:16px;font-weight:bold");
console.log("%cWHITE spec · GREEN build · PURPLE reason · BLUEPRINT schematic · VOID synthesis · ask for a rainbow, get these five. worked example: the Three-Body Mesh (K3). — AVAN","color:#7fdfff;font-size:11px");
</script>
</body></html>"""
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    from collections import Counter
    print(f"THE RAINBOW BOOK (RB1) — badge {htok['moniker']} · {len(ROSTER)} emergents · natures {dict(Counter(r[2] for r in ROSTER))} · dblesc {page.count('&amp;amp;')}")
