# Technisches Projektmanagement: Erneuerung eines 380-kV-Leistungsschalterfeldes

> **Eigenständiges Lern- und Simulationsprojekt**  
> Dieses Repository dokumentiert die fiktive Planung und Steuerung eines technischen Investitionsprojekts in einem Umspannwerk. Es stellt keine reale Projekterfahrung, Rechtsberatung oder Planung für eine konkrete Anlage dar.

## Projektziel

In einem fiktiven Umspannwerk soll ein alter 380-kV-Leistungsschalter einschließlich Nebenkomponenten erneuert werden. Das Projekt umfasst:

- technische Anforderungsdefinition,
- Projektstruktur-, Termin-, Budget- und Ressourcenplanung,
- Risiko- und Stakeholdermanagement,
- Vorbereitung einer technischen Ausschreibung,
- Angebotsbewertung und Vergabeempfehlung,
- Änderungsmanagement,
- Montage-, Prüf- und Abnahmeplanung,
- regelmäßiges Projektstatusreporting,
- Portfolio-Priorisierung und Programmeinordnung,
- Projektumfeld-, Stakeholder- und Kommunikationsanalyse.

Das Projekt demonstriert die strukturierte Anwendung grundlegender Methoden des technischen Projektmanagements im Umfeld der Energieversorgung.

## Demonstrierte Kompetenzen

- Technisches Projektmanagement
- Termin-, Kosten- und Ressourcensteuerung
- Risikomanagement
- Stakeholder-, Schnittstellen- und Machtanalyse
- Persönliche Kommunikation (Kommunikationsmodelle in der Praxis)
- Projektdesign und Wahl des Vorgehensmodells
- Grundkenntnisse im technischen Vertragswesen
- Technische Spezifikation und Angebotsbewertung
- Qualitäts-, Arbeits- und Anlagensicherheitsplanung
- Reporting und Change Management
- Portfolio- und Programmpriorisierung
- Python-basierte Projektauswertung und Datenvisualisierung

## Projektannahmen

| Merkmal | Annahme |
|---|---|
| Anlage | Fiktives 380-kV-Umspannwerk „UW Mitte“ |
| Projektumfang | Austausch eines Leistungsschalters inklusive Antrieb, Sekundärschnittstellen und Dokumentation |
| Projektbeginn | 01.10.2025 |
| Geplante Inbetriebnahme | 30.09.2026 |
| Budgetrahmen | 1.450.000 EUR |
| Auftraggeber | Fiktiver Übertragungsnetzbetreiber |
| Ausführung | Externer Generalunternehmer mit mehreren Fachgewerken |
| Betriebsunterbrechung | Geplantes Abschaltfenster von 10 Tagen |

## Repository-Struktur

```text
.
├── README.md
├── LICENSE
├── DASHBOARD_EXAMPLE.txt
├── portfolio_dashboard.html
├── docs/
│   ├── 01_Projektauftrag.md
│   ├── 02_Anforderungen_und_Lastenheft.md
│   ├── 03_Projektstrukturplan.md
│   ├── 04_Termin_und_Meilensteine.md
│   ├── 05_Budget_und_Ressourcen.md
│   ├── 06_Risikomanagement.md
│   ├── 07_Stakeholder_und_RACI.md
│   ├── 08_Vergabe_und_Vertragsgrundlagen.md
│   ├── 09_Angebotsbewertung.md
│   ├── 10_Change_Management.md
│   ├── 11_Qualitaet_Pruefung_Abnahme.md
│   ├── 12_Statusbericht.md
│   ├── 13_Lessons_Learned.md
│   ├── 14_Portfolio_Priorisierung.md
│   ├── 15_Projektumfeld_und_Stakeholderportfolio.md
│   ├── 16_Projektdesign_und_Ansatz.md
│   ├── 17_Kommunikationsmodell.md
│   └── 18_Kosten_und_Ressourcenkurven.md
├── assets/
│   └── diagrams/
│       ├── projektumfeld.png
│       ├── stakeholder_portfolio.png
│       ├── kostenkurve.png
│       ├── ressourcen_gantt.png
│       └── make_charts.py
├── data/
│   ├── terminplan.csv
│   ├── budgetplan.csv
│   ├── risikoregister.csv
│   ├── raci_matrix_p1.xlsx
│   ├── angebotsbewertung.csv
│   ├── change_log.csv
│   ├── portfolio_uebersicht.csv
│   └── ressourcenkonflikte.csv
├── templates/
│   ├── change_request_template.md
│   ├── meeting_minutes_template.md
│   └── status_report_template.md
└── src/
    └── project_dashboard.py
```

## Inhaltsübersicht `docs/`

| # | Dokument | Inhalt |
|---|---|---|
| 01 | Projektauftrag | Ziele, Nicht-Ziele, Erfolgskennzahlen, Projektorganisation |
| 02 | Anforderungen und Lastenheft | Muss-/Soll-Anforderungen, Liefer- und Leistungsumfang |
| 03 | Projektstrukturplan | Arbeitspakete je Phase, Definition of Done |
| 04 | Termin- und Meilensteinplanung | Meilensteine, kritischer Pfad, Gantt |
| 05 | Budget und Ressourcen | Kostenblöcke, Zahlungsmeilensteine, FTE-Planung |
| 06 | Risikomanagement | Bewertungsmethode, Top-Risiken, Chancen |
| 07 | Stakeholder und RACI | Stakeholderanalyse, RACI-Legende, Kommunikationsplan |
| 08 | Vergabe und Vertragsgrundlagen | Ausschreibungsinhalte, technisches Vertragswesen |
| 09 | Angebotsbewertung | Bewertungsmodell, Vergabeempfehlung |
| 10 | Change Management | Ablauf, Kategorien, Beispiel-Change |
| 11 | Qualität, Prüfung, Abnahme | Prüfplan, Mängelklassen, Abnahmekriterien |
| 12 | Statusbericht | Beispielhafter Monatsbericht mit Ampelstatus |
| 13 | Lessons Learned | Erkenntnisse und persönlicher Lerngewinn |
| 14 | Portfolio-Priorisierung | Einordnung in Portfolio-/Programmkontext |
| 15 | Projektumfeld und Stakeholderportfolio | Umfelddiagramm, Schnittstellen, Einfluss-/Interesse-Portfolio, Machtpromotoren |
| 16 | Projektdesign und Ansatz | Erfolgskriterien-Priorisierung, Wahl des Vorgehensmodells, ausgearbeitetes Arbeitspaket |
| 17 | Kommunikationsmodell | Anwendung des Vier-Seiten-Modells auf ein reales Abstimmungsgespräch |
| 18 | Kosten- und Ressourcenkurven | Kosten-S-Kurve (Plan/Ist/Prognose), Ressourcen-Gantt mit Engpassressource |

## Schnellstart

Python 3.10 oder neuer genügt; externe Pakete sind nicht erforderlich.

Alternativ kann die [Beispielausgabe des Dashboards](DASHBOARD_EXAMPLE.txt) direkt angesehen werden.

```bash
python src/project_dashboard.py
```

Das Skript wertet Budget, Termine, Risiken und Änderungen aus den CSV-Dateien aus.

Die Diagramme unter `assets/diagrams/` (Projektumfeld, Stakeholder-Portfolio, Kostenkurve, Ressourcen-Gantt) lassen sich bei Bedarf neu erzeugen:

```bash
python assets/diagrams/make_charts.py
```

Das Skript benötigt `matplotlib` (`pip install matplotlib`).


## Lizenz

Dieses Lernprojekt darf für Bewerbungs- und Ausbildungszwecke angepasst und weiterentwickelt werden.
