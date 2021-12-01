####################################################################################
######################               CP_Replace               ######################
######################        "Copy&Paste Replace Tool"       ######################
###################### https://github.com/jknapp82/CP_Replace ######################
######################       cp_replace@project-hub.biz       ######################
####################################################################################

"Copy&Paste Replace Tool" ist ein Hilfsprogramm, dass auf Knopfdruck
Zeichenketten in der Zwischenablage durch definierbare alternative 
Zeichenketten ersetzt.

################################ Übersetzungsdatei #################################

Zentrales Element ist die Datei "translate.json", die im Verzeichnis "recources" 
abgelegt werden muss. Diese dient als "Übersetzungsdatei" Die Grundidee zu diesem 
Tool entstand durch den Bedarf Tigrinya-Texte in "Lautschrift" umzuwandeln. 
Daher enthält die standardmäßig enthaltene "translate_tigrinya.json" eine entsprechende 
"Übersetzung" von Tigrinya-Zeichen. Um diese Datei zu verwenden, muss sie in 
"translate.json" umbenannt werden.

Als übersichtlicheres Muster für andere "übersetzungen" kann die Datei 
"translate_Beispiel.json" dienen. Diese muss dafür entsprechen in "translate.json"
umbenannt (oder kopiert) und bearbeitet werden.

################################## Funktionsweise ##################################

Der Text in der Zwischenablage wird nach jedem der Schlüssel (links von ":") in 
"translate.json" durchsucht und mit dem Wert (rechts von ":") ersetzt.  Wichtig ist 
es, die Syntax genau einzuhalten. Häufigster Fehler: Kommasetzung. 

Alle Schlüssel:Wert-Paare müssen durch Kommas getrennt sein. Hinter dem letzten 
Schlüssel:Wert-Paar darf kein Komma folgen.

################################ Haftungsausschluss ################################

Die Software befindet sich im Beta Stadium. Für den Einsatz wird keine Haftung
übernommen. Vom Einsatz in Produktivumgebungen wird abgeraten.

############################## Systemvoraussetzungen ###############################

Windows 10 / 11
Microsoft Visual C++ Redistributables 2015-2022 (32 Bit)
(Download: https://aka.ms/vs/17/release/vc_redist.x86.exe)

#################################### Lizenzen: #####################################

Verwendete Lizenzen:

PySide: PySide is licensed under the LGPL version 2.1 license, allowing both 
Free/Open source software and proprietary software development.

Python: Python is licensed under the Python-Software-Foundation-Lizenz.

