# DACA26 — Nädal 6: RFM Analüüs
## Individuaalne Kokkuvõte

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Nädal:** 6 — RFM Analüüs ja Klientide Segmenteerimine  
**Kontekst:** UrbanStyle.ltd klientide segmenteerimine Anna Metsa turunduskampaaniate jaoks

---

## Mis on RFM?

| Dimensioon | Tähendus | SQL meetod |
|---|---|---|
| **R** — Recency | Kui hiljuti ostis? | `MAX(sale_date)`, päevade vahe |
| **F** — Frequency | Kui tihti ostab? | `COUNT(sale_id)` |
| **M** — Monetary | Kui palju kulutab? | `SUM(total_price)` |

**Äriküsimus:** Anna Mets tahab teada, kes on UrbanStyle'i kõige väärtuslikumad kliendid.

---

## SQL: RFM Arvutamine

```sql
-- Samm 1: Arvuta iga kliendi RFM väärtused
WITH rfm_base AS (
    SELECT
        s.customer_id,
        c.first_name || ' ' || c.last_name AS klient,
        c.city,
        MAX(s.sale_date)                      AS viimane_ost,
        CURRENT_DATE - MAX(s.sale_date)::date AS recency_paevad,
        COUNT(s.sale_id)                      AS frequency,
        ROUND(SUM(s.total_price)::numeric, 2) AS monetary
    FROM sales s
    INNER JOIN customers c ON s.customer_id = c.customer_id
    WHERE s.sale_date IS NOT NULL
    GROUP BY s.customer_id, c.first_name, c.last_name, c.city
),

-- Samm 2: Skoreeri iga dimensioon 1-5
rfm_scores AS (
    SELECT
        customer_id,
        klient,
        city,
        recency_paevad,
        frequency,
        monetary,
        NTILE(5) OVER (ORDER BY recency_paevad ASC)  AS r_score,
        NTILE(5) OVER (ORDER BY frequency DESC)       AS f_score,
        NTILE(5) OVER (ORDER BY monetary DESC)        AS m_score
    FROM rfm_base
)

-- Samm 3: Segmenteeri
SELECT
    customer_id,
    klient,
    city,
    r_score, f_score, m_score,
    r_score + f_score + m_score AS rfm_kokku,
    CASE
        WHEN r_score >= 4 AND f_score >= 4 AND m_score >= 4 THEN 'Tšempion'
        WHEN r_score >= 3 AND f_score >= 3                  THEN 'Lojaalne klient'
        WHEN r_score >= 4 AND f_score <= 2                  THEN 'Uus klient'
        WHEN r_score <= 2 AND f_score >= 3                  THEN 'Ohu all'
        WHEN r_score <= 2 AND f_score <= 2                  THEN 'Kadunud klient'
        ELSE 'Potentsiaalne'
    END AS segment
FROM rfm_scores
ORDER BY rfm_kokku DESC;
```

---

## Klientide Segmentide Jaotus

| Segment | Kirjeldus | Soovituslik tegevus |
|---|---|---|
| **Tšempion** | Ostab sageli, hiljuti, palju | VIP kampaania, eelvaated |
| **Lojaalne klient** | Ostab regulaarselt | Lojaalsusprogramm |
| **Uus klient** | Ostnud hiljuti, aga harva | Onboarding, soovitused |
| **Ohu all** | Varem ostis sageli, nüüd mitte | Win-back kampaania |
| **Kadunud klient** | Pole ammu ostnud | Reaktiveerimine |

---

## Python: RFM Visualiseerimine

```python
import pandas as pd
import plotly.express as px

# Segmentide jaotus
fig = px.pie(
    df.groupby("segment").size().reset_index(name="count"),
    values="count",
    names="segment",
    title="Klientide segmentide jaotus"
)
fig.show()

# R vs M hajuvusdiagramm
fig2 = px.scatter(
    df,
    x="recency_paevad",
    y="monetary",
    color="segment",
    size="frequency",
    hover_data=["klient", "city"],
    title="RFM: Recency vs Monetary (suurus = Frequency)"
)
fig2.show()
```

---

## Peamised Leiud

**Tähelepanuväärne:** "Ohu all" segment — kliendid, kes varem ostid sageli aga nüüd on vaikseks jäänud — on turunduse jaoks kõrgeima prioriteediga win-back võimalus.

---

## Õppimise Reflektsioon

**Mis läks hästi:**
- `NTILE(5) OVER (ORDER BY ...)` on elegantne kvintiilide arvutamiseks
- CTE struktuur muutis keerulise päringu sammude kaupa jälgitavaks

**Mis vajas rohkem tööd:**
- Type casting Supabase'is (`CURRENT_DATE - MAX(sale_date)::date`) vajas katsetamist

**Kokkuvõte — DACA programm nädal 6 seisuga:**
- SQL: SELECT → WHERE → DISTINCT → JOIN → GROUP BY → HAVING → CTE → Window Functions → RFM
- Python: pandas, plotly, streamlit
- Tööriistade stack: Supabase, GitHub, VS Code, NotebookLM

---

*DACA26 · Nädal 6 · UrbanStyle.ltd andmeanalüüs*
