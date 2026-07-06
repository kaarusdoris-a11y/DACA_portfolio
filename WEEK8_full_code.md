# Nädal 8 — Kogu Kood (Individuaalne + Meeskond)

## 1. Individuaalne kood — DACA (`WEEK8_pipeline.ipynb`)

```python
# UrbanStyle RFM Pipeline — Nädal 8

from supabase import create_client
from dotenv import load_dotenv
import os
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

load_dotenv(override=True)
supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
print("Ühendus loodud!")
logger.info("Ühendus loodud!")
```

```python
# Extract — Andmete toomine

def extract():
    logger.info("EXTRACT: Alustan...")

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

    orders = fetch_all('sales')
    customers = fetch_all('customers')

    print(f"[EXTRACT] {len(orders)} müügirida, {len(customers)} klienti")
    return orders, customers

orders, customers = extract()
```

```python
# Transform — Andmete töötlemine

def transform(orders, customers):
    logger.info("TRANSFORM: Alustan...")

    orders['customer_id'] = orders['customer_id'].astype('Int64')
    customers['customer_id'] = customers['customer_id'].astype('Int64')

    df = pd.merge(orders, customers, on='customer_id', how='left')

    df = df.drop_duplicates()
    df = df.dropna(subset=['customer_id', 'sale_date', 'total_price'])
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    df = df[df['total_price'] > 0]

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

    print(f"[TRANSFORM] {len(rfm)} klienti segmenteeritud")
    print(rfm['segment'].value_counts())
    return rfm

rfm = transform(orders, customers)
```

*(Load-lahtri (viimane lahter) täpne lähtekood ei olnud selle koopia GitHub-i JSON-ist taastatav suure manustatud diagrammi väljundi tõttu — vt allpool täielikku meeskonna versiooni.)*

## 2. Meeskonna kood — Sales-Analytics, Roll D + Roll E (mõlemad minu vastutusel)

