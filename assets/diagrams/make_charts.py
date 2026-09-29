import os
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch
import matplotlib.dates as mdates
import datetime as dt

plt.rcParams.update({
    "font.size": 10,
    "font.family": "DejaVu Sans",
    "axes.edgecolor": "#444444",
    "axes.labelcolor": "#222222",
    "text.color": "#222222",
    "xtick.color": "#444444",
    "ytick.color": "#444444",
})

BLUE = "#2b6ca3"
ORANGE = "#d97b29"
GREEN = "#3a8a5e"
RED = "#c14444"
GREY = "#888888"

# ---------------------------------------------------------------
# 1. Project environment diagram (internal/external x technical/social)
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(9, 6.5))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

ax.axvline(5, color="#999999", lw=1.2, ymin=0.03, ymax=0.97)
ax.axhline(5, color="#999999", lw=1.2, xmin=0.03, xmax=0.97)

ax.text(2.5, 9.6, "TECHNISCH", ha="center", fontsize=11, fontweight="bold", color=GREY)
ax.text(7.5, 9.6, "SOZIAL / ORGANISATORISCH", ha="center", fontsize=11, fontweight="bold", color=GREY)
ax.text(0.3, 7.5, "INTERN", va="center", rotation=90, fontsize=11, fontweight="bold", color=GREY)
ax.text(0.3, 2.5, "EXTERN", va="center", rotation=90, fontsize=11, fontweight="bold", color=GREY)

# project box in the center
center = mpatches.FancyBboxPatch((3.9, 4.5), 2.2, 1.0, boxstyle="round,pad=0.05",
                                  facecolor=BLUE, edgecolor="none")
ax.add_patch(center)
ax.text(5, 5, "Projekt\nUW Mitte", ha="center", va="center", color="white", fontsize=10, fontweight="bold")

def box(x, y, text, color):
    b = mpatches.FancyBboxPatch((x-1.15, y-0.45), 2.3, 0.9, boxstyle="round,pad=0.04",
                                 facecolor=color, edgecolor="none", alpha=0.92)
    ax.add_patch(b)
    ax.text(x, y, text, ha="center", va="center", fontsize=8.6, color="white")

# Internal / technical (top-left quadrant)
box(2.0, 8.2, "Fachprojektleitung\nPrimärtechnik", GREEN)
box(2.0, 6.8, "Schutz- /\nLeittechnik", GREEN)

# Internal / social (top-right quadrant)
box(8.0, 8.2, "Auftraggeber\n(Budget, Entscheidungen)", GREEN)
box(8.0, 6.8, "Betrieb\n(Abschaltfenster)", GREEN)
box(8.0, 5.4, "Einkauf", GREEN)

# External / technical (bottom-left)
box(2.0, 3.2, "Auftragnehmer /\nGeneralunternehmer", ORANGE)
box(2.0, 1.8, "Hersteller\nLeistungsschalter", ORANGE)

# External / social (bottom-right)
box(8.0, 3.2, "Genehmigungsbehörden", ORANGE)
box(8.0, 1.8, "Arbeitssicherheit /\nUmweltschutz (extern geprüft)", ORANGE)

for (x, y) in [(2.0,8.2),(2.0,6.8),(8.0,8.2),(8.0,6.8),(8.0,5.4),(2.0,3.2),(2.0,1.8),(8.0,3.2),(8.0,1.8)]:
    ax.annotate("", xy=(x + (0.9 if x<5 else -0.9), y if abs(y-5)<2.4 else y+(0.3 if y>5 else -0.3)),
                xytext=(5,5), arrowprops=dict(arrowstyle="-", color="#bbbbbb", lw=0.8), zorder=0)

ax.set_title("Projektumfeld: intern/extern × technisch/sozial", fontsize=12, fontweight="bold", pad=14)
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "projektumfeld.png"), dpi=200)
plt.close(fig)

print("chart 1 done")

# ---------------------------------------------------------------
# 2. Stakeholder power/interest portfolio
# ---------------------------------------------------------------
# mapping Sehr hoch=4, Hoch=3, Mittel=2, Variabel=2.5 (drawn with marker note)
level_map = {"Sehr hoch": 4.0, "Hoch": 3.0, "Mittel": 2.0, "Variabel": 2.5}
stakeholders = [
    ("Betrieb", "Sehr hoch", "Sehr hoch"),
    ("Auftraggeber", "Hoch", "Sehr hoch"),
    ("Primärtechnik", "Sehr hoch", "Hoch"),
    ("Schutz-/Leittechnik", "Hoch", "Hoch"),
    ("Einkauf", "Mittel", "Hoch"),
    ("Arbeitssicherheit", "Hoch", "Hoch"),
    ("Umweltschutz", "Mittel", "Mittel"),
    ("Auftragnehmer", "Sehr hoch", "Hoch"),
    ("Behörden/Externe", "Variabel", "Hoch"),
]

