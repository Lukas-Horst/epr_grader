# eprgrader

Ein Tool, um die Bewertung von EPR-Abgaben (und auch GPR-Abgaben) zu beschleunigen.

## Installation

1. Legt `eprgrader.py` (das eigentliche Programm), `eprcheck_2019.py` (das pylint-Plugin für die
Author-Variable) und `violation_checker.py` (Klasse um die Stylefehler zusammenzuzählen) im 
   selben Verzeichnis ab.
2. Wenn ihr den automatischen Style-Check benutzen wollt, installiert folgendes via `pip`:
   `pip install pylint==2.15.0 pycodestyle==2.8.0 astroid==2.13.5 openpyxl pandas`

## Zu Beginn

Ladet die ZIP-Datei(en) mit den Abgaben für eure Gruppe(n), die Gesamtbewertung (.csv Datei) für 
eure Gruppe(n) sowie die Bewertungstabelle herunter.
Legt ein Verzeichnis für das Übungsblatt an, und dann einen Unterordner für jedes eurer Tutorien.
Legt die Abgaben-Zips und die Gesamtbewertungen in die jeweiligen Ordner. Das ganze sollte 
jetzt in etwa so aussehen:

```
blatt0
|-- Bewertungstabelle_EPR_0.xlsx
|-- EPR01
|   `-- EPR-2021-Abgabe zu EPR_00-EPR 01 - H 7 - Adrian-88422.zip
|   `-- Bewertungen-EPR 2021-Abgabe zu EPR_00-EPR 01 - H 7 - Adrian-88422.csv
`-- EPR02
    `-- EPR-2021-Abgabe zu EPR_00-EPR 02 - H 6 - Adrian-88422.zip
    `-- Bewertungen-EPR 2021-Abgabe zu EPR_00-EPR 02 - H 6 - Adrian-88422.csv
```

Führt jetzt den Startbefehl aus:
```cmd
cd ...\Tutorium\blatt0
python eprgrader.py begin --table Bewertungstabelle_EPR_0.xlsx
```

Zusätzliche Optionen:
* `--no-stylecheck`: Überspringt die PEP8-Prüfung und verhindert das Anlegen der `stylecheck.txt`-Dateien für jede Abgabe.
* `--pairs`: Überprüft die `__author__`-Variable nach dem Format für Paaraufgaben.
* `--no-deduction`: Wenn es noch keinen Abzug für Stylefehler und docstrings gibt.
* `--no-docstringDeduction`: Wenn es keinen Abzug für docstrings geben soll.

Hierdurch werden alle zip-Archive entpackt, die Bewertungstabellen kopiert und für jeden Teilnehmer
entsprechend umbenannt, und ggf. der Stylechecker ausgeführt.

Wenn der Stylechecker ausgeführt, wird außerdem direkt der Abzug berechnet und in die 
Bewertungstabelle eingetragen. Die überprüften Stylefehler werden dabei in Gruppen eingeteilt 
und dann innerhalb dieser Gruppen zusammengezählt. Wie die Fehlergruppen eingeteilt sind und wie 
viel Abzug es gibt, kann man in der violation_checker.py Datei anpassen.

Damit der Abzug automatisch eingetragen werden kann, muss es folgende Zellen geben: 
   - `__author__`  falsch (Abzug für Fehler bei der author Variable)    
  - ...alle `o.g. Fehler` sind gleichbedeutend... (Abzug für Stylefehler)
  - `Abzug bei` mangelnden Kommentaren... (Abzug für Docstrings)

Markiert sind dabei die Stellen, nach welchen explizit gesucht wird.


## Style-Prüfung erneut ausführen

Bei Bedarf kann die Style-Prüfung erneut ausgeführt werden. Dabei werden alle bestehenden
`stylecheck.txt`-Dateien überschrieben.
Die Punkte werden aber nicht mehr in die Bewertungstabellen eingetragen

```cmd
cd ...\Tutorium\blatt0
python eprgrader.py relint
```

Zusätzliche Optionen:
* `--pairs`: Überprüft die `__author__`-Variable nach dem Format für Paaraufgaben.
* `--no-deduction`: Wenn es noch keinen Abzug für Stylefehler und docstrings gibt.
* `--no-docstringDeduction`: Wenn es keinen Abzug für docstrings geben soll.

## Abschluss

Am Ende können die Bewertungsdateien (Glob-Pattern `Bewertung *`) sowie die `stylecheck.txt`
für jeden Teilnehmer zusammengesammelt und für den Upload als Feedback-Datei wieder zusammengepackt
werden.

Wenn die Gesamtbewertungstabellen in den Ordnern sind, wird die Gesamtpunktzahl von allen 
Einzelbewertungen ausgelesen und in die csv Datei eingefügt. Dafür muss es die Zelle `Summe` geben.

Achtung: das funktioniert nur für die Einzelabgaben sinnvoll!

```cmd
cd ...\Tutorium\blatt0
python eprgrader.py finalise
```

Nun sollte sich in jedem Tutoriums-Unterordner eine neue Zip-Datei finden, die den Namen
des Tutoriums trägt (z. B. `EPR02.zip`). Diese kann über die Moodle-Option "Mehrere Feedbackdateien
in einer Zip-Datei hochladen" hochgeladen werden.
Die Gesamtbewertungstabelle kann unter "Bewertungstabelle hochladen" hochgeladen werden. Dabei 
muss der Haken bei "Update von Datensätzen zulassen, ..." gesetzt werden.

Wenn man den finalise Befehl bei Änderungen erneut ausführen möchte, muss man vorher den Ordner `korrekturen` und die Zip-Datei löschen.

## Änderung der Style-Einstellungen

Die Style-Einstellungen (welche Checks aktiviert bzw. deaktiviert sind) habe ich letztes Jahr
mal nach eigenem Empfinden zusammengestellt. (Es wird deutlich mehr überprüft, als laut unseren
Richtlinien zu Punktabzug führt.) Die aktivierten Checker sind relativ weit oben in `eprgrader.py`
konfiguriert, in den Listen `PYLINT_OPTIONS` und `PYCODESTYLE_SELECT`.

## Bei Problemen

`eprgrader.py` gibt sich Mühe, auch zip-Dateien mit vergurksten Dateinamen zu entpacken (passiert
meistens, wenn Mac- oder Linux-Nutzer Umlaute in ihren Dateinamen haben), und die Dateinamen
dabei zu reparieren. Manche sind aber so kaputt, dass das Tool einfach abstürzt. In dem Fall
hilft nur, die betroffene Datei aus dem heruntergeladenen Zip zu entfernen und nochmal von vorne
anzufangen. Danach kann man die kaputte Datei von Hand ergänzen und ggf. den `relint`-Befehl nutzen.

Bei anderen Problemen, merkt es unter Issues in dem Repo an.
