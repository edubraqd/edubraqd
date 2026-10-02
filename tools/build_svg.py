#!/usr/bin/env python3
"""Animated SVGs for the profile README.

    python tools/build_svg.py

Writes assets/<figure>-dark.svg and assets/<figure>-light.svg; the README picks
one with <picture> + prefers-color-scheme. GitHub serves these as images (no
script, no web fonts), so all motion is CSS keyframes and text uses system
fonts. prefers-reduced-motion stops every animation on the final frame.

A new merged PR: add it to MERGED and rerun.
"""
from pathlib import Path
from xml.sax.saxutils import escape

ASSETS = Path(__file__).resolve().parent.parent / "assets"

# Merged upstream PRs, biggest project first. Stars as of 2026-10-02.
MERGED = [
    ("qdrant/qdrant", ["10448"], "test: Bits1_5 in the TurboQuant test matrices", "34.9k", "Sep 03"),
    ("Stellarium/stellarium", ["5133"], "AppImage: one QtWebEngineProcess path, not two", "10.0k", "Sep 28"),
    ("apache/datafusion", ["24916"], "RANGE window frames over Duration and Interval", "9.4k", "Sep 18"),
    ("sepinf-inc/IPED", ["2975", "2976"], "OCR: skip pages tesseract rejects; drop Tesseract 3", "3.0k", "Sep 24"),
    ("medic/cht-core", ["11439"], "task filter broke under Nepali digits", "558", "Sep 21"),
    ("unicef/adt-studio", ["876"], "CLI: skipped steps no longer drawn as complete", "76", "Oct 02"),
]

ROLES = ["LLM-agent infrastructure", "evals and retrieval", "quantum software tooling (Qiskit)"]

# lastro, report/findings.md section 3: 641 sessions, consecutive calls with >= 20k context.
TTL = [("0–2", 1), ("2–5", 4), ("5–10", 7), ("10–20", 7), ("20–30", 13),
       ("30–45", 17), ("45–60", 20), ("60–90", 97), ("90–180", 97), (">180", 93)]

# GitHub Primer colors, so the figures sit on the page like native UI.
THEMES = {
    "dark": {
        "canvas": "#0d1117", "subtle": "#151b23", "border": "#3d444d", "grid": "#262c36",
        "fg": "#f0f6fc", "muted": "#9198a1", "accent": "#4493f8", "done": "#ab7df8",
        "good": "#3fb950", "bad": "#f85149", "neutral": "#656c76",
    },
    "light": {
        "canvas": "#ffffff", "subtle": "#f6f8fa", "border": "#d1d9e0", "grid": "#eaeef2",
        "fg": "#1f2328", "muted": "#59636e", "accent": "#0969da", "done": "#8250df",
        "good": "#1a7f37", "bad": "#d1242f", "neutral": "#818b98",
    },
}

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

# Octicons git-merge-16 and star-16 (MIT, github.com/primer/octicons).
MERGE = ("M5.45 5.154A4.25 4.25 0 0 0 9.25 7.5h1.378a2.251 2.251 0 1 1 0 1.5H9.25A5.734 5.734 0 0 1 5 7.123v3.505"
         "a2.25 2.25 0 1 1-1.5 0V5.372a2.25 2.25 0 1 1 1.95-.218ZM4.25 13.5a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5Z"
         "m8.5-4.5a.75.75 0 1 0 0-1.5.75.75 0 0 0 0 1.5ZM5 3.25a.75.75 0 1 0 0 .005V3.25Z")
STAR = ("M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192"
        "a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374"
        "a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41"
        "l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456"
        "-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z")


def keyframes(name, frames):
    """@keyframes from (percent, declarations, timing function or None)."""
    body = "".join(f"{p:.2f}%{{{d}" + (f"animation-timing-function:{tf};" if tf else "") + "}"
                   for p, d, tf in frames)
    return f"@keyframes {name}{{{body}}}"


def svg(w, h, title, css, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-labelledby="t">\n<title id="t">{escape(title)}</title>\n<style>\n'
            f"text{{font-family:{SANS}}}.mono{{font-family:{MONO}}}\n" + "\n".join(css) +
            "\n@media (prefers-reduced-motion:reduce){*{animation:none!important}}\n</style>\n"
            + "\n".join(body) + "\n</svg>\n")


