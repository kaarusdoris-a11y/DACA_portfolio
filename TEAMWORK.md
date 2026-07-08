# Meeskonnatöö — Sales-Analytics (UrbanStyle.ltd)

Täielik repo: [github.com/kaarusdoris-a11y/Sales-Analytics](https://github.com/kaarusdoris-a11y/Sales-Analytics)

See leht on kokkuvõte minu panusest meeskonnaprojekti, kuna see panus on dokumenteeritud ühises repos, mitte minu isiklikus kasutajanimes.

## Meeskond

5-liikmeline andmemeeskond, mis analüüsib UrbanStyle.ltd müügiandmeid IT-direktor Toomas Kase jaoks. Koosseis muutus programmi käigus:

| Nimi | OS | Osales |
|---|---|---|
| Doris Kaarus | Mac | Nädal 0–9 |
| Tekla Relika Ani | Win | Nädal 0–9 |
| Ahto Sooaru | Win | Nädal 0–9 |
| Henri Greenbaum | Mac | Nädal 0–6 (lahkus pärast nädalat 6) |
| Kaarin Peet | Win | Nädal 0–1 (lahkus pärast nädalat 1) |

**Eesmärk:** täpsustada ja lihtsustada müügiandmeid ning jagada neid arusaadavalt teistele.

## Minu roll nädalate kaupa

Minu tegelik ülesanne muutus igal nädalal vastavalt sellele nädalale planeeritud analüüsile — allolev tabel kajastab tegelikku tööd (mitte ainult üldist A–E rollirotatsiooni), nagu see on dokumenteeritud nädala materjalides.

| Nädal | Minu tegelik roll/ülesanne | Allikas |
|---|---|---|
| 0 | GitHub repo seadistamine | Team Charter |
| 1 | Tooteandmete uurija — `products` tabeli analüüs (362 rida, `eco_certified` veerus 18 null väärtust) | Data_Landscape_Week1.pdf, [README.md](week-1-sql-basics/README.md) |
| 2 | *(kinnitamisel)* | — |
| 3 | *(kinnitamisel)* | — |
| 4 | Kliendigruppide analüüs — VIP (678 klienti), Regular (266) ja Uus-segment (63) | Data_Landscape_Week4.pdf |
| 5 | *(kinnitamisel)* | — |
| 6 | *(kinnitamisel)* | — |
| 7 | RFM arvutus ja segmenteerimine (koos Ahtoga) | N7_RFM_Analyys.ipynb |
| 8 | Pipeline valideerimine (Monitor & Valideerimisraport) + visualiseerimine | N8_Pipeline.ipynb |
| 9 | Portfoolio struktuur/dokumentatsioon | Team Charter, N9_Peer_Review.md |

## Minu konkreetne panus

Nädal 1 andmemaastiku ülevaates on minu leid otse minu nimega atribueeritud:

> `products`: Doris Kaarus — 362 rida, 9 veergu, `eco_certified` veerus 18 null väärtust

See leid viis otse üle nädal 2 SQL-puhastuse teemasse ja on ka lahti kirjutatud minu individuaalses [`README.md`](./week-1-sql-basics/README.md)-s koos ärliku mõju ja soovitusega.

## Iganädalane äriline kommunikatsioon

Meeskond koostab iga nädal kliendile ("Ühine Väljund") kokkuvõtte, mis järgib läbivalt sama struktuuri:

**Suurim üllatus → Soovitus Toomasele → Puuduvad andmed**

See on äriliku kommunikatsiooni muster (probleem → järeldus → tegevussoovitus juhile), mitte tehniline logi.

## Kokkuvõte

- Formaalne, dokumenteeritud liige meeskonnas kogu programmi vältel (nädal 0–9), mille koosseis muutus teel (Kaarin nädal 0–1, Henri nädal 0–6)
- Individuaalne, arvuliselt täpne ja kontrollitav panus igal nädalal, kus roll on dokumenteeritud (`eco_certified` leid, kliendisegmentide analüüs, RFM, pipeline valideerimine)
- Osalenud meeskonna töökorralduse kokkuleppimises (Team Charter) juba enne tehnilise töö algust

---

## 🇬🇧 In English

Full repo: [github.com/kaarusdoris-a11y/Sales-Analytics](https://github.com/kaarusdoris-a11y/Sales-Analytics)

This page summarises my contribution to the team project, since that work is documented in the shared repo rather than under my personal username.

### Team

A 5-person data team analysing UrbanStyle.ltd sales data for IT Director Toomas Kask. The team's composition changed over the programme:

| Name | OS | Participated |
|---|---|---|
| Doris Kaarus | Mac | Weeks 0–9 |
| Tekla Relika Ani | Win | Weeks 0–9 |
| Ahto Sooaru | Win | Weeks 0–9 |
| Henri Greenbaum | Mac | Weeks 0–6 (left after week 6) |
| Kaarin Peet | Win | Weeks 0–1 (left after week 1) |

### My role, week by week

My actual task changed each week depending on that week's assignment — the table below reflects the real work (not just the general A–E rotation) as documented in each week's materials.

| Week | My actual role/task | Source |
|---|---|---|
| 0 | GitHub repo setup | Team Charter |
| 1 | Product Data Explorer — analysed the `products` table (362 rows, 18 nulls in `eco_certified`) | Data_Landscape_Week1.pdf, [README.md](week-1-sql-basics/README.md) |
| 2 | *(to confirm)* | — |
| 3 | *(to confirm)* | — |
| 4 | Customer segmentation analysis — VIP (678 customers), Regular (266), New segment (63) | Data_Landscape_Week4.pdf |
| 5 | *(to confirm)* | — |
| 6 | *(to confirm)* | — |
| 7 | RFM calculation and segmentation (with Ahto) | N7_RFM_Analyys.ipynb |
| 8 | Pipeline validation (Monitor & Validation Report) + visualisations | N8_Pipeline.ipynb |
| 9 | Portfolio structure/documentation | Team Charter, N9_Peer_Review.md |

### My specific contribution

In the Week 1 data landscape overview, my finding is directly attributed to my name: `products`: Doris Kaarus — 362 rows, 9 columns, 18 null values in the `eco_certified` column. This finding fed directly into the Week 2 SQL cleaning work and is written up in my individual [`README.md`](./week-1-sql-basics/README.md) with business impact and a recommendation.

### Weekly business communication

Each week the team produces a client-facing summary ("Ühine Väljund") that consistently follows the same structure: **Biggest surprise → Recommendation to Toomas → Missing data**.

### Summary

- Formal, documented member of the team for the entire programme (weeks 0–9), through team composition changes (Kaarin weeks 0–1, Henri weeks 0–6)
- Individual, numerically precise and verifiable contribution in every week where the role is documented (`eco_certified` finding, customer segmentation, RFM, pipeline validation)
- Participated in agreeing team working arrangements (Team Charter) before technical work even began
