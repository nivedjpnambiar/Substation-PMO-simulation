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
- regelmäßiges Projektstatusreporting.

Das Projekt demonstriert die strukturierte Anwendung grundlegender Methoden des technischen Projektmanagements im Umfeld der Energieversorgung.

## Demonstrierte Kompetenzen

- Technisches Projektmanagement
- Termin-, Kosten- und Ressourcensteuerung
- Risikomanagement
- Stakeholder- und Schnittstellenmanagement
- Grundkenntnisse im technischen Vertragswesen
- Technische Spezifikation und Angebotsbewertung
- Qualitäts-, Arbeits- und Anlagensicherheitsplanung
- Reporting und Change Management
- Python-basierte Projektauswertung

## Projektannahmen

| Merkmal | Annahme |
|---|---|
| Anlage | Fiktives 380-kV-Umspannwerk „UW Mitte“ |
| Projektumfang | Austausch eines Leistungsschalters inklusive Antrieb, Sekundärschnittstellen und Dokumentation |
| Projektbeginn | 01.10.2026 |
| Geplante Inbetriebnahme | 30.09.2027 |
| Budgetrahmen | 1.450.000 EUR |
| Auftraggeber | Fiktiver Übertragungsnetzbetreiber |
| Ausführung | Externer Generalunternehmer mit mehreren Fachgewerken |
| Betriebsunterbrechung | Geplantes Abschaltfenster von 10 Tagen |

## Repository-Struktur

```text
.
├── README.md
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
│   └── 13_Lessons_Learned.md
├── data/
│   ├── terminplan.csv
│   ├── budgetplan.csv
│   ├── risikoregister.csv
│   ├── raci_matrix.csv
│   ├── angebotsbewertung.csv
│   └── change_log.csv
├── templates/
│   ├── change_request_template.md
│   ├── meeting_minutes_template.md
│   └── status_report_template.md
└── src/
    └── project_dashboard.py
```

## Schnellstart

Python 3.10 oder neuer genügt; externe Pakete sind nicht erforderlich.

Alternativ kann die [Beispielausgabe des Dashboards](DASHBOARD_EXAMPLE.txt) direkt angesehen werden.

```bash
python src/project_dashboard.py
```

Das Skript wertet Budget, Termine, Risiken und Änderungen aus den CSV-Dateien aus.


## Lizenz

Dieses Lernprojekt darf für Bewerbungs- und Ausbildungszwecke angepasst und weiterentwickelt werden.