fig, ax = plt.subplots(figsize=(9, 7))
ax.set_xlim(1, 4.8)
ax.set_ylim(1, 4.8)
ax.axvline(2.8, color="#999999", lw=1)
ax.axhline(2.8, color="#999999", lw=1)

quad_labels = [
    (1.9, 4.55, "Zufriedenstellen", "(geringeres Interesse, hoher Einfluss)"),
    (3.75, 4.55, "Eng einbinden", "(hohes Interesse, hoher Einfluss)"),
    (1.9, 1.2, "Beobachten", "(geringes Interesse, geringer Einfluss)"),
    (3.75, 1.2, "Informiert halten", "(hohes Interesse, geringerer Einfluss)"),
]
for x, y, t1, t2 in quad_labels:
    ax.text(x, y, t1, ha="center", va="center", fontsize=9.5, color=GREY, fontweight="bold", style="italic")
    ax.text(x, y-0.13, t2, ha="center", va="center", fontsize=7.5, color=GREY, style="italic")

# manual offsets to de-clutter overlapping points/labels: (dx, dy, label_dx, label_dy, label_va)
placements = {
    "Betrieb":              (0.05, 0, 0, 14, "bottom"),
    "Auftraggeber":         (-0.05, 0, 0, 14, "bottom"),
    "Primärtechnik":        (0.05, 0.08, 30, 16, "bottom"),
    "Schutz-/Leittechnik":  (-0.40, -0.15, 0, -18, "top"),
    "Einkauf":              (0, 0.05, 0, 16, "bottom"),
    "Arbeitssicherheit":    (0.20, 0.10, 15, 34, "bottom"),
    "Umweltschutz":         (0, 0, 0, 14, "bottom"),
    "Auftragnehmer":        (0.05, -0.05, 40, -20, "top"),
    "Behörden/Externe":     (0.10, 0.03, -15, 14, "bottom"),
}

for name, interesse, einfluss in stakeholders:
    x = level_map[interesse]
    y = level_map[einfluss]
    dx, dy, ldx, ldy, va = placements[name]
    xo, yo = x + dx, y + dy
    ax.scatter([xo], [yo], s=150, color=BLUE, zorder=3, edgecolor="white", linewidth=1.2)
    ax.annotate(name, (xo, yo), textcoords="offset points", xytext=(ldx, ldy),
                ha="center", va=va, fontsize=8.8, fontweight="bold", color="#1a1a1a")

ax.set_xlabel("Interesse →", fontsize=11)
ax.set_ylabel("Einfluss →", fontsize=11)
ax.set_xticks([]); ax.set_yticks([])
ax.set_title("Stakeholder-Portfolio: Einfluss vs. Interesse", fontsize=13, fontweight="bold", pad=14)
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "stakeholder_portfolio.png"), dpi=200)
plt.close(fig)
print("chart 2 done")

# ---------------------------------------------------------------
# 3. Cost curve + cumulative cost curve (S-curve), Plan vs Ist vs Prognose
# ---------------------------------------------------------------
plan_points = [
    (dt.date(2025,10,1), 0),
    (dt.date(2026,2,27), 145000),      # M3 Vergabe - 10%
    (dt.date(2026,4,30), 435000),      # M4 Design Review - 30% cum.
    (dt.date(2026,6,30), 870000),      # M5 FAT bestanden - 60% cum.
    (dt.date(2026,8,31), 1160000),     # M6 Lieferung - 80% cum.
    (dt.date(2026,9,10), 1377500),     # M7 Inbetriebnahme - 95% cum.
    (dt.date(2026,9,30), 1450000),     # M8 Abschluss - 100% cum.
]
ist_point = (dt.date(2026,6,30), 733500)   # Summe Ist_06_2026_EUR aus budgetplan.csv, Berichtsstand Statusbericht 06/2026
prognose_point = (dt.date(2026,9,30), 1362000)  # Summe Ist_EUR aus budgetplan.csv, Endkosten bei Projektabschluss

fig, ax = plt.subplots(figsize=(9.5, 5.5))
px = [p[0] for p in plan_points]
py = [p[1] for p in plan_points]
ax.plot(px, py, color=BLUE, marker="o", lw=2, label="Plan (kumuliert, aus Zahlungsmeilensteinen)")
ax.plot([dt.date(2025,10,1), ist_point[0]], [0, ist_point[1]], color=GREEN, lw=2, marker="o", label="Ist (kumuliert, Stand 06/2026)")
ax.scatter([prognose_point[0]], [prognose_point[1]], color=ORANGE, s=70, zorder=5, label="Endkosten (Projektabschluss, 1.362.000 EUR)")
ax.axhline(1450000, color=RED, lw=1, ls="--", alpha=0.6)
ax.text(dt.date(2026,1,20), 1470000, "Genehmigtes Budget: 1.450.000 EUR", color=RED, fontsize=8, ha="left")

