# 21. Projektorganisation, eigene Position und Kommunikationsmatrix

## 21.1 Eigene Position im Projekt

| Merkmal | Ausprägung |
|---|---|
| Rolle | **Projektleiter** (Projektleitung, Auftraggeberseite) |
| Einsatz | ca. 0,35 FTE über die gesamte Laufzeit (01.10.2025 bis 30.09.2026), parallel zur Linienaufgabe |
| Berichtsweg | An den Auftraggeber, im monatlichen Lenkungskreis |
| Führung | Fachlich-laterale Führung des Kernteams, keine disziplinarische Führung |
| Schnittstelle zum Auftragnehmer | Jour fixe, Leistungsgrenzen, offene Punkte, Eskalation |

**Verantwortung:** Gesamtsteuerung von Terminen, Kosten und Risiken, Reporting, Stakeholder- und Schnittstellenmanagement, Änderungsmanagement.

**Entscheidungsbefugnis:**
- Changes bis 10.000 EUR innerhalb der Reserve entscheidet die Projektleitung.
- Changes über 10.000 EUR oder mit Wirkung auf den Endtermin entscheidet der Auftraggeber.
- Technische Abweichungen entscheiden Fachprojektleitung und Betrieb.
- Sicherheitskritische Entscheidungen treffen Arbeitssicherheit bzw. Anlagenverantwortlicher.

**Aufgaben je Phase (RACI-Rolle der Projektleitung):**

| Phase | Aufgaben der Projektleitung |
|---|---|
| 1 Initiierung | Projektauftrag erstellen (R), Stakeholder identifizieren, Organisation festlegen |
| 2 Bestandsaufnahme | Lastenheft verantworten (A), Betrieb früh einbinden |
| 3 Vergabe | Technische Angebotsbewertung verantworten (A), Vergabeentscheidung vorbereiten (R) |
| 4 Engineering, Fertigung | Detailengineering und FAT verantworten (A), Fortschrittsreviews, Change Management |
| 5 Vorbereitung | Abschaltfenster mit Betrieb absichern, Sicherheits- und Montagekonzept freigeben lassen |
| 6 Montage, Inbetriebnahme | Montage und Inbetriebnahme verantworten (A), tägliches Stand-up, Eskalationen |
| 7 Abschluss | Abnahme vorbereiten (R), Kostenabschluss, Lessons Learned |

## 21.2 Projektorganisation

![Organigramm](../assets/diagrams/organigramm.png)

**Begründung der Organisation (siehe 20.3):**
- Der Auftraggeber entscheidet über Budget und Ziele und ist über den Lenkungskreis eingebunden.
- Die Projektleitung steuert das Projekt zentral. Das begrenzt die Berichtswege auf zwei Ebenen (Auftraggeber, Projektleitung).
- Das Kernteam bündelt die Fach- und Linienfunktionen, die für Anforderungen, Vergabe, Sicherheit und Betrieb zuständig sind. Die fachliche Führung bleibt in der Linie (Matrix).
- Der Auftragnehmer (Generalunternehmer) ist über den Vertrag und den Jour fixe angebunden. Das PMO wirkt als Stab.

## 21.3 Projektrollen mit Aufgaben, Kompetenzen und Verantwortung

| Rolle | Aufgaben | Kompetenzen (Entscheidungsbefugnis) | Verantwortung |
|---|---|---|---|
| **Auftraggeber** | Ziele und Budget vorgeben, Projektauftrag freigeben, Vergabe entscheiden, Abnahme erteilen | Budgetfreigabe, Changes über 10.000 EUR oder mit Endterminwirkung, Vergabeentscheidung | Wirtschaftlicher Projekterfolg, strategische Entscheidungen |
| **Projektleitung** | Termine, Kosten, Risiken, Reporting, Changes, Stakeholder- und Schnittstellenmanagement | Changes bis 10.000 EUR innerhalb der Reserve, Eskalation, Steuerung des Kernteams | Erreichen der Projektziele in Zeit, Kosten und Ergebnis |
| **Fachprojektleitung Primärtechnik** | Technische Spezifikation, technische Bewertung, Reviews, FAT und Abnahmeprüfungen | Technische Klarstellungen, technische Freigabe von Arbeitspaketen | Technische Richtigkeit und Prüfbarkeit der Lösung |
| **Betrieb (Anlagenverantwortung)** | Abschaltplanung, Schaltberechtigung, Betriebsfreigabe, Wiederinbetriebnahme | Freigabe und Verschiebung des Abschaltfensters, technische Abweichungen (gemeinsam mit Fachprojektleitung) | Sicherer Anlagenbetrieb und Netzverfügbarkeit |
| Schutz- und Leittechnik | Signallisten, Schnittstellen, Funktionsprüfung | Freigabe der Sekundärschnittstellen | Funktion der Schutz- und Leittechnik |
| Einkauf | Ausschreibung, kaufmännische Bewertung, Bestellung | Vergabeverfahren und Vertragsgestaltung im Rahmen der Freigabe | Rechtssichere, wirtschaftliche Vergabe |
| Arbeitssicherheit / Umweltschutz | Sicherheits- und Umweltkonzept, Baustellenkontrollen | Freigabe vor Baustart, Stop-Work-Recht | Sicherheit und Umweltschutz auf der Baustelle |
| Auftragnehmer (Montageleitung) | Lieferung, Montage, Prüfung, Dokumentation | Ausführungsentscheidungen im Rahmen des Vertrags | Vertragsgemäße Leistung, Termin und Qualität der Ausführung |

