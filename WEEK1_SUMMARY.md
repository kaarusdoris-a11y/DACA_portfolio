# DACA26 — Nädal 1: SQL Basics
## Individuaalne Kokkuvõte

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Nädal:** 1 — SQL Basics (SELECT, WHERE, DISTINCT, COUNT)  
**Kontekst:** UrbanStyle.ltd müügiandmete analüüs IT-direktor Toomas Kase jaoks

---

## Eesmärgid ja Tulemused

Nädala eesmärk oli õppida SQL põhikäske (`SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, `COUNT`) ja kasutada neid UrbanStyle'i Supabase andmebaasis reaalse äriprobleemi lahendamiseks.

Kõik kolm põhieesmärki täideti:
- Kirjutasin `SELECT` päringuid konkreetsete veergude valimiseks
- Filtreerisin andmeid `WHERE` klausliga, kasutades võrdlus- ja loogikaoperaatoreid
- Tuvastasin duplikaadid ja loendsin unikaalseid väärtusi `DISTINCT` ja `COUNT` abil

---

## Andmebaasi Seadistus (Samm 0)

Laadisin UrbanStyle'i andmed Supabase'i kolme etapis:

| Tabel | Ridu |
|---|---|
| `products` | 350 |
| `customers` | ~3 150 |
| `sales` | 15 234 |

`sales.csv` import nõudis staging-tabelit (`sales_import`), kuna kuupäevad olid kahes erinevas formaadis (`YYYY-MM-DD` ja `DD/MM/YYYY`). Lahendus: `CASE + TO_DATE()` teisendus.

---

## Osa 1 — SELECT ja FROM

**Põhijäreldus:** `SELECT` valib veerge, `FROM` määrab tabeli. `ORDER BY` sorteerib, `LIMIT` piirab.

### Peamised leiud harjutustest

```sql
-- Suurim müük kogu tabelis
SELECT sale_id, total_price AS summa
FROM sales
ORDER BY total_price DESC
LIMIT 5;
-- Tulemus: max 2170.40 €
```

```sql
-- Väikseim müük — negatiivne väärtus avastatud
SELECT sale_id, total_price AS summa
FROM sales
ORDER BY total_price ASC
LIMIT 5;
-- Tulemus: min -1405.32 € → andmekvaliteedi probleem
```

**Tähelepanuväärne:** Tabelis esineb negatiivseid müügisummasid, mis viitavad andmekvaliteedi probleemidele.

---

## Osa 2 — WHERE

**Põhijäreldus:** `WHERE` filtreerib ridu. `IS NULL` leiab puuduvad väärtused (mitte `= NULL`).

### Peamised leiud harjutustest

| Päring | Tulemus |
|---|---|
| Tellimused üle 500 € | 2 499 |
| Q1 2024 müügid | 1 604 |
| Puuduv `customer_id` | 1 487 |
| Suured tellimused 2024 (>200 €) | 4 233 |
| Suured online-tellimused 2024 (>200 €) | 1 581 |

```sql
-- Kahtlased read: summa <= 0 VÕI klient puudub
SELECT customer_id, total_price
FROM sales
WHERE customer_id IS NULL
   OR total_price <= 0;
-- Tulemus: märkimisväärne hulk probleemseid ridu
```

---

## Osa 3 — DISTINCT ja COUNT

**Põhijäreldus:** `COUNT(*)` loeb kõiki ridu, `COUNT(veerg)` jätab NULL-id välja, `COUNT(DISTINCT veerg)` annab unikaalsete arvu.

### Sales tabeli audit

```sql
SELECT
    COUNT(*)                          AS ridu_kokku,        -- 15 234
    COUNT(customer_id)                AS klientidega,       -- 13 747
    COUNT(*) - COUNT(customer_id)     AS puudub_klient,     -- 1 487
    COUNT(DISTINCT customer_id)       AS unikaalseid_kliente -- 2 558
FROM sales;
```

### Duplikaatide tuvastamine (Toomase meetod)

```sql
-- Samm A
SELECT COUNT(*) FROM sales;                  -- 15 234
-- Samm B
SELECT COUNT(DISTINCT sale_id) FROM sales;   -- 10 118
-- Vahe = duplikaadid: 5 116
```

### Customers tabeli audit

```sql
SELECT
    COUNT(*)                        AS kokku,           -- ~3 150
    COUNT(DISTINCT email)           AS unikaalseid,
    COUNT(*) - COUNT(DISTINCT email) AS duplikaatseid   -- 510
FROM customers;
```

---

## Süntees — Vastused Toomase Küsimustele

| Toomase küsimus | Vastus |
|---|---|
| Täpne duplikaatide arv | **5 116** (15 234 − 10 118) |
| NULL `customer_id` väärtused | **1 487** tellimust |
| Suurim müük | **2 170.40 €** |
| Kahtlased read (≤ 0 €) | **305** tellimust |

---

## Grupi Töö — Roll C: Tooteandmete Uurija

Tiimi töös võtsin rolli **C (Product Data Explorer)** — uurisin `products` tabelit Toomase jaoks.

### Peamised leiud

```sql
-- Toodete koguarv ja kategooriad
SELECT
    COUNT(*)               AS toodete_arv,       -- 362
    COUNT(DISTINCT category) AS kategooriaid     -- 5
FROM products;
```

**5 kategooriat:** `jalanõusid`, `meeste_riided`, `naiste_riided`, `laste_riided`, `aksessuaarid`

**Hinnavahemik:** 13.53 € – 434.08 €

```sql
-- Kategooriate jaotus
SELECT category, COUNT(*) AS toodete_arv
FROM products
GROUP BY category
ORDER BY toodete_arv DESC;
```

| Kategooria | Tooteid |
|---|---|
| meeste_riided | 82 |
| jalanõusid | 73 |
| laste_riided | 70 |
| naiste_riided | 70 |
| aksessuaarid | 67 |

```sql
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

| Kategooria | Min | Max | Keskmine |
|---|---|---|---|
| jalanõusid | 58.49 € | 434.08 € | 214.10 € |
| naiste_riided | 32.93 € | 351.33 € | 192.58 € |
| meeste_riided | 48.85 € | 374.54 € | 189.91 € |
| aksessuaarid | 13.53 € | 231.13 € | 125.71 € |
| laste_riided | 22.70 € | 168.82 € | 85.30 € |

**Andmekvaliteet:** `cost_price` ja `retail_price` veergudes puuduvaid väärtusi ei leitud (0 NULL). Küll aga avastati `eco_certified` veerus 18 puuduvat väärtust.

**Märkus:** `category` ja `subcategory` veerud on osaliselt segamini — vajab puhastamist (Nädal 2).

---

## Õppimise Reflektsioon

**Mis läks hästi:**
- SQL-i loogika ja Exceli loogika klapivad intuitiivselt
- `IS NULL` vs `= NULL` erinevus sai selgeks kohe
- Negatiivne müügisumma (-1405.32 €) avastamine näitas, miks andmekvaliteedi kontroll on oluline

**Mis vajas rohkem tööd:**
- Mitme agregaatfunktsiooni kombineerimine ühes päringus
- `UNION ALL` kasutamine ilma `GROUP BY`-ta kanalite võrdlemiseks

**Järgmiseks nädalaks (Nädal 2 — SQL Cleaning):**
- Kuupäevade normaliseerimise lõpetamine (`~3%` on `NULL`)
- Duplikaatide eemaldamise strateegia
- `category`/`subcategory` andmete puhastamine

---

*DACA26 · Nädal 1 · UrbanStyle.ltd andmeanalüüs*
