---

## 3. Pagination — kõik andmed, mitte ainult 1000

```python
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
```

---

## 4. ETL Pipeline

**ETL** = Extract, Transform, Load — andmetehnika standardmuster.

| Etapp | Mida teeb | UrbanStyle näide |
|---|---|---|
| **Extract** | Too andmed allikast | Supabase API → müük + kliendid |
| **Transform** | Puhasta ja analüüsi | pandas → RFM skoorid ja segmendid |
| **Load** | Salvesta tulemused | CSV + Plotly HTML graafikud |

### Pipeline struktuur

```python
def extract():
    # Too andmed Supabase'ist
    ...
    return orders, customers

def transform(orders, customers):
    # Puhasta, merge, RFM arvutamine
    ...
    return rfm

def load(rfm):
    # Salvesta CSV + graafikud
    ...

def run_pipeline():
    try:
        orders, customers = extract()
        rfm = transform(orders, customers)
        load(rfm)
        print("✅ PIPELINE VALMIS")
    except Exception as e:
        logger.error(f"PIPELINE EBAÕNNESTUS: {e}")
```

---

## 5. Logimine

```python
import logging

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info("Pipeline käivitatud")   # normaalne tegevus
logger.warning("0 uut tellimust")    # ebatavaline
logger.error("API ühendus katkestus") # viga
```

---

## Grupitöö (N8 GT) — Modulaarne Pipeline

**Väljund:** Töötav end-to-end pipeline, kus 4 moodulit ühendatakse üheks süsteemiks.

| Roll | Fail | Ülesanne |
|---|---|---|
| **Roll A** | `data_fetcher.py` | API päringud Supabase'ist |
| **Roll B** | `transform.py` | Andmete puhastamine + RFM |
| **Roll C** | `visualize_export.py` | Plotly graafikud + CSV eksport |
| **Roll D** | `pipeline.py` | Ühendab kõik moodulid + logimine |
| **Roll E** | `test_pipeline.py` | Valideerimine + ärisüntees |

---

## Lugemismaterjal

- McKinney *Python for Data Analysis* — Ch 7-8: Data Wrangling
- Supabase Python Client dokumentatsioon
- DACA Kursus 7: Moodul 4 — pandas edasijõudnud

---

*DACA26 · Nädal 8 · UrbanStyle.ltd andmepipeline*