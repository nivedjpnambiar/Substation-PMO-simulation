# 14 – Portfolio-Priorisierung

## Zweck

Dieses Dokument erweitert das ursprüngliche Simulationsprojekt (Erneuerung 380-kV-Leistungsschalterfeld)
um die Portfolioebene. Es zeigt, wie mehrere unabhängige interne LGT-Projekte anhand einheitlicher
Kriterien bewertet, priorisiert und in einem Portfolio "in Balance" gehalten werden können —
entsprechend IPMA ICB4, Practice 14 (Projektselektion und Portfoliobalance).

## Kriterien und Gewichtung

| Kriterium | Gewichtung | Beschreibung |
|---|---|---|
| Strategischer Nutzen | 40 % | Beitrag zu den PME-Zielen von LGT (Transparenz, Governance, Effizienz) |
| Dringlichkeit | 30 % | Zeitliche oder regulatorische Zwänge |
| Risiko (invers) | 30 % | Je geringer das Risiko, desto höher der Score |

## Formel

```
Prioritaet = Nutzen x 0,4 + Dringlichkeit x 0,3 + (6 - Risiko) x 0,3
```

## Anwendung

Die berechneten Scores ergeben eine Rangfolge, die als Diskussionsgrundlage für das Steering Board
dient — nicht als automatische Entscheidung. Ressourcenkonflikte und Abhängigkeiten (siehe
`ressourcenkonflikte.csv`) werden zusätzlich geprüft, bevor eine Priorisierung final freigegeben wird.
Das Dashboard (`portfolio_dashboard.html`) visualisiert das Ergebnis als Nutzen-Risiko-Matrix mit vier
Quadranten (Quick Wins, Strategische Wetten, Hinterfragen, Nice-to-have).

## Grenzen des Modells

Die Gewichtung ist bewusst einfach gehalten, um Nachvollziehbarkeit zu sichern. In einer realen
Portfolioumgebung würden zusätzliche Dimensionen — regulatorische Pflichtprojekte, Abhängigkeitsketten,
Kapazitätsengpässe über mehrere Monate — das Modell verfeinern. Das ist bewusst der nächste Schritt
und nicht Teil dieser ersten Version.
