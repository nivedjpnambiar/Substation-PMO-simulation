# 3. Projektstrukturplan

## 3.1 Arbeitspakete

### 1. Projektinitiierung
- 1.1 Projektauftrag erstellen
- 1.2 Stakeholder identifizieren
- 1.3 Budgetrahmen bestätigen
- 1.4 Projektorganisation festlegen

### 2. Bestandsaufnahme und Anforderungen
- 2.1 Technische Bestandsaufnahme
- 2.2 Schnittstellen erfassen
- 2.3 Anforderungen abstimmen
- 2.4 Lastenheft freigeben

### 3. Ausschreibung und Vergabe
- 3.1 Vergabeunterlagen erstellen
- 3.2 Bieterfragen koordinieren
- 3.3 Angebote technisch bewerten
- 3.4 Kaufmännische Bewertung unterstützen
- 3.5 Vergabeempfehlung und Bestellung

### 4. Engineering und Fertigung
- 4.1 Kick-off mit Auftragnehmer
- 4.2 Dokumenten- und Schnittstellenprüfung
- 4.3 Design Review
- 4.4 Fertigung
- 4.5 Factory Acceptance Test

### 5. Baustellenvorbereitung
- 5.1 Montage- und Logistikkonzept
- 5.2 Sicherheits- und Umweltplanung
- 5.3 Abschalt- und Schaltplanung
- 5.4 Baustelleneinrichtung
- 5.5 Material- und Dokumentenfreigabe

### 6. Montage und Inbetriebnahme
- 6.1 Altgerät demontieren
- 6.2 Fundament und Anschlüsse anpassen
- 6.3 Neugerät montieren
- 6.4 Primär- und Sekundäranschlüsse herstellen
- 6.5 Prüfungen durchführen
- 6.6 Funktionsprüfung und Inbetriebnahme

### 7. Projektabschluss
- 7.1 Mängel bearbeiten
- 7.2 Revisionsunterlagen prüfen
- 7.3 Abnahme und Übergabe
- 7.4 Kostenabschluss
- 7.5 Lessons Learned

### 8. Projektmanagement (Querschnitt, phasenübergreifend)
- 8.1 Projektsteuerung und Reporting
- 8.2 Risiko- und Änderungsmanagement
- 8.3 Stakeholder- und Kommunikationsmanagement

## 3.2 Definition of Done für Arbeitspakete

Ein Arbeitspaket ist abgeschlossen, wenn:

- alle vereinbarten Ergebnisse vorliegen,
- der verantwortliche Prüfer die Ergebnisse freigegeben hat,
- offene Punkte dokumentiert und terminiert sind,
- relevante Unterlagen versioniert abgelegt wurden,
- Termin- und Kostenauswirkungen im Reporting berücksichtigt sind.

## 3.3 Projektstrukturplan (Grafik)

![Projektstrukturplan](../assets/diagrams/psp.png)

**Kodierung:** Ebene 0 = Projekt, Ebene 1 = Phase (Code 1 bis 8), Ebene 2 = Arbeitspaket (Code x.y). AP 6.3 „Neugerät montieren“ ist als Arbeitspaket mit Akzeptanzkriterien und Definition of Done ausgearbeitet (siehe 16.3).

## 3.4 Begründung der Gliederung

- **Phasenorientiert:** Das Projekt läuft klassisch und plangetrieben (16.2). Die Phasen 1 bis 7 entsprechen den Meilensteinen M1 bis M8 und den Quality Gates (FAT, SAT, Abnahme).
- **Verantwortungsklar:** Die Phasen 1 bis 3, 5 und 7 liegen überwiegend beim Auftraggeber, die Phasen 4 und 6 überwiegend beim Auftragnehmer. Das entspricht der Abgrenzung in 2.4 und der RACI-Matrix (21.4).
- **Zahlungs- und kostenfähig:** Jede Phase endet mit einem prüfbaren Ergebnis, an das Zahlungsmeilensteine gekoppelt sind (5.3, 22).
- **Steuerbar:** Zwei Ebenen unterhalb des Projekts halten den Plan übersichtlich. Die Arbeitspakete haben klare Ergebnisse, Verantwortliche und Termine.
- **Vollständig (100-%-Regel):** Der Liefer- und Leistungsumfang aus 2.3 ist vollständig abgedeckt (siehe 3.5). Phase 8 erfasst die Managementleistungen.

## 3.5 Abdeckung des Liefer- und Leistungsumfangs

| Nr. (2.3) | Leistung | Arbeitspakete |
|---|---|---|
| 1 | Engineering und Detailplanung | 4.1, 4.2, 4.3 |
| 2 | Herstellung und Lieferung des Leistungsschalters | 4.4, 4.5, 5.5 |
| 3 | Antriebsschrank und Nebenkomponenten | 4.4 |
| 4 | Transport, Entladung, Baustellenlogistik | 5.1, 5.4, 6.3 |
| 5 | Demontage des Altgeräts | 6.1 |
| 6 | Montage und Anschluss des Neugeräts | 6.2, 6.3, 6.4 |
| 7 | Mechanische, elektrische und funktionale Prüfungen | 4.5, 6.5 |
| 8 | Unterstützung bei der Inbetriebnahme | 6.6 |
| 9 | Schulung und Dokumentation | 7.2, 7.3 |
| 10 | Mängelbeseitigung und Abschlussunterlagen | 7.1, 7.2 |

## 3.6 Zuordnung der Kostenblöcke zum PSP

| Kostenblock (5.1) | Planwert | Arbeitspakete |
|---|---:|---|
| Engineering | 160.000 EUR | 4.1, 4.2, 4.3 |
| Leistungsschalter und Antrieb | 670.000 EUR | 4.4, 4.5, 5.5 |
| Sekundärtechnik und Schnittstellen | 120.000 EUR | 4.2, 6.4 |
| Transport und Logistik | 60.000 EUR | 5.1, 5.4 |
| Demontage und Montage | 210.000 EUR | 6.1, 6.2, 6.3, 6.4 |
| Prüfungen und Inbetriebnahme | 80.000 EUR | 4.5, 6.5, 6.6 |
| Dokumentation und Schulung | 30.000 EUR | 7.2, 7.3 |
| Reserve | 120.000 EUR | 8.2 (Risiko- und Änderungsmanagement) |