ax.axvline(dt.date(2026,6,30), color="#aaaaaa", lw=1, ls=":")
ax.text(dt.date(2026,7,3), 780000, "Berichtsstand\nStatusbericht 06/2026", fontsize=7.5, color=GREY, ha="left")

ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.set_ylim(0, 1600000)
ax.set_ylabel("Kumulierte Kosten (EUR)")
ax.set_title("Kostenverlauf (S-Kurve): Plan, Ist (06/2026) und Endkosten", fontsize=12, fontweight="bold")
ax.legend(loc="lower right", fontsize=8.5, frameon=False)
ax.spines[["top","right"]].set_visible(False)
ax.yaxis.set_major_formatter(lambda v, pos: f"{v/1000:,.0f}k")
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "kostenkurve.png"), dpi=200)
plt.close(fig)
print("chart 3 done")

# ---------------------------------------------------------------
# 4. Resource Gantt highlighting the bottleneck resource
# ---------------------------------------------------------------
# Roles and their loading windows (derived from terminplan.csv phases + FTE table in 05_Budget_und_Ressourcen.md)
resources = [
    ("Projektleitung",                  [(dt.date(2025,10,1), dt.date(2026,9,30), 0.35)]),
    ("Fachprojektleitung Primärtechnik",[(dt.date(2025,10,16), dt.date(2026,9,30), 0.30)]),
    ("Schutz-/Leittechnik",             [(dt.date(2025,11,3), dt.date(2026,9,10), 0.15)]),
    ("Einkauf",                         [(dt.date(2025,12,1), dt.date(2026,2,27), 0.10)]),
    ("Betrieb",                         [(dt.date(2026,8,3), dt.date(2026,9,10), 0.10)]),
    ("Arbeitssicherheit/Umwelt",        [(dt.date(2026,8,3), dt.date(2026,9,10), 0.08)]),
    ("Dokumentation/Qualität",          [(dt.date(2026,7,1), dt.date(2026,9,30), 0.08)]),
    ("Montage-/Inbetriebnahmeteam (AN)",[(dt.date(2026,9,1), dt.date(2026,9,10), 1.00)]),  # bottleneck: capped to 10-day shutdown window
]

fig, ax = plt.subplots(figsize=(10, 5.2))
y_labels = []
for i, (name, bars) in enumerate(resources):
    y_labels.append(name)
    for (start, end, load) in bars:
        is_bottleneck = (name.startswith("Montage"))
        color = RED if is_bottleneck else BLUE
        alpha = 0.55 + 0.45*load if not is_bottleneck else 0.95
        width_days = (end - start).days
        ax.barh(i, width_days, left=start, height=0.55, color=color, alpha=alpha,
                edgecolor="white")
        label = f"{load*100:.0f}% Auslastung"
        if is_bottleneck:
            label = "Spitze 100 % (Ø 84 %)\nKapazität: 8 Pers. = 80 PT"
        if width_days < 60:
            ax.text(end + dt.timedelta(days=6), i, label, ha="left", va="center",
                    fontsize=8, color=RED if is_bottleneck else "#333333", fontweight="bold" if is_bottleneck else "normal")
        else:
            ax.text(start + dt.timedelta(days=width_days/2), i, label, ha="center", va="center",
                    fontsize=7.5, color="white", fontweight="bold" if is_bottleneck else "normal")

ax.axvspan(dt.date(2026,9,1), dt.date(2026,9,10), color=RED, alpha=0.08, zorder=0)
ax.text(dt.date(2026,4,1), -1.15, "Abschaltfenster 01.–10.09.2026 (10 Tage) – einzige Engpassressource: Montageteam, Kapazitätsgrenze 8 Personen",
        fontsize=8.5, color=RED, fontweight="bold", ha="center", va="center")
ax.set_xlim(dt.date(2025, 9, 15), dt.date(2026, 12, 20))
ax.set_yticks(range(len(resources)))
ax.set_yticklabels(y_labels, fontsize=9)
ax.set_ylim(len(resources)-0.5, -1.6)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.set_title("Ressourcen-Gantt mit Engpassressource (Montageteam im Abschaltfenster)", fontsize=11.5, fontweight="bold")
ax.spines[["top","right","left"]].set_visible(False)
fig.autofmt_xdate()
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "ressourcen_gantt.png"), dpi=200)
plt.close(fig)
print("chart 4 done")


# =====================================================================
# Ab hier: Grafiken fuer den PM-Report (Kapitel 6-15)
# =====================================================================
import csv, textwrap
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle

