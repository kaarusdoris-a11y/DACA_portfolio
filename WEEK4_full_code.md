# Nädal 4 — Kogu Kood (Individuaalne + Meeskond)

## 1. Individuaalne kood — DACA (`WEEK4_aggregation_cte_window.sql`)

```sql
-- ============================================================
-- WEEK 4 — SQL Agregatsioon, CTE ja Window Functions
-- Programm: DACA | Andmestik: UrbanStyle.ltd
-- Teemad: GROUP BY, HAVING, CTE (WITH), ROW_NUMBER, RANK, LAG, NTILE
-- ============================================================

-- 1. GROUP BY + HAVING — müügid kuude lõikes
SELECT
    EXTRACT(YEAR FROM order_date)  AS aasta,
    EXTRACT(MONTH FROM order_date) AS kuu,
    TO_CHAR(order_date, 'YYYY-MM') AS kuu_tekst,
    COUNT(order_id)                AS tellimusi,
    SUM(total_price)               AS kaive,
    ROUND(AVG(total_price), 2)     AS keskmine_tellimus
FROM sales
GROUP BY
    EXTRACT(YEAR FROM order_date),
    EXTRACT(MONTH FROM order_date),
    TO_CHAR(order_date, 'YYYY-MM')
HAVING COUNT(order_id) > 50
ORDER BY aasta, kuu;

-- 2. TOP 10 tooted käibe järgi
SELECT
    product_name,
    COUNT(order_id)           AS korda_müüdud,
    SUM(quantity)             AS ühikuid,
    SUM(total_price)          AS kaive,
    ROUND(AVG(unit_price), 2) AS keskmine_hind
FROM sales
GROUP BY product_name
ORDER BY kaive DESC
LIMIT 10;

-- 3. CTE + LAG — kuukäive eelmise kuuga võrdlus
WITH kuukaive AS (
      SELECT
          TO_CHAR(order_date, 'YYYY-MM') AS kuu,
          SUM(total_price)               AS kaive
      FROM sales
      GROUP BY TO_CHAR(order_date, 'YYYY-MM')
  )
SELECT
    kuu,
    kaive,
    LAG(kaive) OVER (ORDER BY kuu)                    AS eelmine_kuu,
    kaive - LAG(kaive) OVER (ORDER BY kuu)            AS muutus_eur,
    ROUND(
          (kaive - LAG(kaive) OVER (ORDER BY kuu)) /
          NULLIF(LAG(kaive) OVER (ORDER BY kuu), 0) * 100, 1
      ) AS muutus_pct
FROM kuukaive
ORDER BY kuu;

-- 4. RANK — klientide pingerida käibe järgi
WITH kliendi_kaive AS (
      SELECT
          s.customer_id,
          c.first_name || ' ' || c.last_name AS klient,
          c.city,
          SUM(s.total_price) AS kokku_kulutatud
      FROM sales s
      JOIN customers c ON s.customer_id = c.customer_id
      GROUP BY s.customer_id, c.first_name, c.last_name, c.city
  )
SELECT
    RANK() OVER (ORDER BY kokku_kulutatud DESC) AS koht,
    klient,
    city,
    kokku_kulutatud
FROM kliendi_kaive
LIMIT 20;

-- 5. ROW_NUMBER — iga kliendi viimane tellimus
WITH viimased AS (
      SELECT
          s.*,
          c.first_name || ' ' || c.last_name AS klient,
          ROW_NUMBER() OVER (
              PARTITION BY s.customer_id
              ORDER BY s.order_date DESC
          ) AS rn
      FROM sales s
      JOIN customers c ON s.customer_id = c.customer_id
  )
SELECT customer_id, klient, order_id, order_date AS viimane_ost, total_price
FROM viimased
WHERE rn = 1
ORDER BY order_date DESC
LIMIT 20;

-- 6. NTILE — kliendid 4 kvartiili (RFM eeltöö)
WITH kliendi_kaive AS (
      SELECT customer_id, SUM(total_price) AS kokku, COUNT(order_id) AS tellimusi
      FROM sales
      GROUP BY customer_id
  )
SELECT
    customer_id,
    kokku,
    tellimusi,
    NTILE(4) OVER (ORDER BY kokku DESC) AS kvartiil,
    CASE NTILE(4) OVER (ORDER BY kokku DESC)
        WHEN 1 THEN 'VIP'
        WHEN 2 THEN 'Lojaalne'
        WHEN 3 THEN 'Tavaline'
        WHEN 4 THEN 'Madala väärtusega'
    END AS segment
FROM kliendi_kaive
ORDER BY kokku DESC
LIMIT 30;

-- 7. Kategooriate osakaal käibest
WITH kat_kaive AS (
      SELECT p.category, SUM(s.total_price) AS kaive
      FROM sales s JOIN products p ON s.product_id = p.product_id
      GROUP BY p.category
  ),
kokku AS (SELECT SUM(kaive) AS kogu FROM kat_kaive)
SELECT k.category, k.kaive,
    ROUND(k.kaive / t.kogu * 100, 1) AS osakaal_pct
FROM kat_kaive k CROSS JOIN kokku t
ORDER BY k.kaive DESC;

-- 8. Kumulatiivne käive ajas (running total)
WITH kuukaive AS (
      SELECT TO_CHAR(order_date, 'YYYY-MM') AS kuu, SUM(total_price) AS kuu_kaive
      FROM sales GROUP BY TO_CHAR(order_date, 'YYYY-MM')
  )
SELECT kuu, kuu_kaive,
    SUM(kuu_kaive) OVER (ORDER BY kuu ROWS UNBOUNDED PRECEDING) AS kumulatiivne
FROM kuukaive ORDER BY kuu;

-- Õppimisjärgeldus (nädal 4):
-- CTE (WITH) muudab keerukad päringud loetavaks.
-- Window funktsioonid (RANK, ROW_NUMBER, LAG, NTILE) arvutavad üle ridade.
-- LAG(x) OVER (ORDER BY y) = eelmise rea väärtus — ideaalne kuude võrdlemiseks.
-- PARTITION BY = GROUP BY window funktsioonide sees.
```

## 2. Meeskonna kood — Sales-Analytics

Nädal 4 meeskonnaraportis ([Data_Landscape_Week4.pdf](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/main/Data_Landscape_Week4.pdf)) on rollid (A–E) selgelt nimeliselt jaotatud vastavalt Team Charterile, kuid see fail sisaldab ainult äriraportit (KPI-d, dashboard-kirjeldusi), mitte kellegi eraldi SQL-koodi. Seetõttu ei ole siin eraldi meeskonnakoodi lisada — minu individuaalne panus nädalal 4 on ülaltoodud SQL.

---
*DACA26 · Nädal 4 · UrbanStyle.ltd andmeanalüüs*
