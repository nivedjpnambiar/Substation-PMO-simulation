# 24. Aufwandsschätzung und Kostenverlauf

Betrachtet wird das Arbeitspaket **AP 6.3 „Neugerät montieren“** (siehe 16.3). Es liegt im Engpassfenster (Tag 3–6 des Abschaltfensters, 03.–06.09.2026). Ergänzend wird der Kostenverlauf des Gesamtprojekts gezeigt.

## 24.1 Schätzmethode: Dreipunktschätzung (PERT)

Für jede Teilaufgabe werden ein optimistischer (O), ein wahrscheinlichster (M) und ein pessimistischer (P) Aufwand in Personentagen geschätzt.

- Erwartungswert: **E = (O + 4 · M + P) / 6**
- Standardabweichung: **σ = (P − O) / 6**; Gesamt-σ = Wurzel aus der Summe der Einzelvarianzen

Begründung der Methode: Der Aufwand ist unsicher (Ausrichttoleranzen, Adapter nach CR-002, Hubarbeiten), aber aus Erfahrung mit Schaltgerätemontagen gut eingrenzbar. Die Dreipunktschätzung macht die Unsicherheit sichtbar. Die Schätzwerte kommen aus einer Expertenschätzung der Montageleitung und der Fachprojektleitung.

## 24.2 Aufwandsschätzung AP 6.3

| Teilaufgabe | O (PT) | M (PT) | P (PT) | E (PT) | σ (PT) |
|---|---:|---:|---:|---:|---:|
| Anlieferung, Entladung, Transport zum Fundament | 3 | 4 | 6 | 4,17 | 0,50 |
| Heben und Positionieren (Autokran) | 6 | 8 | 12 | 8,33 | 1,00 |
| Mechanische Befestigung (Anker, Adapter) | 5 | 8 | 14 | 8,50 | 1,50 |
| Ausrichten und Toleranzprüfung | 3 | 4 | 7 | 4,33 | 0,67 |
| Montageprotokoll und Freigabe | 1 | 2 | 3 | 2,00 | 0,33 |
| **Summe AP 6.3** | **18** | **26** | **42** | **27,33** | **2,01** (Gesamt) |

- **Erwartungswert: 27,3 PT**, Standardabweichung 2,0 PT.
- Bandbreite ca. 68 % (± 1 σ): 25,3 bis 29,3 PT.
- Bandbreite ca. 95 % (± 2 σ): 23,3 bis 31,4 PT.
- **Kapazitätsprüfung:** 4 Tage × 8 Personen = 32 PT. Der Wert von 95 % (31,4 PT) passt gerade noch in die Kapazität, es bleibt fast kein Puffer.

## 24.3 Kostenschätzung AP 6.3

| Kostenart | Ansatz | Kosten |
|---|---|---:|
| Personal Montageteam | 27,3 PT × 800 EUR (Mischsatz Auftragnehmer) | 21.867 EUR |
| Autokran | 4 Einsatztage × 3.200 EUR | 12.800 EUR |
| Anschlag- und Ausrichtmittel | pauschal | 4.000 EUR |
| **Summe (Erwartungswert)** | | **38.667 EUR** |
| Optimistisch | 18 PT | 31.200 EUR |
| Pessimistisch | 42 PT | 50.400 EUR |

Der Erwartungswert entspricht 18,4 % des Kostenblocks „Demontage und Montage“ (210.000 EUR, siehe 5.1). Der Fundamentadapter aus CR-002 (18.500 EUR) ist nicht enthalten. Er wird über den Change aus der Reserve finanziert.

## 24.4 Kostenganglinie und Kostensummenlinie AP 6.3

Beide Kurven verwenden dasselbe Tagesraster (Tag 3 bis Tag 6).

![Kosten AP 6.3](../assets/diagrams/kosten_ap63.png)

| Tag | Datum | Aufwand (PT) | Personal (EUR) | Autokran (EUR) | Hilfsmittel (EUR) | Kosten je Tag (Ganglinie) | Kumuliert (Summenlinie) |
|---:|---|---:|---:|---:|---:|---:|---:|
| 3 | Do 03.09.2026 | 7,0 | 5.600 | 3.200 | 4.000 | 12.800 | 12.800 |
| 4 | Fr 04.09.2026 | 8,0 | 6.400 | 3.200 | 0 | 9.600 | 22.400 |
| 5 | Sa 05.09.2026 | 7,0 | 5.600 | 3.200 | 0 | 8.800 | 31.200 |
| 6 | So 06.09.2026 | 5,3 | 4.267 | 3.200 | 0 | 7.467 | 38.667 |
| | **Summe** | **27,3** | **21.867** | **12.800** | **4.000** | **38.667** | |

## 24.5 Kostenganglinie und Kostensummenlinie des Projekts

Beide Kurven verwenden dasselbe Monatsraster. Die Kosten folgen dem Zahlungsplan (5.3, 22.5).

![Kosten Projekt](../assets/diagrams/kostenganglinie_projekt.png)

| Monat | Kosten je Monat (Ganglinie) | Kumuliert (Summenlinie) | Zahlungsmeilenstein |
|---|---:|---:|---|
| Okt 2025 | 0 | 0 | – |
| Nov 2025 | 0 | 0 | – |
| Dez 2025 | 0 | 0 | – |
| Jan 2026 | 0 | 0 | – |
| Feb 2026 | 145.000 | 145.000 | M3 Bestellung 10 % |
| Mär 2026 | 0 | 145.000 | – |
| Apr 2026 | 290.000 | 435.000 | M4 Freigabe Engineering 20 % |
| Mai 2026 | 0 | 435.000 | – |
| Jun 2026 | 435.000 | 870.000 | M5 FAT 30 % |
| Jul 2026 | 0 | 870.000 | – |
| Aug 2026 | 290.000 | 1.160.000 | M6 Lieferung 20 % |
| Sep 2026 | 290.000 | 1.450.000 | M7 Inbetriebnahme 15 % (217.500) und M8 Dokumentation 5 % (72.500) |

- Zum Berichtsstand Juni 2026 betragen die Ist-Kosten 733.500 EUR und liegen unter dem Plan von 870.000 EUR (siehe 12 und 18).
- Die Prognose zum Projektende beträgt 1.438.000 EUR, 12.000 EUR unter dem Budget von 1.450.000 EUR.
- Die Meilenstein-Darstellung mit linearer Interpolation steht in 18.1.
