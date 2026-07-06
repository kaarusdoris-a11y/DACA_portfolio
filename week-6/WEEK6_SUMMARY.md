# Nädal 6 — Visualiseerimise Andmed (Data Storytelling)

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Teema:** Visualiseerimise andmed — annotatsioonid, andmelood, publiku disain  
**Töövihikud:** N6 IT (Iseseisva õppe töövihik) + N6 GT (Grupitöö juhend)  
**Versioon:** 2.9

---

## Selle nädala eesmärgid

1. Lisada diagrammidele annotatsioonid, mis selgitavad andmete tähendust
2. Kirjutada andmelugusid (data story), mis muudavad numbrid veenvaks narratiiviks
3. Kohandada sama andmestiku esitlust vastavalt erinevatele sihtrühmadele (CEO, IT, turundus)

---

## 1. Annotatsioonid

### Miks annotatsioonid?

Anna Mets: *"Ma arvasin, et hea diagramm räägib ise. Aga Kristi küsis: 'Miks see tõus detsembris on?' Ilma annotatsioonita pidin ma seda suuliselt seletama. See tähendab, et diagramm üksi EI RÄÄKINUD."*

Knaflic (*Storytelling with Data* Ch 5): *"Every element on a page either adds to or takes away from the story you're trying to tell."*

### Annotatsioonide tüübid

| Tüüp | Mida teeb | Millal kasutada | UrbanStyle näide |
|---|---|---|---|
| **Pealkiri (title)** | Ütleb, MIS on graafiku teema | Alati | "UrbanStyle'i kuine käive 2024" |
| **Alapealkiri (subtitle)** | Lisab konteksti või põhijärelduse | Kui pealkiri ei ütle piisavalt | "Kasv +15% — jõulukampaania mõjul" |
| **Teljemärgised** | Selgitab, mida teljed näitavad | Alati | "Käive (EUR)", "Kuud" |
| **Andmesildid** | Konkreetne väärtus otse graafikul | Oluliste punktide juures | "€35 200" tipppunktis |
| **Viitejooned** | Näitab eesmärki või keskmist | Konteksti loomiseks | "Aasta keskmise käive = €25 400" |
| **Tekstiboks** | Selgitab anomaaliat | Kui arv vajab seletust | "↑ Jõulukampaania +€8K" |

---

## 2. Andmelood — "Ja mis siis?" meetod

### Kolm taset

Knaflic Ch 6 põhjal — hea andmelugu liigub faktist tähenduseni:

```
Andmepunkt  →  "Ja mis siis?"  →  "Ja mis siis?"  →  Soovitus/Tegevus
(fakt)          (kontekst)          (tähendus)
```

### Näited UrbanStyle andmetega

**Andmepunkt: "Detsembri käive oli €35 200"**
- Tase 1: See on kõrgeim kuu aastas
- Tase 2: Jõulukampaania tõstis käivet 43% võrreldes novembriga
- Tase 3 (tegevus): Tuleks planeerida sarnane kampaania ka jaanuari languse leevendamiseks

**Andmepunkt: "Juuli käive langes €19 700-le (eelmise kuu €24 500-lt)"**
- Tase 1: Langus 20% — hooajaline mõju
- Tase 2: Pärnu kaupluse käive tõusis samal ajal (+35%) — kliendid liiguvad suveks mujale
- Tase 3: Tallinna kaupluses võiks suvel rõhku nihutada e-poele

**Andmepunkt: "73% klientidest on vanuses 25–35"**
- Tase 1: Selge sihtgrupp on millenniaalid
- Tase 2: See vanusegrupp on digitaalselt aktiivne — e-poe osakaal 28% on seletatav
- Tase 3: Turundus peaks olema sotsiaalmeedia-fookusega, eriti Instagram/TikTok

