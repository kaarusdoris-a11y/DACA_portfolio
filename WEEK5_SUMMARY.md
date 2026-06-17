# DACA26 — Nädal 5: Visualiseerimise Disain
## Individuaalne Kokkuvõte

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Nädal:** 5 — Data Visualization (Plotly, Streamlit, Power BI, dashboard disain)  
**Kontekst:** UrbanStyle.ltd andmete visualiseerimine kolmele stakeholder'ile

---

## Eesmärgid ja Tulemused

Kõik põhieesmärgid täideti:
- Valisin diagrammitüübi vastavalt andmetüübile ja sõnumile
- Ehitasin dashboard'i konkreetsele stakeholder'ile
- Rakendasin data-ink ratio põhimõtet (Tufte) — vähem on rohkem

---

## Kontekst: Kolm Stakeholder'it, Kolm Vaadet

**Kristi Tamm (CEO):** *"Investorid tulevad. Ma tahan ühte lehte, mis ütleb mulle kõik."*

**Anna Mets (turundusjuht):** *"Mina vajan turundusanalüüsi! Kampaaniate ROI, kanalite efektiivsus."*

**Liis Koppel (operatsioonide juht):** *"Mina tahan näha laoseise ja inventuuri numbreid. Mitte ühtegi müügidiagrammi!"*

---

## Diagrammitüüpide Valik

| Sõnum | Diagrammitüüp |
|---|---|
| Trend ajas | Joondiagramm |
| Võrdlus kategooriate vahel | Tulpdiagramm |
| Osakaalud (max 5) | Sektordiagramm |
| Seos kahe muutuja vahel | Hajuvusdiagramm |
| Üks võtmenumber | KPI kaart |

**Mis EI tööta:** 3D diagrammid, sektordiagramm 10+ kategooriaga, kahekordne Y-telg.

---

## Track B: Plotly + Streamlit

Valisin **Track B** (Python + Plotly + Streamlit).

```python
import streamlit as st
import plotly.express as px
import pandas as pd

st.title("UrbanStyle.ltd — Müügiülevaade 2024")

# Kuukäive joondiagrammina
fig = px.line(
    df_monthly,
    x="kuu",
    y="kogukäive",
    title="Kuukäive 2024",
    labels={"kuu": "Kuu", "kogukäive": "Käive (€)"}
)
st.plotly_chart(fig)

# Kategooriad tulpdiagrammina
fig2 = px.bar(
    df_categories,
    x="category",
    y="käive_kokku",
    title="Käive kategooriate kaupa",
    color="category"
)
st.plotly_chart(fig2)
```

---

## Dashboard Anatoomia

Hea dashboard koosneb:
1. **Pealkiri** — selge, ühesõnaline fookus
2. **KPI kaardid** (3–5) — kõige olulisemad numbrid üleval
3. **Peadiagramm** — vastab peamisele küsimusele
4. **Tugigraafikud** (2–3) — kontekst ja detail
5. **Filtrid** — kasutajale paindlikkus

**Minu dashboard Kristi jaoks:**
- KPI kaardid: Kogu käive, Müükide arv, Keskmine tellimus, Aktiivsed kliendid
- Peadiagramm: Kuukäive 2024 (joondiagramm)
- Tugigraafikud: Käive kategooriate kaupa (tulpdiagramm), Müügikanalid (rõngasdiagramm)
- Filter: Kuupäevavahemik

---

## Data-Ink Ratio (Tufte)

**Põhijäreldus:** Iga tindipritsmetus peab kandma infot. Eemalda kõik dekoratiivne.

Eemaldan: taustarvõrk, 3D efektid, liiga palju värve (max 5–7), korduvad andmesildid.

---

## Grupitöö — Kolme Stakeholder'i Dashboard

Meeskond jagas ülesanded kolme stakeholder'i vahel. Lõpuks koondas meeskond need kolmeks eraldi vaateks, mis kõik kasutasid sama andmeallikat.

---

## Õppimise Reflektsioon

**Mis läks hästi:**
- Plotly Express on intuitiivne — ühe reaga professionaalne diagramm
- Streamlit'i `st.columns()` lihtsustab layout'i ehitamist

**Mis vajas rohkem tööd:**
- Streamlit'i seadistamine võttis ~15 min kauem kui Power BI
- Värviskaalade valimine andmete tüübi järgi

**Järgmiseks (Nädal 6 — RFM Analüüs):**
- Klientide segmenteerimine: Recency, Frequency, Monetary

---

*DACA26 · Nädal 5 · UrbanStyle.ltd andmeanalüüs*
