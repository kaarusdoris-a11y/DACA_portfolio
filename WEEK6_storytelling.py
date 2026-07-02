"""
Nädal 6 — Andmelood (Data Storytelling)
UrbanStyle Tartu Kaupluse Lugu
Roll B: Doris Kaarus

Fookus: ülikoolikaupluse hooajalisus — risk ja võimalused.
Meetod: annotatsioonid + "Ja mis siis?" andmelugu + juhtide kokkuvõte.

Käivitamine: Google Colab (Supabase võtmed Secrets-is)
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from supabase import create_client
from google.colab import userdata

# ─── Konfiguratsioon ──────────────────────────────────────────────────────────

URBANSTYLE_COLORS = {
    "teal":       "#009B8D",
    "green":      "#59A472",
    "light_teal": "#A6E3DD",
    "gray":       "#8A8A8A",
    "dark_gray":  "#464646",
}

TODAY = pd.to_datetime("2025-02-28")

# ─── Supabase ühendus ─────────────────────────────────────────────────────────

SUPABASE_URL = userdata.get("SUPABASE_URL")
SUPABASE_KEY = userdata.get("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


def fetch_all(table: str, filters: dict = None) -> pd.DataFrame:
    """Laeb kõik read Supabase tabelist (paginatsiooniga)."""
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

print("Laen Tartu müügiandmeid...")
df = fetch_all("sales", {"store_location": "Tartu"})
df["sale_date"] = pd.to_datetime(df["sale_date"])
df = df[df["sale_date"] <= TODAY].copy()
df["month"]     = df["sale_date"].dt.to_period("M").astype(str)
df["month_num"] = df["sale_date"].dt.month
print(f"✅ Tartu müügikirjeid: {len(df)}")

# ─── 1. Annoteeritud joongraafik — hooajalisus ────────────────────────────────

df_monthly = df.groupby("month")["total_price"].sum().reset_index()
df_monthly.columns = ["Kuu", "Käive"]
keskväärtus = df_monthly["Käive"].mean()

tipp   = df_monthly.loc[df_monthly["Käive"].idxmax()]
madal  = df_monthly.loc[df_monthly["Käive"].idxmin()]

fig1 = px.line(
    df_monthly, x="Kuu", y="Käive",
    title=(
        "UrbanStyle Tartu — kuine käive 2024<br>"
        "<sub>Ülikoolikaupluse hooajalisus: tipp septembris, langus suvel</sub>"
    ),
    color_discrete_sequence=[URBANSTYLE_COLORS["teal"]],
)

# Viitejoon — kuu keskmine
fig1.add_hline(
    y=keskväärtus,
    line_dash="dot",
    line_color=URBANSTYLE_COLORS["gray"],
    annotation_text=f"Kuu keskmine: €{keskväärtus:,.0f}",
    annotation_position="top right",
)

# Tipp (september — sügissemestri algus)
fig1.add_annotation(
    x=tipp["Kuu"], y=tipp["Käive"],
    text=f"↑ Sügissemester algab<br>Üliõpilased tulevad linna<br><b>€{tipp['Käive']:,.0f}</b>",
    showarrow=True, arrowhead=2, ax=0, ay=-50,
    arrowcolor=URBANSTYLE_COLORS["teal"],
    bgcolor="white", bordercolor=URBANSTYLE_COLORS["teal"],
    font=dict(size=11),
)

# Madal (suvi — üliõpilased lahkuvad)
fig1.add_annotation(
    x=madal["Kuu"], y=madal["Käive"],
    text=f"↓ Suvepuhkus<br>Üliõpilased lahkuvad<br><b>€{madal['Käive']:,.0f}</b>",
    showarrow=True, arrowhead=2, ax=0, ay=50,
    arrowcolor=URBANSTYLE_COLORS["gray"],
    bgcolor="white", bordercolor=URBANSTYLE_COLORS["gray"],
    font=dict(size=11),
)

fig1.update_layout(
    xaxis_title="Kuu",
    yaxis_title="Käive (EUR)",
    plot_bgcolor="white",
    paper_bgcolor="white",
    font=dict(family="Arial", size=12, color=URBANSTYLE_COLORS["dark_gray"]),
)
fig1.show()

# ─── 2. Hooajalisuse tulpdiagramm ─────────────────────────────────────────────

KUUNIMED = {
    1: "Jaan", 2: "Veeb", 3: "Mar", 4: "Apr",
    5: "Mai",  6: "Jun",  7: "Jul", 8: "Aug",
    9: "Sep", 10: "Okt", 11: "Nov", 12: "Det",
}

df_season = df.groupby("month_num")["total_price"].mean().reset_index()
df_season["Kuu nimi"] = df_season["month_num"].map(KUUNIMED)
df_season.columns = ["Kuu nr", "Kesk. käive", "Kuu"]

fig2 = px.bar(
    df_season, x="Kuu", y="Kesk. käive",
    title=(
        "Hooajalisuse muster — ülikoolikalender mõjutab ostukäitumist<br>"
        "<sub>Semestri algused (september, jaanuar) toovad müügitõusu</sub>"
    ),
    color="Kesk. käive",
    color_continuous_scale=[
        [0, URBANSTYLE_COLORS["light_teal"]],
        [1, URBANSTYLE_COLORS["teal"]],
    ],
)

# Annotatsioon — semestri algused
fig2.add_vrect(
    x0=7.5, x1=9.5,
    fillcolor=URBANSTYLE_COLORS["teal"], opacity=0.08, line_width=0,
    annotation_text="Sügissemester", annotation_position="top",
)
fig2.add_vrect(
    x0=-0.5, x1=1.5,
    fillcolor=URBANSTYLE_COLORS["green"], opacity=0.08, line_width=0,
    annotation_text="Kevadsemester", annotation_position="top",
)

fig2.update_layout(
    xaxis_title="Kuu",
    yaxis_title="Keskmine käive (EUR)",
    plot_bgcolor="white",
    paper_bgcolor="white",
    coloraxis_showscale=False,
    font=dict(family="Arial", size=12, color=URBANSTYLE_COLORS["dark_gray"]),
)
fig2.show()

# ─── 3. Andmelugu — "Ja mis siis?" meetod ─────────────────────────────────────

aastakäive     = df["total_price"].sum()
kesk_tellimus  = df["total_price"].mean()
kliendid       = df["customer_id"].nunique()
hooaja_delta   = (tipp["Käive"] - madal["Käive"]) / madal["Käive"] * 100

print("\n" + "=" * 60)
print("📖 TARTU KAUPLUSE ANDMELUGU (Roll B)")
print("=" * 60)

print(f"""
━━━ Andmepunkt 1 ━━━
Fakti: Tartu kaupluse aastakäive on €{aastakäive:,.0f}
→ Ja mis siis?  Tipp- ja madalkuu vahel on {hooaja_delta:.0f}% erinevus.
→ Ja mis siis?  Hooajalisus järgib ülikoolikalendrit, mitte rõivasasooni.
→ Tegevus:      Planeerida kampaaniad semestri algustele
                (september + jaanuar) — mitte jõuludele.