**Andmepunkt: "Denim Jacket on müüdud 850 tk — laoseis 12 tk"**
- Tase 1: Kriitiliselt madal laoseis topsellers'il
- Tase 2: Praeguse müügitempoga jätkub ladu 4–5 päevaks
- Tase 3: Kiirtellimus tarnijalt on vajalik, muidu kaotame müügitulu

**Andmepunkt: "Tartu kesk. tellimus €28, Tallinna oma €42"**
- Tase 1: 50% erinevus kaupluste vahel
- Tase 2: Tallinna klientide ostujõud on suurem, või tootemiks on erinev
- Tase 3: Tartu sortimendis võiks katsetada premium tooteid / upselling strateegiat

---

## 3. Publiku disain

Sama andmestik, erinev fookus vastavalt sihtrühmale:

| Sihtrühm | Fookus | Keelekasutus | Üksikasja tase |
|---|---|---|---|
| **CEO (Kristi)** | Koondmõõdikud, kasv, risk | Äriline, kõrgtase | KPI-d + 1 peamine trend |
| **Turundus (Anna)** | Kliendisegmendid, kampaaniad | Kliendikeskne | Segmentide võrdlus |
| **IT/arendus** | Andmekvaliteet, tehniline detail | Tehniline täpsus | Täielik andmestik |
| **Investorid** | Kasvupotentsiaal, ROI | Finantskeelne | Prognoosid + suundumused |

### Juhtide kokkuvõte (Executive Summary)

Kristi investorikoosoleku jaoks — 3 lauset:

> *"UrbanStyle'i 2024. aasta kogukäive on €305 000, mis on +15% võrreldes 2023. aastaga. Kasvu veab jõulukampaania (+43% detsembris) ja e-poe laienemine (28% käibest). Peamine risk: Denim Jacket laoseis on kriitiliselt madal — kiirtellimus on vajalik Q1 müügipotentsiaali säilitamiseks."*

---

## Grupitöö (N6 GT) — Kaupluse-spetsiifilised Dashboard'id

**Väljakutse (Anna Mets, Marketing Lead):**  
*"Iga kaupluse juhataja tahab OMAENDA dashboard'i. Aga juhatusel peab olema koondvaade. Kuidas me seda teeme? Ja see peab LUGU JUTUSTAMA!"*

**Kontekst:** Nädal 5 lõi dashboard'i prototüübi. Nüüd lisatakse lugu ja kontekst.

**Rollid grupis:**

| Roll | Kaupluse lugu | Põhiküsimus |
|---|---|---|
| **Roll A** | Tallinna kaupluse lugu | Linnakaupluse kasv vs e-poe konkurents |
| **Roll B** | Tartu kaupluse lugu | Ülikoolikaupluse hooajalisus |
| **Roll C** | Pärnu kaupluse lugu | Suvekuurordi hooajalisus — risk ja võimalus |
| **Roll D** | E-poe lugu | Digitaalne kasv, geograafia puudub |

**Baastase (kohustuslik):**
- Dashboard näitab ainult oma kaupluse andmeid
- Juhtide kokkuvõte toob välja peamise mustri
- Vähemalt 2 annotatsiooni on lisatud
- Andmelugu sisaldab hooajalist analüüsi

---

## Annoteeritud diagramm — Plotly koodiga

```python
import plotly.express as px
import plotly.graph_objects as go

fig = px.line(df_monthly, x='month', y='total_price',
              title='UrbanStyle kuine käive 2024<br><sub>Kasv +15% — jõulukampaania mõjul</sub>')

# Andmesildi lisamine tipppunktile
fig.add_annotation(x='Detsember', y=35200,
                   text="↑ Jõulukampaania<br>+€8K vs november",
                   showarrow=True, arrowhead=2)

# Viitejoon — aasta keskmine
fig.add_hline(y=25400, line_dash="dot",
              annotation_text="Aasta keskmine: €25 400")

fig.update_layout(xaxis_title="Kuud", yaxis_title="Käive (EUR)")
fig.show()
```

---

## Lugemismaterjal