Meeskonnaprojektis oli minu vastutusel nädal 8 kaks rolli: **Roll D — Monitor & Valideerimisraport** ja **Roll E — Visualiseerimine**. Täielik meeskonnamärkmik: [N8_Pipeline.ipynb](https://github.com/kaarusdoris-a11y/Sales-Analytics/blob/main/N8_Pipeline.ipynb).

### Roll D — Monitor & Valideerimisraport

```python
print("=" * 60)
print("VALIDEERIMISRAPORT — UrbanStyle Pipeline")
print("=" * 60)

leiud = []

def ok(tekst):
    print(f"  ✅ OK     {tekst}")
    leiud.append(('OK', tekst))

def paranda(tekst):
    print(f"  ⚠️  PARANDA {tekst}")
    leiud.append(('PARANDA', tekst))

sales = result['sales_clean']
weekly = result['weekly']

# Roll A kontroll
print("\n📦 Roll A — Andmete laadimine")
assert not sales.empty, "sales_clean on tühi!"
ok(f"sales_clean: {len(sales)} rida laaditud")
ok("Kirjete arv mõistlik (>1000)") if len(sales) > 1000 else paranda(f"Väike kirjete arv: {len(sales)}")

# Roll B kontroll
print("\n🧹 Roll B — Andmete puhastamine")
kriitilised = ['customer_id', 'total_price', 'sale_date']
for veerg in kriitilised:
    if veerg in sales.columns:
        n = sales[veerg].isnull().sum()
        ok(f"{veerg}: pole NULL väärtusi") if n == 0 else paranda(f"{veerg}: {n} NULL väärtust")

neg = (sales['total_price'] < 0).sum()
ok("Negatiivseid hindu pole") if neg == 0 else ok(f"{neg} negatiivset hinda — võivad olla tagastused")

dupl = sales.duplicated(subset=['invoice_id']).sum() if 'invoice_id' in sales.columns else 0
ok("Duplikaate pole (invoice_id alusel)") if dupl == 0 else paranda(f"{dupl} duplikaati")

# Ristkontroll
print("\n🔁 Ristkontroll")
kogutulu_w = weekly['revenue'].sum()
kogutulu_s = sales['total_price'].sum()
erinevus = abs(kogutulu_w - kogutulu_s) / kogutulu_s * 100
ok(f"Kogutulu klapib: €{kogutulu_s:,.0f} (erinevus {erinevus:.2f}%)") if erinevus < 1 else paranda(f"Tulu erinevus: {erinevus:.1f}%")

print("\n" + "=" * 60)
print("KOKKUVÕTE")
ok_arv = sum(1 for l in leiud if l[0] == 'OK')
p_arv = sum(1 for l in leiud if l[0] == 'PARANDA')
print(f"  ✅ OK: {ok_arv}   ⚠️  PARANDA: {p_arv}")
```

### Roll E — Visualiseerimine

```python
import plotly.express as px
import plotly.graph_objects as go
import os
from datetime import datetime

US_COLORS = {
    'teal':       '#00A896',
    'white':      '#FFFFFF',
    'light_gray': '#D4D4D4',
    'dark_gray':  '#4A4A4A',
    'black':      '#1A1A1A',
}

LAYOUT_BASE = dict(
    template='plotly_white',
    paper_bgcolor=US_COLORS['white'],
    plot_bgcolor=US_COLORS['white'],
    font_color=US_COLORS['dark_gray'],
    title_font_color=US_COLORS['black'],
    title_font_size=18,
)
```

```python
# Diagramm 1 — Nädalane tululiikumine
fig_weekly = px.line(
    result['weekly'],
    x='sale_date', y='revenue',
    title='UrbanStyle — Nädalane tulu 2023–2026',
    labels={'sale_date': 'Nädal', 'revenue': 'Tulu (€)'}
)
fig_weekly.update_traces(
    line_color=US_COLORS['teal'], line_width=2.5,
    fill='tozeroy', fillcolor='rgba(0,168,150,0.1)'
)
fig_weekly.update_layout(**LAYOUT_BASE)
fig_weekly.show()
```

```python
# Diagramm 2 — KPI kaardid
df_s = result['sales_clean']
kpis = [
    ("Kogutulu",          df_s['total_price'].sum(),     "€ "),
    ("Unikaalseid kliente", df_s['customer_id'].nunique(), "" ),
    ("Tellimusi kokku",   len(df_s),                    "" ),
    ("Keskmine tellimus", df_s['total_price'].mean(),    "€ "),
]

fig_kpi = go.Figure()
for i, (title, value, prefix) in enumerate(kpis):
    fig_kpi.add_trace(go.Indicator(
        mode="number",
        value=value,
        title={"text": f"<b>{title}</b>", "font": {"color": US_COLORS['dark_gray']}},
        number={"prefix": prefix, "valueformat": ",.0f",
                "font": {"color": US_COLORS['teal'], "size": 36}},
        domain={"row": 0, "column": i}
    ))
fig_kpi.update_layout(
    grid={"rows": 1, "columns": 4},
    title=dict(text="UrbanStyle KPI kokkuvõte", font=dict(size=18)),
    height=200,
    **LAYOUT_BASE
)
fig_kpi.show()
```

```python
# Eksport: CSV + HTML diagrammid output/ kausta
os.makedirs('output', exist_ok=True)
date_str = datetime.now().strftime('%Y%m%d')

df_s.to_csv(f'output/urbanstyle_sales_{date_str}.csv', index=False)
print(f"✅ CSV: output/urbanstyle_sales_{date_str}.csv")

fig_weekly.write_html(f'output/weekly_revenue_{date_str}.html')
fig_kpi.write_html(f'output/kpi_summary_{date_str}.html')
print(f"✅ HTML: output/weekly_revenue_{date_str}.html")
print(f"✅ HTML: output/kpi_summary_{date_str}.html")
```

---
*DACA26 · Nädal 8 · UrbanStyle.ltd andmeanalüüs*
