# 19. Strategie, Business Case und kritische Erfolgsfaktoren

> Alle Zahlen dieses Kapitels sind **fiktive Planungsannahmen** des Simulationsprojekts. Sie beruhen nicht auf Daten einer realen Anlage.

## 19.1 Strategischer Bezug und Ausgangslage

- Der Auftraggeber (fiktiver Übertragungsnetzbetreiber, ÜNB) verfolgt eine Asset-Strategie „Erneuerung vor Ausfall“ für kritische Primärtechnik im 380-kV-Netz.
- Der Leistungsschalter im Feld von „UW Mitte“ hat das Ende seiner vorgesehenen Nutzungsdauer erreicht (siehe 1.2). Ersatzteile sind nur eingeschränkt verfügbar, der Wartungsaufwand steigt.
- Ein Ausfall des Schalters würde das Schaltfeld ungeplant außer Betrieb setzen. Folgen wären Eilreparatur, Netzengpassmanagement und ein Risiko für die Versorgungssicherheit.
- Das Projekt dient dem strategischen Ziel „hohe Anlagenverfügbarkeit bei beherrschbaren Instandhaltungskosten“ und ist im Portfolio des ÜNB als Projekt P1 eingeordnet (siehe 14 und 20.4).

## 19.2 Handlungsoptionen

| Option | Beschreibung | Bewertung |
|---|---|---|
| A – Weiterbetrieb (Nullvariante) | Altgerät bleibt in Betrieb, Instandhaltung und Ersatzteilbeschaffung wie bisher | Keine Investition, aber steigende Instandhaltungskosten und hohes Ausfallrisiko |
| B – Revision / Retrofit | Generalüberholung des Altgeräts (ca. 600.000 EUR), Restnutzung ca. 10 Jahre | Ersatzteilproblem bleibt, Ersatz in Jahr 10 trotzdem nötig |
| **C – Ersatz durch Neugerät (gewählt)** | Neugerät inkl. Antrieb, Sekundärschnittstellen und Dokumentation (1.450.000 EUR Budget) | Niedrigste Gesamtkosten über 20 Jahre, Risiko deutlich reduziert |

## 19.3 Wirtschaftlichkeit (Barwertvergleich der Kosten)

**Annahmen (fiktiv):**

| Annahme | Wert |
|---|---|
| Betrachtungszeitraum | 20 Jahre |
| Kalkulationszins | 4,0 % p. a. |
| Instandhaltung Altgerät | 90.000 EUR im ersten Jahr, steigend um 4 % p. a. |
| Instandhaltung Neugerät | 20.000 EUR p. a. |
| Ausfallwahrscheinlichkeit Altgerät / Retrofit / Neugerät | 4,0 % / 2,0 % / 0,5 % p. a. |
| Schadenshöhe je Ausfall (Eilreparatur, Netzengpassmanagement, Versorgungsunterbrechung) | 3.000.000 EUR |
| Investition Option C | 1.438.000 EUR (Prognose Projektende, siehe 5) |

**Ergebnis (Barwert der Kosten über 20 Jahre):**

| Kostenart | A – Weiterbetrieb | B – Retrofit | C – Neugerät |
|---|---:|---:|---:|
| Investition | 0 EUR | 600.000 EUR | 1.438.000 EUR |
| Instandhaltung | 1.730.769 EUR | – | 271.807 EUR |
| Erwartete Ausfallkosten | 1.630.839 EUR | – | 203.855 EUR |
| Betrieb Jahre 1–10 (Instandhaltung und Ausfallrisiko) | – | 973.307 EUR | – |
| Ersatz in Jahr 10 (abgezinst) | – | 971.461 EUR | – |
| Betrieb Jahre 11–20 (Neugerät) | – | 191.780 EUR | – |
| **Summe Barwert** | **3.361.608 EUR** | **2.736.549 EUR** | **1.913.661 EUR** |

- Vorteil Option C gegenüber A: **1.447.947 EUR** (Barwert der vermiedenen Kosten).
- Vorteil Option C gegenüber B: **822.887 EUR**.
- Statische Amortisation gegenüber A: jährliche Einsparung im ersten Jahr = 70.000 EUR (Instandhaltung) + 105.000 EUR (Ausfallrisiko) = 175.000 EUR. Damit ergibt sich 8,2 Jahre. Der Wert ist konservativ, weil die Instandhaltungskosten des Altgeräts weiter steigen.
- Nicht monetärer Nutzen: bessere Ersatzteilverfügbarkeit, Zustandsüberwachung des Antriebs (siehe CR-001), digitale Dokumentation, geringere Sicherheitsrisiken bei Wartungsarbeiten.

**Entscheidung:** Option C wurde mit dem Projektauftrag (M1, 15.10.2025) durch den Auftraggeber freigegeben.

## 19.4 Kritische Erfolgsfaktoren (KEF)

Erfolgskriterien (Ziele, siehe 1.5 und 1.8) beschreiben *was* erreicht werden soll. Erfolgsfaktoren beschreiben die *Voraussetzungen*, ohne die das nicht gelingt.

| Nr. | Kritischer Erfolgsfaktor | Warum kritisch | Frühindikator / Messgröße | Bezug |
|---|---|---|---|---|
| KEF-1 | Verbindliche Freigabe und Einhaltung des Abschaltfensters durch den Betrieb | Ohne spannungsfreie Anlage ist keine Montage möglich; das Fenster ist extern gesetzt | Schriftliche Bestätigung mindestens 6 Monate vor Fensterbeginn | R-03, Ziel 1, 15.4 |
| KEF-2 | Termingerechte Fertigung und bestandener FAT | Das Neugerät muss vor Fensterbeginn auf der Baustelle sein | Fortschrittsreviews alle 2 Wochen, FAT ohne kritische Abweichung (M5) | R-01, R-08 |
| KEF-3 | Passgenaue mechanische und elektrische Schnittstellen | Abweichungen werden erst im Abschaltfenster sichtbar und sind dort am teuersten | 3D-Aufmaß, freigegebene Signalliste, Design Review (M4) | R-02, CR-002 |
| KEF-4 | Arbeitssicherheit im Abschaltfenster | Personenschaden hat Vorrang vor Termin und Kosten | 0 Arbeitsunfälle, Sicherheitskonzept vor Baustart freigegeben (A-006) | R-06, Ziel 4 |
| KEF-5 | Klare Zuständigkeiten und Änderungsdisziplin | Scope-Änderungen ohne Freigabe gefährden Budget und Termin | 0 nicht genehmigte Scope-Änderungen, RACI gültig (A-007) | 10, 21 |
| KEF-6 | Frühe, belastbare Einbindung von Auftraggeber und Betrieb (Machtpromotoren) | Beide entscheiden über Budget bzw. Zugang zur Anlage | Teilnahme am Kernteam-Jour-fixe und Lenkungskreis, Entscheidungen fristgerecht | 15.4, 17 |
