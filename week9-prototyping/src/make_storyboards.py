#!/usr/bin/env python3
"""Draws the 8-panel journey-map storyboards for The Neighbourhood Growing Table.

Usage: python3 make_storyboards.py <output_dir>
Writes one SVG per persona; render.js turns them into PNGs.
"""
import sys
from pathlib import Path
from PIL import ImageFont

W, H = 2000, 1414
COLS = [38, 527, 1016, 1505]
ROWS = [189, 780]
PW, PH = 457, 309

INK = '#222222'
GREEN = '#1f4435'
LEAF = '#4f8a5f'
BLUE = '#2b6a8f'
SCENE = '#f1f4ec'
GROUND = '#a9bcab'
WOOD = '#f3e2c2'
WOODLINE = '#b3804a'
WOODSOFT = '#c99a62'
BAY = '#d9e6ce'
BAYHI = '#b9d4a7'
STRIP = '#fcefd8'
DOT = '#a8691f'
SKIN = '#e9c6a3'
GREY = '#b8beb6'
BROWN = '#7b4b2a'
JUNE = '#5a9070'
RUBY = '#8e5ea8'
BEN = '#d9993b'
LIMB = '#1c3a31'
WHEEL = '#e2edf6'
CAN = '#cfe2ee'
CANLINE = '#2f79a8'
BASKET = '#e9c98f'
CALLOUT = '#fdeed5'
HL = '#dbe9f3'

SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"
HEAD = "Carlito, Calibri, 'Open Sans', sans-serif"

FONT_DIR = '/usr/share/fonts/truetype/liberation/'
_fonts = {}


def text_width(s, size, bold):
    key = (size, bold)
    if key not in _fonts:
        name = 'LiberationSans-Bold.ttf' if bold else 'LiberationSans-Regular.ttf'
        _fonts[key] = ImageFont.truetype(FONT_DIR + name, size)
    return _fonts[key].getlength(s)


def wrap(s, size, bold, max_w):
    lines, cur = [], ''
    for word in s.split(' '):
        trial = (cur + ' ' + word).strip()
        if cur and text_width(trial, size, bold) > max_w:
            lines.append(cur)
            cur = word
        else:
            cur = trial
    if cur:
        lines.append(cur)
    return lines


def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def f(v):
    return f'{v:.2f}'.rstrip('0').rstrip('.')


def pts(points):
    return ' '.join(f'{f(x)},{f(y)}' for x, y in points)


# ---------------------------------------------------------------- scene parts

def seedling(x, base=114.5, s=1.0, color=LEAF):
    def p(dx, dy):
        return (x + dx * s, base + dy * s)
    stem = f'<line x1="{f(x)}" y1="{f(base)}" x2="{f(x)}" y2="{f(base - 12.5 * s)}" stroke="{color}" stroke-width="{f(2.7 * s)}"/>'
    left = pts([p(0.6, -9), p(-8.6, -15.2), p(-7.2, -17.6), p(0.6, -12.6)])
    right = pts([p(-0.6, -8.6), p(10.4, -15.6), p(12.6, -18.8), p(9.2, -19.4), p(-0.6, -12.8)])
    return (stem + f'<polygon points="{left}" fill="{color}"/>'
            + f'<polygon points="{right}" fill="{color}"/>')