DARK = "#1f4e79"
LIGHT = "#dbe7f3"
DATA_DIR = os.path.join(OUT_DIR, "..", "..", "data")


def _box(ax, x, y, w, h, text, fc=BLUE, tc="white", fs=8.5, ec="none", ls="-", bold=False, lw=1.2):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=fc, edgecolor=ec, linestyle=ls, linewidth=lw))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color=tc,
            fontweight="bold" if bold else "normal")


# ---------------------------------------------------------------
# 5. Organigramm (Projektorganisation, ausgewogene Matrix)
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(11.5, 7.4))
ax.set_xlim(0, 12); ax.set_ylim(0, 8.4); ax.axis("off")

_box(ax, 5.0, 7.7, 4.4, 0.95, "Auftraggeber / Lenkungskreis\n(Budget, Entscheidungen; monatlich)", DARK, bold=True, fs=9)
_box(ax, 5.0, 6.05, 4.4, 0.95, "Projektleitung (0,35 FTE)\nGesamtsteuerung Termin, Kosten, Risiken", BLUE, bold=True, fs=9)
_box(ax, 10.0, 7.2, 3.3, 0.9, "PMO / Projektbüro\n(Standards, Reporting)", GREY, fs=8.8)

ax.add_patch(Rectangle((0.3, 0.9), 7.2, 3.6, facecolor="#f3f8f4", edgecolor=GREEN, linewidth=1.3))
ax.text(0.5, 4.3, "Kernteam Auftraggeberseite (Fach- und Linienfunktionen)", fontsize=9, color=GREEN, fontweight="bold", va="center")
kern = [("Fachprojektleitung\nPrimärtechnik", 1.6, 3.35), ("Schutz- und\nLeittechnik", 3.9, 3.35), ("Einkauf", 6.2, 3.35),
        ("Betrieb\n(Anlagenverantwortung)", 1.6, 1.75), ("Arbeitssicherheit", 3.9, 1.75), ("Umweltschutz", 6.2, 1.75)]
for t, x, y in kern:
    _box(ax, x, y, 2.05, 1.05, t, GREEN, fs=8.6)

ax.add_patch(Rectangle((8.2, 0.9), 3.5, 3.6, facecolor="#fdf5ec", edgecolor=ORANGE, linewidth=1.3))
ax.text(8.4, 4.3, "Auftragnehmer (Generalunternehmer)", fontsize=9, color=ORANGE, fontweight="bold", va="center")
for t, y in [("AN-Projektleitung", 3.5), ("Engineering / Fertigung", 2.5), ("Montageleitung\n(Montageteam 8 Personen)", 1.5)]:
    _box(ax, 9.95, y, 2.9, 0.8, t, ORANGE, fs=8.6)

def line(xs, ys, **kw):
    ax.plot(xs, ys, color=kw.pop("color", "#333333"), lw=kw.pop("lw", 1.6), solid_capstyle="butt", **kw)

line([5.0, 5.0], [7.22, 6.53])                     # Auftraggeber -> PL
line([5.0, 5.0], [5.57, 4.5])                      # PL -> Kernteam
line([7.2, 9.95, 9.95], [6.05, 6.05, 4.5])         # PL -> Auftragnehmer
ax.text(8.75, 6.2, "Vertrag / Jour fixe", fontsize=8, color="#333333", ha="center", va="bottom")
line([8.35, 7.2], [7.2, 6.3], color=GREY, ls="--")  # PMO (Stab)
ax.text(7.55, 7.05, "Stab", fontsize=8, color=GREY, style="italic", ha="left")

ax.text(0.3, 0.45, "durchgezogen: Projektbeziehung (Steuerung, Berichtslinie)      gestrichelt: Stab / Berichtslinie zum PMO      "
        "Fachliche Führung der Linienfunktionen bleibt in den Fachbereichen (Matrix)", fontsize=7.6, color="#444444", va="center")
ax.set_title("Projektorganisation: ausgewogene Matrix", fontsize=12.5, fontweight="bold")
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "organigramm.png"), dpi=200)
plt.close(fig)
print("chart 5 done")

