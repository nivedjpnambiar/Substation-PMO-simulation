# 20. Governance, Projektart und Organisationsform

## 20.1 Das Vorhaben als Projekt (Projektmerkmale nach DIN 69901-5)

| Merkmal | Ausprägung im Projekt | Nachweis |
|---|---|---|
| Einmaligkeit der Bedingungen | Einmaliger Austausch eines 380-kV-Leistungsschalters im Umspannwerk „UW Mitte“ unter den Randbedingungen der Bestandsanlage und eines fest vorgegebenen Abschaltfensters | 1.2, 2 |
| Zielvorgabe | Fünf Projektziele mit messbaren Kennzahlen, priorisiert nach Muss / Soll / Kann | 1.3, 1.5, 1.8 |
| Zeitliche Begrenzung | 01.10.2025 bis 30.09.2026, Abschaltfenster 01.–10.09.2026 | 4.1 |
| Finanzielle Begrenzung | Zielbudget 1.450.000 EUR, zulässige Prognoseabweichung 5 % | 5.1 |
| Personelle und sachliche Begrenzung | Rollen mit 0,08 bis 0,35 FTE, Montageteam mit 8 Personen im Abschaltfenster | 23 |
| Abgrenzung gegenüber anderen Vorhaben | Nicht-Ziele (kein Umbau der Anlage, keine Änderung des Schutzkonzepts) | 1.4 |
| Projektspezifische Organisation | Lenkungskreis, Projektleitung, Kernteam, Auftragnehmer | 21 |
| Komplexität und Risiko | Schnittstellen zur Schutztechnik, externer Generalunternehmer, Sicherheitsrelevanz, Risiken R-01 bis R-09 | 6 |

Das Vorhaben ist ein Projekt und keine Linienaufgabe, weil es einmalig, zeitlich und finanziell begrenzt ist und eine eigene Organisation hat.

## 20.2 Projektart und Klassifizierung

| Kriterium | Einordnung | Begründung |
|---|---|---|
| Projektart | Investitionsprojekt (technisch, Anlagenerneuerung) | Ersatz eines Anlagenteils am Ende der Nutzungsdauer, aktivierbare Investition |
| Kunde | Interner Kunde: Fachbereich Anlagenmanagement des fiktiven ÜNB | Projektleitung und Auftraggeber gehören zum selben Unternehmen |
| Größe | Mittleres Projekt | 1,45 Mio. EUR Budget, 12 Monate Laufzeit, rund 217 PT interner Aufwand |
| Komplexität | Mittel | Wenige, aber kritische Schnittstellen; Anforderungen zu Beginn weitgehend stabil |
| Ausführung | Fremdvergabe an einen Generalunternehmer | Ausschreibung und Vergabe, siehe 8 und 9 |
| Vorgehensmodell | Klassisch, plangetrieben | Begründung in 16.2 |

## 20.3 Organisationsform: ausgewogene Matrix

| Kriterium | Ausprägung im Projekt | Tendenz |
|---|---|---|
| Weisungsbefugnis der Projektleitung | Fachlich-laterale Führung des Kernteams, keine disziplinarische Führung | schwach bis ausgewogen |
| Budget- und Terminverantwortung | Projektleitung verantwortet Termin, Kosten und Ergebnis; Reserve bis 10.000 EUR je Change (1.7) | ausgewogen bis stark |
| Personalausstattung | Teilzeit aus den Fachbereichen (0,08 bis 0,35 FTE), keine eigenen Vollzeitkräfte | schwach bis ausgewogen |
| Entscheidungsrechte | Geteilt: Projektleitung, Fachprojektleitung, Betrieb, Arbeitssicherheit, Auftraggeber (1.7, RACI) | ausgewogen |
| Fachliche Hoheit | Bleibt in der Linie (Betrieb, Einkauf, Arbeitssicherheit, Primärtechnik) | ausgewogen |

**Ergebnis:** Das Projekt läuft als **ausgewogene Matrixorganisation**.

