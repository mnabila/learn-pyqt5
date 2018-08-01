import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QMessageBox
    )
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QLabel, QComboBox)

class window(QWidget):
    def __init__(self):
        super().__init__()

        # list widget items
        self.lbl_jenis = QLabel("Jenis Pivot Point")
        self.lbl_hight = QLabel("Tertinggi (Hight)")
        self.lbl_low = QLabel("Terendah (Low)")
        self.lbl_open = QLabel("Pembukaan (Open)")
        self.lbl_close = QLabel("Penutupan (Close)")
        self.lbl_r4 = QLabel("Resistance 4")
        self.lbl_r3 = QLabel("Resistance 3")
        self.lbl_r2 = QLabel("Resistance 2")
        self.lbl_r1 = QLabel("Resistance 1")
        self.lbl_pp = QLabel("Pivot Point")
        self.lbl_s1 = QLabel("Support 1")
        self.lbl_s2 = QLabel("Support 2")
        self.lbl_s3 = QLabel("Support 3")
        self.lbl_s4 = QLabel("Support 4")
        self.r4 = QLabel()
        self.r3 = QLabel()
        self.r2 = QLabel()
        self.r1 = QLabel()
        self.pp = QLabel()
        self.s1 = QLabel()
        self.s2 = QLabel()
        self.s3 = QLabel()
        self.s4 = QLabel()
        self.option = QComboBox()
        self.option.addItems([
            "Klasik",
            "Woodie's",
            "Camarilla",
            "De Mark"
        ])

        self.le_hight = QLineEdit()
        self.le_low = QLineEdit()
        self.le_open = QLineEdit()
        self.le_close = QLineEdit()

        self.hitung = QPushButton("Hitung")
        self.result = QLabel()

        # event
        # self.option.activated.connect(self.function)
        self.hitung.clicked.connect(self.function)


        # call  main UI
        self.main_UI()

    def main_UI(self):
        self.grid_box = QGridLayout()

        self.grid_box.addWidget(self.lbl_jenis, 0, 0)
        self.grid_box.addWidget(self.option, 0, 1)
        self.grid_box.addWidget(self.lbl_hight, 1, 0)
        self.grid_box.addWidget(self.le_hight, 1, 1)
        self.grid_box.addWidget(self.lbl_low, 2, 0)
        self.grid_box.addWidget(self.le_low, 2, 1)
        self.grid_box.addWidget(self.lbl_open, 3, 0)
        self.grid_box.addWidget(self.le_open, 3, 1)
        self.grid_box.addWidget(self.lbl_close, 4, 0)
        self.grid_box.addWidget(self.le_close, 4, 1)
        self.grid_box.addWidget(self.hitung, 5, 1)
        self.grid_box.addWidget(self.lbl_r4, 6, 0)
        self.grid_box.addWidget(self.r4, 6, 1)
        self.grid_box.addWidget(self.lbl_r3, 7, 0)
        self.grid_box.addWidget(self.r3, 7, 1)
        self.grid_box.addWidget(self.lbl_r2, 8, 0)
        self.grid_box.addWidget(self.r2, 8, 1)
        self.grid_box.addWidget(self.lbl_r1, 9, 0)
        self.grid_box.addWidget(self.r1, 9, 1)
        self.grid_box.addWidget(self.lbl_pp, 10, 0)
        self.grid_box.addWidget(self.pp, 10, 1)
        self.grid_box.addWidget(self.lbl_s1, 11, 0)
        self.grid_box.addWidget(self.s1, 11, 1)
        self.grid_box.addWidget(self.lbl_s2, 12, 0)
        self.grid_box.addWidget(self.s2, 12, 1)
        self.grid_box.addWidget(self.lbl_s3,13, 0)
        self.grid_box.addWidget(self.s3,13, 1)
        self.grid_box.addWidget(self.lbl_s4, 14, 0)
        self.grid_box.addWidget(self.s4, 14, 1)

        self.setLayout(self.grid_box)
        self.setWindowTitle("Pivot Point")
        self.setMaximumSize(400,200)
        self.show()

    def function(self):
        try:
            option = str(self.option.currentText())
            hight = float(self.le_hight.text())
            low = float(self.le_low.text())
            buka = float(self.le_open.text())
            tutup = float(self.le_close.text())
            if option == "Klasik":
                pp = (hight + low + tutup)/3
                lr3 = hight + (2 * (pp - low))
                lr2 = pp + (hight - low)
                lr1 = (2 * pp) - low
                ls1 = (2 * pp) - hight
                ls2 = pp - (hight - low)
                ls3 = low - (2 * (hight - pp))
                self.r4.clear()
                self.r3.setText(str(lr3))
                self.r2.setText(str(lr2))
                self.r1.setText(str(lr1))
                self.pp.setText(str(pp))
                self.s1.setText(str(ls1))
                self.s2.setText(str(ls2))
                self.s3.setText(str(ls3))
                self.s4.clear()
            elif option == "Woodie's":
                pp = (hight + low + tutup)/3
                lr2 = pp + (hight - low)
                lr1 = (2 * pp) - low
                ls1 = (2 * pp) - hight
                ls2 = pp - (hight - low)
                # set qlabel value
                self.r4.clear()
                self.r3.clear()
                self.r2.setText(str(lr2))
                self.r1.setText(str(lr1))
                self.pp.setText(str(pp))
                self.s1.setText(str(ls1))
                self.s2.setText(str(ls2))
                self.s3.clear()
                self.s4.clear()
            elif option == "Camarilla":
                pp = (hight + low + tutup)/3
                lr4 = tutup + (((hight - low) * 1.1)/2)
                lr3 = tutup + (((hight - low)*1.1)/4)
                lr2 = tutup + (((hight - low)*1.1)/6)
                lr1 = tutup + (((hight - low)*1.1)/12)
                ls1 = tutup - (((hight - low)*1.1)/12)
                ls2 = tutup - (((hight - low)*1.1)/6)
                ls3 = tutup - (((hight - low)*1.1)/4)
                ls4 = tutup - (((hight - low)*1.1)/2)
                self.r4.setText(str(lr4))
                self.r3.setText(str(lr3))
                self.r2.setText(str(lr2))
                self.r1.setText(str(lr1))
                self.pp.setText(str(pp))
                self.s1.setText(str(ls1))
                self.s2.setText(str(ls2))
                self.s3.setText(str(ls3))
                self.s4.setText(str(ls4))
            elif option == "De Mark":
                if tutup < 0:
                    x = hight + (2(low + tutup))
                elif tutup > 0:
                    x = 2 * (hight + low + tutup)
                elif tutup == 0:
                    x = hight + low + (2*tutup)
                lr1 = x / 2 - low
                ls1 = x / 2 - hight
                self.r4.clear()
                self.r3.clear()
                self.r2.clear()
                self.r1.setText(str(lr1))
                self.pp.clear()
                self.s1.setText(str(ls1))
                self.s2.clear()
                self.s3.clear()
                self.s4.clear()
        except ValueError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Alert")
            msg.setText("sepertinya ada yang belum terisi")
            msg.exec_()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window()
    sys.exit(app.exec_())