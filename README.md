# DACA Portfoolio

**Programm:** Data Analyst Career Accelerator (DACA)  
**Osaleja:** Doris Kaarus  
**Algus:** 27.04.2026

## Kirjeldus

See repositoorium sisaldab minu DACA õppeprojekte ja portfooliot. Andmestik: UrbanStyle.ltd fiktiivsed müügiandmed (sales, customers, products).

## Minust

Enne DACA programmi töötasin mobiilitehnikuna, mis andis kindla tehnilise taipu ja oskuse probleemide juurpõhjuseni jõuda, ning personalijuhina, mis arendas inimestega klappimise ja suhtlemise oskust. See kombinatsioon sobib hästi andmeanalüütiku rolliga — tuleb nii tehniliselt süveneda kui ka tulemused selgelt lahti seletada.

Praegu tunnen kõige rohkem huvi Marketing/Customer Analytics suuna vastu: Python-kood ja visuaalid on täpselt see, mida tahan igapäevaselt teha, ja olen seda juba proovinud — nädal 7 RFM-analüüsis selgitasin välja, kes on VIP kliendid, kes on lahkumas ning kellele mis kampaaniat suunata. Pikemas plaanis näen end mentorina, kes aitab uusi andmeanalüütikuid järele.

## Nädalate Kokkuvõtted

| Nädal | Teema | Fail |
|---|---|---|
| 0 | Süsteemide seadistamine (GitHub, Supabase, NotebookLM) | [README.md](week-0-system-setup/README.md) |
| 1 | SQL Põhitõed — SELECT, WHERE, DISTINCT, COUNT | [README.md](week-1-sql-basics/README.md) |
| 2 | SQL Puhastamine — duplikaadid, NULL-id, vormingud | [README.md](week-2-sql-cleaning/README.md) |
| 3 | SQL JOINs — INNER JOIN, LEFT JOIN, mitu tabelit | [README.md](week-3-sql-joins/README.md) |
| 4 | SQL Agregatsioon — GROUP BY, HAVING, CTE, window functions | [README.md](week-4-sql-aggregation/README.md) |
| 5 | Visualiseerimise disain — diagrammitüübid, dashboard, Plotly+Streamlit | [README.md](week-5-visualization-design/README.md) |
| 6 | Visualiseerimise andmed — annotatsioonid, andmelood, publiku disain | [README.md](week-6-data-storytelling/README.md) |
| 7 | Python Pandas — DataFrame, groupby, merge, RFM analüüs | [README.md](week-7-python-pandas-rfm/README.md) |
| 8 | Python APIs — Supabase Python Client, Pipeline | [README.md](week-8-python-apis-pipeline/README.md) |
| 9 | Karjääri Ettevalmistus — värbamisjuhendi koostamine, peer review | [README.md](week-9-career-prep/README.md) |
| 10 | Portfoolio Kaitsmine — grupitöö, lõpuesitlus | [README.md](week-10-portfolio-defense/README.md) |

## Oskused

- **SQL:** PostgreSQL, Supabase — SELECT, JOIN, GROUP BY, HAVING, CTE, window functions
- **Python:** pandas, plotly, streamlit, Jupyter Notebook
- **Visualiseerimine:** Plotly Express, Streamlit, CodePen
- **Tööriistad:** Git, GitHub, VS Code, NotebookLM

## Andmebaas

UrbanStyle.ltd — fiktiivsed müügiandmed

| Tabel | Ridu |
|---|---|
| sales | ~10 118 (pärast puhastamist) |
| customers | ~3 150 |
| products | 362 |

## Meeskonnatöö

