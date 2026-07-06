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
---

## 🇬🇧 In English

### DACA26 — Week 0: System Setup
**Individual Summary**

Programme: DACA — Data Analyst Career Accelerator
Week: 0 — Onboarding (GitHub, Supabase, NotebookLM)
Date: April 2026

#### Goal
Set up all tools and connect the team into a unified work environment before the first data analysis week.

#### Work Completed

**GitHub**
- Created team repo: kaarusdoris-a11y/Sales-Analytics
- Configured main branch
- Added team members as collaborators
- Role: GitHub Repo Setup

**Supabase**
- Created project: Urban Style ltd
- Connected database: gfsllgirzwcqdxliozcv
- Created tables: sales, customers, products, inventory
- Data import: sales.csv required a staging table (sales_import) due to mixed date formats

**NotebookLM**
- Set up RAG workspace based on course materials
- Added CORE files: urbanstyle_company, urbanstyle_characters, daca_program_framework, da_tools_guide

#### Database Structure

| Table | Rows | Description |
|-------|------|-------------|
| sales | 15,234 | Sales transactions (before cleaning) |
| customers | ~3,150 | Customers |
| products | 362 | Products |
| inventory | — | Stock levels |

#### Team

| Name | Role |
|------|------|
| Doris Kaarus | GitHub Repo Setup |
| Henri Greenbaum | Supabase Setup |
| Tekla Relika Ani | Data Processing |
| Ahto Sooaru | Team Charter Author |
| Kaarin Peet | Portfolio Structure |

#### Learning Reflection

**What went well:**
- GitHub repo setup was intuitive
- Supabase SQL Editor worked immediately — SELECT 1; returned a result right away

**Biggest surprise:**
- Toomas gave us free rein — I expected more guidance, but this forced us to make decisions independently

**What needed more work:**
- sales.csv import — mixed date formats (YYYY-MM-DD and DD/MM/YYYY) required a CASE + TO_DATE() solution

**Next week (Week 1 — SQL Basics):**
- First SELECT queries on UrbanStyle data
- Answering Toomas's questions: duplicates, NULLs, largest sales
