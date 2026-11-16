#!/usr/bin/env python3
"""Line-drawing template of The Neighbourhood Growing Table, meant to be copied by hand.

Usage: python3 make_sketch_template.py <output_dir>
Writes sketch-template.svg; render.js turns it into a PNG.
"""
import sys
from pathlib import Path

W, H = 1700, 1202
INK = '#1e1e1e'
SANS = "'Liberation Sans', Arial, Helvetica, sans-serif"


def line(x1, y1, x2, y2, w=5):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="{w}" '
            f'stroke-linecap="round"/>')


def poly(points, w=5):
    d = ' '.join(f'{x},{y}' for x, y in points)
    return (f'<polyline points="{d}" fill="none" stroke="{INK}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def rect(x, y, w, h, rx=6, sw=5):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="#ffffff" '
            f'stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round"/>')


def circle(cx, cy, r, fill='#ffffff', sw=5):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{INK}" stroke-width="{sw}"/>'


def path(d, fill='none', w=5):
    return (f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{w}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def sprout(x, base=440, s=1.0):
    top = base - 46 * s
    def leaf(sign):
        return path(f'M{x},{top} C{x + sign * 10 * s},{top - 22 * s} {x + sign * 30 * s},{top - 26 * s} '
                    f'{x + sign * 38 * s},{top - 28 * s} C{x + sign * 36 * s},{top - 10 * s} '
                    f'{x + sign * 20 * s},{top} {x},{top} Z', '#ffffff', 4)
    return line(x, base, x, top, 4) + leaf(-1) + leaf(1)


def label(x, y, text, size=30, anchor='middle', weight=400):
    return (f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="{size}" font-weight="{weight}" '
            f'fill="{INK}" text-anchor="{anchor}">{text}</text>')


def arrow(x1, y1, x2, y2):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    h = 13
    p1 = (round(x2 - h * math.cos(a - 0.5), 1), round(y2 - h * math.sin(a - 0.5), 1))
    p2 = (round(x2 - h * math.cos(a + 0.5), 1), round(y2 - h * math.sin(a + 0.5), 1))
    return line(x1, y1, x2, y2, 3) + poly([p1, (x2, y2), p2], 3)


def build():
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="2000" height="1414">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>']

    # ground
    o.append(line(90, 820, 1610, 820, 4))

    # table: worktop with an overhang on the left, two legs
    o.append(rect(560, 568, 40, 252, 2))
    o.append(rect(1160, 568, 40, 252, 2))
    o.append(rect(430, 520, 820, 48))

    # growing bays and plants
    for bx, xs in ((520, (570, 670)), (1020, (1065, 1150))):
        o.append(rect(bx, 440, 200, 80))
        for x in xs:
            o.append(sprout(x))

    # growing tips board
    o.append(line(810, 520, 810, 385))
    o.append(rect(755, 295, 110, 90))
    o.append(line(772, 320, 848, 320, 4) + line(772, 340, 848, 340, 4) + line(772, 360, 825, 360, 4))

    # harvest basket
    o.append(path('M915,470 Q945,404 975,470'))
    o.append(path('M905,470 L985,470 L975,520 L915,520 Z', '#ffffff'))
    o.append(line(932, 478, 935, 512, 3) + line(958, 478, 955, 512, 3))

    # picture sliders on the front of the worktop, enlarged underneath
    o.append(rect(800, 529, 200, 30, 13, 4))
    for x in (850, 900, 950):
        o.append(circle(x, 544, 7, INK, 0))
    o.append(line(900, 559, 900, 628, 3))
    o.append(rect(715, 628, 370, 168, 18, 4))
    o.append(label(900, 664, 'Picture sliders', 27, weight=700))
    o.append(path('M775,683 C765,701 755,711 755,723 A20,20 0 0 0 795,723 C795,711 785,701 775,683 Z', '#ffffff', 4))
    o.append(circle(874, 708, 17, '#ffffff', 4) + line(886, 721, 902, 738, 5))
    o.append(sprout(1005, 742, 0.62))
    o.append(label(775, 779, 'water', 23) + label(878, 779, 'check', 23) + label(1005, 779, 'leave to grow', 23))

    # older neighbour in a wheelchair, rolled in under the overhang
    o.append(poly([(212, 466), (246, 472), (252, 650)]))            # push handle and backrest
    o.append(line(455, 772, 512, 772))                             # footrest
    o.append(line(292, 442, 285, 640))                             # body
    o.append(poly([(285, 640), (452, 626), (498, 766)]))           # leg
    o.append(circle(300, 705, 115))                                # big wheel
    o.append(circle(300, 705, 9, INK, 0))
    o.append(circle(482, 795, 25))                                 # small wheel
    o.append(circle(292, 400, 42))                                 # head
    o.append(poly([(290, 492), (400, 542), (545, 430)]))           # arm reaching the plants

    # child with the small watering can
    o.append(circle(1330, 440, 42))
    o.append(line(1330, 482, 1330, 665))
    o.append(line(1330, 665, 1298, 820) + line(1330, 665, 1362, 820))
    o.append(poly([(1330, 525), (1266, 478), (1262, 374)]))
    o.append(line(1330, 525, 1372, 612))
    o.append(path('M1252,332 Q1286,349 1252,366'))
    o.append(line(1190, 356, 1148, 318) + line(1139, 327, 1157, 309, 4))
    o.append(rect(1190, 322, 62, 53, 9))
    o.append(line(1140, 342, 1137, 354, 3) + line(1153, 346, 1151, 358, 3) + line(1127, 348, 1123, 359, 3))

    # parent
    o.append(circle(1490, 228, 42))
    o.append(line(1490, 270, 1490, 560))
    o.append(line(1490, 560, 1455, 820) + line(1490, 560, 1525, 820))
    o.append(line(1490, 335, 1432, 448) + line(1490, 335, 1545, 452))

    # labels
    o.append(label(790, 232, 'Growing tips board'))
    o.append(arrow(790, 246, 800, 286))
    o.append(label(620, 330, 'Growing bay A'))
    o.append(arrow(620, 344, 620, 430))
    o.append(label(1085, 262, 'Growing bay B'))
    o.append(arrow(1108, 276, 1108, 430))
    o.append(label(985, 178, 'Harvest basket'))
    o.append(arrow(962, 192, 948, 428))
    o.append(label(300, 866, 'older neighbour', 27))
    o.append(label(1330, 866, 'child', 27))
    o.append(label(1490, 866, 'parent', 27))
    o.append(label(458, 918, 'Open space underneath: a wheelchair can roll in', 30, 'start'))
    o.append(arrow(535, 886, 535, 646))

    # title
    o.append(label(850, 1062, 'The Neighbourhood Growing Table', 60, weight=700))
    o.append(line(392, 1084, 1308, 1084, 4))

    o.append('</svg>')
    return '\n'.join(o)


if __name__ == '__main__':
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    (out / 'sketch-template.svg').write_text(build(), encoding='utf-8')
    print('wrote', out / 'sketch-template.svg')