def table(tx, hi=None, active=None, skip=()):
    """Front view of the growing table. hi: 'A'/'B' bay to emphasise,
    active: index of the slider marker shown in blue, skip: seedlings left out."""
    o = []
    for lx in (tx + 13.5, tx + 190):
        o.append(f'<rect x="{f(lx)}" y="143" width="14.5" height="52" fill="{WOOD}" stroke="{WOODSOFT}" stroke-width="1.2"/>')
    o.append(f'<rect x="{f(tx)}" y="115.5" width="217" height="27" rx="5" fill="{WOOD}" stroke="{WOODLINE}" stroke-width="2"/>')
    for name, bx, seeds in (('A', tx + 5, (22, 48.5)), ('B', tx + 150.5, (17.5, 43.5))):
        fill = BAYHI if hi == name else BAY
        o.append(f'<rect x="{f(bx)}" y="105.5" width="61" height="24.5" rx="5" fill="{fill}" stroke="{WOODSOFT}" stroke-width="1.1"/>')
        for i, sx in enumerate(seeds):
            if (name, i) not in skip:
                o.append(seedling(bx + sx))
    o.append(f'<rect x="{f(tx + 79)}" y="123" width="61" height="13" rx="5" fill="{STRIP}" stroke="{WOODSOFT}" stroke-width="1.2"/>')
    for i, dx in enumerate((88.5, 109.5, 130.5)):
        if i == active:
            o.append(f'<circle cx="{f(tx + dx)}" cy="129.5" r="4.2" fill="{BLUE}"/>')
        else:
            o.append(f'<circle cx="{f(tx + dx)}" cy="129.5" r="3.6" fill="{DOT}"/>')
    return ''.join(o)


def marker_xy(tx, i):
    return (tx + (88.5, 109.5, 130.5)[i], 129.5)


def head(x, y, r, hair):
    k = r / 14.0
    cap = [(-13.6, -3), (-13.2, -9), (-9, -13.6), (-4, -15.6), (2, -16.2), (8, -14.4),
           (12.4, -10), (13.8, -3.4), (10.6, -6.6), (6.6, -4.8), (2.4, -7.4), (-2.6, -5.2),
           (-7, -7.8), (-10.8, -4.6)]
    if hair == GREY:
        cap = [(-14.4, -1), (-13.4, -9), (-10.6, -14.6), (-5, -17.6), (1, -17), (4.4, -18.6),
               (8, -15.6), (12.6, -12.6), (14, -6.6), (9.4, -9.4), (3.4, -10.6), (-3, -9.6),
               (-8.6, -6.4), (-11, -1.4)]
    d = pts([(x + a * k, y + b * k) for a, b in cap])
    return (f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="{SKIN}" stroke="{LIMB}" stroke-width="1.4"/>'
            f'<polygon points="{d}" fill="{hair}" stroke="{hair}" stroke-width="0.8" stroke-linejoin="round"/>')


