# 5. Budget- und Ressourcenplanung

## 5.1 Budgetbasis

Das genehmigte Zielbudget beträgt **1.450.000 EUR**. Es beinhaltet eine Managementreserve für nicht vollständig quantifizierbare Projektrisiken.

| Kostenblock | Planwert |
|---|---:|
| Engineering | 160.000 EUR |
| Leistungsschalter und Antrieb | 670.000 EUR |
| Sekundärtechnik und Schnittstellen | 120.000 EUR |
| Transport und Logistik | 60.000 EUR |
| Demontage und Montage | 210.000 EUR |
| Prüfungen und Inbetriebnahme | 80.000 EUR |
| Dokumentation und Schulung | 30.000 EUR |
| Reserve | 120.000 EUR |
| **Gesamt** | **1.450.000 EUR** |

## 5.2 Kostensteuerung

- Plan, Ist, Beauftragt und Prognose werden getrennt geführt.
- Abweichungen über 25.000 EUR werden im Monatsbericht erläutert.
- Die Reserve darf nur nach dokumentierter Risikobewertung oder freigegebenem Change Request genutzt werden.
- Scope-Änderungen werden nicht durch stille Budgetverschiebung ausgeglichen.
- Zahlungen werden an überprüfbare Liefer- und Leistungsmeilensteine gekoppelt.

## 5.3 Beispielhafte Zahlungsmeilensteine

| Meilenstein | Anteil |
|---|---:|
| Bestellung und bestätigter Terminplan | 10 % |
| Freigabe Engineering | 20 % |
| Erfolgreicher FAT | 30 % |
| Lieferung auf Baustelle | 20 % |
| Erfolgreiche Inbetriebnahme | 15 % |
| Vollständige Abschlussdokumentation | 5 % |

## 5.4 Ressourcenannahmen

| Rolle | Durchschnittlicher Aufwand |
|---|---:|
| Projektleitung | 0,35 FTE |
| Fachprojektleitung Primärtechnik | 0,30 FTE |
| Schutz-/Leittechnik | 0,15 FTE |
| Einkauf | 0,10 FTE |
| Betrieb | 0,10 FTE |
| Arbeitssicherheit/Umwelt | 0,08 FTE |
| Dokumentation/Qualität | 0,08 FTE |

## 5.5 Kostenstand bei Projektabschluss (30.09.2026)

Quelle: `data/budgetplan.csv` (Spalten `Ist_EUR`, `Prognose_EUR`). Zum Abschluss sind Beauftragt, Ist und Prognose identisch.

| Kostenblock | Plan | Endkosten | Abweichung |
|---|---:|---:|---:|
| Engineering | 160.000 EUR | 158.000 EUR | −2.000 EUR |
| Leistungsschalter und Antrieb | 670.000 EUR | 665.000 EUR | −5.000 EUR |
| Sekundärtechnik und Schnittstellen | 120.000 EUR | 121.000 EUR | +1.000 EUR |
| Transport und Logistik | 60.000 EUR | 59.000 EUR | −1.000 EUR |
| Demontage und Montage | 210.000 EUR | 213.000 EUR | +3.000 EUR |
| Prüfungen und Inbetriebnahme | 80.000 EUR | 79.000 EUR | −1.000 EUR |
| Dokumentation und Schulung | 30.000 EUR | 30.000 EUR | 0 EUR |
| Reserve (verbraucht) | 120.000 EUR | 37.000 EUR | −83.000 EUR |
| **Gesamt** | **1.450.000 EUR** | **1.362.000 EUR** | **−88.000 EUR (−6,1 %)** |

**Verwendung der Reserve (37.000 EUR):**

| Verwendung | Betrag |
|---|---:|
| CR-002 Anpassung Fundamentadapter (Genehmigung 20.07.2026, siehe 10.4) | 18.500 EUR |
| Voruntersuchung und Reparaturkonzept Fundament (Risiko R-04) | 12.000 EUR |
| Sonstige Risikovorsorge (Abschaltfenster R-03, Montagekapazität R-09) | 6.500 EUR |

Die nicht verbrauchten 83.000 EUR der Reserve gehen an den Auftraggeber zurück. Die Toleranz von 5 % (Erfolgskennzahl in 1.5) gilt für Überschreitungen und ist eingehalten.