def card(t, w, h):
    return f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="12" fill="{t["canvas"]}" stroke="{t["border"]}"/>'


def hero(t):
    W, H, X = 880, 376, 28
    css, out = [], []

    # Window frame: title bar and body clipped to one rounded rectangle.
    out.append(f'<clipPath id="win"><rect width="{W}" height="{H}" rx="12"/></clipPath>')
    out.append(f'<g clip-path="url(#win)"><rect width="{W}" height="{H}" fill="{t["canvas"]}"/>'
               f'<rect width="{W}" height="36" fill="{t["subtle"]}"/>'
               f'<path d="M0 36.5H{W}" stroke="{t["border"]}"/></g>')
    out.append(f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="12" fill="none" stroke="{t["border"]}"/>')
    out += [f'<circle cx="{cx}" cy="18" r="5.5" fill="{t["border"]}"/>' for cx in (22, 40, 58)]
    out.append(f'<text class="mono" x="{W / 2}" y="22" text-anchor="middle" font-size="12" '
               f'fill="{t["muted"]}">edubraqd — upstream</text>')

    out.append(f'<text x="{X}" y="82" font-size="30" font-weight="600" fill="{t["fg"]}">Eduardo Alcantara</text>')
    out.append(f'<text x="{W - X}" y="82" text-anchor="end" font-size="13" '
               f'fill="{t["muted"]}">São Paulo · UTC−3 · open to remote</text>')

    # Roles, typed and erased in turn. Each role is a text with an opaque cover
    # that slides right one character per step; the caret rides the cover's edge.
    # textLength pins the text to the monospace grid whatever font the viewer has.
    cw, slot = 9.6, 4.6
    period = slot * len(ROLES)
    rx = X + 20
    out.append(f'<text class="mono" x="{X}" y="114" font-size="16" fill="{t["accent"]}">›</text>')
    for i, role in enumerate(ROLES):
        n, w = len(role), len(role) * cw
        start = i * slot
        typed = start + n * 0.06
        erased = start + slot - 0.35
        erasing = erased - n * 0.025
        pct = lambda s: s / period * 100
        last = i == len(ROLES) - 1
        vis = [(0, f"opacity:{0 if i else 1};", "step-end")]
        if i:
            vis.append((pct(start), "opacity:1;", "step-end"))
        if not last:
            vis.append((pct(start + slot), "opacity:0;", "step-end"))
        vis.append((100, f"opacity:{1 if last else 0};", None))
        move = [(0, "transform:translateX(0px);", "step-end" if i else f"steps({n},end)")]
        if i:
            move.append((pct(start), "transform:translateX(0px);", f"steps({n},end)"))
        move += [(pct(typed), f"transform:translateX({w:.1f}px);", "step-end"),
                 (pct(erasing), f"transform:translateX({w:.1f}px);", f"steps({n},end)"),
                 (pct(erased), "transform:translateX(0px);", "step-end"),
                 (100, "transform:translateX(0px);", None)]
        css += [keyframes(f"v{i}", vis), keyframes(f"k{i}", move),
                f".v{i}{{animation:v{i} {period:.1f}s infinite}}.k{i}{{animation:k{i} {period:.1f}s infinite}}"]
        out.append(f'<g class="v{i}" style="opacity:{0 if i else 1}">'
                   f'<text class="mono" x="{rx}" y="114" font-size="16" fill="{t["fg"]}" textLength="{w:.1f}" '
                   f'lengthAdjust="spacingAndGlyphs">{escape(role)}</text>'
                   f'<rect class="k{i}" x="{rx - 1}" y="96" width="{w + 4:.1f}" height="24" fill="{t["canvas"]}" '
                   f'style="transform:translateX({w:.1f}px)"/>'
                   f'<g class="blink"><rect class="k{i}" x="{rx}" y="99" width="9" height="19" fill="{t["accent"]}" '
                   f'style="transform:translateX({w:.1f}px)"/></g></g>')
    css.append("@keyframes blink{0%{opacity:1}50%{opacity:0}}.blink{animation:blink 1.1s step-end infinite}")

    out.append(f'<path d="M{X} 136.5H{W - X}" stroke="{t["grid"]}"/>')

    # The command types itself once, then its output arrives row by row.
    cmd = "gh search prs --author edubraqd --merged"
    cx, cwid = X + 18, len(cmd) * 8.4
    out.append(f'<text class="mono" x="{X}" y="166" font-size="14" fill="{t["muted"]}">$</text>')
    out.append(f'<text class="mono" x="{cx}" y="166" font-size="14" fill="{t["fg"]}" textLength="{cwid:.1f}" '
               f'lengthAdjust="spacingAndGlyphs">{cmd}</text>')
    out.append(f'<rect class="cmd" x="{cx - 1}" y="150" width="{cwid + 4:.1f}" height="22" fill="{t["canvas"]}" '
               f'style="transform:translateX({cwid:.1f}px)"/>')
    out.append(f'<rect class="cmdc" x="{cx}" y="152" width="8" height="17" fill="{t["accent"]}" style="opacity:0"/>')
    css.append(f"@keyframes cmd{{from{{transform:translateX(0)}}to{{transform:translateX({cwid:.1f}px)}}}}"
               f".cmd{{animation:cmd 1.3s steps({len(cmd)},end) .5s both}}")
    css.append(f"@keyframes cmdc{{from{{opacity:1;transform:translateX(0)}}to{{opacity:1;transform:translateX({cwid:.1f}px)}}}}"
               f".cmdc{{animation:cmdc 1.3s steps({len(cmd)},end) .5s backwards}}")

    prs = sum(len(nums) for _, nums, *_ in MERGED)
    out.append(f'<text class="mono fade" x="{X}" y="190" font-size="13" fill="{t["muted"]}">'
               f'Showing {prs} merged pull requests in {len(MERGED)} upstream projects</text>')
    css.append("@keyframes fade{from{opacity:0}}.fade{animation:fade .4s ease-out 2s both}")

    # Rows slide in; a ring pulses out of each merge icon, a wave every 8 s.
    css.append("@keyframes row{from{opacity:0;transform:translateX(-10px)}}"
               ".row{animation:row .5s cubic-bezier(.2,.7,.2,1) both}")
    css.append("@keyframes rip{0%{opacity:.8;transform:scale(.6)}14%,100%{opacity:0;transform:scale(2.2)}}"
               ".rip{animation:rip 8s ease-out infinite}")
    for i, (repo, nums, desc, stars, date) in enumerate(MERGED):
        y, delay = 222 + i * 26, 2.3 + i * 0.16
        out.append(f'<g transform="translate({X + 8} {y - 4.5})"><circle class="rip" r="9" fill="none" '
                   f'stroke="{t["done"]}" stroke-width="1.5" style="opacity:0;animation-delay:{delay:.2f}s"/></g>')
        out.append(f'<g class="row" style="animation-delay:{delay:.2f}s">'
                   f'<path transform="translate({X} {y - 12.5})" d="{MERGE}" fill="{t["done"]}"/>'
                   f'<text class="mono" x="{X + 26}" y="{y}" font-size="14" fill="{t["fg"]}">{escape(repo)}'
                   f'<tspan fill="{t["muted"]}">{" ".join("#" + n for n in nums)}</tspan></text>'
                   f'<text x="292" y="{y}" font-size="14" fill="{t["muted"]}">{escape(desc)}</text>'
                   f'<path transform="translate(716 {y - 11}) scale(.8125)" d="{STAR}" fill="{t["muted"]}"/>'
                   f'<text class="mono" x="734" y="{y}" font-size="13" fill="{t["muted"]}">{stars}</text>'
                   f'<text class="mono" x="{W - X}" y="{y}" text-anchor="end" font-size="13" '
                   f'fill="{t["muted"]}">{date}</text></g>')

    title = ("Eduardo Alcantara: LLM-agent infrastructure and quantum software. Merged upstream: "
             + ", ".join(f"{repo} " + " ".join("#" + n for n in nums) for repo, nums, *_ in MERGED) + ".")
    return svg(W, H, title, css, out)


def ttl(t):
    W, H = 880, 284
    x0, x1, yt, yb = 72, 856, 100, 228
    ph, band, bw = yb - yt, (x1 - x0) / len(TTL), 44
    cliff = next(i for i, (_, v) in enumerate(TTL) if v > 50)
    css, out = [], [card(t, W, H)]
    out.append(f'<text x="24" y="38" font-size="16" font-weight="600" fill="{t["fg"]}">The one-hour cliff</text>')
    out.append(f'<text x="24" y="60" font-size="13" fill="{t["muted"]}">Calls that re-wrote the whole cached '
               f'history, by idle gap before the call · 641 Claude Code sessions</text>')
    for v in (0, 50, 100):
        y = yb - ph * v / 100
        out.append(f'<path d="M{x0} {y}H{x1}" stroke="{t["border"] if v == 0 else t["grid"]}"/>')
        out.append(f'<text class="mono" x="{x0 - 10}" y="{y + 4}" text-anchor="end" font-size="11" '
                   f'fill="{t["muted"]}">{v}{"%" if v == 100 else ""}</text>')

    # Bars grow left to right like the clock running; past the TTL they overshoot.
    grow = ("0%{{transform:scaleY(0);animation-timing-function:{}}}9%{{transform:scaleY(1)}}"
            "92%{{transform:scaleY(1);opacity:1}}97%{{transform:scaleY(1);opacity:0}}100%{{transform:scaleY(0);opacity:0}}")
    css.append("@keyframes grow{" + grow.format("cubic-bezier(.2,.7,.2,1)") + "}"
               "@keyframes growc{" + grow.format("cubic-bezier(.3,1.5,.55,1)") + "}"
               ".bar{animation:grow 14s infinite backwards}.barc{animation:growc 14s infinite backwards}")
    css.append("@keyframes lab{0%,8%{opacity:0}12%,92%{opacity:1}97%,100%{opacity:0}}"
               ".lab{animation:lab 14s linear infinite backwards}")
    for i, (label, v) in enumerate(TTL):
        h = ph * v / 100
        r = min(4, h)
        x = x0 + i * band + (band - bw) / 2
        path = (f"M0 0V{r - h:.2f}Q0 {-h:.2f} {r:.2f} {-h:.2f}H{bw - r:.2f}"
                f"Q{bw} {-h:.2f} {bw} {r - h:.2f}V0Z")
        cls, color = ("barc", t["bad"]) if i >= cliff else ("bar", t["neutral"])
        out.append(f'<g transform="translate({x:.2f} {yb})"><path class="{cls}" d="{path}" fill="{color}" '
                   f'style="animation-delay:{0.15 * i:.2f}s"/></g>')
        out.append(f'<text class="mono" x="{x + bw / 2:.2f}" y="{yb + 18}" text-anchor="middle" font-size="11" '
                   f'fill="{t["muted"]}">{escape(label)}</text>')
    for i in (0, cliff - 1, cliff, len(TTL) - 1):
        v = TTL[i][1]
        out.append(f'<text class="mono lab" x="{x0 + i * band + band / 2:.2f}" y="{yb - ph * v / 100 - 7:.2f}" '
                   f'text-anchor="middle" font-size="12" fill="{t["fg"]}" style="animation-delay:{0.15 * i:.2f}s">{v}%</text>')
    tx = x0 + cliff * band
    out.append(f'<g class="lab" style="animation-delay:{0.15 * cliff:.2f}s">'
               f'<path d="M{tx:.2f} {yt - 14}V{yb}" stroke="{t["fg"]}" stroke-dasharray="3 3"/>'
               f'<text class="mono" x="{tx - 8:.2f}" y="{yt - 2}" text-anchor="end" font-size="12" '
               f'fill="{t["fg"]}">1 h cache TTL</text></g>')
    out.append(f'<text x="{x0}" y="{yb + 42}" font-size="12" fill="{t["muted"]}">idle gap before the call, minutes</text>')
    title = ("The one-hour cliff: share of Claude Code calls that re-wrote the whole cached history, by idle gap. "
             + ", ".join(f"{label} min {v}%" for label, v in TTL) + ".")
    return svg(W, H, title, css, out)


def cswap(t):
    W, H = 880, 192
    c, a, b = 78, 118, 158
    css, out = [], [card(t, W, H)]
    out.append(f'<text x="24" y="34" font-size="13" fill="{t["muted"]}"><tspan class="mono" fill="{t["accent"]}">'
               f'qiskit-aer#2463</tspan>  open-controlled SWAP, as the Python assembler emitted it · in review</text>')
    for name, y in (("c", c), ("a", a), ("b", b)):
        out.append(f'<text class="mono" x="44" y="{y + 5}" text-anchor="end" font-size="14" fill="{t["muted"]}">{name}</text>')
        out.append(f'<path d="M56 {y}H596" stroke="{t["muted"]}" stroke-width="1.2"/>')

    # A pulse runs the wires once per phase; gates drawn later hide it as it passes.
    css.append("@keyframes pulse{0%{opacity:0;transform:translateX(0)}4%{opacity:1}36%{opacity:1;transform:translateX(540px)}"
               "40%{opacity:0;transform:translateX(540px)}50%{opacity:0;transform:translateX(0)}54%{opacity:1}"
               "86%{opacity:1;transform:translateX(540px)}90%,100%{opacity:0;transform:translateX(540px)}}"
               ".pulse{animation:pulse 8s linear infinite}")
    out += [f'<circle class="pulse" cx="56" cy="{y}" r="3.5" fill="{t["accent"]}" style="opacity:0"/>' for y in (c, a, b)]

    def xgate(x, y, color):
        return (f'<rect x="{x - 15}" y="{y - 15}" width="30" height="30" rx="5" fill="{t["canvas"]}" '
                f'stroke="{color}" stroke-width="1.5"/><text class="mono" x="{x}" y="{y + 5}" text-anchor="middle" '
                f'font-size="15" fill="{color}">X</text>')

    # main: the X pair that implements the open control lands on target a too.
    css.append("@keyframes bug{0%,44%{opacity:1;transform:scale(1)}50%,94%{opacity:0;transform:scale(.4)}"
               "100%{opacity:1;transform:scale(1)}}.bug{animation:bug 8s ease-in-out infinite}")
    for gx in (190, 460):
        out.append(xgate(gx, c, t["fg"]))
        out.append(f'<g transform="translate({gx} {a})"><g class="bug" style="opacity:0">{xgate(0, 0, t["bad"])}</g></g>')
    sx = 325
    out.append(f'<path d="M{sx} {c + 7}V{b}" stroke="{t["fg"]}" stroke-width="2"/>')
    out.append(f'<circle cx="{sx}" cy="{c}" r="7" fill="{t["canvas"]}" stroke="{t["fg"]}" stroke-width="2"/>')
    out += [f'<path d="M{sx - 6} {y - 6}l12 12m0-12l-12 12" stroke="{t["fg"]}" stroke-width="2"/>' for y in (a, b)]

    out.append(f'<path d="M612 56V172" stroke="{t["grid"]}"/>')
    css.append("@keyframes stmain{0%,44%{opacity:1}50%,94%{opacity:0}100%{opacity:1}}"
               "@keyframes stfix{0%,44%{opacity:0}50%,94%{opacity:1}100%{opacity:0}}"
               ".stmain{animation:stmain 8s ease-in-out infinite}.stfix{animation:stfix 8s ease-in-out infinite}")
    px = 636
    for cls, ok, chip, line, value in (("stmain", False, "✗ main", "X also hits target a", "|sv[0]| = 0.5"),
                                       ("stfix", True, "✓ fix", "X only on the control", "|sv[0]| = 1.0")):
        color = t["good"] if ok else t["bad"]
        out.append(f'<g class="{cls}" style="opacity:{1 if ok else 0}">'
                   f'<rect x="{px}" y="58" width="64" height="22" rx="11" fill="none" stroke="{color}"/>'
                   f'<text class="mono" x="{px + 32}" y="73.5" text-anchor="middle" font-size="12" fill="{color}">{chip}</text>'
                   f'<text x="{px}" y="108" font-size="14" fill="{t["fg"]}">{line}</text>'
                   f'<text class="mono" x="{px}" y="140" font-size="22" fill="{t["fg"]}">{escape(value)}</text>'
                   f'<text x="{px}" y="162" font-size="12" fill="{t["muted"]}">issue reproducer: statevector, unitary, MPS</text></g>')
    title = ("qiskit-aer#2463: an open-controlled SWAP. Before the fix the X gates implementing the open control "
             "also hit target qubit a and |sv[0]| was 0.5; after it they act on the control only and |sv[0]| is 1.0.")
    return svg(W, H, title, css, out)


def main():
    ASSETS.mkdir(exist_ok=True)
    for name, build in (("hero", hero), ("ttl", ttl), ("cswap", cswap)):
        for theme, colors in THEMES.items():
            with open(ASSETS / f"{name}-{theme}.svg", "w", encoding="utf-8", newline="\n") as f:
                f.write(build(colors))


if __name__ == "__main__":
    main()
