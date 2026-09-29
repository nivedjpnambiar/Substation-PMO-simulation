# 15. Projektumfeld, Schnittstellen und Stakeholder-Portfolio

## 15.1 Projektumfeld

Das Projekt bewegt sich in einem Umfeld aus internen/externen und technischen/sozialen Einflussfaktoren. Die folgende Darstellung ordnet die wichtigsten Umfeldfaktoren diesen vier Feldern zu:

![Projektumfeld](../assets/diagrams/projektumfeld.png)

Intern-technische Faktoren (Fachprojektleitung Primärtechnik, Schutz-/Leittechnik) bestimmen, ob die Lösung überhaupt zur Bestandsanlage passt. Intern-soziale Faktoren (Auftraggeber, Betrieb, Einkauf) bestimmen Budget, Freigaben und das Abschaltfenster. Extern-technische Faktoren (Auftragnehmer, Hersteller) liefern die eigentliche Ausrüstung und Montageleistung. Extern-soziale Faktoren (Genehmigungsbehörden, extern geprüfte Arbeitssicherheits-/Umweltauflagen) setzen den regulatorischen Rahmen, auf den das Projekt reagieren, aber den es nicht verändern kann.

## 15.2 Schnittstellen

**Schnittstelle 1 – Technische Schnittstelle zur Sekundär-/Schutztechnik**
- **Partner:** Fachbereich Schutz- und Leittechnik
- **Gegenstand:** Melde-, Steuer- und Schutzsignale zwischen neuem Leistungsschalter und bestehender Schutztechnik (siehe Anforderung A-003).
- **Risiko bei fehlendem Management:** Fehlfunktion oder ungewollte Netzabschaltung bei Inbetriebnahme.
- **Managementmaßnahme:** Frühzeitige Signal- und Schnittstellenliste, gemeinsamer Design Review vor Fertigungsfreigabe (Meilenstein M4), gemeinsamer Funktionstest vor Abnahme.

**Schnittstelle 2 – Organisatorische Schnittstelle zum Betrieb (Abschaltplanung)**
- **Partner:** Betrieb (Anlagenverantwortliche)
- **Gegenstand:** Freigabe und verbindliche Terminierung des 10-tägigen Abschaltfensters, in dem Montage, Prüfung und Inbetriebnahme stattfinden müssen.
- **Risiko bei fehlendem Management:** Verschiebung des Abschaltfensters (Risiko R-03) gefährdet den gesamten kritischen Pfad, da Montage- und Inbetriebnahmeressourcen nur in diesem Fenster verfügbar sind.
- **Managementmaßnahme:** Frühzeitige, schriftlich bestätigte Terminabstimmung mit dem Betrieb (spätestens sechs Monate vorher, siehe 2.5), regelmäßige Statusabstimmung im Lenkungskreis.

**Schnittstelle 3 – Mechanische Schnittstelle zur Bestandsanlage**
- **Partner:** Hersteller / Auftragnehmer
- **Gegenstand:** Fundament- und Anschlussgeometrie zwischen Neugerät und bestehender Stahlbau-/Sammelschienenkonstruktion (siehe Anforderung A-002, Change CR-002).
- **Risiko bei fehlendem Management:** Wie bereits im Change-Beispiel CR-002 eingetreten, führen abweichende Befestigungspunkte zu Mehrkosten und Terminverzug im kritischen Abschaltfenster.
- **Managementmaßnahme:** 3D-Aufmaß vor Detailengineering, Design Review, vorgefertigte Adapterlösung.

## 15.3 Stakeholder-Portfolio (Einfluss vs. Interesse)

![Stakeholder-Portfolio](../assets/diagrams/stakeholder_portfolio.png)

**Achsen und Skala:**

- **Achse Interesse (x):** Wie stark berühren Verlauf und Ergebnis des Projekts die Ziele und die Arbeit des Stakeholders? Diese Größe bestimmt, wie viel Information und Beteiligung er erwartet.
- **Achse Einfluss (y):** Wie stark kann der Stakeholder Freigaben, Budget, Ressourcen oder Termine des Projekts beeinflussen? Diese Größe bestimmt, wie stark sein Verhalten das Projekt verändern kann.
- **Skala:** Mittel = 2, Hoch = 3, Sehr hoch = 4 (Bewertung aus 7.1). „Variabel“ (Behörden) liegt bei 2,5. Die Trennlinie liegt bei 2,8, ab „Hoch“ zählt ein Wert als hoch.
- **Wahl der Achsen:** Einfluss und Interesse sind ohne Umfrage gut beurteilbar und führen direkt zu einer Strategie. Die Macht der Stakeholder wird in 15.6 getrennt und begründet bewertet.

Die Positionierung im Portfolio bestätigt und begründet die in 7.1 gewählten Strategien:

| Position (Interesse / Einfluss) | Stakeholder | Begründung | Strategie |
|---|---|---|---|
| Eng einbinden (hoch / hoch) | Betrieb (4 / 4), Auftraggeber (3 / 4), Primärtechnik (4 / 3), Auftragnehmer (4 / 3), Schutz-/Leittechnik (3 / 3), Arbeitssicherheit (3 / 3) | Sie haben hohes Interesse und hohen Einfluss auf Termin, Technik, Lieferung, Budget oder Sicherheit. Ohne enge Einbindung drohen Verzug oder Fehlanpassungen. | Regelmäßige Abstimmung im Kernteam und Lenkungskreis, Entscheidungsreporting, Reviews, Freigaben vor Baustart |
| Zufriedenstellen (mittel / hoch) | Einkauf (2 / 3), Behörden und externe Stellen (2,5 / 3) | Sie haben hohen Einfluss über Vergabeverfahren bzw. Genehmigungen, aber nur punktuelles Interesse am Projektalltag. | Zum richtigen Zeitpunkt beteiligen (Vergabefahrplan, Genehmigungsbedarf früh klären) |
| Beobachten (mittel / mittel) | Umweltschutz (2 / 2) | Geringer Einfluss und Interesse, aber Auflagen können sich ergeben. | Anforderungen früh prüfen, bei Bedarf einbinden |
| Informiert halten (hoch / gering) | keiner | Kein Stakeholder hat hohes Interesse bei geringem Einfluss. | – |

