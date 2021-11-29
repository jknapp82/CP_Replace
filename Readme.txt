##############################################################################
######################            CP_Replace            ######################
######################     "Copy&Paste Replace Tool"    ######################
######################    cp_replace@project-hub.biz    ######################
##############################################################################

"Copy&Paste Replace Tool" ist ein Hilfsprogramm, dass auf Knopfdruck
Zeichenketten in der Zwischenablage durch definierbare alternative 
Zeichenketten ersetzt.

Zentrales Element ist die Datei "translate.json", die im Verzeichnis "recources" 
abgelegt werden muss. Diese dient als "Übersetzungsdatei". Der Text in der 
Zwischenablage wird nach jedem der Schlüssel (links von ":") in "translate.json" 
durchsucht und mit dem Wert (rechts von ":") ersetzt. Als Muster kann die Datei 
"translate_Beispiel.json" dienen. Wichtig ist es, die Syntax genau einzuhalten.
Häufigster Fehler: Kommasetzung. Alle Schlüssel:Wert-Paare müssen durch Kommas
getrennt sein. Hinter dem letzten Schlüssel:Wert-Paar darf kein Komma folgen.

Die Software befindet sich im Beta Stadium. Für den Einsatz wird keine Haftung
übernommen. Für die 

Verwendete Lizenzen:

PySide: PySide is licensed under the LGPL version 2.1 license, allowing both 
Free/Open source software and proprietary software development.

Python: Python is licensed under the Python-Software-Foundation-Lizenz.