# ---------------------------------------------------------------
# 6. Projektstrukturplan (codiert, phasenorientiert)
# ---------------------------------------------------------------
psp = [
    ("1", "Projekt-\ninitiierung", ["Projektauftrag erstellen", "Stakeholder identifizieren", "Budgetrahmen bestätigen", "Projektorganisation festlegen"]),
    ("2", "Bestandsaufnahme\nund Anforderungen", ["Technische Bestandsaufnahme", "Schnittstellen erfassen", "Anforderungen abstimmen", "Lastenheft freigeben"]),
    ("3", "Ausschreibung\nund Vergabe", ["Vergabeunterlagen erstellen", "Bieterfragen koordinieren", "Angebote technisch bewerten", "Kaufmännische Bewertung unterstützen", "Vergabeempfehlung und Bestellung"]),
    ("4", "Engineering\nund Fertigung", ["Kick-off mit Auftragnehmer", "Dokumenten- und Schnittstellenprüfung", "Design Review", "Fertigung", "Factory Acceptance Test"]),
    ("5", "Baustellen-\nvorbereitung", ["Montage- und Logistikkonzept", "Sicherheits- und Umweltplanung", "Abschalt- und Schaltplanung", "Baustelleneinrichtung", "Material- und Dokumentenfreigabe"]),
    ("6", "Montage und\nInbetriebnahme", ["Altgerät demontieren", "Fundament und Anschlüsse anpassen", "Neugerät montieren", "Primär- und Sekundäranschlüsse herstellen", "Prüfungen durchführen", "Funktionsprüfung und Inbetriebnahme"]),
    ("7", "Projekt-\nabschluss", ["Mängel bearbeiten", "Revisionsunterlagen prüfen", "Abnahme und Übergabe", "Kostenabschluss", "Lessons Learned"]),
    ("8", "Projekt-\nmanagement", ["Projektsteuerung und Reporting", "Risiko- und Änderungsmanagement", "Stakeholder- und Kommunikations-management"]),
]
fig, ax = plt.subplots(figsize=(16, 8.6))
ax.set_xlim(0, 16); ax.set_ylim(0, 8.6); ax.axis("off")
_box(ax, 8.0, 8.0, 7.0, 0.8, "0  Erneuerung 380-kV-Leistungsschalterfeld UW Mitte", DARK, bold=True, fs=11)
cw = 16 / len(psp)
line([8.0, 8.0], [7.6, 7.25]); line([cw/2, 16 - cw/2], [7.25, 7.25])
for i, (code, title, kids) in enumerate(psp):
    cx = cw/2 + i*cw
    line([cx, cx], [7.25, 6.95])
    _box(ax, cx, 6.5, cw - 0.2, 0.85, f"{code}  {title}", BLUE if code != "8" else GREY, bold=True, fs=8.6)
    for k, kid in enumerate(kids, start=1):
        y = 5.55 - (k-1)*0.92
        hi = (code == "6" and k == 3)
        _box(ax, cx, y, cw - 0.2, 0.78, f"{code}.{k}  " + textwrap.fill(kid, 22, break_long_words=False), "#fdebd6" if hi else LIGHT,
             tc="#1a1a1a", fs=7.4, ec=ORANGE if hi else BLUE, lw=2.0 if hi else 0.8)
        if k == 1:
            line([cx, cx], [6.07, y + 0.39], color="#777777", lw=1)
        else:
            line([cx, cx], [y + 0.92 - 0.39, y + 0.39], color="#777777", lw=1)
ax.text(0.2, 0.15, "Orange umrandet: in Kapitel 11, 14 und 15 ausgearbeitetes Arbeitspaket AP 6.3 „Neugerät montieren“", fontsize=9, color=ORANGE, fontweight="bold")
ax.set_title("Projektstrukturplan (phasenorientiert, codiert)", fontsize=13, fontweight="bold")
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "psp.png"), dpi=200)
plt.close(fig)
print("chart 6 done")

# ---------------------------------------------------------------
# 7. Vernetzter Terminplan (Gantt mit Vorgaengern, Meilensteinen, Puffer)
# ---------------------------------------------------------------
with open(os.path.join(DATA_DIR, "terminplan.csv"), encoding="utf-8-sig") as fh:
    plan = list(csv.DictReader(fh, delimiter=";"))
fig, ax = plt.subplots(figsize=(12.5, 6.6))
ypos = {r["ID"]: i for i, r in enumerate(plan)}
d = lambda s: dt.date.fromisoformat(s)
for r in plan:
    i = ypos[r["ID"]]
    s, e = d(r["Start"]), d(r["Ende"])
    crit = r["Kritischer_Pfad"].lower() == "ja"
    ax.barh(i, (e - s).days + 1, left=s, height=0.5, color=RED if crit else BLUE, alpha=0.85, edgecolor="white")
    ax.text(s - dt.timedelta(days=4), i, f'{r["ID"]}  {r["Arbeitspaket"]}', ha="right", va="center", fontsize=8.3)
    if r["Meilenstein"] != "-":
        ax.scatter([e + dt.timedelta(days=1)], [i], marker="D", s=70, color="#222222", zorder=5)
        ax.text(e + dt.timedelta(days=6), i, f'{r["Meilenstein"]}  {e.strftime("%d.%m.%Y")}', va="center", fontsize=8, fontweight="bold")
