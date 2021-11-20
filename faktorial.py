## PROGRAM MENGHITUNG NILAI FAKTORIAL

## NAMA     : MARISA NAOFA
## NIM      : 200511074
## KELAS    : K1 TEKNIK INFORMATIKA



from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore
import sys

qtcreator_file = "faktorial.ui"
Ui_faktorialWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class MyfaktorialWindow(QtWidgets.QMainWindow, Ui_faktorialWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_faktorialWindow.__init__(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.txtnilai.textChanged.connect(self.hasilfaktorial)



    def hasilfaktorial(self):
        n = int(self.txtnilai.text())
        fac = 1
        for i in range(1, n + 1):
            fac *= i

        self.txthasil.setText(str(fac))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    faktorial = MyfaktorialWindow()
    faktorial.show() # Show in normal mode
    sys.exit(app.exec_())  