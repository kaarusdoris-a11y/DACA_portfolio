"""
Nädal 5 — Visualiseerimise Disain
UrbanStyle Tartu Kaupluse Dashboard
Roll B: Doris Kaarus

Streamlit + Plotly dashboard Tartu kaupluse müügiandmete visualiseerimiseks.
Andmed tulevad Supabase andmebaasist (st.secrets kaudu).

Käivitamine:
    streamlit run WEEK5_dashboard.py
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from supabase import create_client

# ─── Konfiguratsioon ──────────────────────────────────────────────────────────

URBANSTYLE_COLORS = {
    "teal":       "#009B8D",
    "green":      "#59A472",
    "light_teal": "#A6E3DD",
    "gray":       "#8A8A8A",
    "dark_gray":  "#464646",
}

KUUNIMED = {
    1: "Jaan", 2: "Veeb", 3: "Mar", 4: "Apr",
    5: "Mai",  6: "Jun",  7: "Jul", 8: "Aug",
    9: "Sep", 10: "Okt", 11: "Nov", 12: "Det",
}

# ─── Supabase ühendus ─────────────────────────────────────────────────────────

@st.cache_resource
def get_supabase():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)


@st.cache_data(ttl=3600)
def fetch_all(table: str, filters: dict = None) -> pd.DataFrame:
    """Laeb kõik read Supabase tabelist (paginatsiooniga)."""
    supabase = get_supabase()
    all_rows, offset, limit = [], 0, 1000
    while True:
        q = supabase.table(table).select("*").range(offset, offset + limit - 1)
        if filters:
            for col, val in filters.items():
                q = q.eq(col, val)
        rows = q.execute().data
        if not rows:
            break
        all_rows.extend(rows)
        if len(rows) < limit:
            break
        offset += limit
    return pd.DataFrame(all_rows)


# ─── Andmete ettevalmistus ────────────────────────────────────────────────────

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["sale_date"] = pd.to_datetime(df["sale_date"])
    df["month"]     = df["sale_date"].dt.to_period("M").astype(str)
    df["month_num"] = df["sale_date"].dt.month
    df["year"]      = df["sale_date"].dt.year
    return df

# ─── Dashboard ────────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="UrbanStyle Tartu",
    page_icon="🛍️",
    layout="wide",
)

st.title("🛍️ UrbanStyle — Tartu Kaupluse Dashboard")
st.markdown("**Roll B · Ülikoolikaupluse hooajalisus** · DACA Nädal 5")
st.divider()

# Lae andmed
with st.spinner("Laen andmeid Supabase'ist..."):
    df_raw   = fetch_all("sales", {"store_location": "Tartu"})
    df_tartu = prepare_data(df_raw)

# ─── KPI-d ───────────────────────────────────────────────────────────────────

st.subheader("Põhimõõdikud")
k1, k2, k3, k4 = st.columns(4)
k1.metric("Kokku käive",        f"€{df_tartu['total_price'].sum():,.0f}")
k2.metric("Tellimuste arv",     f"{len(df_tartu):,}")
k3.metric("Kesk. tellimus",     f"€{df_tartu['total_price'].mean():.0f}")
k4.metric("Unikaalseid kliente", f"{df_tartu['customer_id'].nunique():,}")

st.divider()

# ─── Filtrid ──────────────────────────────────────────────────────────────────

aastad = sorted(df_tartu["year"].unique().tolist())
valitud_aasta = st.selectbox("Vali aasta", ["Kõik"] + [str(a) for a in aastad])
df_f = df_tartu[df_tartu["year"] == int(valitud_aasta)] if valitud_aasta != "Kõik" else df_tartu

# ─── Graafikud ────────────────────────────────────────────────────────────────

col_a, col_b = st.columns(2)

# Kuine käive — joongraafik
with col_a:
    df_monthly = df_f.groupby("month")["total_price"].sum().reset_index()
    df_monthly.columns = ["Kuu", "Käive (EUR)"]
    fig_line = px.line(
        df_monthly, x="Kuu", y="Käive (EUR)",
        title="Kuine käive — Tartu kauplus",
        color_discrete_sequence=[URBANSTYLE_COLORS["teal"]],
    )
    fig_line.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_line, use_container_width=True)

# Hooajalisus — tulpdiagramm (kuu keskmised kõigi aastate põhjal)
with col_b:
    df_season = df_tartu.groupby("month_num")["total_price"].mean().reset_index()
    df_season["Kuu"] = df_season["month_num"].map(KUUNIMED)
    df_season.columns = ["month_num", "Kesk. käive (EUR)", "Kuu"]
    fig_bar = px.bar(
        df_season, x="Kuu", y="Kesk. käive (EUR)",
        title="Hooajalisus — keskmine kuukäive",
        color="Kesk. käive (EUR)",
        color_continuous_scale=[
            [0, URBANSTYLE_COLORS["light_teal"]],
            [1, URBANSTYLE_COLORS["teal"]],
        ],
    )
    fig_bar.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        coloraxis_showscale=False,
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# ─── Tooted ───────────────────────────────────────────────────────────────────

st.subheader("Top 10 tooted käibe järgi")
if "product_id" in df_f.columns:
    df_prod = (
        df_f.groupby("product_id")["total_price"]
        .sum()
        .reset_index()
        .sort_values("total_price", ascending=False)
        .head(10)
    )
    df_prod.columns = ["Toode", "Käive (EUR)"]
    fig_prod = px.bar(
        df_prod, x="Toode", y="Käive (EUR)",
        color_discrete_sequence=[URBANSTYLE_COLORS["green"]],
    )
    fig_prod.update_layout(plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig_prod, use_container_width=True)

st.caption("DACA 2025 · UrbanStyle Tartu · Doris Kaarus")
