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
    (dt.date(2026,2,28), 145000),      # M3 Vergabe - 10%
    (dt.date(2026,4,30), 435000),      # M4 Design Review - 30% cum.
    (dt.date(2026,6,30), 870000),      # M5 FAT bestanden - 60% cum.
    (dt.date(2026,8,31), 1160000),     # M6 Lieferung - 80% cum.
    (dt.date(2026,9,20), 1377500),     # M7 Inbetriebnahme - 95% cum.
    (dt.date(2026,9,30), 1450000),     # M8 Abschluss - 100% cum.
]
ist_point = (dt.date(2026,6,30), 733500)   # Summe Ist_EUR aus budgetplan.csv, Berichtsstand Statusbericht 06/2026
prognose_point = (dt.date(2026,9,30), 1438000)  # Summe Prognose_EUR aus budgetplan.csv

fig, ax = plt.subplots(figsize=(9.5, 5.5))
px = [p[0] for p in plan_points]
py = [p[1] for p in plan_points]
ax.plot(px, py, color=BLUE, marker="o", lw=2, label="Plan (kumuliert, aus Zahlungsmeilensteinen)")
ax.plot([dt.date(2025,10,1), ist_point[0]], [0, ist_point[1]], color=GREEN, lw=2, marker="o", label="Ist (kumuliert, Stand 06/2026)")
ax.scatter([prognose_point[0]], [prognose_point[1]], color=ORANGE, s=70, zorder=5, label="Prognose Gesamtkosten (Projektende)")
ax.axhline(1450000, color=RED, lw=1, ls="--", alpha=0.6)
ax.text(dt.date(2026,1,20), 1470000, "Genehmigtes Budget: 1.450.000 EUR", color=RED, fontsize=8, ha="left")

ax.axvline(dt.date(2026,6,30), color="#aaaaaa", lw=1, ls=":")
ax.text(dt.date(2026,7,3), 780000, "Berichtsstand\nStatusbericht 06/2026", fontsize=7.5, color=GREY, ha="left")

ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %y"))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
ax.set_ylim(0, 1600000)
ax.set_ylabel("Kumulierte Kosten (EUR)")
ax.set_title("Kostenverlauf (S-Kurve): Plan, Ist und Prognose", fontsize=12, fontweight="bold")
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
    ("Fachprojektleitung Primärtechnik",[(dt.date(2025,10,16), dt.date(2026,9,20), 0.30)]),
    ("Schutz-/Leittechnik",             [(dt.date(2025,11,1), dt.date(2026,9,20), 0.15)]),
    ("Einkauf",                         [(dt.date(2025,12,1), dt.date(2026,2,28), 0.10)]),
    ("Betrieb",                         [(dt.date(2026,8,1), dt.date(2026,9,20), 0.10)]),
    ("Arbeitssicherheit/Umwelt",        [(dt.date(2026,8,1), dt.date(2026,9,20), 0.08)]),
    ("Montage-/Inbetriebnahmeteam (AN)",[(dt.date(2026,9,1), dt.date(2026,9,10), 1.00)]),  # bottleneck: capped to 10-day shutdown window
]

fig, ax = plt.subplots(figsize=(10, 4.8))
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
        if width_days < 25:
            ax.text(end + dt.timedelta(days=6), i, label, ha="left", va="center",
                    fontsize=8, color=RED, fontweight="bold")
        else:
            ax.text(start + dt.timedelta(days=width_days/2), i, label, ha="center", va="center",
                    fontsize=7.5, color="white", fontweight="bold" if is_bottleneck else "normal")

ax.axvspan(dt.date(2026,9,1), dt.date(2026,9,10), color=RED, alpha=0.08, zorder=0)
ax.text(dt.date(2026,4,1), -1.15, "Abschaltfenster (10 Tage) – einzige Engpassressource des Projekts: Montageteam auf 100% Auslastung begrenzt",
        fontsize=8.5, color=RED, fontweight="bold", ha="center", va="center")
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
