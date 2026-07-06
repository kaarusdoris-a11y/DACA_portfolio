# Nädal 3 — Kogu Kood (Individuaalne + Meeskond)

## 1. Individuaalne kood — DACA (`WEEK3_joins_analysis.sql`)

```sql
-- ============================================================
-- WEEK 3 — SQL JOINid
-- Programm: DACA | Andmestik: UrbanStyle.ltd
-- Teemad: INNER JOIN, LEFT JOIN, mitu tabelit
-- Tabelid: sales, customers, products
-- ============================================================

-- 1. INNER JOIN — müügid koos kliendi nimega
SELECT
    s.order_id,
    s.order_date,
    c.first_name || ' ' || c.last_name AS kliendi_nimi,
    c.city AS kliendi_linn,
    s.total_price
FROM sales s
INNER JOIN customers c ON s.customer_id = c.customer_id
ORDER BY s.order_date DESC
LIMIT 20;

-- 2. LEFT JOIN — müügid ilma kliendita
SELECT
    s.order_id,
    s.customer_id,
    c.first_name,
    c.last_name,
    s.total_price
FROM sales s
LEFT JOIN customers c ON s.customer_id = c.customer_id
WHERE c.customer_id IS NULL
LIMIT 10;

-- 3. Kolme tabeli JOIN — müük + klient + toode
SELECT
    s.order_id,
    s.order_date,
    c.first_name || ' ' || c.last_name AS klient,
    p.product_name,
    p.category,
    s.quantity,
    s.unit_price,
    s.total_price,
    (s.unit_price - p.cost_price) * s.quantity AS kasum
FROM sales s
INNER JOIN customers c ON s.customer_id = c.customer_id
INNER JOIN products p ON s.product_id = p.product_id
ORDER BY kasum DESC
LIMIT 20;

-- 4. Kliendi ostuajalugu
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS klient,
    c.city,
    COUNT(s.order_id)     AS tellimuste_arv,
    SUM(s.total_price)    AS kokku_kulutatud,
    AVG(s.total_price)    AS keskmine_tellimus,
    MAX(s.order_date)     AS viimane_ost
FROM customers c
LEFT JOIN sales s ON c.customer_id = s.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.city
ORDER BY kokku_kulutatud DESC NULLS LAST
LIMIT 20;

-- 5. Toote kasumlikkus
SELECT
    p.product_name,
    p.category,
    COUNT(s.order_id)                               AS korda_müüdud,
    SUM(s.quantity)                                 AS ühikuid_kokku,
    SUM(s.total_price)                              AS käive,
    SUM((s.unit_price - p.cost_price) * s.quantity) AS kasum,
    ROUND(
          SUM((s.unit_price - p.cost_price) * s.quantity) /
          NULLIF(SUM(s.total_price), 0) * 100, 1
      ) AS kasumimarginaal_pct
FROM products p
LEFT JOIN sales s ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY kasum DESC NULLS LAST
LIMIT 15;

-- 6. Vanusegrupp vs ostukäitumine
SELECT
    CASE
        WHEN c.age < 25 THEN '18-24'
        WHEN c.age < 35 THEN '25-34'
        WHEN c.age < 45 THEN '35-44'
        WHEN c.age < 55 THEN '45-54'
        ELSE '55+'
    END AS vanusegrupp,
    COUNT(DISTINCT c.customer_id) AS kliente,
    COUNT(s.order_id)             AS tellimusi,
    SUM(s.total_price)            AS käive_kokku,
    ROUND(AVG(s.total_price), 2)  AS keskmine_tellimus
FROM customers c
LEFT JOIN sales s ON c.customer_id = s.customer_id
GROUP BY vanusegrupp
ORDER BY vanusegrupp;

-- 7. Kliendi linn vs poe asukoht
SELECT
    c.city             AS kliendi_linn,
    s.store_location   AS poe_linn,
    COUNT(*)           AS tehinguid,
    SUM(s.total_price) AS käive
FROM sales s
INNER JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.city, s.store_location
ORDER BY tehinguid DESC;

-- Õppimisjärgeldus (nädal 3):
-- INNER JOIN = ühisosa (mõlemas tabelis olemas).
-- LEFT JOIN = kõik vasaku tabeli read, paremast ainult sobivad.
-- NULLIF(x, 0) hoiab ära jagamise nulliga.
```

## 2. Meeskonna kood — Sales-Analytics

Nädal 3 kohta puudub minu isiklikule nimele atribueeritud eraldi meeskonnakood — [TEAMWORK.md](./TEAMWORK.md)-s on see nädal märgitud kui "kinnitamisel". Vaata [Data_Landscape_Week3.pdf](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/main/Data_Landscape_Week3.pdf) meeskonna üldise JOIN-analüüsi jaoks.

---
*DACA26 · Nädal 3 · UrbanStyle.ltd andmeanalüüs*
