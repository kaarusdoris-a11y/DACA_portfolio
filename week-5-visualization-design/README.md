# Nädal 5 — Visualiseerimise Disain

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Teema:** Visualiseerimise disain  
**Töövihikud:** N5 IT (Iseseisva õppe töövihik) + N5 GT (Grupitöö juhend)  
**Versioon:** 2.9

**Äriprobleem:** CEO Kristi Tamm kohtub investoritega viie nädala pärast — vale diagrammitüüp või halvasti disainitud dashboard varjab UrbanStyle'i tegelikku äriolukorda, mistõttu investorid ei saa 30 sekundiga õiget pilti ettevõtte tervisest.

---

## Selle nädala eesmärgid

1. Valida õige diagrammitüübi iga äriküsimuse jaoks (joon-, tulp-, sektor-, hajuvusdiagramm, KPI kaart)
2. Kavandada dashboard'i paigutust, mis järgib visuaalset hierarhiat ja Z/F-mustrit
3. Planeerida filtrite ja interaktiivsuse loogika, mis muudab staatilise dashboard'i dünaamiliseks

---

## 1. Diagrammitüübid

### Millal kasutada mida?

| Diagrammitüüp | Äriküsimus | UrbanStyle näide |
|---|---|---|
| **Joondiagramm** | Trend ajas | Kuine käive jaanuar–detsember |
| **Vertikaalne tulpdiagramm** | Võrdlus kategooriate vahel | Müük kuude lõikes |
| **Horisontaalne tulpdiagramm** | Pingerida / ranking | TOP 5 toodet käibe järgi |
| **Sektordiagramm** | Osade osakaal (max 5 viilu) | Müük linnade lõikes |
| **Hajuvusdiagramm** | Kahe muutuja korrelatsioon | Tellimuste arv vs käive |
| **KPI kaart** | Üks võtmemõõdik numbrina | Kokku käive: €305 000 |

### Harjutus 1B — UrbanStyle andmestik

**Andmekogum A** — kuine käive (EUR, jan–dets): → **joondiagramm** (trend ajas)  
**Andmekogum B** — TOP 5 toote müük: → **horisontaalne tulpdiagramm** (pingerida)  
**Andmekogum C** — müük linnade lõikes (Tallinn 42%, Online 28%, Tartu 18%, Pärnu 12%): → **sektordiagramm** (4 viilu — sobib)

### Põhijäreldus

> Iga äriküsimus dikteerib diagrammitüübi. Küsi alati: *"Mida ma tahan näidata — trendi, võrdlust, osakaalu või korrelatsiooni?"*

---

## 2. Dashboard'i disain

### Investor Dashboard näide (Q4 2024)

```
┌─────────────────────────────────────────────────────┐
│  UrbanStyle Investor Dashboard — Q4 2024            │
├──────────┬──────────┬──────────┬────────────────────┤
│ €305K    │ 2 500    │ €32      │ +15% kasv          │
│ Käive    │ Kliendid │ Kesk.tell│ vs Q3              │
├──────────┴──────────┴──────────┴────────────────────┤
│  Müügitulu trend (joondiagramm, Jan–Dec)            │
├──────────────────────────┬──────────────────────────┤
│  TOP 5 toodet            │  Müük linnade lõikes     │
│  (horisontaalne tulp)    │  (sektordiagramm)        │
│  Denim Jacket  ████ 45K  │  Tallinn 42%             │
│  Sneakers      ███  35K  │  Online  28%             │
│  Hoodie        ██   28K  │  Tartu   18%             │
│                          │  Pärnu   12%             │
└──────────────────────────┴──────────────────────────┘
```

### Z/F-muster ja visuaalne hierarhia

Silm liigub ekraanil Z- või F-kujuliselt — vasak ülaosa on kõige tähelepanuvääravam.

- **Vasakus ülanurgas:** KPI-d (kõige olulisemad numbrid)
- **Keskel:** Peamine trendijoon
- **All:** Detailid ja võrdlusvaated

**Checklist:**
- [ ] Kõige olulisem info on vasakus ülanurgas
- [ ] Maksimaalselt 5–6 elementi ühel vaatel
- [ ] Iga element vastab konkreetsele äriküsimusele
- [ ] Värvid on konsistentsed (1–2 põhivärvi)

---

## 3. Filtrid ja interaktiivsus

| Filter | Vaikeväärtus | Mõju dashboard'ile |
|---|---|---|
| Ajavahemik | Viimased 12 kuud | Kõik diagrammid uuenduvad |
| Linn/kaupluse asukoht | Kõik | Ainult valitud linna andmed |
| Tootekategooria | Kõik | Filtreerib TOP-nimekiri ja käibenumbrid |

### Cross-filtering

Klikk "Tallinn" sektordiagrammis → KPI-d ja trendijoon näitavad ainult Tallinna andmeid.

### 30-sekundi test

> *Kujuta ette, et investor näeb su dashboard'i 30 sekundit. Mis on peamine sõnum, mis jääb meelde?*

Hea dashboard vastab sellele küsimusele ilma selgitusteta.

---

## Track B — Plotly + Streamlit

