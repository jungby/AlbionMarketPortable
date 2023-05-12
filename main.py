from PyQt5 import QtCore, QtGui, QtWidgets
from tab_items import Ui_Dialog as UI_items
from tab_cities import Ui_Dialog as UI_cities
from tab_prices import Ui_Dialog as UI_prices

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Naming UIs
        self.ui1 = UI_items()
        self.ui2 = UI_cities()
        self.ui3 = UI_prices()

        # Initializing tabs
        self.ui1.setupUi(self)
        self.ui2.setupUi(self)
        self.ui3.setupUi(self)

    def initUI(self):
        # Main tab (items)
        self.ui1.setupUi(self)

        self.tab_cities = self.ui2.tab_cities
        self.tab_prices = self.ui3.tab_prices

        # Adding tabs to the main tab
        self.ui1.tabWidget.addTab(self.tab_cities, "Ciudades")
        self.ui1.tabWidget.addTab(self.tab_prices, "Precios")

# Avoiding circular imports
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    MyWindow.initUI(w)
    w.show()
    sys.exit(app.exec_())