for r in plan:
    if r["Vorgaenger"] in ("-", ""):
        continue
    p = next(x for x in plan if x["ID"] == r["Vorgaenger"])
    j, i = ypos[r["ID"]], ypos[p["ID"]]
    if r["Beziehung"].startswith("AA"):
        ax.annotate("", xy=(d(r["Start"]), j - 0.27), xytext=(d(p["Start"]) + dt.timedelta(days=1), i + 0.27),
                    arrowprops=dict(arrowstyle="-|>", color="#333333", lw=1.1, ls="--", connectionstyle="angle,angleA=0,angleB=90"))
        ax.text(d(p["Start"]) + dt.timedelta(days=2), i + 0.55, "AA + 12 AT", fontsize=7.4, color="#333333", va="center", ha="right")
    else:
        ax.annotate("", xy=(d(r["Start"]) + dt.timedelta(days=1), j - 0.27), xytext=(d(p["Ende"]) + dt.timedelta(days=1), i),
                    arrowprops=dict(arrowstyle="-|>", color="#333333", lw=1.1, connectionstyle="angle,angleA=0,angleB=90"))
ax.axvspan(dt.date(2026, 9, 1), dt.date(2026, 9, 10), color=ORANGE, alpha=0.25, zorder=0)
ax.text(dt.date(2026, 9, 1), -0.95, "Abschaltfenster\n01.–10.09.2026", ha="right", fontsize=7.6, color=ORANGE, fontweight="bold")
ax.axvline(dt.date(2026, 9, 30), color=RED, lw=1.3, ls="--")
ax.text(dt.date(2026, 10, 2), -0.95, "Frist\n30.09.2026", ha="left", fontsize=7.6, color=RED, fontweight="bold")
ax.annotate("", xy=(dt.date(2026, 9, 30), 13.0), xytext=(dt.date(2026, 9, 10), 13.0),
            arrowprops=dict(arrowstyle="<->", color=GREEN, lw=1.5))
ax.text(dt.date(2026, 9, 28), 13.45, "Puffer 14 AT", ha="right", va="center", fontsize=8, color=GREEN, fontweight="bold")
ax.set_ylim(13.8, -1.5)
ax.set_xlim(dt.date(2025, 6, 1), dt.date(2026, 11, 20))
ax.set_yticks([])
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
ax.tick_params(axis="x", labelsize=8)
ax.spines[["top", "right", "left"]].set_visible(False)
ax.grid(axis="x", color="#e2e2e2", lw=0.6)
ax.legend(handles=[mpatches.Patch(color=RED, label="kritischer Pfad"), mpatches.Patch(color=BLUE, label="nicht kritisch"),
                   plt.Line2D([], [], marker="D", color="#222222", ls="", label="Meilenstein")],
          loc="lower left", fontsize=8, frameon=False)
ax.set_title("Vernetzter Terminplan mit kritischem Pfad", fontsize=12.5, fontweight="bold")
plt.setp(ax.get_xticklabels(), rotation=35, ha="right")
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "gantt_vernetzt.png"), dpi=200)
plt.close(fig)
print("chart 7 done")

# ---------------------------------------------------------------
# 8. Kostenganglinie und Kostensummenlinie (Projekt, Monatsraster)
# ---------------------------------------------------------------
months = [dt.date(2025, 10, 1) + dt.timedelta(days=0)]
months = [dt.date(2025 + (9 + k) // 12, (9 + k) % 12 + 1, 1) for k in range(12)]
zahl = {dt.date(2026, 2, 1): 145000, dt.date(2026, 4, 1): 290000, dt.date(2026, 6, 1): 435000,
        dt.date(2026, 8, 1): 290000, dt.date(2026, 9, 1): 290000}
gang = [zahl.get(m, 0) for m in months]
summe = list(np.cumsum(gang))
xs = np.arange(len(months))
fig, ax = plt.subplots(figsize=(10.5, 5.6))
ax.bar(xs, [g/1000 for g in gang], color=BLUE, alpha=0.85, width=0.6, label="Kostenganglinie (Plan je Monat)")
for x, g in zip(xs, gang):
    if g:
        ax.text(x, g/1000 + 12, f"{g/1000:,.0f}k".replace(",", "."), ha="center", fontsize=8, color=BLUE, fontweight="bold")
ax.set_ylabel("Kosten je Monat (Tsd. EUR)")
ax.set_ylim(0, 520)
ax2 = ax.twinx()
ax2.plot(xs, [s/1000 for s in summe], color=DARK, marker="o", lw=2.2, label="Kostensummenlinie (Plan, kumuliert)")
ax2.scatter([8], [733.5], color=GREEN, s=80, zorder=6, label="Ist kumuliert (Stand 06/2026: 733.500 EUR)")
ax2.scatter([11], [1362], color=ORANGE, s=80, zorder=6, label="Endkosten Projektabschluss (1.362.000 EUR)")
ax2.axhline(1450, color=RED, lw=1, ls="--", alpha=0.6)
ax2.text(0.0, 1468, "Genehmigtes Budget 1.450.000 EUR", color=RED, fontsize=8)
ax2.set_ylim(0, 1650)
ax2.set_ylabel("Kosten kumuliert (Tsd. EUR)")
ax.set_xticks(xs)
ax.set_xticklabels([m.strftime("%b %y") for m in months], fontsize=8.5)
h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, loc="center left", bbox_to_anchor=(0.01, 0.55), fontsize=8, frameon=False)
ax.set_title("Kostenganglinie und Kostensummenlinie (Zahlungsplan, gleiches Monatsraster)", fontsize=11.5, fontweight="bold")
ax.spines[["top"]].set_visible(False); ax2.spines[["top"]].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "kostenganglinie_projekt.png"), dpi=200)
plt.close(fig)
print("chart 8 done")

