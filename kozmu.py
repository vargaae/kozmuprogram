import sys
import datetime
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox


class UtilityTracker(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Közmű Diktálás és Számla Összesítő")
        self.setGeometry(300, 200, 500, 400)

        # Label és beviteli mezők a típushoz
        self.label_type = QtWidgets.QLabel(self)
        self.label_type.setText("Közmű típusa:")
        self.label_type.setGeometry(50, 50, 150, 30)

        self.combo_type = QtWidgets.QComboBox(self)
        self.combo_type.setGeometry(200, 50, 200, 30)
        self.combo_type.addItems(["Gáz", "Áram", "Víz"])

        # Előző és új diktálási érték beviteli mezők
        self.label_prev = QtWidgets.QLabel(self)
        self.label_prev.setText("Előző érték:")
        self.label_prev.setGeometry(50, 100, 150, 30)

        self.input_prev = QtWidgets.QLineEdit(self)
        self.input_prev.setGeometry(200, 100, 200, 30)

        self.label_current = QtWidgets.QLabel(self)
        self.label_current.setText("Új érték:")
        self.label_current.setGeometry(50, 150, 150, 30)

        self.input_current = QtWidgets.QLineEdit(self)
        self.input_current.setGeometry(200, 150, 200, 30)

        # Számla összeg beviteli mező
        self.label_bill = QtWidgets.QLabel(self)
        self.label_bill.setText("Számla összege (Ft):")
        self.label_bill.setGeometry(50, 200, 150, 30)

        self.input_bill = QtWidgets.QLineEdit(self)
        self.input_bill.setGeometry(200, 200, 200, 30)

        # Mentés gomb
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Mentés")
        self.btn_save.setGeometry(200, 250, 100, 40)
        self.btn_save.clicked.connect(self.save_data)

    def save_data(self):
        # Adatok beolvasása
        utility_type = self.combo_type.currentText()
        try:
            prev_reading = int(self.input_prev.text())
            current_reading = int(self.input_current.text())
            bill_amount = int(self.input_bill.text())
        except ValueError:
            QMessageBox.warning(self, "Hiba", "Kérjük, helyesen adja meg az értékeket!")
            return

        # Fogyasztás és dátum
        consumption = current_reading - prev_reading
        date = datetime.date.today().strftime("%Y-%m-%d")

        # Adatok fájlba írása
        with open("kozmu_adatok.txt", "a") as file:
            file.write(f"Típus: {utility_type}\n")
            file.write(f"Dátum: {date}\n")
            file.write(f"Előző érték: {prev_reading}\n")
            file.write(f"Új érték: {current_reading}\n")
            file.write(f"Fogyasztás: {consumption}\n")
            file.write(f"Számla összeg: {bill_amount} Ft\n")
            file.write("---------------\n")

        # Üzenet a sikeres mentésről
        QMessageBox.information(self, "Sikeres mentés", "Az adatokat sikeresen mentettük a fájlba.")

        # Beviteli mezők törlése
        self.input_prev.clear()
        self.input_current.clear()
        self.input_bill.clear()


# Alkalmazás futtatása
app = QApplication(sys.argv)
window = UtilityTracker()
window.show()
sys.exit(app.exec_())
