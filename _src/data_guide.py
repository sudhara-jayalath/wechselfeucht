# Design guide content (bilingual). Some sections are rendered from data in JS (types, structures, care).

GUIDE = [
{"id":"regimes",
 "en_t":"Wechselfeucht in three states","de_t":"Wechselfeucht in drei Zuständen",
 "en":"""<p>A swale or retention basin is not one habitat but a sequence of wet and dry phases. Plan every planting zone for all three states:</p>
<ul>
<li><b>Dry summer.</b> Weeks without rain. The swale floor cracks and only permanent water remains.</li>
<li><b>Winter, high groundwater.</b> Soils stay saturated for weeks. In the Marsch the groundwater can come close to the surface.</li>
<li><b>After heavy rain.</b> The basin fills for hours to days. In infiltration swales the ponding is limited to about 30 cm.</li>
</ul>
<p>Plants on the swale floor must survive both extremes. That is why the palette leans on wechselfeuchte species such as tufted hair-grass, purple loosestrife and yellow iris rather than on pure wetland or pure meadow plants.</p>""",
 "de":"""<p>Eine Mulde oder ein Retentionsbecken ist kein einzelner Lebensraum, sondern eine Abfolge nasser und trockener Phasen. Plane jede Pflanzzone für alle drei Zustände:</p>
<ul>
<li><b>Trockener Sommer.</b> Wochen ohne Regen. Die Muldensohle reißt auf, nur das Dauerwasser bleibt.</li>
<li><b>Winter, hoher Grundwasserstand.</b> Die Böden sind wochenlang wassergesättigt. In der Marsch kann das Grundwasser bis nah an die Oberfläche steigen.</li>
<li><b>Nach Starkregen.</b> Das Becken füllt sich für Stunden bis Tage. In Versickerungsmulden ist der Einstau auf etwa 30 cm begrenzt.</li>
</ul>
<p>Pflanzen der Muldensohle müssen beide Extreme überstehen. Deshalb setzt die Palette auf wechselfeuchte Arten wie Rasen-Schmiele, Blut-Weiderich und Sumpf-Schwertlilie statt auf reine Sumpf- oder reine Wiesenpflanzen.</p>""",
 "action":"crosssection"},
{"id":"types",
 "en_t":"Choose the system","de_t":"Das passende System",
 "en":"<p>The system type sets how long water stands, and that decides which biotopes can grow. Typical combinations:</p>",
 "de":"<p>Der Anlagentyp bestimmt, wie lange Wasser steht – und damit, welche Biotope wachsen können. Typische Kombinationen:</p>",
 "table":"types"},
{"id":"site",
 "en_t":"Read the site: Geest or Marsch","de_t":"Den Standort lesen: Geest oder Marsch",
 "en":"""<div class="duo">
<div class="duo-card geest"><h4>Geest</h4><p>Sandy, acidic and often nutrient-poor. Groundwater is usually deep and infiltration works well, so infiltration swales and swale–trench systems are the default.</p><p class="small">Plant for acid soils: eared willow, alder buckthorn, devil's-bit scabious, lesser spearwort, harebell.</p></div>
<div class="duo-card marsch"><h4>Marsch</h4><p>Clay and silt, fertile, with groundwater close to the surface. Infiltration is limited, so retention, ditches and wet ponds carry the water.</p><p class="small">Plant for richer, base-rich soils: flowering-rush, arrowhead, hard rush, osier, white willow. Avoid compacting wet clay during construction.</p></div>
</div>
<div class="keybox"><h4>Key numbers from DWA-A 138-1 (2024)</h4>
<ul>
<li>Permeability (k<sub>f</sub>) generally between 1 × 10<sup>−3</sup> and 1 × 10<sup>−6</sup> m/s.</li>
<li>At least 1 m between the bottom of the infiltration facility and the mean highest groundwater level.</li>
<li>Ponding in infiltration swales limited to 30 cm; basins usually 0.5 m and more.</li>
<li>A vegetated soil layer of 20–30 cm treats the runoff.</li>
</ul>
<p class="small">Always design with the current standard and agree the details with the local water authority.</p></div>""",
 "de":"""<div class="duo">
<div class="duo-card geest"><h4>Geest</h4><p>Sandig, sauer und oft nährstoffarm. Das Grundwasser steht meist tief und die Versickerung funktioniert gut – Versickerungsmulden und Mulden-Rigolen-Elemente sind der Normalfall.</p><p class="small">Für saure Böden pflanzen: Ohr-Weide, Faulbaum, Teufelsabbiss, Brennender Hahnenfuß, Rundblättrige Glockenblume.</p></div>
<div class="duo-card marsch"><h4>Marsch</h4><p>Ton und Schluff, nährstoffreich, mit Grundwasser nah unter Flur. Die Versickerung ist begrenzt, deshalb tragen Retention, Gräben und Teiche das Wasser.</p><p class="small">Für reichere, basenreiche Böden pflanzen: Schwanenblume, Pfeilkraut, Blaugrüne Binse, Korb-Weide, Silber-Weide. Nassen Klei beim Bau nicht verdichten.</p></div>
</div>
<div class="keybox"><h4>Eckwerte aus dem DWA-A 138-1 (2024)</h4>
<ul>
<li>Durchlässigkeit (k<sub>f</sub>) in der Regel zwischen 1 × 10<sup>−3</sup> und 1 × 10<sup>−6</sup> m/s.</li>
<li>Mindestens 1 m zwischen Sohle der Versickerungsanlage und mittlerem höchstem Grundwasserstand.</li>
<li>Einstau in Versickerungsmulden auf 30 cm begrenzt; Becken meist ab 0,5 m.</li>
<li>Eine bewachsene Bodenzone von 20–30 cm reinigt den Abfluss.</li>
</ul>
<p class="small">Immer nach dem aktuellen Regelwerk planen und die Details mit der zuständigen Wasserbehörde abstimmen.</p></div>"""},
{"id":"grading",
 "en_t":"Grading for diversity","de_t":"Modellierung für Vielfalt",
 "en":"""<ul>
<li><b>Keep slopes flat.</b> 1:3 or flatter for mowing; 1:5 or flatter on shores where people, amphibians and dragonflies need gentle access.</li>
<li><b>Add micro-relief of ±10–20 cm on the swale floor.</b> A few centimetres decide between flood sward and tall-sedge swamp, so small hollows and humps create several communities on one floor.</li>
<li><b>Draw irregular outlines.</b> A curving edge is longer than a straight one and gives more transition habitat.</li>
<li><b>Make ditches asymmetric.</b> A flat, sunny berm on one side for tall herbs and amphibians, a steeper bank on the other.</li>
<li><b>Orient for sun.</b> Keep south and west banks open. Put willows and alders on the north or east side so they don't shade the water.</li>
<li><b>Vary the depth of permanent ponds.</b> Combine a shallow shelf of 0–30 cm with a deeper zone so not everything freezes or dries out.</li>
</ul>""",
 "de":"""<ul>
<li><b>Böschungen flach halten.</b> 1:3 oder flacher für die Mahd; 1:5 oder flacher an Ufern, an denen Menschen, Amphibien und Libellen sanft hinein- und herauskommen sollen.</li>
<li><b>Mikrorelief von ±10–20 cm in der Muldensohle.</b> Wenige Zentimeter entscheiden zwischen Flutrasen und Großseggenried – kleine Senken und Kuppen schaffen mehrere Gesellschaften auf einer Sohle.</li>
<li><b>Unregelmäßige Umrisse zeichnen.</b> Eine geschwungene Kante ist länger als eine gerade und bietet mehr Übergangslebensraum.</li>
<li><b>Gräben asymmetrisch ausbilden.</b> Auf einer Seite eine flache, sonnige Berme für Hochstauden und Amphibien, auf der anderen eine steilere Böschung.</li>
<li><b>Nach der Sonne ausrichten.</b> Süd- und Westufer offen halten. Weiden und Erlen auf die Nord- oder Ostseite, damit sie das Wasser nicht beschatten.</li>
<li><b>Dauerteiche in der Tiefe staffeln.</b> Eine Flachwasserzone von 0–30 cm mit einem tieferen Bereich kombinieren, damit nicht alles durchfriert oder austrocknet.</li>
</ul>"""},
{"id":"substrate",
 "en_t":"Soil and substrate","de_t":"Boden und Substrat",
 "en":"""<p>Where an infiltration swale treats runoff, DWA-A 138-1 asks for a vegetated soil layer of about 20–30 cm. It filters pollutants, so keep it. For biodiversity, its nutrient level is what counts:</p>
<ul>
<li>Use a low-nutrient, low-humus topsoil without compost or fertiliser. Rich topsoil favours grasses and nettles and crowds out flowering herbs.</li>
<li>On rims and slopes outside the treatment zone, lean sandy substrate is fine and raises diversity.</li>
<li>Reuse suitable site topsoil; it carries local seed and soil life.</li>
<li>Keep heavy machinery off the swale floor, especially on wet Marsch clay.</li>
</ul>""",
 "de":"""<p>Wo eine Versickerungsmulde Abfluss reinigt, fordert das DWA-A 138-1 eine bewachsene Bodenzone von etwa 20–30 cm. Sie hält Schadstoffe zurück und bleibt deshalb. Für die Artenvielfalt zählt ihr Nährstoffgehalt:</p>
<ul>
<li>Nährstoff- und humusarmen Oberboden ohne Kompost oder Dünger verwenden. Reicher Oberboden fördert Gräser und Brennnesseln und verdrängt Blühstauden.</li>
<li>An Rändern und Böschungen außerhalb der Reinigungszone ist mageres, sandiges Substrat gut und erhöht die Vielfalt.</li>
<li>Geeigneten Oberboden vor Ort wiederverwenden; er bringt heimisches Saatgut und Bodenleben mit.</li>
<li>Schwere Maschinen von der Muldensohle fernhalten, besonders auf nassem Marschklei.</li>
</ul>"""},
{"id":"flow",
 "en_t":"Inflow, outflow and sediment","de_t":"Zulauf, Ablauf und Sediment",
 "en":"""<ul>
<li><b>Break the energy at inflows</b> with a stone apron or cobbles so the planting doesn't wash out.</li>
<li><b>Add a sediment trap</b> or settling zone in front of the main basin. It is easier to clean than a whole planted floor.</li>
<li><b>Plan an emergency overflow</b> to the next element or to a safe flood route.</li>
<li><b>Keep shrubs and trees out of the main flow line</b> and away from overflows. DWA-A 138-1 (2024) now allows trees in surface infiltration swales; underground storage needs root protection.</li>
<li><b>Close the surface quickly</b> after construction: dense vegetation slows water and holds the soil.</li>
</ul>""",
 "de":"""<ul>
<li><b>Energie am Zulauf brechen</b> – mit Steinschüttung oder Pflaster, damit die Pflanzung nicht ausgespült wird.</li>
<li><b>Sedimentfang vorschalten</b> oder eine Absetzzone vor dem Hauptbecken anlegen. Sie lässt sich leichter reinigen als eine ganze bepflanzte Sohle.</li>
<li><b>Notüberlauf einplanen</b> – zum nächsten Element oder auf einen sicheren Notwasserweg.</li>
<li><b>Sträucher und Bäume aus der Hauptfließstrecke</b> und von Überläufen fernhalten. Das DWA-A 138-1 (2024) erlaubt inzwischen Bäume in oberirdischen Versickerungsmulden; unterirdische Speicher brauchen Wurzelschutz.</li>
<li><b>Oberfläche nach dem Bau schnell schließen</b> – dichte Vegetation bremst Wasser und hält den Boden.</li>
</ul>"""},
{"id":"planting",
 "en_t":"Planting and establishment","de_t":"Pflanzung und Etablierung",
 "en":"""<ul>
<li><b>Map the zones first,</b> then give each one a biotope (see the cross-section).</li>
<li><b>Sow certified Regiosaatgut</b> from Ursprungsgebiet 1, Nordwestdeutsches Tiefland: a wet-meadow or bank mix on the floor, a lean mix on the rims.</li>
<li><b>Add plugs of key herbs</b> in drifts of 5–15, and plant sedges and rushes where water stands longer.</li>
<li><b>Sow in autumn or early spring.</b> Plant marginal and aquatic plants from late April to June, when the water warms up.</li>
<li><b>Hold the water low in the first season</b> if you can, so plugs root before they are flooded.</li>
<li><b>Protect new pond plantings from geese</b> with temporary netting or fencing.</li>
<li><b>Water plugs in the first summer only;</b> after that the system should manage on its own.</li>
</ul>""",
 "de":"""<ul>
<li><b>Erst die Zonen kartieren,</b> dann jeder Zone ein Biotop zuordnen (siehe Querschnitt).</li>
<li><b>Zertifiziertes Regiosaatgut säen</b> aus Ursprungsgebiet 1, Nordwestdeutsches Tiefland: auf der Sohle eine Feuchtwiesen- oder Ufermischung, an den Rändern eine magere Mischung.</li>
<li><b>Initialpflanzen wichtiger Stauden</b> in Gruppen von 5–15 ergänzen; Seggen und Binsen dort pflanzen, wo das Wasser länger steht.</li>
<li><b>Im Herbst oder zeitigen Frühjahr säen.</b> Sumpf- und Wasserpflanzen von Ende April bis Juni pflanzen, wenn sich das Wasser erwärmt.</li>
<li><b>Wasserstand in der ersten Saison möglichst niedrig halten,</b> damit die Pflanzen anwurzeln, bevor sie überstaut werden.</li>
<li><b>Neue Teichpflanzungen vor Gänsen schützen</b> – mit vorübergehenden Netzen oder Zäunen.</li>
<li><b>Nur im ersten Sommer wässern;</b> danach sollte sich das System selbst tragen.</li>
</ul>"""},
{"id":"structures",
 "en_t":"Habitat structures","de_t":"Habitatstrukturen",
 "en":"<p>Plants feed animals; structures house them. Each of these costs little and brings in specific species. Tap an animal to see its profile.</p>",
 "de":"<p>Pflanzen ernähren Tiere, Strukturen beherbergen sie. Jede dieser Strukturen kostet wenig und holt bestimmte Arten auf die Fläche. Tippe auf ein Tier, um sein Profil zu sehen.</p>",
 "table":"structures"},
{"id":"care",
 "en_t":"Maintenance calendar","de_t":"Pflegekalender",
 "en":"<p>The main rule: never maintain everything at once. Work in sections so animals always find somewhere to retreat to.</p>",
 "de":"<p>Die wichtigste Regel: nie alles auf einmal pflegen. Abschnittsweise arbeiten, damit Tiere immer einen Rückzugsort finden.</p>",
 "table":"care",
 "en_after":"<p class=\"small\">§ 39 BNatSchG: trees, hedges and shrubs may not be cut back or removed between 1 March and 30 September, apart from gentle care cuts. Check inflows and sediment traps after every heavy rain as well.</p>",
 "de_after":"<p class=\"small\">§ 39 BNatSchG: Bäume, Hecken und Gebüsche dürfen vom 1. März bis 30. September nicht zurückgeschnitten oder beseitigt werden, ausgenommen schonende Pflegeschnitte. Zuläufe und Sedimentfänge zusätzlich nach jedem Starkregen prüfen.</p>"},
{"id":"rules",
 "en_t":"Rules and references","de_t":"Regelwerke und Quellen",
 "en":"""<ul class="refs">
<li><b>DWA-A 138-1 (2024)</b>: design, construction and operation of rainwater infiltration systems.</li>
<li><b>§ 40 BNatSchG</b>: since March 2020, plants and seed of non-local origin need approval in the open landscape.</li>
<li><b>§ 39 BNatSchG</b>: cutting period for trees and shrubs.</li>
<li><b>Origin regions</b>: Regiosaatgut from Ursprungsgebiet 1, Nordwestdeutsches Tiefland; gebietseigene Gehölze from Vorkommensgebiet 1, Norddeutsches Tiefland (<a href="https://www.bfn.de/sites/default/files/BfN/recht/Dokumente/leitfaden_gehoelze_.pdf" target="_blank" rel="noopener">BfN guideline</a>).</li>
<li><b>Hamburg</b>: RISA (RegenInfraStrukturAnpassung), <a href="https://www.risa-hamburg.de/wissen/bibliothek" target="_blank" rel="noopener">RISA library</a>; <a href="https://www.hamburg.de/politik-und-verwaltung/behoerden/bvm/die-themen-der-behoerde/grundlagen-strassenwesen/wassersensible-strassenraumgestaltung-text-193190" target="_blank" rel="noopener">Hinweise für eine wassersensible Straßenraumgestaltung</a>.</li>
<li><b>Flora</b>: Poppendieck et al. (2010), Der Hamburger Pflanzenatlas; Rote Liste der Farn- und Blütenpflanzen Hamburgs; <a href="https://www.floraweb.de" target="_blank" rel="noopener">FloraWeb</a>.</li>
</ul>
<p class="small">This tool gives planning orientation, not a design calculation. Tolerance, height and pollinator values are indicative guide values; check them against current standards, nursery data and the site.</p>""",
 "de":"""<ul class="refs">
<li><b>DWA-A 138-1 (2024)</b>: Planung, Bau und Betrieb von Anlagen zur Versickerung von Niederschlagswasser.</li>
<li><b>§ 40 BNatSchG</b>: seit März 2020 brauchen Pflanzen und Saatgut nicht gebietseigener Herkunft in der freien Natur eine Genehmigung.</li>
<li><b>§ 39 BNatSchG</b>: Schnittzeiten für Bäume und Gehölze.</li>
<li><b>Herkunftsregionen</b>: Regiosaatgut aus Ursprungsgebiet 1, Nordwestdeutsches Tiefland; gebietseigene Gehölze aus Vorkommensgebiet 1, Norddeutsches Tiefland (<a href="https://www.bfn.de/sites/default/files/BfN/recht/Dokumente/leitfaden_gehoelze_.pdf" target="_blank" rel="noopener">BfN-Leitfaden</a>).</li>
<li><b>Hamburg</b>: RISA (RegenInfraStrukturAnpassung), <a href="https://www.risa-hamburg.de/wissen/bibliothek" target="_blank" rel="noopener">RISA-Bibliothek</a>; <a href="https://www.hamburg.de/politik-und-verwaltung/behoerden/bvm/die-themen-der-behoerde/grundlagen-strassenwesen/wassersensible-strassenraumgestaltung-text-193190" target="_blank" rel="noopener">Hinweise für eine wassersensible Straßenraumgestaltung</a>.</li>
<li><b>Flora</b>: Poppendieck et al. (2010), Der Hamburger Pflanzenatlas; Rote Liste der Farn- und Blütenpflanzen Hamburgs; <a href="https://www.floraweb.de" target="_blank" rel="noopener">FloraWeb</a>.</li>
</ul>
<p class="small">Dieses Werkzeug gibt Planungsorientierung, ersetzt aber keine Bemessung. Toleranz-, Höhen- und Bestäuberwerte sind Richtwerte; mit aktuellem Regelwerk, Baumschuldaten und dem Standort abgleichen.</p>"""},
]

