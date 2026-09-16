# -*- coding: utf-8 -*-
"""Génère tools/carte.py : les tracés SVG des 4 départements bretons.

Source : contours officiels france-geojson (licence ODbL), simplifiés par
Douglas-Peucker. À relancer seulement si l'on veut changer la précision.
"""
import json, math

def charger(num):
    g = json.load(open("/tmp/geo/%s.json" % num))["geometry"]
    polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    return [anneau[0] for anneau in polys]

def simplifier(pts, eps):
    if len(pts) < 3: return pts
    def dist(p, a, b):
        if a == b: return math.hypot(p[0]-a[0], p[1]-a[1])
        t = max(0, min(1, ((p[0]-a[0])*(b[0]-a[0]) + (p[1]-a[1])*(b[1]-a[1])) /
                       ((b[0]-a[0])**2 + (b[1]-a[1])**2)))
        return math.hypot(p[0]-(a[0]+t*(b[0]-a[0])), p[1]-(a[1]+t*(b[1]-a[1])))
    dmax, idx = 0, 0
    for i in range(1, len(pts)-1):
        d = dist(pts[i], pts[0], pts[-1])
        if d > dmax: dmax, idx = d, i
    if dmax > eps:
        return simplifier(pts[:idx+1], eps)[:-1] + simplifier(pts[idx:], eps)
    return [pts[0], pts[-1]]

def aire(pts):
    s = 0
    for i in range(len(pts)):
        x1, y1 = pts[i]; x2, y2 = pts[(i+1) % len(pts)]
        s += x1*y2 - x2*y1
    return abs(s) / 2

NUMS = ["22", "29", "35", "56"]
brut = {n: charger(n) for n in NUMS}
tous = [p for n in NUMS for a in brut[n] for p in a]
lon0, lon1 = min(p[0] for p in tous), max(p[0] for p in tous)
lat0, lat1 = min(p[1] for p in tous), max(p[1] for p in tous)
k = math.cos(math.radians((lat0+lat1)/2))
L = 1000.0
H = L * (lat1-lat0) / ((lon1-lon0)*k)

def projeter(p):
    return (round((p[0]-lon0)/(lon1-lon0)*L, 1), round((lat1-p[1])/(lat1-lat0)*H, 1))

EPS, AIRE_MIN = 3.2, 12.0
centres = {}        # îlots de moins de 12 px² : invisibles à l'écran
sorties, total = {}, 0
for n in NUMS:
    chemins = []
    for anneau in brut[n]:
        pts = simplifier([projeter(p) for p in anneau], EPS)
        if len(pts) < 4 or aire(pts) < AIRE_MIN: continue
        chemins.append("M" + "L".join("%g %g" % p for p in pts) + "Z")
    d = "".join(chemins)
    sorties[n] = d; total += len(d)
    # centre du plus grand contour : point d'ancrage du numéro
    principal = max((simplifier([projeter(p) for p in a], EPS) for a in brut[n]), key=aire)
    centres[n] = (round(sum(p[0] for p in principal)/len(principal), 1),
                  round(sum(p[1] for p in principal)/len(principal), 1))
    print("%s : %d contour(s) retenus, %d caractères" % (n, len(chemins), len(d)))

open("tools/carte.py", "w", encoding="utf-8").write(
    '# -*- coding: utf-8 -*-\n"""Tracés SVG des départements bretons.\n\n'
    'Générés depuis les contours officiels (france-geojson, licence ODbL) puis\n'
    'simplifiés. Fichier produit par tools/generer_carte.py — ne pas éditer.\n"""\n\n'
    'CARTE_LARGEUR = %d\nCARTE_HAUTEUR = %d\n\nTRACES = {\n' % (round(L), round(H))
    + "".join('    "%s": "%s",\n' % (n, sorties[n]) for n in NUMS) + "}\n\n"
    + "CENTRES = {\n"
    + "".join('    "%s": (%s, %s),\n' % (n, centres[n][0], centres[n][1]) for n in NUMS)
    + "}\n")
print("\nviewBox %d x %d | total %.1f Ko" % (L, H, total/1024))
