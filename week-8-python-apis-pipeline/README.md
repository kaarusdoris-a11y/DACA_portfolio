# Nädal 8 — Python APIs ja Andmepipeline

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Teema:** Python APIs — automatiseeritud andmepipeline  
**Töövihikud:** N8 IT (Iseseisva õppe töövihik) + N8 GT (Grupitöö juhend)  
**Versioon:** 2.9

**Äriprobleem:** Käsitsi CSV-eksport iga nädal ei püsi UrbanStyle'i kasvades — ilma automatiseeritud ja turvalise API-pipelineta kulub liiga palju aega korduvale käsitööle ning risk vananenud või valede andmete peal otsuseid teha kasvab.

---

## Selle nädala eesmärgid

1. Pääseda ligi UrbanStyle andmetele Supabase Python client'i kaudu, kasutades API päringuid
2. Kirjutada parameetritega funktsioone, mis automatiseerivad korduvaid analüüsiülesandeid
3. Ehitada andmepipeline, mis ühendab andmete toomise, töötlemise ja visualiseerimise üheks automatiseeritud vooluks

---

## 1. CSV vs API

Nädal 7-s laadisime andmeid käsitsi. Nädal 8-s räägib Python otse Supabase'iga.

| Viis | Sammud | Sobib |
|---|---|---|
| CSV | Dashboard, Export, Salvesta, read_csv() | Ühekordne analüüs |
| API | Python helistab Supabase'ile, andmed kohe | Automatiseerimine |

### Supabase Python Client vs SQL

| SQL | Supabase Python Client |
|---|---|
| SELECT * FROM sales | .table('sales').select('*') |
| WHERE store_location = 'Tallinn' | .eq('store_location', 'Tallinn') |
| ORDER BY total_price DESC | .order('total_price', desc=True) |
| LIMIT 10 | .limit(10) |

---

## 2. Turvalisus — .env fail

API key ei tohi kunagi otse koodi kirjutada.

.env faili sisu:

    SUPABASE_URL=https://sinu-projekt.supabase.co
    SUPABASE_KEY=eyJhbGci...

.gitignore peab sisaldama:

    .env

---

## 3. Pagination — kõik andmed, mitte ainult 1000

Supabase tagastab vaikimisi max 1000 rida. Kõigi andmete saamiseks:

    def fetch_all(table_name):
        all_data = []
        page = 0
        page_size = 1000
        while True:
            response = supabase.table(table_name).select('*').range(
                page * page_size, (page + 1) * page_size - 1
            ).execute()
            all_data.extend(response.data)
            if len(response.data) < page_size:
                break
            page += 1
        return pd.DataFrame(all_data)

---

## 4. ETL Pipeline

ETL = Extract, Transform, Load — andmetehnika standardmuster.

| Etapp | Mida teeb | UrbanStyle näide |
|---|---|---|
| Extract | Too andmed allikast | Supabase API, müük ja kliendid |
| Transform | Puhasta ja analüüsi | pandas, RFM skoorid ja segmendid |
| Load | Salvesta tulemused | CSV ja Plotly HTML graafikud |

---

## 5. Logimine

Logimine annab nähtavuse — näed täpselt mis pipeline'is toimus.

| Tase | Millal |
|---|---|
| logger.info() | Normaalne tegevus |
| logger.warning() | Ebatavaline olukord |
| logger.error() | Viga |

---

## Grupitöö (N8 GT) — Modulaarne Pipeline

**Äriprobleem (grupitöö):** Viis eraldi moodulit (andmete toomine, teisendus, visualiseerimine, orkestreerimine, testimine) peavad ühenduma üheks veatuks pipeline'iks — kui üks moodul katkeb, katkeb kogu automatiseeritud aruandlus, millele ettevõte tugineb.

Väljund: töötav end-to-end pipeline, kus 4 moodulit ühendatakse üheks süsteemiks.

| Roll | Fail | Ülesanne |
|---|---|---|
| Roll A | data_fetcher.py | API päringud Supabase'ist |
| Roll B | transform.py | Andmete puhastamine ja RFM |
| Roll C | visualize_export.py | Plotly graafikud ja CSV eksport |
| Roll D | pipeline.py | Ühendab kõik moodulid ja logimine |
| Roll E | test_pipeline.py | Valideerimine ja ärisüntees |

---

## Lugemismaterjal

- McKinney Python for Data Analysis, Ch 7-8: Data Wrangling
- Supabase Python Client dokumentatsioon
- DACA Kursus 7, Moodul 4: pandas edasijõudnud

---

DACA26 · Nädal 8 · UrbanStyle.ltd andmepipeline
