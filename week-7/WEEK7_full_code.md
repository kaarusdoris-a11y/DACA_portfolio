# Nädal 7 — Kogu Kood (Individuaalne + Meeskond)

## 1. Individuaalne kood — DACA (`WEEK7_rfm_analyys.ipynb`)

```python
# UrbanStyle RFM Analüüs — Nädal 7

from supabase import create_client
from dotenv import load_dotenv
import os
import pandas as pd
import plotly.express as px

load_dotenv(override=True)
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
print("Ühendus loodud!")
```

```python
# Roll A — Andmete laadimine

def fetch_all(table_name):
    all_data = []
    page = 0
    page_size = 1000
    while True:
        response = supabase.table(table_name).select('*').range(page * page_size, (page + 1) * page_size - 1).execute()
        all_data.extend(response.data)
        if len(response.data) < page_size:
            break
        page += 1
    return pd.DataFrame(all_data)

df_sales = fetch_all('sales')
df_customers = fetch_all('customers')

print(f"Müügiridu: {df_sales.shape[0]}")
print(f"Kliente: {df_customers.shape[0]}")
```

```python
# Roll B — Andmete puhastamine

df_sales['customer_id'] = df_sales['customer_id'].astype('Int64')
df_customers['customer_id'] = df_customers['customer_id'].astype('Int64')

df = pd.merge(df_sales, df_customers, on='customer_id', how='left')
print(f"Enne puhastamist: {df.shape[0]} rida")

print(f"Duplikaate: {df.duplicated().sum()}")
df = df.drop_duplicates()

df = df.dropna(subset=['customer_id', 'sale_date', 'total_price'])
df['sale_date'] = pd.to_datetime(df['sale_date'])
df = df[df['total_price'] > 0]

print(f"Pärast puhastamist: {df.shape[0]} rida")
print(f"Kuupäevavahemik: {df['sale_date'].min()} kuni {df['sale_date'].max()}")
print(f"Unikaalseid kliente: {df['customer_id'].nunique()}")
```

```python
# Roll C — RFM arvutamine

today = pd.to_datetime('2026-06-22')

recency = df.groupby('customer_id')['sale_date'].max().reset_index()
recency.columns = ['customer_id', 'last_purchase']
recency['recency_days'] = (today - recency['last_purchase']).dt.days

frequency = df.groupby('customer_id').size().reset_index(name='frequency')

monetary = df.groupby('customer_id')['total_price'].sum().reset_index()
monetary.columns = ['customer_id', 'monetary']

rfm = recency[['customer_id', 'recency_days']].merge(
    frequency, on='customer_id'
).merge(
    monetary, on='customer_id'
)

print(f"RFM tabel: {rfm.shape[0]} klienti")
print(rfm.sort_values('monetary', ascending=False).head(10))
```

```python
# Roll D — RFM skoorid ja segmendid

rfm['R_score'] = pd.qcut(rfm['recency_days'], q=3, labels=[3, 2, 1]).astype(int)
rfm['F_score'] = pd.qcut(rfm['frequency'].rank(method='first'), q=3, labels=[1, 2, 3]).astype(int)
rfm['M_score'] = pd.qcut(rfm['monetary'], q=3, labels=[1, 2, 3]).astype(int)
rfm['RFM_score'] = rfm['R_score'] + rfm['F_score'] + rfm['M_score']

def assign_segment(score):
    if score >= 8:
        return 'VIP Champions'
    elif score >= 6:
        return 'Loyal Customers'
    elif score >= 4:
        return 'Potential Loyalists'
    else:
        return 'At Risk'

rfm['segment'] = rfm['RFM_score'].apply(assign_segment)

print("Segmentide jaotus:")
print(rfm['segment'].value_counts())
print(f"\nKeskmine monetary VIP: {rfm[rfm['segment']=='VIP Champions']['monetary'].mean():.2f} EUR")
```

