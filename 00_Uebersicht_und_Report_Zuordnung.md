# 00. Übersicht und Zuordnung zum IPMA-Level-D-Report

Diese Datei ordnet jedem Kapitel des PM-Reports (Leitfaden Z01D, Vorlage `PM-Report_LevelD_Overleaf`) die passenden Dokumente, Grafiken und Daten des Repositories zu. Die Richtwerte für den Umfang stammen aus den VORGABE-Kästen der Vorlage. Den genauen Wortlaut der Anforderungen bitte im Leitfaden Z01D prüfen.

## 0.1 Zuordnung Kapitel, Quellen, Grafiken

| Kap. | Thema | Richtwert | Quelle im Repository | Grafik (assets/diagrams) | Daten |
|---|---|---|---|---|---|
| 1 | Management-Zusammenfassung | 1 Seite | 01 (1.9, 1.10), 21.1 | – | – |
| 2 | Strategie, Business Case, Erfolgsfaktoren | 1 | 19 | – | – |
| 3 | Governance, Projektart, Organisationsform | 1,5 | 20, 14 | – | portfolio_uebersicht.csv |
| 4 | Anforderungen und Ziele | 2 | 01 (1.3, 1.5, 1.8, 1.9), 02, 16.1 | – | – |
| 5 | Stakeholder, Umfeld, Schnittstellen | 3 | 15 (15.1–15.3, 15.5), 07 | projektumfeld.png, stakeholder_portfolio.png | – |
| 6 | Macht und Interessen | 1 | 15 (15.4, 15.6) | – | – |
| 7 | Chancen und Risiken | 2 | 06 (6.3–6.8) | risikomatrix.png | risikoregister.csv, chancenregister.csv |
| 8 | Projektdesign | 1,5 | 16 (16.1, 16.2) | – | – |
| 9 | Organisation | 2 | 21 (21.2–21.5), 01.6 | organigramm.png | raci_matrix_p1.xlsx |
| 10 | Ablauf und Termine, Teil 1 (Phasenplan) | 2 | 22, 04.1 | – | terminplan.csv |
| 11 | Leistungsumfang | 2 | 03 (3.1–3.6), 16.3 | psp.png | – |
| 12 | Ablauf und Termine, Teil 2 (Gantt) | 1,5 | 04 (4.5–4.8) | gantt_vernetzt.png | terminplan.csv |
| 13 | Ressourcen | 1,5 | 23 | ressourcen_gantt.png, engpass_montageteam.png | – |
| 14 | Kosten | 1,5 | 24, 05 | kosten_ap63.png, kostenganglinie_projekt.png (optional: kostenkurve.png) | budgetplan.csv |
| 15 | Planung und Steuerung | 1,5 | 25 (zusätzlich 12 als Kontext) | – | – |
| 16 | Kommunikation | 1 | 17 | – | – |
| Anhang | z. B. Lastenheft, RACI, Risikoregister, Change CR-002, Bewertungsmatrix | max. 15 Seiten | 02, 21.4, 06, 10.4, 09 | – | siehe Spalte Daten |

## 0.2 Kennzahlen auf einen Blick

| Kennzahl | Wert |
|---|---|
| Projekt | Erneuerung 380-kV-Leistungsschalterfeld, UW Mitte (fiktiv, abgeschlossen) |
| Laufzeit | 01.10.2025 – 30.09.2026 (365 Kalendertage, 261 Arbeitstage) |
| Abschaltfenster | 01.–10.09.2026 (10 Kalendertage) |
| Budget / Prognose | 1.450.000 EUR / 1.438.000 EUR (−0,8 %) |
| Reserve | 120.000 EUR |
| Ist-Kosten zum Berichtsstand 06/2026 | 733.500 EUR (Plan 870.000 EUR) |
| Interner Aufwand gesamt | ca. 217 PT (Projektleitung 91,4 PT) |
| Aufwand Montageteam im Abschaltfenster | 67 PT von 80 PT Kapazität (84 %) |
| AP 6.3 „Neugerät montieren“ | 27,3 PT (PERT), 38.667 EUR Plan, Stichtag 04.09.2026: 57 % fertig, Prognose 28,5 PT / 39.600 EUR |
| Risikosumme vorher / nachher | 102 / 53 (−48 %) |
| Business Case | Barwertvorteil Neugerät gegenüber Weiterbetrieb ca. 1,45 Mio. EUR (20 Jahre, 4 %) |
| Puffer bis zur Frist | 14 Arbeitstage (M7 10.09.2026, Frist 30.09.2026) |

## 0.3 Hinweise zum Schreiben

- Alle Zahlen sind **fiktive Planungsannahmen**. Im Report sollte das in Kapitel 1 klar stehen (siehe 1.10).
- Der Report soll aus einem Guss sein: dasselbe Arbeitspaket AP 6.3 zieht sich durch Kapitel 11, 13, 14 und 15.
- Die neuen Grafiken müssen in Overleaf in den Ordner `abbildungen/` hochgeladen werden. Dort liegen bisher nur die vier ursprünglichen Grafiken.
- Für Kapitel 9 sind vier Rollen gefordert. Empfehlung: Auftraggeber, Projektleitung, Fachprojektleitung Primärtechnik, Betrieb (siehe 21.3).

## 0.4 Änderungen dieser Überarbeitung (Konsistenz)

| Änderung | Grund |
|---|---|
| Alle Projektdaten um ein Jahr vorverlegt (10/2025 – 09/2026) | Projekt gilt als abgeschlossen, Abgabe des Reports am 03.10.2026 |
| Meilensteine M2, M3, M7 auf Werktage gelegt (28.11.2025, 27.02.2026, 10.09.2026) | Zuvor fielen M2 und M3 auf ein Wochenende |
| M7 Inbetriebnahme von 20.09. auf 10.09.2026 vorgezogen; T-11 und T-12 in das 10-tägige Abschaltfenster gelegt | Prüfung und Inbetriebnahme sollten laut 2, 15.2 und 16.1 im Abschaltfenster liegen |
| Anforderung A-004 präzisiert (Lieferung vor dem Fenster) | Die Lieferung erfolgt bis 31.08.2026 |
| `terminplan.csv` um Vorgänger, Nachfolger, Beziehung, Dauer und Meilenstein erweitert | Vernetzter Terminplan (Kapitel 12) |
| Stakeholder-Quadranten in 15.3 an die Grafik angepasst | Tabelle und Grafik widersprachen sich |
| CR-002: Entscheidungsdatum 20.07.2026 ergänzt | Konsistenz zu Datenstand 13.07.2026 und Statusbericht 06/2026 |
| Doc 14, Portfolio-CSV und Dashboard von unternehmensfremden Begriffen bereinigt; Portfolio-Daten auf Datenstand 13.07.2026 gesetzt | Einheitliche Geschichte des fiktiven ÜNB |
| Risikoregister um Ursachen, Korrekturmaßnahmen, Restwerte und Risiko R-09 erweitert; Chancenregister neu | Kapitel 7 |
| Ressourcen-Gantt um Dokumentation/Qualität ergänzt, Einsatzzeiträume angepasst | Konsistenz zu 5.4 und den neuen Terminen |
| `make_charts.py` schreibt relativ zum Skriptordner und erzeugt alle Grafiken | Vorher fest verdrahteter Pfad |
