# DACA26 — Nädal 0: Süsteemide Seadistamine
## Individuaalne Kokkuvõte

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Nädal:** 0 — Onboarding (GitHub, Supabase, NotebookLM)  
**Kuupäev:** Aprill 2026

---

## Eesmärk

Kõikide tööriistade seadistamine ja meeskonna ühendamine ühtsesse töökeskkonda enne esimest andmeanalüüsi nädalat.

---

## Tehtud tööd

### GitHub
- Loodud meeskonna repo: `kaarusdoris-a11y/Sales-Analytics`
- Seadistatud `main` haru
- Lisatud meeskonnaliikmed kaastöötajatena
- **Roll:** GitHub Repo Seadistaja

### Supabase
- Loodud projekt: **Urban Style ltd**
- Ühendatud andmebaas: `gfsllgirzwcqdxliozcv`
- Loodud tabelid: `sales`, `customers`, `products`, `inventory`
- Andmete import: `sales.csv` vajas staging-tabelit (`sales_import`), kuna kuupäevad olid kahes formaadis

### NotebookLM
- Seadistatud RAG töökeskkond kursusematerjalide põhjal
- Lisatud CORE failid: `urbanstyle_company`, `urbanstyle_characters`, `daca_program_framework`, `da_tools_guide`

---

## Andmebaasi Struktuur

| Tabel | Ridu | Kirjeldus |
|---|---|---|
| `sales` | 15 234 | Müügitehingud (enne puhastamist) |
| `customers` | ~3 150 | Kliendid |
| `products` | 362 | Tooted |
| `inventory` | — | Laoseis |

---

## Meeskond

| Nimi | Roll |
|---|---|
| Doris Kaarus | GitHub Repo Seadistaja |
| Henri Greenbaum | Supabase Seadistaja |
| Tekla Relika Ani | Data Processing |
| Ahto Sooaru | Team Charter Koostaja |
| Kaarin Peet | Portfoolio Struktuur |

---

## Õppimise Reflektsioon

**Mis läks hästi:**
- GitHub repo seadistamine oli intuitiivne
- Supabase SQL Editor töötas kohe — `SELECT 1;` andis kohe tulemuse

**Suurim üllatus:**
- Toomas andis meile vabad käed — ootasin rohkem juhendamist, aga see sundis ise otsuseid tegema

**Mis vajas rohkem tööd:**
- `sales.csv` import — kuupäevaformaatide segu (`YYYY-MM-DD` ja `DD/MM/YYYY`) nõudis CASE + TO_DATE() lahendust

**Järgmiseks nädalaks (Nädal 1 — SQL Põhitõed):**
- Esimesed SELECT päringud UrbanStyle'i andmestikul
- Toomase küsimustele vastamine: duplikaadid, NULL-id, suurimad müügid

---

*DACA26 · Nädal 0 · UrbanStyle.ltd andmeanalüüs*
