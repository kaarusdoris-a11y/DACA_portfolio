# Nädal 1 — Kogu Kood (Individuaalne + Meeskond)

See fail koondab kõik nädal 1 jooksul kirjutatud päris SQL-koodi ühte kohta: minu individuaalse DACA harjutuse ja minu meeskonnapanuse Sales-Analytics projektis.

## 1. Individuaalne kood — DACA (`WEEK1_sales_exploration.sql`)

```sql
-- ============================================================
-- WEEK 1 — SQL Põhitõed
-- Programm: DACA | Andmestik: UrbanStyle.ltd
-- Teemad: SELECT, WHERE, DISTINCT, COUNT, ORDER BY, LIMIT
-- ============================================================

-- 1. Mis tabelid on olemas? Vaatan müügiandmete struktuuri
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'sales'
ORDER BY ordinal_position;

-- 2. Esimesed 10 rida — mis andmed üldse on?
SELECT *
FROM sales
LIMIT 10;

-- 3. Kui palju tellimusi kokku on?
SELECT COUNT(*) AS tellimusi_kokku
FROM sales;

-- 4. Kui palju unikaalseid kliente on müügiandmetes?
SELECT COUNT(DISTINCT customer_id) AS unikaalseid_kliente
FROM sales;

-- 5. Mis linnad on müügiandmetes? (unikaalsed)
SELECT DISTINCT store_location
FROM sales
ORDER BY store_location;

-- 6. Mis on kõige kallim toode, mis on müüdud?
SELECT product_name, unit_price
FROM sales
ORDER BY unit_price DESC
LIMIT 5;

-- 7. Tallinna poe müügid — filtreerin WHERE-ga
SELECT order_id, order_date, product_name, quantity, total_price
FROM sales
WHERE store_location = 'Tallinn'
ORDER BY order_date DESC
LIMIT 20;

-- 8. Suured tellimused — üle 100 euro
SELECT order_id, customer_id, product_name, total_price
FROM sales
WHERE total_price > 100
ORDER BY total_price DESC;

-- 9. Detsembri müügid (jõuluhooaeg)
SELECT order_id, order_date, product_name, total_price
FROM sales
WHERE order_date >= '2024-12-01'
  AND order_date < '2025-01-01'
ORDER BY order_date;

-- 10. Mitu müüki on igas linnas?
SELECT store_location, COUNT(*) AS tehinguid
FROM sales
GROUP BY store_location
ORDER BY tehinguid DESC;

-- Õppimisjärgeldus (nädal 1):
-- SELECT + WHERE + ORDER BY on SQL-i selgroog.
-- COUNT(*) loeb kõik read, COUNT(DISTINCT x) loeb unikaalsed väärtused.
-- LIMIT on kasulik — ei tõmba kogu 10 000 rea tabelit korraga.
```

## 2. Meeskonna kood — Sales-Analytics, Roll C: Tooteandmete Uurija

Minu roll nädal 1 meeskonnaprojektis oli `products` tabeli uurimine Toomase jaoks (vt [TEAMWORK.md](./TEAMWORK.md)).

```sql
-- Toodete koguarv ja kategooriad
SELECT
    COUNT(*)               AS toodete_arv,       -- 362
    COUNT(DISTINCT category) AS kategooriaid     -- 5
FROM products;

-- Kategooriate jaotus
SELECT category, COUNT(*) AS toodete_arv
FROM products
GROUP BY category
ORDER BY toodete_arv DESC;

-- Keskmised hinnad kategooriate kaupa
SELECT
    category,
    COUNT(*)       AS tooteid,
    MIN(retail_price) AS min_hind,
    MAX(retail_price) AS max_hind,
    ROUND(AVG(retail_price), 2) AS kesk_hind
FROM products
GROUP BY category
ORDER BY kesk_hind DESC;
```

**Leid:** `eco_certified` veerus 18 null väärtust — täielik analüüs ja äriline mõju on kirjas [WEEK1_SUMMARY.md](./WEEK1_SUMMARY.md)-s.

---
*DACA26 · Nädal 1 · UrbanStyle.ltd andmeanalüüs*
