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

## Äriline Mõju — Mida UrbanStyle Sellest Auditist Võidab

- **Käibearuandlus on praegu ebausaldusväärne.** Kui 5 116 rida (~34% tabelist) on duplikaadid, siis senised müügi- ja käibenumbrid on tõenäoliselt üle hinnatud, mis mõjutab otseselt eelarve- ja prognoosiotsuseid.
- **Kliendisegmenteerimine ja CRM-kampaaniad on osaliselt "pimedad".** 1 487 tehingut ilma `customer_id`-ta tähendab, et ligi 10% müügist ei saa siduda konkreetse kliendiga — see nõrgendab lojaalsusprogrammide ja personaliseeritud turunduse täpsust.
- **Negatiivsed ja nullilähedased summad (305 rida) viitavad protsessiveale**, mitte ainult andmesisestusveale — need tuleks IT/kassasüsteemi tasandil uurida, sest need võivad korduda ka tulevikus, kui algpõhjust ei paranda.

## Minu Soovitused (Iseseisev Analüüs)

1. **Enne mistahes müügianalüüsi:** deduplitseerida `sales` tabel `sale_id` põhjal ja dokumenteerida reegel (nt "hoia viimane sisestatud rida"), et duplikaatide eemaldamine oleks korratav, mitte ühekordne käsitsitöö.
2. **`customer_id` puudumise algpõhjus tuleks kaardistada müügikanaliti** — kahtlustan, et enamik puuduvatest väärtustest tuleb kassapõhistest (offline) tehingutest, kus klient ei registreerinud end. Kui see peab paika, on lahendus pigem protsessis (nt küsi e-mail kassas) kui andmetes.
3. **Negatiivsete summade (305 rida) jaoks soovitan eraldi käsitlust tagastustena**, mitte veana — kui äriloogika tunnistab tagastusi, tuleks lisada `transaction_type` veerg, et need edaspidi kohe eristada müügist.

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

**Miks see UrbanStyle'ile oluline on:** kuna `eco_certified` on otseselt seotud toodete keskkonnasõbralikkuse märgistusega, mõjutavad need 18 puuduvat väärtust otseselt jätkusuutlikkuse-raporteerimist — soovitan need 18 rida käsitsi üle vaadata enne, kui neid raportites "ei ole sertifitseeritud" kategooriasse arvestatakse.

**Märkus:** `category` ja `subcategory` veerud on juhendis segamini.

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

---

*DACA26 · Nädal 1 · UrbanStyle.ltd andmeanalüüs*

---

## 🇬🇧 In English

### DACA26 — Week 1: SQL Basics
**Individual Summary**

Programme: DACA — Data Analyst Career Accelerator  
Week: 1 — SQL Basics (SELECT, WHERE, DISTINCT, COUNT)  
Context: UrbanStyle.ltd sales data analysis for IT Director Toomas Kask

#### Goals and Results

All three core goals were achieved:
- Wrote SELECT queries to retrieve specific columns
- Filtered data with WHERE using comparison and logical operators
- Identified duplicates and counted unique values with DISTINCT and COUNT

#### Key Findings

**Part 1 — SELECT and FROM**
- Largest sale in the table: **€2,170.40**
- Smallest value discovered: **−€1,405.32** → data quality issue

**Part 2 — WHERE**

| Query | Result |
|-------|--------|
| Orders over €500 | 2,499 |
| Q1 2024 sales | 1,604 |
| Missing customer_id | 1,487 |
| Large orders 2024 (>€200) | 4,233 |
| Large online orders 2024 (>€200) | 1,581 |

**Part 3 — DISTINCT and COUNT (Sales table audit)**

| Metric | Value |
|--------|-------|
| Total rows | 15,234 |
| Rows with customer_id | 13,747 |
| Missing customer_id | 1,487 |
| Unique customers | 2,558 |
| Unique sale_id | 10,118 |
| Duplicates | 5,116 |

#### Business Impact — What UrbanStyle Gains From This Audit

- Revenue reporting is currently unreliable: with 5,116 duplicate rows (~34% of the table), past sales figures are likely overstated, directly affecting budgeting and forecasting.
- Customer segmentation and CRM campaigns are partly "blind": 1,487 transactions have no `customer_id`, so roughly 10% of sales can't be tied to a customer, weakening loyalty and personalisation efforts.
- The negative/near-zero amounts (305 rows) point to a process issue, not just a data-entry error, and should be investigated at the POS/IT level so it doesn't keep recurring.

#### My Recommendations (Independent Analysis)

1. Deduplicate the `sales` table on `sale_id` with a documented rule (e.g. "keep the most recently entered row") so the fix is repeatable, not manual.
2. Map the root cause of missing `customer_id` by sales channel — likely concentrated in offline/POS transactions where the customer wasn't registered; if so, the fix belongs in the process (e.g. ask for an email at checkout), not in the data.
3. Treat the negative amounts (305 rows) as returns rather than errors — add a `transaction_type` column so returns are separated from sales going forward instead of being filtered out each time.

**Team role — Product Data Explorer**

| Category | Products | Min | Max | Avg |
|----------|----------|-----|-----|-----|
| Footwear | 73 | €58.49 | €434.08 | €214.10 |
| Women's clothing | 70 | €32.93 | €351.33 | €192.58 |
| Men's clothing | 82 | €48.85 | €374.54 | €189.91 |
| Accessories | 67 | €13.53 | €231.13 | €125.71 |
| Children's clothing | 70 | €22.70 | €168.82 | €85.30 |

Data quality: no missing values in `cost_price` or `retail_price` (0 NULL), but 18 missing values were found in `eco_certified` — directly relevant to sustainability reporting, so worth a manual review before those rows are counted as "not certified."

#### Learning Reflection

**What went well:**
- SQL logic maps intuitively to Excel logic
- The difference between IS NULL and = NULL became clear immediately
- Discovering the negative sale (−€1,405.32) showed why data quality checks matter

**What needed more work:**
- Combining multiple aggregate functions in one query
- Using UNION ALL without GROUP BY for channel comparison

**Next week (Week 2 — SQL Cleaning):**
- Complete date normalisation (~3% are NULL)
- Duplicate removal strategy