Paralleelselt individuaalsete ülesannetega olen 5-liikmelise meeskonna (koos Tekla, Ahto, Henri ja Kaariniga) liige projektis [Sales-Analytics](https://github.com/kaarusdoris-a11y/Sales-Analytics) — UrbanStyle.ltd müügiandmete analüüs IT-direktor Toomas Kase jaoks. Kokkuvõte minu panusest ja tiimi töökorraldusest: [TEAMWORK.md](./TEAMWORK.md).

## AI Kasutamine

Kasutasin AI-d (Claude) läbivalt kogu programmi vältel:

- **SQL debugimine:** window function'ite (`LAG`, `NTILE`, `ROW_NUMBER`) loogika kontroll nädalal 4 ja CTE struktuuri selgitamine.
- **RFM segmenteerimise valideerimine:** nädalal 7 kontrollisin AI abiga oma R/F/M skoorimise loogikat ja segmentide piiride mõistlikkust enne äriraporti kirjutamist.
- **Python koodi ülevaatus:** Streamlit dashboard'i (nädal 5) ja ETL pipeline'i (nädal 8) veakäsitluse ja loogika kontroll.


**Aus reflektsioon:** AI aitas kõige rohkem tehnilise debugimise ja vormistamise juures — kiirem on lasta AI-l kontrollida süntaksit või SQL-loogikat, kui ise iga viga käsitsi otsida. Lõplikud äriotsused ja soovitused (nt millist segmenti prioriseerida, kellele mis kampaania saata) pidin siiski ise sõnastama.

## Kontakt

- GitHub: [github.com/kaarusdoris-a11y](https://github.com/kaarusdoris-a11y)
- Email: kaarusdoris@gmail.com
- Linkedin : www.linkedin.com/in/kaarusdoris


---

## 🇬🇧 In English

**DACA Portfolio**

Programme: Data Analyst Career Accelerator (DACA)
Participant: Doris Kaarus
Start: 27 April 2026

### Description

This repository contains my DACA learning projects and portfolio. Dataset: UrbanStyle.ltd fictional sales data (sales, customers, products).

### About Me

Before DACA I worked as a mobile phone technician, which built solid technical instincts and a habit of tracing problems to their root cause, and as an HR manager, which developed my people skills and communication. That combination fits data analytics well — it takes both technical depth and the ability to explain results clearly.

Right now I'm most drawn to Marketing/Customer Analytics: writing Python code and building visuals is exactly what I want to do day to day, and I've already put it into practice — in Week 7's RFM analysis I identified VIP customers, customers at risk of churning, and who should receive which campaign. Longer term, I'd like to become a mentor for new data analysts.

### Weekly Summaries

| Week | Topic | File |
|------|-------|------|
| 0 | System Setup (GitHub, Supabase, NotebookLM) | [README.md](week-0-system-setup/README.md) |
| 1 | SQL Basics — SELECT, WHERE, DISTINCT, COUNT | [README.md](week-1-sql-basics/README.md) |
| 2 | SQL Cleaning — duplicates, NULLs, formats | [README.md](week-2-sql-cleaning/README.md) |
| 3 | SQL JOINs — INNER JOIN, LEFT JOIN, multiple tables | [README.md](week-3-sql-joins/README.md) |
| 4 | SQL Aggregation — GROUP BY, HAVING, CTE, window functions | [README.md](week-4-sql-aggregation/README.md) |
| 5 | Visualisation Design — chart types, dashboard, Plotly+Streamlit | [README.md](week-5-visualization-design/README.md) |
| 6 | Data Storytelling — annotations, narratives, audience design | [README.md](week-6-data-storytelling/README.md) |
| 7 | Python Pandas — DataFrame, groupby, merge, RFM analysis | [README.md](week-7-python-pandas-rfm/README.md) |
| 8 | Python APIs — Supabase Python Client, Pipeline | [README.md](week-8-python-apis-pipeline/README.md) |
| 9 | Career Prep — hiring guide, peer review | [README.md](week-9-career-prep/README.md) |
| 10 | Portfolio Defense — group work, final presentation | [README.md](week-10-portfolio-defense/README.md) |

### Skills
- **SQL:** PostgreSQL, Supabase — SELECT, JOIN, GROUP BY, HAVING, CTE, window functions
- **Python:** pandas, plotly, streamlit, Jupyter Notebook
- **Visualisation:** Plotly Express, Streamlit, CodePen
- **Tools:** Git, GitHub, VS Code, NotebookLM

### Database

UrbanStyle.ltd — fictional sales data

| Table | Rows |
|-------|------|
| sales | ~10,118 (after cleaning) |
| customers | ~3,150 |
| products | 362 |

### Teamwork

Alongside the individual weekly tasks, I'm a member of a 5-person team (with Tekla, Ahto, Henri and Kaarin) working on [Sales-Analytics](https://github.com/kaarusdoris-a11y/Sales-Analytics) — a UrbanStyle.ltd sales-data analysis for IT Director Toomas Kask. Summary of my contribution and the team's setup: [TEAMWORK.md](./TEAMWORK.md).

### AI Usage

I used AI (Claude) throughout the programme:

- **SQL debugging:** checking window function (`LAG`, `NTILE`, `ROW_NUMBER`) logic in Week 4 and clarifying CTE structure.
- **RFM segmentation validation:** in Week 7 I used AI to sanity-check my R/F/M scoring logic and segment boundaries before writing the business report.
- **Python code review:** reviewing error handling and logic in the Streamlit dashboard (Week 5) and the ETL pipeline (Week 8).


**Honest reflection:** AI helped most with technical debugging and formatting — it's faster to have AI check syntax or SQL logic than to hunt down every error myself. But the final business decisions and recommendations (e.g. which segment to prioritize, which campaign to send to whom) I still had to work out myself.

### Contact
- GitHub: github.com/kaarusdoris-a11y
- Email: kaarusdoris@gmail.com
- Linkedin : www.linkedin.com/in/kaarusdoris