def limb(points, w=4.6):
    return (f'<polyline points="{pts(points)}" fill="none" stroke="{LIMB}" stroke-width="{f(w)}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def june(wx, pose='rest', flip=False):
    o = []
    o.append(f'<line x1="-9.5" y1="110" x2="-9.5" y2="152" stroke="{BLUE}" stroke-width="3.6"/>')
    o.append(f'<rect x="-4" y="110" width="23" height="44.5" fill="{JUNE}"/>')
    o.append(f'<line x1="-9.5" y1="152" x2="37" y2="152.6" stroke="{BLUE}" stroke-width="2.4"/>')
    o.append(limb([(17, 155.2), (38.5, 155.6), (42, 186)], 5))
    o.append(f'<circle cx="0" cy="172" r="22.5" fill="{WHEEL}" stroke="{BLUE}" stroke-width="4.6"/>')
    o.append(f'<circle cx="0" cy="172" r="5.8" fill="{BLUE}"/>')
    o.append(f'<circle cx="38" cy="188.4" r="6.2" fill="#f4f8fb" stroke="{BLUE}" stroke-width="2.8"/>')
    o.append(head(7, 84, 14, GREY))
    if pose == 'reach':
        o.append(limb([(13.5, 124), (28.5, 135), (53, 116)]))
    else:
        o.append(limb([(13.5, 124), (29, 134), (30, 151)]))
    t = f'translate({f(wx)},0) scale(-1,1)' if flip else f'translate({f(wx)},0)'
    return f'<g transform="{t}">{"".join(o)}</g>'


def ruby(x, arm='down', side='L', walk=False):
    """arm: 'down' or an (x, y) hand position. side: which shoulder the arm uses."""
    o = []
    if walk:
        o.append(limb([(x - 4.5, 166), (x - 15, 196)], 5))
        o.append(limb([(x + 4.5, 166), (x + 12, 196)], 5))
    else:
        o.append(limb([(x - 5.5, 166), (x - 11, 196)], 5))
        o.append(limb([(x + 5.5, 166), (x + 11, 196)], 5))
    o.append(f'<polygon points="{pts([(x - 11.5, 114), (x + 12, 114), (x + 15, 167.5), (x - 14, 167.5)])}" fill="{RUBY}"/>')
    o.append(head(x, 95.5, 14, BROWN))
    sgn = -1 if side == 'L' else 1
    if arm == 'down':
        o.append(limb([(x + sgn * 10.5, 121), (x + sgn * 15, 141)]))
    else:
        o.append(limb([(x + sgn * 8.5, 120.5), arm]))
    return ''.join(o)


def ben(x, arm='down', side='L', walk=False):
    o = []
    if walk:
        o.append(limb([(x - 5, 166), (x - 14, 196)], 5))
        o.append(limb([(x + 5, 166), (x + 12.5, 196)], 5))
    else:
        o.append(limb([(x - 6.5, 166), (x - 10, 196)], 5))
        o.append(limb([(x + 7, 166), (x + 11.5, 196)], 5))
    o.append(f'<polygon points="{pts([(x - 10.5, 147), (x + 11, 147), (x + 14.5, 167.5), (x - 13.5, 167.5)])}" fill="{BEN}"/>')
    o.append(head(x, 128, 12.3, BROWN))
    sgn = -1 if side == 'L' else 1
    if arm == 'down':
        o.append(limb([(x + sgn * 9.5, 151.5), (x + sgn * 14.5, 164)]))
    else:
        o.append(limb([(x + sgn * 8.5, 152), arm]))
    return ''.join(o)


def can(cx, cy, flip=False):
    """Watering can. Spout points left unless flipped."""
    o = (f'<polyline points="-14,-2 -27.2,-14.5 -35.8,-15" fill="none" stroke="{BLUE}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
         f'<polyline points="11.2,-9.5 24.8,-12.5 24.8,3.5 15.2,5.5" fill="none" stroke="{BLUE}" stroke-width="2.6" stroke-linejoin="round"/>'
         f'<rect x="-15.2" y="-11.5" width="30.5" height="23" rx="6" fill="{CAN}" stroke="{CANLINE}" stroke-width="1.8"/>')
    t = f'translate({f(cx)},{f(cy)})' + (' scale(-1,1)' if flip else '')
    return f'<g transform="{t}">{o}</g>'


def drops(points):
    return ''.join(f'<circle cx="{f(x)}" cy="{f(y)}" r="3" fill="{BLUE}"/>' for x, y in points)


def basket(bx, by=110, s=1.0):
    o = (f'<polyline points="8.5,0 10,-10.5 29.5,-10.5 30.5,0" fill="none" stroke="{WOODLINE}" stroke-width="2.5" stroke-linejoin="round"/>'
         f'<rect x="0" y="0" width="39" height="24.5" rx="6" fill="{BASKET}" stroke="{WOODLINE}" stroke-width="2"/>'
         + ''.join(f'<line x1="{dx}" y1="5" x2="{dx}" y2="21" stroke="{WOODLINE}" stroke-width="1.5"/>' for dx in (10, 20, 30.5)))
    return f'<g transform="translate({f(bx)},{f(by)}) scale({f(s)})">{o}</g>'


def drop_icon(x, y, s=1.0):
    """Water drop, tip at (x, y), about 33 px tall at s=1."""
    d = (f'M0,0.5 C-3,8.5 -11.5,15.5 -11.5,22.5 A11.5,11.5 0 0 0 11.5,22.5 '
         f'C11.5,15.5 3,8.5 0,0.5 Z')
    return f'<path transform="translate({f(x)},{f(y)}) scale({f(s)})" d="{d}" fill="{BLUE}"/>'


def magnifier(x, y, s=1.0):
    return (f'<g transform="translate({f(x)},{f(y)}) scale({f(s)})">'
            f'<circle cx="-2" cy="-3" r="9.5" fill="none" stroke="{BLUE}" stroke-width="2.6"/>'
            f'<line x1="4.6" y1="3.8" x2="15" y2="14" stroke="{BLUE}" stroke-width="3.2" stroke-linecap="round"/></g>')


def tips_card(x, y, s=1.0):
    return (f'<g transform="translate({f(x)},{f(y)}) scale({f(s)})">'
            f'<rect x="-21.5" y="-19" width="43" height="38" rx="6" fill="#ffffff" stroke="{WOODSOFT}" stroke-width="1.6"/>'
            + ''.join(f'<line x1="-13" y1="{yy}" x2="{x2}" y2="{yy}" stroke="{c}" stroke-width="2.4"/>'
                      for yy, x2, c in ((-8, 13, LEAF), (0, 13, GROUND), (8, 13, GROUND))) + '</g>')


def callout(x0, y0, hi, target):
    """Enlarged picture slider: water / check / leave to grow. hi = active icon."""
    xs = (x0 + 22.5, x0 + 65.5, x0 + 109)
    o = [f'<line x1="{f(xs[hi])}" y1="{f(y0 + 48.5)}" x2="{f(target[0])}" y2="{f(target[1] - 3.5)}" stroke="{BLUE}" stroke-width="2.4" stroke-linecap="round"/>']
    o.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="131.5" height="48.5" rx="8" fill="{CALLOUT}" stroke="{WOODSOFT}" stroke-width="1.5"/>')
    o.append(f'<circle cx="{f(xs[hi])}" cy="{f(y0 + 19.5)}" r="18.5" fill="{HL}"/>')
    o.append(drop_icon(xs[0], y0 + 3.5, 0.94))
    o.append(magnifier(xs[1], y0 + 19.5))
    o.append(seedling(xs[2], y0 + 31.5, 1.35))
    for i, x in enumerate(xs):
        c = BLUE if i == hi else DOT
        o.append(f'<line x1="{f(x - 10)}" y1="{f(y0 + 40.5)}" x2="{f(x + 10)}" y2="{f(y0 + 40.5)}" stroke="{c}" stroke-width="1.6"/>')
        o.append(f'<circle cx="{f(x)}" cy="{f(y0 + 40.5)}" r="3.6" fill="{c}"/>')
    return ''.join(o)


def arrow(x1, y1, x2, y2, w=2.6, hs=7.5):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - hs * math.cos(a - 0.62), y2 - hs * math.sin(a - 0.62))
    p2 = (x2 - hs * math.cos(a + 0.62), y2 - hs * math.sin(a + 0.62))
    return (f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{BLUE}" stroke-width="{w}" stroke-linecap="round"/>'
            f'<polyline points="{pts([p1, (x2, y2), p2])}" fill="none" stroke="{BLUE}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>')


