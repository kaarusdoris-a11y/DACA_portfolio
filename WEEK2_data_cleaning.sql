-- ============================================================
-- WEEK 2 — SQL Andmepuhastamine
-- Programm: DACA | Andmestik: UrbanStyle.ltd
-- Teemad: duplikaadid, NULL-id, COALESCE, TRIM, kuupäevavormingud
-- ============================================================

-- 1. DUPLIKAATIDE TUVASTAMINE
SELECT order_id, COUNT(*) AS kordusi
FROM sales
GROUP BY order_id
HAVING COUNT(*) > 1
ORDER BY kordusi DESC;

-- 2. Duplikaatread täpsemalt
SELECT *
FROM sales
WHERE order_id IN (
      SELECT order_id
      FROM sales
      GROUP BY order_id
      HAVING COUNT(*) > 1
  )
ORDER BY order_id;

-- 3. NULL-IDE LEIDMINE
SELECT
    COUNT(*) FILTER (WHERE customer_id IS NULL)    AS null_customer_id,
    COUNT(*) FILTER (WHERE product_name IS NULL)   AS null_product_name,
    COUNT(*) FILTER (WHERE total_price IS NULL)    AS null_total_price,
    COUNT(*) FILTER (WHERE order_date IS NULL)     AS null_order_date,
    COUNT(*) FILTER (WHERE store_location IS NULL) AS null_store_location
FROM sales;

-- 4. COALESCE — NULL asendamine vaikeväärtusega
SELECT
    order_id,
    customer_id,
    COALESCE(store_location, 'Tundmatu') AS store_location,
    total_price
FROM sales
WHERE store_location IS NULL
LIMIT 10;

-- 5. TÜHIKUTE PUHASTAMINE (TRIM)
SELECT
    product_name,
    TRIM(product_name) AS product_name_cleaned,
    LENGTH(product_name) AS orig_pikkus,
    LENGTH(TRIM(product_name)) AS puhas_pikkus
FROM sales
WHERE LENGTH(product_name) != LENGTH(TRIM(product_name))
LIMIT 10;

-- 6. KUUPÄEVAVORMINGUD
SELECT
    order_date,
    order_date::DATE AS kuupäev,
    EXTRACT(YEAR FROM order_date)  AS aasta,
    EXTRACT(MONTH FROM order_date) AS kuu,
    EXTRACT(DOW FROM order_date)   AS nädalapäev
FROM sales
LIMIT 10;

-- 7. VIGASED HINNAD
SELECT order_id, product_name, total_price
FROM sales
WHERE total_price <= 0;

-- 8. PUHASTATUD VAADE (CTE-ga)
WITH cleaned_sales AS (
      SELECT DISTINCT ON (order_id)
          order_id,
          customer_id,
          TRIM(product_name)                   AS product_name,
          quantity,
          unit_price,
          total_price,
          order_date::DATE                     AS order_date,
          COALESCE(store_location, 'Tundmatu') AS store_location
      FROM sales
      WHERE total_price > 0
        AND customer_id IS NOT NULL
      ORDER BY order_id, order_date DESC
  )
SELECT COUNT(*) AS puhastatud_ridu
FROM cleaned_sales;

-- 9. ENNE vs PÄRAST
SELECT
    (SELECT COUNT(*) FROM sales)                       AS algne_ridade_arv,
    (SELECT COUNT(DISTINCT order_id) FROM sales)       AS unikaalsed_tellimused,
    (SELECT COUNT(*) FROM sales WHERE total_price > 0) AS positiivsed_hinnad;

-- Õppimisjärgeldus (nädal 2):
-- Andmepuhastamine on ~80% andmeanalüütiku tööst.
-- DISTINCT ON (PostgreSQL) duplikaatide eemaldamiseks.
-- COALESCE asendab NULL vaikeväärtusega.