- Knaflic *Storytelling with Data* Ch 5: Think Like a Designer
- Knaflic Ch 6: Tell a Story — kuidas lisada narratiivi voog
- DACA Kursus 6, Moodul 2: Visualiseerimistööriistade kasutamine

---

*DACA26 · Nädal 6 · UrbanStyle.ltd andmeanalüüs*
---

## 🇬🇧 In English

### Week 6 — Data Storytelling
**Individual Summary**

Programme: DACA — Data Analyst Career Accelerator
Topic: Data visualisation — annotations, data stories, audience design
Workbooks: W6 IL (Independent Learning) + W6 GT (Group Work)

#### Week Goals
- Add annotations to charts that explain the meaning of data
- Write data stories that turn numbers into a compelling narrative
- Adapt the same dataset's presentation for different audiences (CEO, IT, Marketing)

#### Annotations

Anna Mets: "I thought a good chart speaks for itself. But Kristi asked: 'Why is there a spike in December?' Without an annotation I had to explain it verbally. That means the chart alone DID NOT speak."

Knaflic (Storytelling with Data Ch 5): *"Every element on a page either adds to or takes away from the story you're trying to tell."*

**Annotation types:**

| Type | What it does | When to use | UrbanStyle example |
|------|-------------|-------------|-------------------|
| Title | States WHAT the chart shows | Always | "UrbanStyle monthly revenue 2024" |
| Subtitle | Adds context or key insight | When title isn't enough | "Growth +15% — driven by Christmas campaign" |
| Axis labels | Explains what axes show | Always | "Revenue (EUR)", "Months" |
| Data labels | Concrete value directly on chart | At key points | "€35,200" at peak |
| Reference line | Shows target or average | For context | "Annual avg revenue = €25,400" |
| Text box | Explains an anomaly | When a number needs explanation | "↑ Christmas campaign +€8K" |

#### Data Stories — The "So What?" Method

Good data storytelling moves from fact to meaning:

**Data point → "So what?" → "So what?" → Recommendation/Action**

**UrbanStyle examples:**

- December revenue was €35,200
  - → This is the highest month of the year
  - → Christmas campaign boosted revenue 43% vs November
  - → **Action:** Plan a similar campaign to ease January's decline

- Denim Jacket sold 850 units — stock: 12 units
  - → Critically low stock on top seller
  - → At current sales pace, stock lasts 4–5 days
  - → **Action:** Urgent order from supplier needed, or revenue will be lost

- Tartu avg order €28, Tallinn avg €42
  - → 50% difference between stores
  - → Tallinn customers have higher purchasing power, or product mix differs
  - → **Action:** Trial premium products / upselling strategy in Tartu

#### Audience Design

Same dataset, different focus per audience:

| Audience | Focus | Language | Detail level |
|----------|-------|----------|-------------|
| CEO (Kristi) | Summary metrics, growth, risk | Business, high-level | KPIs + 1 main trend |
| Marketing (Anna) | Customer segments, campaigns | Customer-centric | Segment comparison |
| IT/Dev | Data quality, technical detail | Technical precision | Full dataset |
| Investors | Growth potential, ROI | Financial language | Forecasts + trends |

**Executive Summary for Kristi's investor meeting:**
*"UrbanStyle's 2024 total revenue is €305,000, up +15% vs 2023. Growth is driven by the Christmas campaign (+43% in December) and e-store expansion (28% of revenue). Main risk: Denim Jacket stock is critically low — urgent order needed to preserve Q1 sales potential."*

#### Group Work — Store-Specific Dashboards

Challenge (Anna Mets): "Each store manager wants THEIR OWN dashboard. But management needs a consolidated view. How do we do this? And it has to TELL A STORY!"

| Role | Store story | Key question |
|------|-------------|-------------|
| A | Tallinn store | City store growth vs e-store competition |
| B | Tartu store | University store seasonality |
| C | Pärnu store | Summer resort seasonality — risk and opportunity |
| D | E-store | Digital growth, no geography |