━━━ Andmepunkt 2 ━━━
Fakti: Kesk. tellimus €{kesk_tellimus:.0f} vs Tallinna €42 (≈50% vahe)
→ Ja mis siis?  Üliõpilased on hinnatundlikumad ostjad.
→ Ja mis siis?  Odavamate toodete osakaal on suurem; premium müüb halvasti.
→ Tegevus:      Katsetada üliõpilashinnangut / ISIC lojaalsusprogrammi;
                premium sortimendi laieni pigem e-poodi.

━━━ Andmepunkt 3 ━━━
Fakti: {kliendid} unikaalset klienti, kuid paljud ei tule tagasi suvel
→ Ja mis siis?  Üliõpilased lahkuvad linna — kliendisuhe katkeb.
→ Ja mis siis?  E-pood võimaldab suhtlust ka väljaspool linnakauplust.
→ Tegevus:      Suunata suvekuu kliendid e-poodi (push-teated, soodusmeilid).
""")

# ─── 4. Juhtide kokkuvõte (CEO Kristi jaoks) ─────────────────────────────────

aasta = df["sale_date"].dt.year.max()

print("=" * 60)
print("📊 JUHTIDE KOKKUVÕTE — CEO Kristi jaoks (3 lauset)")
print("=" * 60)
print(f"""
UrbanStyle Tartu kaupluse {aasta}. aasta käive on €{aastakäive:,.0f},
mida iseloomustab tugev hooajalisus: tipp septembris (+{hooaja_delta:.0f}% võrreldes
madalaimaga) peegeldab ülikoolikalendrit. Peamine risk on suvine käibelangus,
peamine võimalus — ISIC koostöö ja e-poe aktiveerimine semestriväliseks ajaks.
""")
