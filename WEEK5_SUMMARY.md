# Nädal 5 — Visualiseerimise Disain

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Teema:** Visualiseerimise disain  
**Töövihikud:** N5 IT (Iseseisva õppe töövihik) + N5 GT (Grupitöö juhend)  
**Versioon:** 2.9

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