def attention(x, y=46):
    o = ''
    for x1, y1, x2, y2 in ((0, 0, 0, 18), (-19.5, 7, -10, 22), (19, 7, 10, 22)):
        o += f'<line x1="{f(x + x1)}" y1="{f(y + y1)}" x2="{f(x + x2)}" y2="{f(y + y2)}" stroke="{LEAF}" stroke-width="2.5"/>'
    return o


def qmark(x, y):
    return f'<text x="{f(x)}" y="{f(y)}" font-family="{SANS}" font-weight="700" font-size="27" fill="{BLUE}" text-anchor="middle">?</text>'


def edge_mark(x1, x2, y):
    return (f'<line x1="{f(x1)}" y1="{f(y)}" x2="{f(x2)}" y2="{f(y)}" stroke="{BLUE}" stroke-width="2.6" stroke-linecap="round"/>'
            f'<line x1="{f(x1)}" y1="{f(y - 6)}" x2="{f(x1)}" y2="{f(y + 6)}" stroke="{BLUE}" stroke-width="2.6" stroke-linecap="round"/>'
            f'<line x1="{f(x2)}" y1="{f(y - 6)}" x2="{f(x2)}" y2="{f(y + 6)}" stroke="{BLUE}" stroke-width="2.6" stroke-linecap="round"/>')