- Gegen eine Stabslinienorganisation spricht, dass die Projektleitung Termin, Kosten und Ergebnis verantworten muss und dafür mehr als koordinieren können muss.
- Gegen eine starke Matrix oder reine Projektorganisation spricht, dass das Projekt mit 1,45 Mio. EUR zu klein ist. Betrieb und Arbeitssicherheit müssen in der Linie bleiben, weil dort die Anlagen- und Sicherheitsverantwortung liegt.
- Typisches Konfliktfeld der Matrix sind konkurrierende Prioritäten zwischen Projekt und Linie. Das Projekt begegnet dem durch Eskalation an den Lenkungskreis und durch das Ressourcenmanagement des Portfolios (siehe 14, Ressourcenkonflikt Fachprojektleitung Technik im Juli 2026).

## 20.4 PMO-, Portfolio- und Programmkontext

**PMO des ÜNB (fiktiv):**
- stellt Standards und Vorlagen bereit (Statusbericht, Change Request, Sitzungsprotokoll; siehe `templates/`),
- gibt die Methodik der Risikobewertung vor (6.1),
- führt das Portfolio und bereitet die Priorisierung für das Steering Board vor (14).

**Portfolio „Anlagenerneuerung und Prozessverbesserung“:** Das Projekt ist P1 von fünf Projekten mit 2,155 Mio. EUR Gesamtbudget. Bewertung nach der Formel aus 14 (Nutzen × 0,4 + Dringlichkeit × 0,3 + (6 − Risiko) × 0,3):

| ID | Projekt | Nutzen | Risiko | Dringlichkeit | Priorität | Budget |
|---|---|---:|---:|---:|---:|---:|
| P2 | Einheitliches PM-Reporting für interne Projekte | 5 | 2 | 5 | 4,7 | 180.000 EUR |
| P1 | 380-kV-Leistungsschalterfeld UW Mitte | 4 | 4 | 4 | 3,4 | 1.450.000 EUR |
| P4 | Digitalisierung Ersatzteillager-Verwaltung | 4 | 3 | 3 | 3,4 | 310.000 EUR |
| P3 | Standardisierung Inbetriebnahme-Checklisten | 3 | 2 | 3 | 3,3 | 95.000 EUR |
| P5 | Automatisierung Angebotsprüfung Instandhaltung | 3 | 3 | 2 | 2,7 | 120.000 EUR |

P1 liegt gemeinsam mit P4 auf Rang 2. Grund ist der hohe Nutzen und die Dringlichkeit bei gleichzeitig hohem Risiko.

**Programmkontext:** P1 ist ein Einzelprojekt und gehört zu keinem Programm. Es gibt eine fachliche Schnittstelle zu P3 (Standardisierung der Inbetriebnahme-Checklisten): Praxiserfahrungen aus den Prüfungen in AP 6.5 und 6.6 fließen in P3 zurück (siehe Chance C-01 in 6.8).

## 20.5 Gremien, Entscheidungswege und Eskalation

| Gremium | Teilnehmer | Rhythmus | Entscheidungen |
|---|---|---|---|
| Lenkungskreis | Auftraggeber, Projektleitung | monatlich | Budget und Termin, Changes über 10.000 EUR oder mit Endterminwirkung, Eskalationen |
| Projekt-Kernteam | Projektleitung, Fachprojektleitung, Betrieb, Einkauf | zweiwöchentlich | Termine, Risiken, Maßnahmen, technische Klarstellungen |
| Auftragnehmer-Jour-fixe | Projektleitung, Fachprojektleitung, Auftragnehmer | zweiwöchentlich | Engineering, Fertigung, offene Punkte |
| Baustellen-Stand-up | Baustellenteam | täglich im Abschaltfenster | Sicherheit, Tagesplan, Behinderungen |

**Eskalationsstufen:**

| Stufe | Auslöser | Entscheider |
|---|---|---|
| 1 | Change bis 10.000 EUR innerhalb der Reserve; Prognoseverzug bis 5 Arbeitstage | Projektleitung |
| 2 | Change über 10.000 EUR; Prognoseverzug über 5 Arbeitstage; Endterminwirkung | Auftraggeber im Lenkungskreis |
| Sonderfall | Sicherheitskritische Sachverhalte | Arbeitssicherheit bzw. Anlagenverantwortlicher, sofort (Stop-Work) |

Die Meilensteine M1 bis M8 dienen als Freigabepunkte (Quality Gates), siehe 4.1 und 11.1.
