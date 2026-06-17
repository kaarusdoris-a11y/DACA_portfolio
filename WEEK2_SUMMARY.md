# DACA26 — Nädal 2: SQL Puhastamine
## Individuaalne Kokkuvõte

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Nädal:** 2 — SQL Cleaning (duplikaadid, NULL-id, andmevormingud)  
**Kontekst:** UrbanStyle.ltd andmete puhastamine IT-direktor Toomas Kase jaoks

---

## Eesmärgid ja Tulemused

Nädala eesmärk oli õppida andmeid puhastama: tuvastada ja eemaldada duplikaate, käsitleda NULL väärtusi ning ühtlustada andmevälju.

Kõik kolm põhieesmärki täideti:
- Tuvastasin ja eemaldasin duplikaate `GROUP BY + HAVING` ja `ROW_NUMBER()` abil
- Leidsin ja käsitlesin NULL väärtusi `IS NULL`, `COALESCE()` ja `NULLIF()` abil
- Puhasted ja ühtlustasin andmevälju `CAST`, `TRIM()`, `UPPER()/LOWER()` ja kuupäevafunktsioonidega

---

## Kontekst: Toomas Tahab Puhtaid Andmeid

Kristi Tamm (CEO) helistas Toomasele: *"Mul on juhatuse koosolek kahe nädala pärast. Ma tahan puhtaid numbreid."*

Liis Koppel (Tartu kaupluse juhataja) kinnitas probleemid: duplikaattellimusnumbrid, kliendid ilma nimeta, segased kuupäevaformaadid (`03/12/2024` — märts või detsember?).

**Toomas Kase reegel:** *Tuvasta → Dokumenteeri → Testi → alles siis Paranda.*

---

## Osa 1 — Duplikaatide Tuvastamine ja Eemaldamine

**Põhijäreldus:** Duplikaadid tekivad andmete importimisel. Enne kustutamist tuleb alati teha test koopia.

```sql
-- Duplikaatide tuvastamine GROUP BY + HAVING abil
SELECT sale_id, COUNT(*) AS kordade_arv
FROM sales
GROUP BY sale_id
HAVING COUNT(*) > 1
ORDER BY kordade_arv DESC;
-- Tulemus: 847 duplikaat-sale_id-d
```

```sql
-- ROW_NUMBER() meetod — säilitab esimese, eemaldab ülejäänud
WITH ranked AS (
    SELECT id,
           ROW_NUMBER() OVER (PARTITION BY sale_id ORDER BY id) AS rn
    FROM sales
)
DELETE FROM sales
WHERE id IN (SELECT id FROM ranked WHERE rn > 1);
-- Tulemus: ~5 116 rida eemaldatud → sales jäi 10 118 rida
```

| Meede | Enne | Pärast |
|---|---|---|
| `sales` ridu kokku | 15 234 | 10 118 |
| Unikaalseid `sale_id` | 10 118 | 10 118 |
| Eemaldatud duplikaate | — | 5 116 |

---

## Osa 2 — NULL Väärtuste Käsitlemine

**Põhijäreldus:** `IS NULL` töötab, `= NULL` ei tööta. `COALESCE()` asendab NULL vaikeväärtusega.

```sql
-- NULL-ide audit
SELECT
    COUNT(*) AS kokku,
    COUNT(*) - COUNT(customer_id) AS null_customer,
    COUNT(*) - COUNT(total_price)  AS null_price,
    COUNT(*) - COUNT(sale_date)    AS null_date
FROM sales;
```

| Väli | NULL väärtusi |
|---|---|
| `customer_id` | 1 487 |
| `total_price` | 0 |
| `sale_date` | ~456 |

```sql
-- COALESCE — asenda NULL vaikeväärtusega
SELECT
    sale_id,
    COALESCE(customer_id::text, 'TUNDMATU') AS klient,
    COALESCE(total_price, 0)                AS summa
FROM sales
WHERE customer_id IS NULL OR total_price IS NULL;
```

---

## Osa 3 — Andmeväljade Ühtlustamine

**Põhijäreldus:** `TRIM()` eemaldab tühikud, `INITCAP()` ühtlustab nimed, `TO_DATE()` parandab kuupäevaformaadid.

```sql
-- Linnanimed olid 50+ variandis (nt "tallinn", "TALLINN", " Tallinn ")
UPDATE customers
SET city = INITCAP(TRIM(city))
WHERE city IS NOT NULL;
-- Tulemus: 50+ varianti → 12 linna
```

```sql
-- Kuupäevade normaliseerimine (kaks formaati: YYYY-MM-DD ja DD/MM/YYYY)
UPDATE sales
SET sale_date = TO_DATE(sale_date_raw, 'DD/MM/YYYY')
WHERE sale_date_raw ~ '^\d{2}/\d{2}/\d{4}$';
```

```sql
-- Tuleviku kuupäevade parandamine
UPDATE sales
SET sale_date = CURRENT_DATE
WHERE sale_date > CURRENT_DATE;
```

---

## Grupi Töö — Toomase 847 Duplikaati

Tiimis uurisime, kuidas 847 duplikaat-sale_id jagunevad domeenide vahel:

```sql
-- Duplikaadid müügikanalite kaupa
SELECT channel, COUNT(*) AS duplikaate
FROM sales s
JOIN (
    SELECT sale_id
    FROM sales
    GROUP BY sale_id
    HAVING COUNT(*) > 1
) dup ON s.sale_id = dup.sale_id
GROUP BY channel
ORDER BY duplikaate DESC;
```

**Tähelepanuväärne:** Enamik duplikaate pärinesid andmete importimisest — sama tellimus imporditi kaks korda erinevate ID-dega.

---

## Kontrollpäringud Pärast Puhastamist

```sql
SELECT COUNT(*) AS sales_ridu FROM sales;            -- Oodatav: ~10 118
SELECT COUNT(DISTINCT city) AS linnu FROM customers; -- Oodatav: 12
SELECT COUNT(*) FROM sales WHERE sale_date > CURRENT_DATE; -- Oodatav: 0
```

---

## Õppimise Reflektsioon

**Mis läks hästi:**
- `ROW_NUMBER()` OVER PARTITION BY loogika sai selgeks — elegantne viis duplikaatide märgistamiseks
- `INITCAP(TRIM())` kombinatsioon on lihtne aga võimas tekstipuhastuseks

**Mis vajas rohkem tööd:**
- `NULLIF()` kasutus — millal kasutada `COALESCE` vs `NULLIF`
- Regex mustrid kuupäevaformaatide tuvastamiseks

**Järgmiseks nädalaks (Nädal 3 — SQL JOINs):**
- Puhastatud andmed on valmis JOINide jaoks
- Anna Mets vajab ühendatud andmeid tabelitest `sales`, `customers`, `products`

---

*DACA26 · Nädal 2 · UrbanStyle.ltd andmeanalüüs*
