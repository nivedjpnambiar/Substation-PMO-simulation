# 23. Ressourcenplanung

## 23.1 Personalressourcen mit benötigter Qualifikation

Grundlage sind die Aufwandsannahmen aus 5.4. Die Einsatzzeiträume entsprechen dem Ressourcen-Gantt (23.3). Die Werte sind Planungsannahmen des Simulationsprojekts.

| Rolle | Auslastung | Einsatzzeitraum | Aufgabe im Projekt | Benötigte Qualifikation |
|---|---:|---|---|---|
| Projektleitung | 0,35 | 01.10.2025 – 30.09.2026 | Gesamtsteuerung, Vertrags- und Kostensteuerung, Stakeholdermanagement | Projektmanagement-Ausbildung (IPMA Level D oder höher), Erfahrung mit technischen Investitionsprojekten in der Energieversorgung, Kenntnisse in Vertrags- und Änderungsmanagement |
| Fachprojektleitung Primärtechnik | 0,30 | 16.10.2025 – 30.09.2026 | Technische Spezifikation, Reviews, FAT und Abnahmeprüfungen | Ingenieur Elektrotechnik, Kenntnis von Hochspannungs-Schaltgeräten (Normenreihe IEC 62271), Erfahrung mit Werks- und Abnahmeprüfungen |
| Schutz-/Leittechnik | 0,15 | 03.11.2025 – 10.09.2026 | Signallisten, Schnittstellen, Funktionsprüfung | Ingenieur Schutz- und Leittechnik, Kenntnis der Stationsleittechnik (IEC 61850), Erfahrung mit Signal- und Funktionstests |
| Einkauf | 0,10 | 01.12.2025 – 27.02.2026 | Ausschreibung, kaufmännische Bewertung, Bestellung | Erfahrung in technischer Beschaffung und Vergabeverfahren, Vertragsrecht-Grundkenntnisse |
| Betrieb | 0,10 | 03.08.2026 – 10.09.2026 | Abschaltplanung, Schaltberechtigung, Betriebsfreigabe | Anlagenverantwortlicher mit Schaltberechtigung (Betrieb elektrischer Anlagen nach DIN VDE 0105-100), Kenntnis der Bestandsanlage |
| Arbeitssicherheit/Umwelt | 0,08 | 03.08.2026 – 10.09.2026 | Sicherheits- und Umweltkonzept, Baustellenkontrollen | Fachkraft für Arbeitssicherheit, Kenntnis der Vorschriften für elektrische Anlagen (DGUV Vorschrift 3), Umweltfachwissen einschließlich SF6-Handhabung |
| Dokumentation/Qualität | 0,08 | 01.07.2026 – 30.09.2026 | Dokumentenplan, Prüfung von Revisionsunterlagen, Qualitätsnachweise | Erfahrung in technischer Dokumentation und Qualitätssicherung, Kenntnis des Dokumentationsstandards des Auftraggebers |
| Montage-/Inbetriebnahmeteam (Auftragnehmer) | 8 Personen | 01.09.2026 – 10.09.2026 | Demontage, Montage, Anschluss, Prüfunterstützung | Montageleiter, 2 Fachmonteure Schaltgeräte, 2 Elektromonteure Sekundärtechnik, Kranführer/Anschläger, 2 Monteure; Schaltanlagen-Erfahrung, Unterweisung für Arbeiten in 380-kV-Anlagen, Sachkunde für SF6-Handhabung im Team |

## 23.2 Sachressourcen mit Spezifikation