# ---------------------------------------------------------------
# 9. AP 6.3: Kostenganglinie und Kostensummenlinie (Tagesraster)
# ---------------------------------------------------------------
RATE, KRAN, HILFS = 800, 3200, 4000
pt_day = [7.0, 8.0, 7.0, 27.3333333 - 22.0]
tage = ["Tag 3\nDo 03.09.", "Tag 4\nFr 04.09.", "Tag 5\nSa 05.09.", "Tag 6\nSo 06.09."]
pers = [p * RATE for p in pt_day]
kran = [KRAN] * 4
hilf = [HILFS, 0, 0, 0]
tot = [a + b + c for a, b, c in zip(pers, kran, hilf)]
cum = list(np.cumsum(tot))
fig, ax = plt.subplots(figsize=(9.5, 5.4))
xs = np.arange(4)
ax.bar(xs, pers, color=BLUE, width=0.55, label="Personal Montageteam (PT × 800 EUR)")
ax.bar(xs, kran, bottom=pers, color=ORANGE, width=0.55, label="Autokran (3.200 EUR je Einsatztag)")
ax.bar(xs, hilf, bottom=[a + b for a, b in zip(pers, kran)], color=GREY, width=0.55, label="Anschlag- und Ausrichtmittel")
for x, t in zip(xs, tot):
    ax.text(x, t + 500, f"{t:,.0f}".replace(",", ".") + " EUR", ha="center", fontsize=8.5, fontweight="bold")
ax.set_ylabel("Kosten je Tag (EUR)")
ax.set_ylim(0, 20000)
ax2 = ax.twinx()
ax2.plot(xs, cum, color=DARK, marker="o", lw=2.2, label="Kostensummenlinie (kumuliert)")
for x, c in zip(xs, cum):
    ax2.text(x, c + (1700 if x != 1 else -3600), f"Σ {c:,.0f}".replace(",", "."), fontsize=8.5, color=DARK, ha="center", fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.2", facecolor="white", edgecolor="none", alpha=0.85))
ax2.set_ylim(0, 50000)
ax2.set_ylabel("Kosten kumuliert (EUR)")
ax.set_xticks(xs); ax.set_xticklabels(tage, fontsize=8.5)
h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, loc="upper left", fontsize=7.8, frameon=False)
ax.set_title("AP 6.3 „Neugerät montieren“: Kostenganglinie und Kostensummenlinie (Plan 38.667 EUR)", fontsize=11, fontweight="bold")
ax.spines[["top"]].set_visible(False); ax2.spines[["top"]].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "kosten_ap63.png"), dpi=200)
plt.close(fig)
print("chart 9 done")

# ---------------------------------------------------------------
# 10. Engpassressource Montageteam im Abschaltfenster
# ---------------------------------------------------------------
tw = 27.3333333 - 22.0
win = [
    (1, {"6.1": 8}), (2, {"6.1": 4, "6.2": 4}), (3, {"6.3": 7, "6.4": 1}), (4, {"6.3": 8}), (5, {"6.3": 7, "6.4": 1}),
    (6, {"6.3": tw, "6.4": 8 - tw}), (7, {"6.4": 8}), (8, {"6.5": 4}), (9, {"6.5": 4}), (10, {"6.6": 3}),
]
aps = [("6.1", "6.1 Altgerät demontieren", "#7f8c9b"), ("6.2", "6.2 Fundament/Adapter (CR-002)", "#a8b8c9"),
       ("6.3", "6.3 Neugerät montieren", ORANGE), ("6.4", "6.4 Anschlüsse herstellen", GREEN),
       ("6.5", "6.5 Prüfungen (Unterstützung)", BLUE), ("6.6", "6.6 Inbetriebnahme (Unterstützung)", DARK)]
