#!/usr/bin/env python3
"""Rebuild Wechselfeucht Hamburg from its data files.

Edit the data in data_species.py, data_rest.py and data_guide.py (or the page
design in template.html), then run:

    python _src/build.py

It checks that every cross-reference between plants, animals, biotopes and
structures resolves, then rewrites index.html in the repository root.
Commit and push, and GitHub publishes the new version.

    python _src/build.py --artifact out.html
also writes a fragment without <html>/<head> for hosts that add their own.
"""
import json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from data_species import S, COLOURS
from data_rest import GROUPS, ROLES, STRUCT, F, B, INVASIVE
from data_guide import GUIDE, TYPES, CARE

species = []
for r in S:
    (sid,z,de,en,la,t,fl,dr,h,m,c,p,hb,so,sa,nen,nde,flags) = r
    species.append(dict(id=sid,z=z,de=de,en=en,la=la,t=t,fl=fl,dr=dr,h=h,m=list(m),c=c,p=p,hb=hb,so=so,sa=sa,n=dict(en=nen,de=nde),f=flags))
sids = {s['id'] for s in species}
assert len(sids) == len(species), "duplicate species id"

fauna = []
for r in F:
    (fid,g,de,en,la,m,sten,stde,txen,txde,pl,sr) = r
    fauna.append(dict(id=fid,g=g,de=de,en=en,la=la,m=list(m),st=dict(en=sten,de=stde),tx=dict(en=txen,de=txde),pl=[list(x) for x in pl],sr=sr))
fids = {f['id'] for f in fauna}
assert len(fids) == len(fauna)

biotopes = []
for r in B:
    (bid,nen,nde,alen,alde,wen,wde,ren,rde,so,den,dde,core,comp,fa,sr,cen,cde,veg) = r
    biotopes.append(dict(id=bid,n=dict(en=nen,de=nde),al=dict(en=alen,de=alde),wh=dict(en=wen,de=wde),rg=dict(en=ren,de=rde),so=so,d=dict(en=den,de=dde),core=core,comp=comp,fauna=fa,sr=sr,care=dict(en=cen,de=cde),veg=veg))
bids = {b['id'] for b in biotopes}

errors = []
for s in species:
    if s['c'] not in COLOURS: errors.append(('colour', s['id'], s['c']))
for f in fauna:
    if f['g'] not in GROUPS: errors.append(('group', f['id']))
    for pid, role in f['pl']:
        if pid not in sids: errors.append(('fauna plant', f['id'], pid))
        if role not in ROLES: errors.append(('role', f['id'], role))
    for st in f['sr']:
        if st not in STRUCT: errors.append(('fauna struct', f['id'], st))
for b in biotopes:
    for pid in b['core'] + b['comp']:
        if pid not in sids: errors.append(('bio plant', b['id'], pid))
    if len(set(b['core'] + b['comp'])) != len(b['core'] + b['comp']): errors.append(('bio dup plant', b['id']))
    for fid in b['fauna']:
        if fid not in fids: errors.append(('bio fauna', b['id'], fid))
    for st in b['sr']:
        if st not in STRUCT: errors.append(('bio struct', b['id'], st))
for t in TYPES:
    for bid in t['b']:
        if bid not in bids: errors.append(('type bio', t['en'], bid))
used = set()
for b in biotopes: used |= set(b['core'] + b['comp'])
orph = sids - used
if orph: errors.append(('species not in any biotope', sorted(orph)))
fused = set()
for b in biotopes: fused |= set(b['fauna'])
forph = fids - fused
if forph: errors.append(('fauna not in any biotope', sorted(forph)))
if errors:
    for e in errors: print('ERROR', e)
    sys.exit(1)

data = dict(
    species=species,
    colours={k: list(v) for k, v in COLOURS.items()},
    fauna=fauna,
    groups={k: dict(en=v[0], de=v[1]) for k, v in GROUPS.items()},
    roles={k: dict(en=v[0], de=v[1]) for k, v in ROLES.items()},
    struct={k: dict(en=v[0], de=v[1], wen=v[2], wde=v[3]) for k, v in STRUCT.items()},
    biotopes=biotopes,
    invasive=[dict(de=r[0], en=r[1], la=r[2], p=dict(en=r[3], de=r[4]), a=dict(en=r[5], de=r[6])) for r in INVASIVE],
    guide=GUIDE,
    types=TYPES,
    care=[dict(en=r[0], de=r[1], m=r[2]) for r in CARE],
)
js = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
tpl = (HERE / 'template.html').read_text(encoding='utf-8')
assert '__DATA__' in tpl and '<!--HEAD-END-->' in tpl and '__HOMELINK__' in tpl
page = tpl.replace('__DATA__', js)

DESCRIPTION = ("Native plants, plant communities and fauna for swales, ditches and "
               "retention basins in Hamburg. Bilingual, English and German.")

# Standalone page: a full HTML document.
head, body = page.split('<!--HEAD-END-->', 1)
site_page = (
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    f'<meta name="description" content="{DESCRIPTION}">\n'
    '<meta property="og:title" content="Wechselfeucht Hamburg">\n'
    f'<meta property="og:description" content="{DESCRIPTION}">\n'
    '<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'
    + head.strip() + '\n</head>\n<body>\n'
    + body.replace('__HOMELINK__', '').strip()
    + '\n</body>\n</html>\n'
)
target = HERE.parent / 'index.html'
target.write_text(site_page, encoding='utf-8')
print('species', len(species), 'fauna', len(fauna), 'biotopes', len(biotopes),
      '->', target.name, f'({len(site_page.encode()) // 1024} KB)')

if '--artifact' in sys.argv:
    out = Path(sys.argv[sys.argv.index('--artifact') + 1])
    out.write_text(page.replace('<!--HEAD-END-->\n', '').replace('__HOMELINK__', ''), encoding='utf-8')
    print('fragment ->', out)
