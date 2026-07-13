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

Das Projekt ist auf eine Einstiegsposition im technischen Projektmanagement der Energieversorgung ausgerichtet.

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

```bash
python src/project_dashboard.py
```

Das Skript wertet Budget, Termine, Risiken und Änderungen aus den CSV-Dateien aus.

## Beispiel für den Lebenslauf

```latex
\begin{rSubsection}{Technisches Projektmanagement – Umspannwerksprojekt}
{}{Eigenständiges Simulationsprojekt}{}
\item Planung der fiktiven Erneuerung eines 380-kV-Leistungsschalterfeldes mit Termin-, Budget-, Ressourcen- und Risikosteuerung
\item Erstellung von Lastenheft, Projektstrukturplan, RACI-Matrix, Vergabeunterlagen sowie Prüf- und Abnahmekriterien
\item Entwicklung eines Python-Dashboards zur automatisierten Auswertung von Projektstatus, Budgetabweichungen und Risiken
\end{rSubsection}
```

## Ehrliche Einordnung im Bewerbungsgespräch

Geeignete Formulierung:

> „Ich habe mir Grundkenntnisse im technischen Projektmanagement und Vertragswesen durch ein eigenständig aufgebautes Simulationsprojekt erarbeitet. Dabei habe ich einen vollständigen Projektablauf von der Anforderungsdefinition über Vergabe, Termin- und Risikoplanung bis zur Abnahme modelliert. Mir ist bewusst, dass dies reale Projekterfahrung nicht ersetzt; es zeigt jedoch, dass ich die Methoden strukturiert anwenden und mich schnell in reale Prozesse einarbeiten kann.“

## Lizenz

Dieses Lernprojekt darf für Bewerbungs- und Ausbildungszwecke angepasst und weiterentwickelt werden.
