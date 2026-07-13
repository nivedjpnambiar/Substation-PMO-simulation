#!/usr/bin/env python3
"""
Einfaches, dependency-freies Projekt-Dashboard für die Simulation.

Liest CSV-Dateien aus ../data und zeigt:
- Budgetstatus
- Terminstatus
- Top-Risiken
- offene Change Requests
- gewichtete Angebotsbewertung

Keine externe Bibliothek erforderlich.
"""

from __future__ import annotations

import csv
from pathlib import Path
from datetime import date, datetime
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def read_csv(filename: str) -> list[dict[str, str]]:
    path = DATA / filename
    if not path.exists():
        raise FileNotFoundError(f"Datei nicht gefunden: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle, delimiter=";"))


def eur(value: float) -> str:
    return f"{value:,.0f} EUR".replace(",", ".")


def heading(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def budget_summary() -> None:
    rows = read_csv("budgetplan.csv")
    plan = sum(float(r["Plan_EUR"]) for r in rows)
    committed = sum(float(r["Beauftragt_EUR"]) for r in rows)
    actual = sum(float(r["Ist_EUR"]) for r in rows)
    forecast = sum(float(r["Prognose_EUR"]) for r in rows)
    variance = forecast - plan
    variance_pct = variance / plan * 100 if plan else 0.0

    heading("BUDGETSTATUS")
    print(f"Plan:        {eur(plan)}")
    print(f"Beauftragt: {eur(committed)}")
    print(f"Ist:         {eur(actual)}")
    print(f"Prognose:    {eur(forecast)}")
    print(f"Abweichung:  {eur(variance)} ({variance_pct:+.2f} %)")

    if abs(variance_pct) <= 2:
        status = "GRÜN"
    elif abs(variance_pct) <= 5:
        status = "GELB"
    else:
        status = "ROT"
    print(f"Ampel:       {status}")


def schedule_summary() -> None:
    rows = read_csv("terminplan.csv")
    progress = [float(r["Fortschritt_Prozent"]) for r in rows]
    mean_progress = sum(progress) / len(progress) if progress else 0.0
    critical_issues = [
        r for r in rows
        if r["Kritischer_Pfad"].lower() == "ja"
        and r["Status"].lower() in {"gefährdet", "verzögert"}
    ]

    heading("TERMINSTATUS")
    print(f"Mittlerer Arbeitspaket-Fortschritt: {mean_progress:.1f} %")
    print(f"Kritische gefährdete Vorgänge:     {len(critical_issues)}")
    for item in critical_issues:
        print(f" - {item['ID']}: {item['Arbeitspaket']} ({item['Status']})")


def risk_summary() -> None:
    rows = read_csv("risikoregister.csv")
    open_risks = [r for r in rows if r["Status"].lower() != "geschlossen"]
    top = sorted(open_risks, key=lambda r: int(r["Risikowert"]), reverse=True)[:5]

    heading("TOP-RISIKEN")
    for r in top:
        print(
            f"{r['ID']:5} | Wert {int(r['Risikowert']):2} | "
            f"{r['Klasse']:6} | {r['Risiko']} | Owner: {r['Eigentuemer']}"
        )


def change_summary() -> None:
    rows = read_csv("change_log.csv")
    open_changes = [
        r for r in rows
        if r["Status"].lower() not in {"genehmigt", "abgelehnt", "geschlossen"}
    ]
    approved_cost = sum(
        float(r["Kostenwirkung_EUR"])
        for r in rows
        if r["Status"].lower() == "genehmigt"
    )

    heading("CHANGE MANAGEMENT")
    print(f"Offene Changes:                   {len(open_changes)}")
    print(f"Genehmigte Kostenwirkung netto:  {eur(approved_cost)}")
    for r in open_changes:
        print(
            f" - {r['Change_ID']}: {r['Titel']} | "
            f"{eur(float(r['Kostenwirkung_EUR']))} | "
            f"{r['Terminwirkung_Tage']} Tage"
        )


def bid_evaluation() -> None:
    rows = read_csv("angebotsbewertung.csv")
    bidders = ["Bieter_A_Punkte", "Bieter_B_Punkte", "Bieter_C_Punkte"]
    totals = {bidder: 0.0 for bidder in bidders}

    for row in rows:
        weight = float(row["Gewichtung_Prozent"]) / 100.0
        for bidder in bidders:
            totals[bidder] += weight * float(row[bidder])

    heading("GEWICHTETE ANGEBOTSBEWERTUNG")
    ranking = sorted(totals.items(), key=lambda item: item[1], reverse=True)
    for index, (bidder, score) in enumerate(ranking, start=1):
        display = bidder.replace("_Punkte", "").replace("_", " ")
        print(f"{index}. {display}: {score:.2f} von 5.00 Punkten")


def main() -> None:
    print("PROJEKT-DASHBOARD: 380-kV-LEISTUNGSSCHALTERFELD")
    print(f"Datenstand: {date.today().isoformat()}")
    try:
        budget_summary()
        schedule_summary()
        risk_summary()
        change_summary()
        bid_evaluation()
    except (FileNotFoundError, KeyError, ValueError) as exc:
        raise SystemExit(f"Fehler beim Einlesen der Projektdaten: {exc}") from exc


if __name__ == "__main__":
    main()