```python
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("UrbanStyle Dashboard")

df = pd.read_csv("urbanstyle_sales.csv")

# KPI-d
col1, col2, col3 = st.columns(3)
col1.metric("Kokku käive", f"€{df['total_price'].sum():,.0f}")
col2.metric("Kliendid", df['customer_id'].nunique())
col3.metric("Kesk. tellimus", f"€{df['total_price'].mean():.0f}")

# Filter
linn = st.selectbox("Vali linn", ["Kõik"] + list(df['store_location'].unique()))
if linn != "Kõik":
    df = df[df['store_location'] == linn]

# Trendijoon
fig = px.line(df.groupby('month')['total_price'].sum().reset_index(),
              x='month', y='total_price', title='Kuine käive')
st.plotly_chart(fig)
```

---

## Grupitöö (N5 GT) — Dual-Track Dashboard

**Äriprobleem (grupitöö):** Kolm erinevat sisemist kasutajat (CEO, turundus, operatsioonid) vajavad samast andmestikust kolme erinevat vaadet — dashboard peab vastama kõigi kolme otsustajate küsimustele ilma, et keegi peaks andmeid uuesti käsitsi filtreerima.

**Väljakutse:** CEO Kristi Tamm kutsub investorid viie nädala pärast — vaja on professionaalset interaktiivset dashboard'i.

**Kolm stakeholder'it, kolm vaadet:**
- **Kristi (CEO):** Koondvaade — käive, kasv, KPI-d
- **Anna Mets (turundus):** Kampaaniate ROI, kliendiandmed
- **Liis Koppel (operatsioonid):** Laoseis, tarneajad

**Rollid grupitöös:**

| Roll | Ülesanne |
|---|---|
| Roll A | KPI kaardid + ajavahemiku filter |
| Roll B | Trendijoon + tootekategooria analüüs |
| Roll C | Geograafiline jaotus (linnad) |
| Roll D | Koondvaade + esitlus Kristile |

---

## Lugemismaterjal

- Knaflic *Storytelling with Data* Ch 5: Think Like a Designer
- Knaflic Ch 6: Tell a Story (eelvaade Nädal 6 teemadele)
- McKinney *Python for Data Analysis* Ch 9: Plotting and Visualization
- DACA Kursus 6, Moodul 1: Andmete visualiseerimine

---

*DACA26 · Nädal 5 · UrbanStyle.ltd andmeanalüüs*
---

## 🇬🇧 In English

### Week 5 — Visualisation Design
**Individual Summary**

Programme: DACA — Data Analyst Career Accelerator
Topic: Visualisation design
Workbooks: W5 IL (Independent Learning) + W5 GT (Group Work)

#### Week Goals
- Choose the right chart type for each business question (line, bar, pie, scatter, KPI card)
- Design dashboard layouts following visual hierarchy and Z/F-patterns
- Plan filter and interactivity logic to make a static dashboard dynamic

#### Chart Types — When to Use What

| Chart type | Business question | UrbanStyle example |
|------------|-------------------|-------------------|
| Line chart | Trend over time | Monthly revenue Jan–Dec |
| Vertical bar chart | Comparison between categories | Sales by month |
| Horizontal bar chart | Ranking / leaderboard | TOP 5 products by revenue |
| Pie chart | Part-to-whole (max 5 slices) | Sales by city |
| Scatter plot | Correlation between two variables | Order count vs revenue |
| KPI card | One key metric as a number | Total revenue: €305,000 |

**UrbanStyle dataset decisions:**
- Dataset A — monthly revenue: → line chart (trend over time)
- Dataset B — TOP 5 products: → horizontal bar chart (ranking)
- Dataset C — sales by city (Tallinn 42%, Online 28%, Tartu 18%, Pärnu 12%): → pie chart (4 slices — appropriate)

**Key insight:** Every business question dictates the chart type. Always ask: "What am I showing — a trend, a comparison, a proportion, or a correlation?"

#### Dashboard Design

**Visual hierarchy & Z/F-pattern:**
- Top-left corner: KPIs (most important numbers)
- Centre: Main trend line
- Bottom: Details and comparison views

**Checklist:**
- Most important info is in the top-left corner
- Maximum 5–6 elements in one view
- Each element answers a specific business question
- Colours are consistent (1–2 primary colours)

#### Filters and Interactivity

| Filter | Default value | Effect on dashboard |
|--------|--------------|---------------------|
| Date range | Last 12 months | All charts update |
| City/store location | All | Only selected city's data |
| Product category | All | Filters TOP list and revenue numbers |

**Cross-filtering:** Click "Tallinn" in pie chart → KPIs and trend line show only Tallinn data.

**30-second test:** Imagine an investor sees your dashboard for 30 seconds. What is the main message they remember? A good dashboard answers this without any explanation.

#### Group Work — Dual-Track Dashboard

Challenge: CEO Kristi Tamm is inviting investors in five weeks — need a professional interactive dashboard.

Three stakeholders, three views:
- **Kristi (CEO):** Overview — revenue, growth, KPIs
- **Anna Mets (Marketing):** Campaign ROI, customer data
- **Liis Koppel (Operations):** Stock levels, delivery times

#### Learning Reflection

**Next week (Week 6 — Data Storytelling):**
- Adding annotations and narratives to make charts tell a story
