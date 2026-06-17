# Nädal 7 — Python Pandas

**Programm:** DACA — Andmeanalüütiku Karjäärikiirendi  
**Teema:** Python Pandas — andmeanalüüs programmeerimisega  
**Töövihikud:** N7 IT (Iseseisva õppe töövihik) + N7 GT (Grupitöö juhend)  
**Versioon:** 2.9

---

## Selle nädala eesmärgid

1. Laadida ja uurida andmeid pandas DataFrame'ina (`read_csv()`, `head()`, `describe()`, `info()`)
2. Filtreerida, grupeerida ja transformeerida andmeid (`boolean indexing`, `groupby`, `merge`) — ja mõista, kuidas need vastavad SQL lausetele
3. Luua interaktiivseid Plotly graafikuid pandas andmete põhjal

---

## 1. SQL → Python sild

Kuus nädalat kirjutasime SQL-i. Python/pandas kasutab samu kontseptsioone — lihtsalt erineva süntaksiga.

| SQL | Python (pandas) |
|---|---|
| `SELECT * FROM tabel` | `df` (kogu DataFrame) |
| `SELECT * FROM tabel LIMIT 5` | `df.head()` |
| `SELECT COUNT(*) FROM tabel` | `df.shape[0]` |
| `DESCRIBE tabel` | `df.dtypes` või `df.info()` |
| `SELECT AVG(hind), MAX(hind) FROM tabel` | `df.describe()` |
| `WHERE linn = 'Tallinn'` | `df[df['store_location'] == 'Tallinn']` |
| `WHERE hind > 100 AND linn = 'Tallinn'` | `df[(df['total_price'] > 100) & (df['store_location'] == 'Tallinn')]` |
| `GROUP BY linn` + `SUM(hind)` | `df.groupby('store_location')['total_price'].sum()` |
| `JOIN customers ON customer_id` | `pd.merge(df_sales, df_customers, on='customer_id', how='left')` |

---

## 2. DataFrame põhioperatsioonid

### Andmete laadimine

```python
import pandas as pd

# CSV-st
df = pd.read_csv('urbanstyle_sales.csv')

# Esimene ülevaade
df.head()        # esimesed 5 rida
df.shape         # (read, veerud) — nt (1250, 8)
df.dtypes        # veerutüübid
df.info()        # tüübid + null-väärtuste arv
df.describe()    # statistika (min, max, mean, std)
```

### Boolean indexing (= SQL WHERE)

```python
# Lihtne filter
tallinn = df[df['store_location'] == 'Tallinn']

# Mitu tingimust — AND kasutab &, OR kasutab |
# NB! Iga tingimus peab olema ümarsulgudes!
suured_tallinn = df[(df['total_price'] > 100) & (df['store_location'] == 'Tallinn')]

# NOT — tilde ~
mitte_tallinn = df[~(df['store_location'] == 'Tallinn')]
```

### groupby (= SQL GROUP BY)

```python
# Käive kaupluste lõikes
df.groupby('store_location')['total_price'].sum()

# Mitu statistikut korraga
df.groupby('store_location')['total_price'].agg(['sum', 'mean', 'count'])

# Grupeeri mitme veeru järgi
df.groupby(['store_location', 'category'])['total_price'].sum().reset_index()
```

### merge (= SQL JOIN)

```python
# LEFT JOIN customers tabeliga
df = pd.merge(df_sales, df_customers,
              on='customer_id',
              how='left')  # how='inner', 'left', 'right', 'outer'
```

---

## 3. Plotly Express koos Pandas'iga

```python
import plotly.express as px

# Tulpdiagramm — käive kaupluste lõikes
kauplused = df.groupby('store_location')['total_price'].sum().reset_index()
fig = px.bar(kauplused,
             x='store_location', y='total_price',
             title='Käive kaupluste lõikes',
             labels={'store_location': 'Kaupluse asukoht', 'total_price': 'Käive (EUR)'})
fig.show()

# Joondiagramm — kuine trend
kuud = df.groupby('month')['total_price'].sum().reset_index()
fig2 = px.line(kuud, x='month', y='total_price',
               title='Kuine käive 2024')
fig2.show()
```

---

## 4. RFM analüüs Python'is

**Väljakutse (Marko Saar, Product Manager):**  
*"Meil on uus kliendiandmestik. Ma tahan teada: kes on meie VIP-kliendid? Palju nad kulutavad? Ja miks mõned lõpetavad ostmise? Ma tahan saata erinevaid e-maile VIP-dele ja riskiklientidele."*

### RFM arvutamine pandas'iga

```python
from datetime import date
import pandas as pd

today = pd.Timestamp('today')

rfm = df.groupby('customer_id').agg(
    recency=('sale_date', lambda x: (today - pd.to_datetime(x).max()).days),
    frequency=('sale_id', 'count'),
    monetary=('total_price', 'sum')
).reset_index()

# Skoreeri 1–5 (5 = parim)
rfm['r_score'] = pd.qcut(rfm['recency'], 5, labels=[5,4,3,2,1])
rfm['f_score'] = pd.qcut(rfm['frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm['m_score'] = pd.qcut(rfm['monetary'], 5, labels=[1,2,3,4,5])

# Segmenteerimine
def segment(row):
    r, f, m = int(row['r_score']), int(row['f_score']), int(row['m_score'])
    if r >= 4 and f >= 4 and m >= 4:
        return 'Tšempion'
    elif r >= 3 and f >= 3:
        return 'Lojaalne klient'
    elif r >= 4 and f <= 2:
        return 'Uus klient'
    elif r <= 2 and f >= 3:
        return 'Ohu all'
    else:
        return 'Kadunud klient'

rfm['segment'] = rfm.apply(segment, axis=1)
```

### Segmentide tähendus

| Segment | Kirjeldus | Tegevus |
|---|---|---|
| **Tšempion** | Ostab sageli, hiljuti, palju | VIP kampaania, eelvaated |
| **Lojaalne klient** | Regulaarne ostja | Lojaalsusprogramm |
| **Uus klient** | Hiljuti ostnud, aga harva | Onboarding, soovitused |
| **Ohu all** | Varem ostis sageli, nüüd mitte | Win-back kampaania |
| **Kadunud klient** | Pole ammu ostnud | Reaktiveerimine |

---

## Grupitöö (N7 GT) — Terviklik RFM Jupyter Notebook

**Väljund:** Üks Jupyter Notebook, kus iga roll täidab ühe etapi — notebook jookseb algusest lõpuni ilma veata.

| Roll | Ülesanne | Väljund |
|---|---|---|
| **Roll A** | Andmete laadimine + merge | `df` (sales + customers liidatud) |
| **Roll B** | Andmete puhastamine | Duplikaadid, NULL-id, kuupäevade parsimine |
| **Roll C** | RFM arvutamine + segmendid | `rfm` DataFrame skooride ja segmentidega |
| **Roll D** | Visualiseerimine + kokkuvõte | 2+ Plotly diagrammi, kirjalik soovitus Markole |

**Edasijõudnute tase (vabatahtlik):**
- Kaalutud skoorid: Monetary 2× kaal
- 6–8 täpsemat segmenti
- Eksport: salvesta segmendid CSV-sse e-posti kampaaniateks

---

## Lugemismaterjal

- McKinney *Python for Data Analysis* — pandas põhifunktsioonid
- Plotly Express dokumentatsioon
- DACA Kursus 7: Python andmeanalüüs (Jupyter Notebook, pandas, Plotly)

---

*DACA26 · Nädal 7 · UrbanStyle.ltd andmeanalüüs*
