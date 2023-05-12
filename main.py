# -//////////////////////////////// IMPORTACIONES ////////////////////////////////-
# Importamos objetos de PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets

# Importamos las UI's de los demas archivos
from tab_items import Ui_Tab1
from tab_ciudades import Ui_Tab2
from tab_precios import Ui_Tab3


# -/////////////////////////////////// CODIGO ////////////////////////////////////-
class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Definifmos las UI's
        # UI Items
        self.ui1 = Ui_Tab1()
        # UI Ciudades
        self.ui2 = Ui_Tab2()
        # UI Precios
        self.ui3 = Ui_Tab3()

        # Inicializamos las UI's para poder acceder a la info de las mismas.
        self.ui1.setupUiTab1(self)
        self.ui2.setupUiTab2(self)
        self.ui3.setupUiTab3(self)


    # Funcion que inicia al principio del programa para inicializar objetos.
    def initUI(self):

        # Iniciamos nuestra UI principal para agregar las demas tabs
        # Esta UI es la de items, y ya continue su tab items.
        self.ui1.setupUiTab1(self)

        # Definimos las otras tabs
        self.tab_cities = self.ui2.tab_cities
        self.tab_prices = self.ui3.tab_prices

        # Agregamos las tabs faltantes a nuestro widget de UI's
        self.ui1.tabWidget.addTab(self.tab_cities, "Ciudades")
        self.ui1.tabWidget.addTab(self.tab_prices, "Precios")



# -////////////////////////////// INICIALIZACION ///////////////////////////////-
# Colocamos un if statement de __main__ para evitar circular imports
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MyWindow()
    MyWindow.initUI(w)
    w.show()
    sys.exit(app.exec_())