fig, ax = plt.subplots(figsize=(10.5, 5.6))
bottom = np.zeros(10)
for code, label, col in aps:
    vals = np.array([dct.get(code, 0) for _, dct in win], dtype=float)
    ax.bar(np.arange(10), vals, bottom=bottom, color=col, width=0.62, label=label)
    bottom += vals
ax.axhline(8, color=RED, lw=2, ls="--")
ax.text(9.45, 8.75, "Kapazitätsgrenze: 8 Personen (80 PT)", color=RED, fontsize=9, fontweight="bold", ha="right")
for x, b in enumerate(bottom):
    ax.text(x, b + 0.12, f"{b:.1f}".replace(".", ","), ha="center", fontsize=8)
ax.set_ylim(0, 9.6)
ax.set_xticks(np.arange(10))
ax.set_xticklabels([f"Tag {t}\n{dt.date(2026, 9, t).strftime('%d.%m.')}" for t in range(1, 11)], fontsize=8)
ax.set_ylabel("Eingesetzte Personen")
ax.set_title("Engpassressource Montageteam: Bedarf je Tag gegen Kapazitätsgrenze (Bedarf 67 PT = 84 % von 80 PT)", fontsize=10.5, fontweight="bold")
ax.legend(loc="upper right", bbox_to_anchor=(1.0, 0.80), fontsize=7.8, frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "engpass_montageteam.png"), dpi=200)
plt.close(fig)
print("chart 10 done")

# ---------------------------------------------------------------
# 11. Risikomatrix (vor und nach Massnahmen)
# ---------------------------------------------------------------
risks = [  # id, (A, P) vorher, (A, P) nachher
    ("R-01", (5, 4), (4, 3)), ("R-02", (4, 4), (4, 2)), ("R-03", (5, 3), (5, 2)),
    ("R-04", (4, 3), (3, 2)), ("R-05", (3, 4), (3, 2)), ("R-06", (5, 3), (5, 1)), ("R-09", (4, 3), (3, 2)),
]
fig, ax = plt.subplots(figsize=(8.6, 7.0))
for a in range(1, 6):
    for p in range(1, 6):
        v = a * p
        col = "#e8f3ec" if v <= 5 else ("#fbf2d8" if v <= 12 else "#f6dcd9")
        ax.add_patch(Rectangle((a - 0.5, p - 0.5), 1, 1, facecolor=col, edgecolor="white", lw=2))
        ax.text(a + 0.4, p - 0.42, str(v), fontsize=6.5, color="#999999", ha="right", va="bottom")
cells = {}
def place(pt, tag, marker, filled, rid):
    n = cells.get(pt, 0); cells[pt] = n + 1
    offs = {("R-01", "n"): (0.2, -0.2)}.get((rid, tag)) or [(-0.2, 0.2), (0.2, 0.2), (-0.2, -0.2), (0.2, -0.2)][n % 4]
    x, y = pt[0] + offs[0], pt[1] + offs[1]
    ax.scatter([x], [y], marker=marker, s=190, facecolor=(BLUE if filled else "white"), edgecolor=BLUE, lw=1.8, zorder=4)
    ax.text(x, y - 0.02, rid[2:], fontsize=6.8, ha="center", va="center", color="white" if filled else BLUE, fontweight="bold", zorder=5)
    return x, y
pos = {}
for rid, before, after in risks:
    pos[rid] = [place(before, "v", "o", True, rid)]
for rid, before, after in risks:
    pos[rid].append(place(after, "n", "s", False, rid))
for rid, (p0, p1) in pos.items():
    ax.annotate("", xy=p1, xytext=p0, arrowprops=dict(arrowstyle="-|>", color="#555555", lw=1.0, shrinkA=9, shrinkB=9), zorder=3)
ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.5)
ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
ax.set_xlabel("Auswirkung (1–5)"); ax.set_ylabel("Eintrittswahrscheinlichkeit (1–5)")
ax.legend(handles=[plt.Line2D([], [], marker="o", color=BLUE, ls="", markersize=9, label="vor Maßnahmen (Ausgangswert)"),
                   plt.Line2D([], [], marker="s", markerfacecolor="white", markeredgecolor=BLUE, ls="", markersize=9, label="nach Maßnahmen (Restwert)")],
          loc="upper center", bbox_to_anchor=(0.5, -0.09), ncol=2, fontsize=8.5, frameon=False)
ax.set_title("Risikomatrix: Wirkung der Maßnahmen (Zahl = Nummer des Risikos R-0x)", fontsize=11.5, fontweight="bold")
for s_ in ("top", "right"):
    ax.spines[s_].set_visible(False)
fig.tight_layout()
fig.savefig(os.path.join(OUT_DIR, "risikomatrix.png"), dpi=200)
plt.close(fig)
print("chart 11 done")
