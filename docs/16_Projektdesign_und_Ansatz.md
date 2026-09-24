# 16. Projektdesign, Vorgehensansatz und Arbeitspaket im Detail

## 16.1 Erfolgskriterien aus Sicht des Auftraggebers (magisches Dreieck)

Die Erfolgskriterien aus 1.5 werden hier nach Leistungsumfang, Termin und Kosten priorisiert, um Zielkonflikte transparent zu machen:

| Priorität | Dimension | Kriterium | Begründung der Priorisierung |
|---|---|---|---|
| 1 (höchste) | Leistungsumfang/Qualität | 0 offene A-Mängel bei Inbetriebnahme, 0 Arbeitsunfälle | Sicherheits- und Funktionsfähigkeit der Anlage sind nicht verhandelbar; ein sicherheitskritischer Mangel gefährdet Personal und Netzstabilität. |
| 2 | Termin | Wiederinbetriebnahme innerhalb des 10-tägigen Abschaltfensters (≤10 AT Abweichung) | Das Abschaltfenster ist extern durch den Netzbetrieb vorgegeben und nicht kurzfristig verschiebbar (siehe Schnittstelle 2, R-03). |
| 3 (niedrigste) | Kosten | ≤5 % Abweichung vom genehmigten Budget | Kosten sind wichtig, aber im Konfliktfall nachrangig gegenüber Sicherheit und Termin – zusätzliche, dokumentierte Kosten (z. B. CR-002) werden akzeptiert, wenn sie Sicherheit oder Termin absichern. |

**Zielkonflikt und Auflösung:** Der Change CR-002 (Fundamentadapter, 10.3/10.4) zeigt diesen Konflikt exemplarisch: eine Kostenüberschreitung von 18.500 EUR wurde zugunsten der Termin- und Sicherheitsziele akzeptiert, weil ein Montageverzug im kritischen Abschaltfenster ungleich teurer und riskanter gewesen wäre als der Mehraufwand für die Adapterkonstruktion.

## 16.2 Gewählter Vorgehensansatz

Für dieses Projekt wurde ein **klassisches, plangetriebenes Vorgehen** gewählt (kein hybrider oder agiler Anteil). Begründung:

- Das Projekt liefert ein physisches, sicherheitsrelevantes Anlagenteil (380-kV-Leistungsschalter) mit hohem regulatorischem und normativem Rahmen (Arbeitssicherheit, Netzbetrieb) – die Anforderungen sind zu Projektbeginn weitgehend stabil und eindeutig spezifizierbar (siehe 2.1).
- Der Ablauf ist durch verbindliche Qualitäts-Gates strukturiert (FAT, SAT, Abnahme, siehe 11.1), die sequenziell und nicht iterativ durchlaufen werden müssen.
- Das Abschaltfenster ist ein fixer, extern gesetzter Termin ohne Möglichkeit inkrementeller Lieferung „in Produktion" – ein iteratives Vorgehen mit mehreren Feedback-Zyklen am realen Objekt ist technisch nicht möglich.
- Ein rein agiles Vorgehen nach Scrum Guide scheidet daher aus; es gibt keinen sinnvollen Produktinkrement-Rhythmus für den Austausch eines einzelnen Leistungsschalters.

Die Strukturierung erfolgt stattdessen über einen klassischen Projektstrukturplan mit Arbeitspaketen (siehe 3.1) und einer expliziten Definition of Done je Arbeitspaket (3.2).

## 16.3 Vollständig ausgearbeitetes Arbeitspaket: „Neugerät montieren" (AP 6.3)

Um die Anwendung der Definition of Done (3.2) konkret zu zeigen, wird das Arbeitspaket mit dem höchsten Termin- und Sicherheitsrisiko vollständig ausgearbeitet – es liegt exakt im Engpassfenster der Ressourcenplanung (siehe 18.2).

| Feld | Inhalt |
|---|---|
| **AP-ID** | 6.3 |
| **Bezeichnung** | Neugerät montieren |
| **Übergeordnete Phase** | 6. Montage und Inbetriebnahme |
| **Verantwortlich** | Auftragnehmer (Montageleitung), Freigabe durch Fachprojektleitung Primärtechnik |
| **Zeitraum** | innerhalb des 10-tägigen Abschaltfensters, Tag 3–6 (nach Demontage Altgerät, vor Anschlussarbeiten) |
| **Vorgänger** | 6.1 Altgerät demontieren, 6.2 Fundament und Anschlüsse anpassen |
| **Nachfolger** | 6.4 Primär- und Sekundäranschlüsse herstellen |
| **Eingaben** | freigegebene Montageanweisung, geprüftes Fundament (6.2 abgeschlossen), FAT-freigegebenes Gerät, Sicherheits-/Montagekonzept freigegeben (A-006) |
| **Tätigkeiten** | Anlieferung auf Baustelle, Hebe- und Positionierarbeiten, mechanische Befestigung, Ausrichtung nach Herstellervorgabe |
| **Ergebnis** | mechanisch montierter, ausgerichteter Leistungsschalter, bereit für Anschlussarbeiten |
| **Aufwand/Kosten** | Teil des Kostenblocks „Demontage und Montage" (210.000 EUR, siehe 5.1) |

**Akzeptanzkriterien:**
1. Der Leistungsschalter ist gemäß Herstellervorgabe positioniert und ausgerichtet (Toleranzprüfung dokumentiert).
2. Alle Befestigungspunkte entsprechen der freigegebenen (ggf. per CR-002 angepassten) Fundament-/Adapterkonstruktion.
3. Die mechanische Montagekontrolle (siehe Prüfplan 11.2) wurde durch die Montageleitung durchgeführt und von der Fachprojektleitung freigegeben.
4. Keine offenen A-Mängel; B-Mängel sind terminiert und dokumentiert (Mängelklassen gemäß 11.3).
5. Der Montagefortschritt ist im Terminplan als abgeschlossen erfasst und wirkt sich nicht negativ auf den kritischen Pfad aus.

**Definition of Done (instanziiert aus 3.2):**
- [x] alle vereinbarten Ergebnisse liegen vor (montiertes, ausgerichtetes Gerät),
- [x] der verantwortliche Prüfer (Fachprojektleitung) hat die Ergebnisse freigegeben,
- [x] offene Punkte (z. B. kleinere B-Mängel) sind dokumentiert und terminiert,
- [x] Montageprotokoll und Prüfchecklisten sind versioniert abgelegt,
- [x] Termin- und Kostenauswirkungen (z. B. aus CR-002) sind im Statusbericht berücksichtigt.

Erst wenn alle Kriterien erfüllt sind, gilt AP 6.3 als abgeschlossen und AP 6.4 (Anschlussarbeiten) kann beginnen – im Abschaltfenster ist dafür keine Pufferzeit vorgesehen, weshalb dieses Arbeitspaket besonders eng gesteuert wird (siehe 4.3 Terminsteuerung).