# system types table
TYPES = [
 {"en":"Infiltration swale","de":"Versickerungsmulde",
  "fn_en":"Infiltrates runoff through a vegetated soil layer; dry most of the time.","fn_de":"Versickert Abfluss durch eine bewachsene Bodenzone; meist trocken.",
  "d_en":"Ponding ≤ 30 cm, drains again quickly","d_de":"Einstau ≤ 30 cm, entleert sich rasch",
  "s_en":"Geest, permeable sand","s_de":"Geest, durchlässiger Sand",
  "b":["flutrasen","feuchtwiese","magerrasen"]},
 {"en":"Swale–trench system","de":"Mulden-Rigolen-Element",
  "fn_en":"A swale above a gravel or crate trench that stores water and releases it slowly; for less permeable soils.","fn_de":"Mulde über einer Kies- oder Kastenrigole, die Wasser speichert und langsam abgibt; für weniger durchlässige Böden.",
  "d_en":"Swale ≤ 30 cm plus storage below","d_de":"Mulde ≤ 30 cm plus Speicher darunter",
  "s_en":"Loamy soils, low kf","s_de":"Lehmige Böden, geringer kf-Wert",
  "b":["flutrasen","feuchtwiese","hochstauden"]},
 {"en":"Dry retention basin","de":"Retentionsbecken (trocken)",
  "fn_en":"Holds water temporarily and releases it throttled; dry between events.","fn_de":"Hält Wasser vorübergehend zurück und gibt es gedrosselt ab; zwischen den Ereignissen trocken.",
  "d_en":"Usually 0.5 m and more","d_de":"Meist ab 0,5 m",
  "s_en":"Geest and Marsch","s_de":"Geest und Marsch",
  "b":["flutrasen","hochstauden","grossseggen","feuchtwiese"]},
 {"en":"Wet retention pond","de":"Retentionsteich (Dauerstau)",
  "fn_en":"A permanent pool with storage space above it; settles sediment.","fn_de":"Dauerwasserfläche mit Rückhalteraum darüber; lässt Sediment absetzen.",
  "d_en":"Permanent water plus fluctuation","d_de":"Dauerwasser plus Schwankungsbereich",
  "s_en":"Marsch, high groundwater","s_de":"Marsch, hoher Grundwasserstand",
  "b":["offenwasser","roehricht","grossseggen","weiden"]},
 {"en":"Drainage ditch","de":"Graben",
  "fn_en":"Conveys and stores water in a linear network; the backbone of drainage in the Marsch.","fn_de":"Leitet und speichert Wasser in einem linearen Netz; das Rückgrat der Entwässerung in der Marsch.",
  "d_en":"Permanently or seasonally wet","d_de":"Dauerhaft oder zeitweise wasserführend",
  "s_en":"Marsch","s_de":"Marsch",
  "b":["offenwasser","roehricht","hochstauden","weiden"]},
 {"en":"Conveyance swale","de":"Fließmulde",
  "fn_en":"A shallow, vegetated channel that slows water and passes it on to the next element.","fn_de":"Flache, bewachsene Rinne, die Wasser bremst und zum nächsten Element weiterleitet.",
  "d_en":"Shallow flow","d_de":"Flacher Abfluss",
  "s_en":"Any","s_de":"Alle",
  "b":["flutrasen","feuchtwiese"]},
]

# maintenance calendar: (en, de, months)
CARE = [
 ("Mow wet meadows, 1st cut","Feuchtwiese mähen, 1. Schnitt",[6,7]),
 ("Mow wet meadows, 2nd cut","Feuchtwiese mähen, 2. Schnitt",[9]),
 ("Mow tall herbs (every 1–3 years)","Hochstauden mähen (alle 1–3 Jahre)",[9,10]),
 ("Cut reed in sections","Röhricht abschnittsweise schneiden",[1,2,10,11,12]),
 ("Coppice and pollard willows","Weiden auf den Stock setzen, Kopfweiden schneiden",[1,2,10,11,12]),
 ("Clear ditches in sections","Gräben abschnittsweise räumen",[10,11]),
 ("Cut back old stems","Altstängel zurückschneiden",[3]),
 ("Pull invasive plants","Invasive Pflanzen entfernen",[6,7,8]),
 ("Sow seed","Aussaat",[3,4,9,10]),
 ("Plant marginal plants","Sumpfpflanzen pflanzen",[4,5,6]),
 ("Check inflows and sediment traps","Zuläufe und Sedimentfang prüfen",[3,9]),
]