def bay_edge(bx):
    """Highlights the top and outer edge of the bay whose left side is at bx."""
    d = f'M{f(bx + 8)},105.5 L{f(bx + 56)},105.5 Q{f(bx + 61)},105.5 {f(bx + 61)},110.5 L{f(bx + 61)},126'
    return f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="3.2" stroke-linecap="round"/>'


# ------------------------------------------------------------ touchpoint icons

def icon(kind):
    if kind == 'bay':
        return (f'<rect x="-29.5" y="-3" width="59" height="17" rx="4.5" fill="{BAY}" stroke="{WOODSOFT}" stroke-width="1.3"/>'
                + seedling(-11.5, 4.5, 1.05) + seedling(13.5, 4.5, 1.05))
    if kind == 'edge':
        return (f'<rect x="-29.5" y="-3" width="59" height="17" rx="4.5" fill="{BAY}" stroke="{WOODSOFT}" stroke-width="1.3"/>'
                + f'<path d="M-2,-3 L25,-3 Q29.5,-3 29.5,1.5 L29.5,10" fill="none" stroke="{BLUE}" stroke-width="3" stroke-linecap="round"/>'
                + seedling(-11.5, 4.5, 1.05) + seedling(13.5, 4.5, 1.05))
    if kind == 'arrow':
        return arrow(-26, 6, 26, 6, 2.6, 8)
    if kind == 'check':
        return magnifier(-3, 2, 1.25)
    if kind == 'basket':
        return basket(-20, -4, 1.02)
    if kind == 'tips':
        return tips_card(0, 4, 1.0)
    if kind == 'water':
        return drop_icon(0, -14, 1.1)
    if kind == 'grow':
        return seedling(-1, 18, 2.0)
    if kind == 'can':
        return can(4, 6)
    if kind == 'worktop':
        return (f'<rect x="-32" y="-2" width="64" height="16" rx="4.5" fill="{WOOD}" stroke="{WOODLINE}" stroke-width="1.6"/>'
                f'<rect x="-17" y="2" width="34" height="8" rx="3.5" fill="{STRIP}" stroke="{WOODSOFT}" stroke-width="1"/>'
                + ''.join(f'<circle cx="{dx}" cy="6" r="2.2" fill="{DOT}"/>' for dx in (-10, 0, 10)))
    if kind == 'front':
        return (f'<rect x="-32" y="-2" width="64" height="16" rx="4.5" fill="{WOOD}" stroke="{WOODLINE}" stroke-width="1.6"/>'
                f'<line x1="-26" y1="14" x2="26" y2="14" stroke="{BLUE}" stroke-width="3" stroke-linecap="round"/>')
    raise ValueError(kind)


# ------------------------------------------------------------------- template