| Nr. | Sachressource | Spezifikation (Planungsannahme) | Einsatz | Bereitstellung | Bezug |
|---|---|---|---|---|---|
| S1 | Leistungsschalter 380 kV mit Federspeicherantrieb (Neugerät) | Bemessungsspannung 420 kV, Bemessungsstrom 4.000 A, Bemessungs-Kurzschlussausschaltstrom 50 kA, Isoliergas SF6, Masse ca. 8 t, Antriebsschrank, Prüfung nach IEC 62271-100 | Lieferung bis 31.08.2026, Montage 03.–06.09.2026 | Auftragnehmer (Hersteller) | A-001, 2.3 |
| S2 | Autokran | Nennlast 100 t, Hublast mindestens 10 t bei 18 m Ausladung, Sicherheitsabstände zu spannungsführenden Teilen nach DIN VDE 0105-100 | 01.–06.09.2026 (Demontage, Montage) | Auftragnehmer | R-07, 23.4 |
| S3 | Sondertransport (Tieflader) für Neugerät und Altgerät | Nutzlast mindestens 12 t, Baustellenzufahrt geklärt | Anlieferung 31.08./01.09.2026, Abtransport Altgerät | Auftragnehmer | R-07 |
| S4 | SF6-Gasservicegerät | Absaugen, Aufbereiten und Befüllen, Feuchte- und Reinheitsmessung, Dichtheitsprüfung, Bediener mit Sachkunde | Demontage Altgerät und Inbetriebnahme Neugerät | Auftragnehmer, Prüfung durch Umweltschutz | Umweltschutz |
| S5 | Prüf- und Messtechnik | Schaltzeitenmessgerät, Kontaktwiderstandsmessgerät (Gleichstrom mindestens 100 A), Sekundärprüfkoffer für Signal- und Funktionstests | 08.–10.09.2026 (AP 6.5, 6.6) | Auftragnehmer und Schutz-/Leittechnik | A-003, 11.2 |
| S6 | Fundamentadapter | Vorgefertigte Adapterkonstruktion für zwei Befestigungspunkte außerhalb der Toleranz | Fertigung vor dem Abschaltfenster, Einbau am 02.09.2026 | Auftragnehmer | CR-002, 10.4 |

## 23.3 Ressourcen-Gantt

![Ressourcen-Gantt](../assets/diagrams/ressourcen_gantt.png)

Die internen Rollen sind über die Projektlaufzeit gleichmäßig mit 8 bis 35 % ausgelastet. Betrieb sowie Arbeitssicherheit und Umwelt werden vor allem in der Vorbereitung und im Abschaltfenster gebraucht. Das Montageteam des Auftragnehmers ist die einzige Ressource, die an ein festes Zeitfenster gebunden ist.

## 23.4 Engpassressource Montageteam und Kapazitätsgrenze

![Engpass Montageteam](../assets/diagrams/engpass_montageteam.png)

| Größe | Wert |
|---|---|
| Teamgröße (Kapazitätsgrenze) | 8 Personen |
| Verfügbare Zeit | 10 Einsatztage (01.–10.09.2026, Wochenendarbeit vereinbart) |
| **Kapazität** | **80 PT** |
| Planbedarf | 67 PT |
| Durchschnittliche Auslastung | 84 % |
| Tage mit 100 % Auslastung | Tag 1 bis 7 (kein Puffer) |

Tagesplan des Montageteams (Personen je Arbeitspaket):

| Tag | Datum | Einsatz je Arbeitspaket (Personen) | Summe | Auslastung |
|---:|---|---|---:|---:|
| 1 | 01.09.2026 | 6.1: 8,0 | 8,0 | 100 % |
| 2 | 02.09.2026 | 6.1: 4,0, 6.2: 4,0 | 8,0 | 100 % |
| 3 | 03.09.2026 | 6.3: 7,0, 6.4: 1,0 | 8,0 | 100 % |
| 4 | 04.09.2026 | 6.3: 8,0 | 8,0 | 100 % |
| 5 | 05.09.2026 | 6.3: 7,0, 6.4: 1,0 | 8,0 | 100 % |
| 6 | 06.09.2026 | 6.3: 5,3, 6.4: 2,7 | 8,0 | 100 % |
| 7 | 07.09.2026 | 6.4: 8,0 | 8,0 | 100 % |
| 8 | 08.09.2026 | 6.5: 4,0 | 4,0 | 50 % |
| 9 | 09.09.2026 | 6.5: 4,0 | 4,0 | 50 % |
| 10 | 10.09.2026 | 6.6: 3,0 | 3,0 | 38 % |
| | | **Summe** | **67,0** | **84 %** |

**Folgerungen:**
- An den Tagen 1 bis 7 gibt es keine Reserve. Jede Verzögerung wirkt direkt auf den Fensterabschluss am 10.09.2026.
- AP 6.3 „Neugerät montieren“ liegt im Kern der Engpassphase (Tag 3–6) und ist deshalb vollständig ausgearbeitet (16.3, 24).
- Maßnahmen: Springer-Vereinbarung im Vertrag (zwei Monteure auf Abruf), Vorfertigung der Adapter (CR-002), frühe Kranreservierung (R-07), tägliches Stand-up mit Neuplanung, Eskalation ab 5 Arbeitstagen Prognoseverzug (4.3).
- Auf Portfolioebene bestand im Juli 2026 ein Kapazitätskonflikt bei der Fachprojektleitung Technik (Bedarf 2,3 FTE, verfügbar 2,0 FTE, siehe 14). Lösung: P3 um vier Wochen verschieben.
