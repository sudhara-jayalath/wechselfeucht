# Wechselfeucht Hamburg

An interactive, bilingual (English/German) guide to native plants, plant communities and fauna
for swales, ditches and retention basins in the Hamburg region: places that are sometimes wet
and sometimes dry (*wechselfeucht*).

**Live:** https://sudhara-jayalath.github.io/wechselfeucht/

- **Biotopes:** cross-sections of a Geest retention basin and a Marsch ditch in three water states, with the plant community, fauna, habitat structures and care for each zone
- **Plants:** 74 native species with German, English and Latin names, filterable by zone, soil, flood tolerance, flowering month, pollinator value and road salt
- **Fauna:** 37 animals linked to the plants and structures they depend on
- **My mix:** a planting mix checked for nectar gaps, spreading species and soil fit
- **Design guide:** system types, Geest and Marsch, grading, substrate, planting, structures and a maintenance calendar

Values are indicative guide values for planning orientation, not a design calculation.

---

## How it's published

Every push to `main` runs **Publish** (`.github/workflows/deploy.yml`). It runs `publish.py`,
which copies the page into `_site/` and downloads its web fonts so they are served from this
site. Visitors' browsers never contact Google. The page sets no cookies; it keeps the visitor's
language choice and plant mix in their own browser (local storage), and nothing is sent anywhere.

GitHub Pages must be set to **Settings → Pages → Source: GitHub Actions**.

## Changing the content

`index.html` is generated. Edit the files in `_src/`:

| File | Contents |
|---|---|
| `_src/data_species.py` | plants: names, zone, tolerances, height, flowering, notes |
| `_src/data_rest.py` | animals, biotopes, habitat structures, invasive species |
| `_src/data_guide.py` | design guide text, system types, maintenance calendar |
| `_src/template.html` | page design and interface text |

Then rebuild and push (needs Python 3, no extra packages):

```
python _src/build.py
git commit -am "Update plants" && git push
```

`build.py` checks that every link between plants, animals, biotopes and structures resolves
before it writes `index.html`.