def panel(idx, p, uid):
    col, top = COLS[idx % 4], ROWS[idx // 4]
    o = []
    o.append(f'<text x="{col + 1}" y="{top - 8}" font-family="{SANS}" font-weight="700" font-size="18.5" fill="{GREEN}" xml:space="preserve">Action  {idx + 1:02d}</text>')
    o.append(f'<rect x="{col}" y="{top}" width="{PW}" height="{PH}" fill="#ffffff" stroke="{INK}" stroke-width="2"/>')
    sx, sy = col + 10, top + 14
    o.append(f'<clipPath id="{uid}c{idx}"><rect x="0" y="0" width="438" height="208" rx="10"/></clipPath>')
    o.append(f'<g transform="translate({sx},{sy})" clip-path="url(#{uid}c{idx})">'
             f'<rect x="0" y="0" width="438" height="208" rx="10" fill="{SCENE}"/>'
             f'<line x1="14" y1="197.5" x2="422.5" y2="197.5" stroke="{GROUND}" stroke-width="2"/>'
             f'{p["scene"]}</g>')
    # writing lines
    for dy in (356, 403):
        o.append(f'<line x1="{col + 1}" y1="{top + dy}" x2="{col + 272}" y2="{top + dy}" stroke="{INK}" stroke-width="1.6" stroke-dasharray="8 5"/>')
    for dy in (451, 498, 545):
        o.append(f'<line x1="{col + 1}" y1="{top + dy}" x2="{col + 453}" y2="{top + dy}" stroke="{INK}" stroke-width="1.6" stroke-dasharray="8 5"/>')
    # caption
    o.append(f'<rect x="{col + 4}" y="{top + PH + 2}" width="254" height="100" fill="#ffffff"/>')
    lines = wrap(p['action'], 26, True, 236)
    if len(lines) > 2:  # keep the ruled line's first dash from showing beside a third line
        o.append(f'<rect x="{col - 1}" y="{top + 396}" width="14" height="14" fill="#ffffff"/>')
    for i, line in enumerate(lines):
        o.append(f'<text x="{col + 9}" y="{top + 345 + i * 31}" font-family="{SANS}" font-weight="700" font-size="26" fill="{GREEN}">{esc(line)}</text>')
    # question box
    if p.get('question'):
        o.append(f'<rect x="{col + 2}" y="{top + 453}" width="453" height="87" rx="10" fill="#e4eef6"/>')
        o.append(f'<text x="{col + 13}" y="{top + 473}" font-family="{SANS}" font-weight="700" font-size="15.5" fill="{BLUE}">Question to test</text>')
        for i, line in enumerate(wrap(p['question'], 20, False, 428)):
            o.append(f'<text x="{col + 13}" y="{top + 502 + i * 25}" font-family="{SANS}" font-size="20" fill="{GREEN}">{esc(line)}</text>')
    # touchpoint circle
    cx, cy, r = col + 371, top + 338, 107
    o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f0f0f0" stroke="#111111" stroke-width="1.6" stroke-dasharray="7 5"/>')
    import math
    ra = r + 7
    a1, a2 = math.radians(199), math.radians(246)
    x1, y1 = cx + ra * math.cos(a1), cy + ra * math.sin(a1)
    x2, y2 = cx + ra * math.cos(a2), cy + ra * math.sin(a2)
    o.append(f'<path id="{uid}a{idx}" d="M{f(x1)},{f(y1)} A{ra},{ra} 0 0 1 {f(x2)},{f(y2)}" fill="none"/>')
    o.append(f'<text font-family="{HEAD}" font-size="18.5" fill="#4a4a4a" letter-spacing="0.3"><textPath href="#{uid}a{idx}" startOffset="2">touchpoint</textPath></text>')
    o.append(f'<g transform="translate({cx},{cy - 46})">{icon(p["icon"])}</g>')
    o.append(f'<text x="{cx}" y="{cy - 1}" font-family="{SANS}" font-weight="700" font-size="15.5" fill="{BLUE}" text-anchor="middle">Touchpoint</text>')
    for i, line in enumerate(wrap(p['touchpoint'], 22, False, 178)):
        o.append(f'<text x="{cx}" y="{cy + 27 + i * 27}" font-family="{SANS}" font-size="22" fill="{GREEN}" text-anchor="middle">{esc(line)}</text>')
    return ''.join(o)


def page(title, page_no, panels, uid):
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         f'<text x="38" y="78" font-family="{HEAD}" font-weight="700" font-size="45" fill="{INK}" letter-spacing="1.2">JOURNEY MAP</text>',
         f'<text x="38" y="131" font-family="{HEAD}" font-weight="700" font-size="25" fill="{INK}">TITLE:</text>',
         f'<text x="122" y="132" font-family="{SANS}" font-weight="700" font-size="31.5" fill="{GREEN}" xml:space="preserve">{esc(title)}</text>',
         f'<line x1="117" y1="151" x2="1470" y2="151" stroke="{INK}" stroke-width="1.6" stroke-dasharray="8 5"/>',
         f'<text x="1722" y="108" font-family="{HEAD}" font-weight="700" font-size="21" fill="{INK}">page:</text>',
         f'<text x="1821" y="113" font-family="{SANS}" font-weight="700" font-size="24.5" fill="{GREEN}">{esc(page_no)}</text>',
         f'<line x1="1780" y1="130" x2="1962" y2="130" stroke="{INK}" stroke-width="1.6" stroke-dasharray="8 5"/>']
    for i, p in enumerate(panels):
        o.append(panel(i, p, uid))
    o.append('</svg>')
    return '\n'.join(o)