*(Visualiseerimislahtri (Roll D) täpne lähtekood ei olnud selle koopia GitHub-i JSON-ist taastatav suure manustatud diagrammi väljundi tõttu — vt allpool täielikku meeskonna versiooni, kus see kood on täies mahus olemas.)*

## 2. Meeskonna kood — Sales-Analytics, Roll C: RFM Arvutus ja Segmenteerimine (koos Ahtoga)

Minu roll nädal 7 meeskonnaprojektis oli Roll C — RFM arvutus ja segmenteerimine (koos Ahtoga). Täielik meeskonnamärkmik: [N7_RFM_Analyys.ipynb](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/main/N7_RFM_Analyys.ipynb).

```python
# Recency: päevade arv tänasest viimase ostuni
recency_df = df.groupby('customer_id')['sale_date'].max().reset_index()
recency_df.columns = ['customer_id', 'last_purchase_date']
recency_df['recency'] = (TODAY - recency_df['last_purchase_date']).dt.days

# Frequency: ostude arv
frequency_df = df.groupby('customer_id')['sale_id'].count().reset_index()
frequency_df.columns = ['customer_id', 'frequency']

# Monetary: kogukulutus
monetary_df = df.groupby('customer_id')['total_price'].sum().reset_index()
monetary_df.columns = ['customer_id', 'monetary']

print("R, F, M arvutatud ✅")
print(recency_df.head(3))
```

```python
# Liida R, F, M üheks tabeliks
rfm = recency_df.merge(frequency_df, on='customer_id').merge(monetary_df, on='customer_id')

# Skoorid 1–5 (Recency: VASTUPIDINE — madal recency = kõrge skoor)
rfm['R_score'] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1]).astype(int)
rfm['F_score'] = pd.qcut(rfm['frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5]).astype(int)
rfm['M_score'] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5]).astype(int)

# Koguskoor
rfm['RFM_Score'] = rfm['R_score'] + rfm['F_score'] + rfm['M_score']

print(f"R skoorid: {sorted(rfm['R_score'].unique())}")
print(f"F skoorid: {sorted(rfm['F_score'].unique())}")
print(f"M skoorid: {sorted(rfm['M_score'].unique())}")
```

```python
def määra_segment(skoor):
    if skoor >= 13:
        return 'VIP Champions'
    elif skoor >= 10:
        return 'Loyal'
    elif skoor >= 7:
        return 'Potential'
    elif skoor >= 4:
        return 'At Risk'
    else:
        return 'Lost'

rfm['Segment'] = rfm['RFM_Score'].apply(määra_segment)

print("\n" + "=" * 40)
print("     SEGMENTIDE KOKKUVÕTE")
print("=" * 40)
print(rfm['Segment'].value_counts())
print("\nProtsentuaalne jaotus:")
print((rfm['Segment'].value_counts(normalize=True) * 100).round(1).astype(str) + '%')
```

```python
# Ärilised võtmenäitajad
vip_arv = (rfm['Segment'] == 'VIP Champions').sum()
vip_kaive = rfm[rfm['Segment'] == 'VIP Champions']['monetary'].sum()
kogu_kaive = rfm['monetary'].sum()
vip_osakaal = vip_kaive / kogu_kaive * 100

at_risk_arv = (rfm['Segment'] == 'At Risk').sum()
at_risk_kaive = rfm[rfm['Segment'] == 'At Risk']['monetary'].sum()

print(f"VIP klientide arv:     {vip_arv}  ({vip_osakaal:.1f}% käibest)")
print(f"VIP klientide käive:   {vip_kaive:,.2f}€")
print(f"At-Risk klientide arv: {at_risk_arv}")
print(f"At-Risk käive:         {at_risk_kaive:,.2f}€")
```

**Ärikokkuvõte:** VIP Champions genereerivad suurima osa käibest ja soovitasime lojaalsusprogrammi; At-Risk kliendid vajavad win-back kampaaniat. Täielik ärikokkuvõte Markole on N7_RFM_Analyys.ipynb-s (Roll D, Ahto).

---
*DACA26 · Nädal 7 · UrbanStyle.ltd andmeanalüüs*
