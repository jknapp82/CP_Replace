
import sys
from typing import List
from PySide2.QtCore import QObject, QFile
from PySide2.QtWidgets import QApplication, QPushButton, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QClipboard
import json

class Form(QObject):

    # በ=be
    # ጃ=dscha
    # ኻ=cha
    # ኤ=ä
    # ር=r
    # ም=m
    # ያ=ya
    # ስ=s
    # ኣ=a
    # ን=n
    # ብ=b

    # Opening JSON file
    
    def __init__(self, ui_file, parent=None):
        super(Form, self).__init__(parent)
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        #ui_file.close()

        self.btnTranslageClipboard = self.window.findChild(QPushButton, 'btnTranslageClipboard')
        self.btnTranslageClipboard.clicked.connect(self.translate_clipboard)
        self.window.show()
        self.openTranslateFile()

    def openTranslateFile(self):
        try:
            with open('resources/translate.json', encoding="utf-8") as json_file:
                data = json.load(json_file)
                self.translatioDict=data["translationDict"][0]
        except:
            print("Einlesen der Übersetzungsdatei fehlgeschlagen.")
            self.ShowWarnMessage(
                                'Fehler', 
                                'Übersetzungsdatei "translate.json" konnte nicht eingelesen werden. Entweder Sie ist nicht im Unterordner "resources" vorhanden oder sie enthält Fehler. Bitte achte besonders auf Kommas, siehe "translate_Beispiel.json".'
                                )
            sys.exit()


    
    def getClipboard(self):
        data = QClipboard().text()
        print('clipboard eingelesen...')
        return data

    def setClipboard(self, data):
        QClipboard().setText(data)
        print('clipboard gesetzt.')
    

    def translate_clipboard(self):
        clip = self.getClipboard()
        for key in self.translatioDict:
            DictKey = key
            DictVal = self.translatioDict[key]
            clip = clip.replace(DictKey,DictVal)
        print('Eingelesenen Text Übersetzt...')
        self.setClipboard(clip)
    


    def ShowWarnMessage(self,Titel='Warnung', Message='Keine Information zum Fehler'):
        mb = QMessageBox()
        mb.setIcon(mb.Icon.Warning)
        mb.setText("{0}".format(Message))
        mb.setWindowTitle(Titel)
        #mb.setStandardButtons(QMessageBox.Yes)
        mb.addButton(QMessageBox.Abort)
        result = mb.exec_()
        if result == QMessageBox.Yes:
            result = 'Yes'
        else:
            result = 'undefined'
        #self.log_status(result)
        return result


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form('resources/CP_Replace.ui')
    sys.exit(app.exec_())