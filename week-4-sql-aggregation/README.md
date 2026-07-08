# DACA26 — Nädal 4: SQL Agregatsioon
## Individuaalne Kokkuvõte

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Nädal:** 4 — SQL Aggregation (GROUP BY, HAVING, CTE, window functions)  
**Kontekst:** UrbanStyle.ltd koondnumbrid Kristi Tamme juhatuse koosolekuks

**Äriprobleem:** Kristi Tamm ei saa juhatuse koosolekul esitada 15 000+ üksikut müügirida — ta vajab kokkuvõtvaid, usaldusväärseid koondnumbreid (parim kategooria, kanal, trend, lojaalsed kliendid), mille peale saab ehitada strateegilisi otsuseid.

---

## Eesmärgid ja Tulemused

Kõik kolm põhieesmärki täideti:
- Grupeerisin andmeid äriloogika järgi `GROUP BY` lausetega
- Filtreerisin grupeeritud tulemusi `HAVING` klausliga ja eristasin seda `WHERE`-st
- Struktureerisin keerulisi päringuid CTE-de ja window function'itega

---

## Kontekst

Anna Mets: *"Kristi tahab juhatuse koosolekuks numbreid. Keskmine tellimusväärtus, top kategooriad, müügitrendid — KIIRESTI!"*

**Oluline erinevus:**
- `WHERE` filtreerib enne grupeerimist (üksikuid ridu)
- `HAVING` filtreerib pärast grupeerimist (grupeeritud tulemusi)

---

## Osa 1 — GROUP BY ja Agregaatfunktsioonid

```sql
-- Müügikäive kategooriate kaupa
SELECT
    p.category,
    COUNT(s.sale_id)             AS müügid_kokku,
    SUM(s.total_price)           AS käive_kokku,
    ROUND(AVG(s.total_price), 2) AS kesk_tellimus,
    MAX(s.total_price)           AS suurim_tellimus
FROM sales s
INNER JOIN products p ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY käive_kokku DESC;
```

---

## Osa 2 — HAVING

```sql
-- Linnad, kus käive üle 50 000 €
SELECT
    c.city,
    COUNT(s.sale_id)   AS müügid,
    SUM(s.total_price) AS käive
FROM sales s
INNER JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.city
HAVING SUM(s.total_price) > 50000
ORDER BY käive DESC;
```

```sql
-- Lojaalsed kliendid (üle 5 ostu)
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS nimi,
    COUNT(s.sale_id)   AS ostude_arv,
    SUM(s.total_price) AS koguostud
FROM sales s
INNER JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name
HAVING COUNT(s.sale_id) > 5
ORDER BY koguostud DESC;
```

---

## Osa 3 — CTE ja Kuukäibe Trend

```sql
-- Kuukäive 2024. aastal
SELECT
    DATE_TRUNC('month', sale_date) AS kuu,
    SUM(total_price)               AS kogukäive
FROM sales
WHERE sale_date >= '2024-01-01'
  AND sale_date < '2025-01-01'
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY kuu;
```

```sql
-- CTE: TOP kategooriad vs kogu käive
WITH kategooriad AS (
    SELECT
        p.category,
        SUM(s.total_price) AS kategooria_käive
    FROM sales s
    INNER JOIN products p ON s.product_id = p.product_id
    GROUP BY p.category
),
kokku AS (
    SELECT SUM(total_price) AS kogu_käive FROM sales
)
SELECT
    k.category,
    k.kategooria_käive,
    ROUND(k.kategooria_käive / c.kogu_käive * 100, 1) AS osakaal_pct
FROM kategooriad k, kokku c
ORDER BY k.kategooria_käive DESC;
```

---

## Osa 4 — Window Functions

```sql
-- Kumulatiivne käive 2024
SELECT
    DATE_TRUNC('month', sale_date) AS kuu,
    SUM(total_price)               AS kuu_käive,
    SUM(SUM(total_price)) OVER (
        ORDER BY DATE_TRUNC('month', sale_date)
    ) AS kumulatiivne_käive
FROM sales
WHERE sale_date >= '2024-01-01' AND sale_date < '2025-01-01'
GROUP BY DATE_TRUNC('month', sale_date)
ORDER BY kuu;
```

---

## Juhatuse Koosoleku Numbrid

| Kristi küsimus | Vastus |
|---|---|
| Parim kategooria? | Jalanõud |
| Parim müügikanal? | Online |
| Kuu-üle-kuu trend? | Detsember kõrgeim |
| Lojaalsed kliendid? | ~1 200 klienti |

---

## Õppimise Reflektsioon

**Mis läks hästi:**
- `WHERE` vs `HAVING` erinevus sai lõpuks selgeks praktiliste näidete kaudu
- CTE struktuur on palju loetavam kui pesastatud subpäringud

**Mis vajas rohkem tööd:**
- Window functions — `PARTITION BY` loogika vajas kordamist

**Järgmiseks (Nädal 5 — Visualiseerimine):**
- SQL tulemuste visualiseerimine Plotly / Streamlit / Power BI-ga

---

*DACA26 · Nädal 4 · UrbanStyle.ltd andmeanalüüs*
---

## 🇬🇧 In English

### DACA26 — Week 4: SQL Aggregation
**Individual Summary**

Programme: DACA — Data Analyst Career Accelerator
Week: 4 — SQL Aggregation (GROUP BY, HAVING, CTE, window functions)
Context: UrbanStyle.ltd summary numbers for CEO Kristi Tamm's board meeting

#### Goals and Results

All three core goals were achieved:
- Grouped data by business logic with GROUP BY statements
- Filtered grouped results with HAVING and understood the difference from WHERE
- Structured complex queries using CTEs and window functions

#### Key Concept

- **WHERE** filters before grouping (individual rows)
- **HAVING** filters after grouping (grouped results)

#### Board Meeting Numbers

| Kristi's question | Answer |
|-------------------|--------|
| Best category? | Footwear |
| Best sales channel? | Online |
| Month-over-month trend? | December highest |
| Loyal customers? | ~1,200 customers |

**CTE result — category revenue shares:**
Categories with their % of total revenue, ranked by turnover.

**Window function — cumulative revenue 2024:**
Monthly revenue shown alongside running total across the year.

#### Learning Reflection

**What went well:**
- The WHERE vs HAVING difference finally clicked through practical examples
- CTE structure is much more readable than nested subqueries

**What needed more work:**
- Window functions — PARTITION BY logic needed repeated practice

**Next week (Week 5 — Visualisation):**
- Visualising SQL results with Plotly / Streamlit / Power BI
