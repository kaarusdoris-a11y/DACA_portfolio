# DACA26 — Nädal 3: SQL JOINs
## Individuaalne Kokkuvõte

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Nädal:** 3 — SQL JOINs (INNER JOIN, LEFT JOIN, mitu tabelit)  
**Kontekst:** UrbanStyle.ltd andmete ühendamine Anna Metsa turundusküsimustele vastamiseks

---

## Eesmärgid ja Tulemused

Kõik kolm põhieesmärki täideti:
- Ühendasin kaks tabelit `INNER JOIN` abil `ON` klauslit ja tabeli aliaseid kasutades
- Tuvastasin "kadunud" andmeid `LEFT JOIN + WHERE IS NULL` mustriga
- Ehitasin 3+ tabeli päringuid, mis vastasid Anna äriküsimustele

---

## Kontekst: Anna Tahab Vastuseid

Pärast W2 puhastamist ütles Toomas: *"Sales tabel on nüüd usaldusväärne."*

Kuid Anna Mets (turundusjuht): *"Ma ei saa sellest midagi! Ma näen ainult numbreid. Kes on meie parimad kliendid? Mida nad ostavad?"*

Toomas selgitab: *"JOIN on nagu VLOOKUP Excelis, aga palju võimsam."*

---

## Osa 1 — INNER JOIN

**Põhijäreldus:** `INNER JOIN` tagastab ainult read, mis mõlemas tabelis vastavad.

```sql
-- Müügid koos kliendi nimedega
SELECT
    s.sale_id,
    s.sale_date,
    s.total_price,
    c.first_name || ' ' || c.last_name AS kliendi_nimi,
    c.city
FROM sales s
INNER JOIN customers c ON s.customer_id = c.customer_id
ORDER BY s.total_price DESC
LIMIT 10;
```

```sql
-- Müügid koos tootenimede ja kategooriatega
SELECT
    s.sale_id,
    p.product_name,
    p.category,
    s.total_price,
    s.channel
FROM sales s
INNER JOIN products p ON s.product_id = p.product_id
ORDER BY s.sale_date DESC
LIMIT 20;
```

---

## Osa 2 — LEFT JOIN: Kadunud Andmete Tuvastamine

**Põhijäreldus:** `LEFT JOIN + WHERE parempoolne.id IS NULL` leiab "auke" andmetes.

```sql
-- Kliendid, kes pole kunagi ostnud
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS nimi,
    c.email,
    c.city
FROM customers c
LEFT JOIN sales s ON c.customer_id = s.customer_id
WHERE s.customer_id IS NULL
ORDER BY c.customer_id;
-- Tulemus: 592 klienti pole kunagi ostnud
```

```sql
-- Tooted, mida pole kunagi müüdud
SELECT
    p.product_id,
    p.product_name,
    p.category,
    p.retail_price
FROM products p
LEFT JOIN sales s ON p.product_id = s.product_id
WHERE s.product_id IS NULL;
-- Tulemus: 23 toodet pole kordagi müüdud
```

---

## Osa 3 — Mitme Tabeli JOINid

```sql
-- TOP 20 klienti
SELECT
    c.first_name || ' ' || c.last_name AS klient,
    c.city,
    COUNT(s.sale_id)             AS ostude_arv,
    SUM(s.total_price)           AS koguostud,
    ROUND(AVG(s.total_price), 2) AS kesk_ost
FROM sales s
INNER JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.city
ORDER BY koguostud DESC
LIMIT 20;
```

```sql
-- Parimad tooted linnade kaupa (3 tabelit)
SELECT
    c.city,
    p.category,
    COUNT(s.sale_id)   AS müügid,
    SUM(s.total_price) AS käive
FROM sales s
INNER JOIN customers c ON s.customer_id = c.customer_id
INNER JOIN products  p ON s.product_id  = p.product_id
GROUP BY c.city, p.category
ORDER BY c.city, käive DESC;
```

---

## Anna Küsimustele Vastused

| Anna küsimus | Tulemus |
|---|---|
| Kes on parimad kliendid? | TOP klient: ~12 000+ € ostud |
| Millised tooted müüvad? | Jalanõud → kõrgeim käive |
| Kes pole kunagi ostnud? | 592 klienti |
| Millised tooted pole müüdud? | 23 toodet |
| Millised kanalid töötavad? | Online > Store |

---

## Õppimise Reflektsioon

**Mis läks hästi:**
- `LEFT JOIN + IS NULL` muster on elegantne — leiab "auke" andmetes
- Kolme tabeli JOIN-päring tuli loogiliselt välja, kui aliased selged olid

**Mis vajas rohkem tööd:**
- `RIGHT JOIN` vs `LEFT JOIN` — kumba poolt vaadata?

**Järgmiseks (Nädal 4 — SQL Agregatsioon):**
- Kristi (CEO) vajab juhatuse koosolekuks koondnumbreid
- `GROUP BY`, `HAVING`, CTE-d ja window functions

---

*DACA26 · Nädal 3 · UrbanStyle.ltd andmeanalüüs*