*Empfehlung für den Report (vier Rollen):* Auftraggeber, Projektleitung, Fachprojektleitung Primärtechnik, Betrieb. Die Rollen decken Machtpromotoren, technische Verantwortung und Steuerung ab.

## 21.4 RACI-Matrix

Quelle: `data/raci_matrix_p1.xlsx`. R = Responsible, A = Accountable, C = Consulted, I = Informed, A/R = Accountable und Responsible.

| Aktivität | Auftraggeber | Projektleitung | FPL Primärtechnik | Betrieb | Einkauf | Arbeitssicherheit | Auftragnehmer (GU) |
|---|---|---|---|---|---|---|---|
| Projektauftrag | A | R | C | C | I | I | I |
| Lastenheft | I | A | R | C | C | C | C |
| Ausschreibung | I | C | C | C | A/R | C | I |
| Technische Angebotsbewertung | I | A | R | C | C | C | I |
| Vergabeentscheidung | A | R | C | C | R | I | I |
| Detailengineering | I | A | C | C | I | C | R |
| FAT | I | A | R | C | I | I | R |
| Abschaltplanung | I | C | C | A/R | I | C | C |
| Montage | I | A | C | C | I | C | R |
| Inbetriebnahme | I | A | R | R | I | C | R |
| Abnahme | A | R | R | C | C | C | C |

## 21.5 Kommunikationsmatrix

| Stakeholder | Informationsbedarf | Format / Medium | Rhythmus | Verantwortlich (Sender) | Ziel |
|---|---|---|---|---|---|
| Auftraggeber | Status (Ampel), Budget, Risiken, Entscheidungsvorlagen | Statusbericht und Lenkungskreis | monatlich | Projektleitung | Steuerung, Entscheidungen, Rückhalt |
| Betrieb | Abschaltplanung, Termine, Schaltberechtigung | Kernteam-Jour-fixe, persönliches Abstimmungsgespräch | zweiwöchentlich, anlassbezogen | Projektleitung | Verbindliche Zusage des Abschaltfensters (siehe 17) |
| Auftragnehmer | Engineering, Fertigung, Dokumente, Termine, offene Punkte | Jour fixe, Protokoll, im Abschaltfenster Baustellen-Stand-up | zweiwöchentlich, täglich im Fenster | Projektleitung, Fachprojektleitung | Termin- und Qualitätssicherung |
| Fachprojektleitung Primärtechnik | Technische Reviews, Prüfergebnisse, Änderungen | Kernteam-Jour-fixe, Design Review, FAT | zweiwöchentlich, zu Meilensteinen | Projektleitung | Technische Freigaben |
| Schutz- und Leittechnik | Signal- und Schnittstellenliste, Funktionstest | Schnittstellenworkshop, Signalliste | bis M4 monatlich, danach anlassbezogen | Fachprojektleitung | Fehlerfreie Schnittstellen |
| Einkauf | Vergabefahrplan, Angebotsstand, Vertragsentwurf | Kernteam-Jour-fixe, Vergabefahrplan | zweiwöchentlich, in Phase 3 wöchentlich | Projektleitung | Termingerechte Vergabe |
| Arbeitssicherheit / Umweltschutz | Sicherheits- und Umweltkonzept, Baustellenplanung | Freigabetermin vor Baustart, Sicherheitsunterweisung, Stand-up | vor Baustart, täglich im Fenster | Projektleitung | Freigabe und sicherer Ablauf |
| Behörden / externe Stellen | Genehmigungsbedarf, Nachweise | Schriftlicher Austausch | anlassbezogen | Projektleitung, Umweltschutz | Rechtzeitige Genehmigungen |

**Grundsätze:** Entscheidungen werden schriftlich dokumentiert (Protokollvorlage in `templates/`). Änderungen laufen ausschließlich über das Change-Verfahren (10). Beim Betrieb gilt die in 17.4 abgeleitete Regel: zuerst betriebliche Randbedingungen erfragen, dann einen Terminwunsch äußern.