# --------------------------------------------------------------------- stories

CONCEPT = 'The Neighbourhood Growing Table'


def june_story():
    tx = 194
    wide_slab = (f'<rect x="366" y="107" width="15" height="89" fill="{WOOD}" stroke="{WOODSOFT}" stroke-width="1.2"/>'
                 f'<rect x="190" y="90" width="213" height="19" rx="5" fill="{WOOD}" stroke="{WOODLINE}" stroke-width="2"/>'
                 f'<rect x="201" y="75" width="30" height="12" rx="4" fill="{STRIP}" stroke="{WOODSOFT}" stroke-width="1.2"/>')
    return [
        dict(action='Notices the herbs.', touchpoint='Growing bay A', icon='bay',
             scene=table(tx, hi='A') + attention(tx + 33) + june(106)),
        dict(action='Rolls up to the table.', touchpoint='Clear front space', icon='arrow',
             scene=table(tx) + june(106) + arrow(152, 185, 186, 185)),
        dict(action='Lines up with the worktop.', touchpoint='Knee clearance', icon='arrow',
             scene=wide_slab + june(172) + edge_mark(212, 352, 172) ),
        dict(action='Reaches for the slider.', touchpoint='Picture slider', icon='check',
             question='Can she reach the slider while seated?',
             scene=table(tx, active=1) + callout(256, 35.5, 1, marker_xy(tx, 1)) + june(169, 'reach')),
        dict(action='Shows Ben where to water.', touchpoint='Growing bay A', icon='bay',
             scene=table(tx, hi='A') + can(280, 104.5) + drops([(241.5, 101), (235, 112.5), (245, 122.5)])
             + june(165, 'reach') + ben(313, arm=(276, 145.5))),
        dict(action='Passes the basket to Ruby.', touchpoint='Shared worktop', icon='basket',
             scene=table(tx) + basket(230.5) + arrow(235.5, 76, 286, 76) + june(172, 'reach') + ruby(349, arm=(312.5, 114))),
        dict(action='Shares a growing tip.', touchpoint='Growing tips board', icon='tips',
             scene=table(tx) + tips_card(263, 104) + june(169, 'reach') + ruby(379)),
        dict(action='Rolls away.', touchpoint='Clear front space', icon='arrow',
             scene=table(tx) + june(120, flip=True) + arrow(72, 170, 31, 170)),
    ]