## 15.4 Macht und Interessen: Machtpromotoren

Zwei Stakeholder wirken im Projekt als **Machtpromotoren**, deren aktive Unterstützung projektentscheidend ist:

- **Auftraggeber:** verfügt über Budgetfreigabe und strategische Entscheidungsgewalt (siehe 1.6/1.7). Seine frühzeitige und sichtbare Unterstützung der Projektziele legitimiert Entscheidungen der Projektleitung gegenüber allen übrigen Stakeholdern.
- **Betrieb:** verfügt faktisch über ein Vetorecht, da ohne die Freigabe des Abschaltfensters keine Montage stattfinden kann. Die frühzeitige, persönliche Einbindung des Betriebs (siehe 17. Kommunikationsmodell) war notwendig, um dieses Machtpotenzial in Unterstützung statt in Blockade umzuwandeln.

Die Strategie der Projektleitung bestand darin, beide Promotoren früh und mit klaren, überprüfbaren Zusagen (Meilensteine, Entscheidungsvorlagen) einzubinden, statt ihre Zustimmung erst bei Bedarf einzuholen.

## 15.5 Interessen, Einfluss und Maßnahmen je Stakeholder

| Stakeholder | Interessen und Erwartungen | Einfluss auf das Projekt | Maßnahmen |
|---|---|---|---|
| Auftraggeber | Ziele im Budget erreichen, fristgerechte Wiederinbetriebnahme, transparente Entscheidungsvorlagen | Budgetfreigabe, Entscheidung über Changes über 10.000 EUR und über den Endtermin | Monatlicher Lenkungskreis, Ampelreporting, frühe Entscheidungsvorlagen |
| Betrieb | Sichere Anlage, kurze Abschaltdauer, Mitsprache bei Terminen | Freigabe des Abschaltfensters, Schaltberechtigung, faktisches Vetorecht | Kernteam-Jour-fixe, persönliche Abstimmung, schriftliche Bestätigung mindestens 6 Monate vorher |
| Fachprojektleitung Primärtechnik | Technische Qualität, prüfbare Lösung, abnahmefähiges Gerät | Technische Freigaben, FAT, Abnahmeprüfungen | Technische Reviews, Design Review, FAT-Readiness-Review |
| Schutz-/Leittechnik | Fehlerfreie Signale ohne Netzrisiko | Freigabe der Sekundärschnittstellen | Frühe Signalliste, gemeinsamer Funktionstest |
| Einkauf | Rechtssichere, wirtschaftliche Vergabe, verlässlicher Fahrplan | Vergabeverfahren und Vertragsgestaltung | Vergabefahrplan abstimmen, wöchentlicher Austausch in Phase 3 |
| Arbeitssicherheit | Keine Unfälle, konforme Baustelle | Freigabe vor Baustart, Stop-Work-Recht | Sicherheitskonzept vor Baustart, Unterweisung, Kontrollen |
| Umweltschutz | SF6-Handhabung, Entsorgung des Altgeräts, Auflagen | Auflagen, Freigabe des Umweltkonzepts | Anforderungen früh prüfen, Nachweise einfordern |
| Auftragnehmer | Auftrag ausführen, klare Leistungsgrenzen, pünktliche Zahlung, wenig Störungen | Lieferung, Montage, Termin und Qualität der Ausführung | Klare Leistungsgrenzen (2.4), Jour fixe, Eskalationswege, Zahlungsmeilensteine |
| Behörden und externe Stellen | Rechtskonforme Ausführung, vollständige Nachweise | Genehmigungen und Auflagen | Genehmigungsbedarf früh klären, Ansprechpartner benennen |

## 15.6 Bewertung der Macht der Stakeholder

Skala: 1 = kann das Projekt kaum beeinflussen, 5 = kann das Projekt stoppen oder grundlegend verändern.

| Stakeholder | Machtbasis | Macht | Begründung | Promotorenrolle |
|---|---|---:|---|---|
| Auftraggeber | Legitimation und Ressourcen | 5 | Entscheidet über Budget, Ziele und Changes über 10.000 EUR | Machtpromotor |
| Betrieb | Veto | 5 | Ohne Freigabe des Abschaltfensters und Schaltberechtigung gibt es keine Montage | Machtpromotor |
| Auftragnehmer | Ressourcen und Information | 4 | Kontrolliert Lieferung, Montagekapazität und Ausführungsqualität | – |
| Fachprojektleitung Primärtechnik | Expertise | 4 | Erteilt technische Freigaben, führt Prüfungen und Abnahme durch | Fachpromotor |
| Arbeitssicherheit | Veto in Sicherheitsfragen | 4 | Kann jederzeit die Arbeiten stoppen (Stop-Work) und gibt vor Baustart frei | – |
| Behörden und externe Stellen | Legitimation (extern) | 4 | Genehmigungen und Auflagen lassen sich nicht beeinflussen | – |
| Schutz-/Leittechnik | Expertise | 3 | Gibt Sekundärschnittstellen frei, Fehler wirken erst bei Inbetriebnahme | Fachpromotor |
| Einkauf | Verfahren | 3 | Steuert Vergabeverfahren und Vertragsgestaltung | Prozesspromotor |
| Umweltschutz | Auflagen | 2 | Auflagen wirken situativ | – |