def ruby_story():
    tx = 84          # table sits left so Ruby can come in from the bay B side
    jx = tx - 27     # June's wheel when rolled in
    side = tx + 229  # Ruby standing beside bay B
    return [
        dict(action='Spots the plants.', touchpoint='Growing bay B', icon='bay',
             scene=table(tx, hi='B') + attention(tx + 181) + ruby(392)),
        dict(action='Walks to the side.', touchpoint='Growing bay B', icon='bay',
             scene=table(tx, hi='B') + arrow(350, 185, 314, 185) + ruby(374, walk=True)),
        dict(action='Stands beside the planter.', touchpoint='Bay edge', icon='edge',
             scene=table(tx, hi='B') + bay_edge(tx + 150.5)
             + ruby(side, arm=(tx + 215, 109))),
        dict(action='Checks the leaves.', touchpoint='Check icon', icon='check',
             scene=table(tx, hi='B', active=1) + callout(tx + 44, 26, 1, marker_xy(tx, 1))
             + ruby(side, arm=(tx + 200, 104))),
        dict(action='Picks a herb that is ready.', touchpoint='Growing bay B', icon='bay',
             scene=table(tx, hi='B', skip=(('B', 1),)) + seedling(tx + 196, 96, 1.15)
             + arrow(tx + 180, 100, tx + 180, 80, 2.4, 6.5) + ruby(side, arm=(tx + 199, 98))),
        dict(action='Puts the herb in the basket.', touchpoint='Harvest basket', icon='basket',
             scene=table(tx, skip=(('B', 1),)) + basket(tx + 92) + seedling(tx + 122, 98, 1.15)
             + arrow(tx + 108, 72, tx + 108, 93, 2.4, 6.5)
             + june(jx, 'reach') + ruby(tx + 166, arm=(tx + 126, 100))),
        dict(action='Slides the marker to “Leave to grow”.', touchpoint='Picture slider', icon='grow',
             question='Will she update the slider before she leaves?',
             scene=table(tx, active=2, skip=(('B', 1),)) + callout(tx + 6, 22, 2, marker_xy(tx, 2))
             + ruby(tx + 172, arm=(tx + 135, 129))),
        dict(action='Leaves with the family.', touchpoint='Path beside the table', icon='arrow',
             scene=table(205, skip=(('B', 1),)) + arrow(50, 170, 20, 170)
             + june(98, flip=True) + ben(147, walk=True) + ruby(181, walk=True)),
    ]


def ben_story():
    tx = 194
    return [
        dict(action='Notices the water icon.', touchpoint='Picture sliders', icon='water',
             scene=table(tx, active=0) + callout(256, 35.5, 0, marker_xy(tx, 0)) + attention(tx + 84.5, 6)
             + ben(118)),
        dict(action='Walks over with June.', touchpoint='Front approach', icon='arrow',
             scene=table(tx) + ben(46, walk=True) + june(110) + arrow(156, 185, 188, 185)),
        dict(action='Finds a spot next to Ruby.', touchpoint='Front edge', icon='front',
             scene=table(tx) + june(165) + ruby(352) + ben(306)
             + arrow(306, 84, 306, 106, 2.4, 6.5)),
        dict(action='Points to the water icon.', touchpoint='Picture slider', icon='water',
             question='Does he know what the water icon means?',
             scene=table(tx, active=0) + callout(256, 35.5, 0, marker_xy(tx, 0))
             + ben(312, arm=(286.5, 133.5)) + qmark(335, 111)),
        dict(action='Waters the plant with help.', touchpoint='Small watering can', icon='can',
             scene=table(tx, hi='A') + can(271, 104.5) + drops([(232.5, 101), (226, 112.5), (236, 122.5)])
             + june(165, 'reach') + ben(324, arm=(297, 108))),
        dict(action='Passes the watering can back.', touchpoint='Shared worktop', icon='can',
             scene=table(tx) + can(259, 99) + arrow(292, 68, 242, 68)
             + june(165, 'reach') + ben(312, arm=(285, 102))),
        dict(action='Puts the can down.', touchpoint='Shared worktop', icon='worktop',
             scene=table(tx) + can(286, 103.8) + arrow(286, 62, 286, 84, 2.4, 6.5)
             + ben(338, arm=(313, 110))),
        dict(action='Follows the family.', touchpoint='Front approach', icon='arrow',
             scene=table(205) + arrow(50, 170, 20, 170)
             + june(98, flip=True) + ruby(146, walk=True) + ben(183, walk=True)),
    ]


# June's page 1 already exists; june_story() redraws it and was used to match its style.
# Add ('storyboard-1-june', f'{CONCEPT}  |  June (68)', '1 of 3', june_story) to regenerate it.
PAGES = [
    ('storyboard-2-ruby', f'{CONCEPT}  |  Ruby (36)', '2 of 3', ruby_story),
    ('storyboard-3-ben', f'{CONCEPT}  |  Ben (5)', '3 of 3', ben_story),
]

if __name__ == '__main__':
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for i, (name, title, page_no, story) in enumerate(PAGES):
        (out / f'{name}.svg').write_text(page(title, page_no, story(), f'p{i}'), encoding='utf-8')
        print('wrote', out / f'{name}.svg')
