# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab items.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


import json
import requests

from pdb import Pdb as pdb
pdb_instance = pdb()


class Ui_Tab1(object):
    def setupUiTab1(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(705, 388)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        Dialog.setFont(font)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 691, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_items = QtWidgets.QWidget()
        self.tab_items.setObjectName("tab_items")

        self.fr_general_items = QtWidgets.QFrame(self.tab_items)
        self.fr_general_items.setGeometry(QtCore.QRect(0, 0, 681, 341))
        self.fr_general_items.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_general_items.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_general_items.setObjectName("fr_general_items")

        self.list_items = QtWidgets.QListWidget(self.fr_general_items)
        self.list_items.setGeometry(QtCore.QRect(10, 40, 321, 291))
        self.list_items.setObjectName("list_items")

        self.lb_filtro_search = QtWidgets.QLabel(self.fr_general_items)
        self.lb_filtro_search.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.lb_filtro_search.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_filtro_search.setObjectName("lb_filtro_search")

        self.entry_search = QtWidgets.QLineEdit(self.fr_general_items)
        self.entry_search.setGeometry(QtCore.QRect(70, 10, 261, 22))
        self.entry_search.setObjectName("entry_search")

        self.fr_details = QtWidgets.QFrame(self.fr_general_items)
        self.fr_details.setGeometry(QtCore.QRect(360, 40, 321, 291))
        self.fr_details.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_details.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_details.setObjectName("fr_details")

        self.lb_staticname = QtWidgets.QLabel(self.fr_details)
        self.lb_staticname.setGeometry(QtCore.QRect(10, 170, 61, 16))

        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)

        self.lb_staticname.setFont(font)
        self.lb_staticname.setObjectName("lb_staticname")
        self.lb_staticdescription = QtWidgets.QLabel(self.fr_details)
        self.lb_staticdescription.setGeometry(QtCore.QRect(10, 220, 81, 16))

        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.lb_staticdescription.setFont(font)
        self.lb_staticdescription.setObjectName("lb_staticdescription")
        self.lb_img = QtWidgets.QLabel(self.fr_details)
        self.lb_img.setGeometry(QtCore.QRect(10, 40, 111, 111))
        self.lb_img.setText("")
        self.lb_img.setPixmap(QtGui.QPixmap("../../../../../Pictures/reactions/bb72016e-a8f2-407a-8ee9-854823e4f28c.png"))
        self.lb_img.setScaledContents(True)
        self.lb_img.setObjectName("lb_img")
        self.lb_details = QtWidgets.QLabel(self.fr_details)
        self.lb_details.setGeometry(QtCore.QRect(10, 10, 301, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_details.setFont(font)
        self.lb_details.setObjectName("lb_details")
        self.lb_name = QtWidgets.QLabel(self.fr_details)
        self.lb_name.setGeometry(QtCore.QRect(10, 190, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.lb_name.setFont(font)
        self.lb_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_name.setWordWrap(True)
        self.lb_name.setObjectName("lb_name")
        self.lb_description = QtWidgets.QLabel(self.fr_details)
        self.lb_description.setGeometry(QtCore.QRect(10, 240, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.lb_description.setFont(font)
        self.lb_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_description.setWordWrap(True)
        self.lb_description.setObjectName("lb_description")
        self.combo_category = QtWidgets.QComboBox(self.fr_general_items)
        self.combo_category.setGeometry(QtCore.QRect(440, 10, 231, 22))
        self.combo_category.setObjectName("combo_category")
        self.lb_category = QtWidgets.QLabel(self.fr_general_items)
        self.lb_category.setGeometry(QtCore.QRect(360, 10, 71, 16))
        self.lb_category.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_category.setObjectName("lb_category")
        self.tabWidget.addTab(self.tab_items, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # carga el archivo JSON
        with open(r'FTTS.json', errors='ignore', encoding='UTF-8') as f:
            self.data = json.load(f)

        # DEPURAR
        # pdb_instance.set_trace()

        # mostrar elementos en lista
        for item in self.data:
            self.list_items.addItem(item['Name'])

        # muestra la información del item seleccionado
        def show_details():
            index = self.list_items.currentRow()
            item = self.list_items.item(index).text()
            description = self.data[index]['Description']
            image_url = self.data[index]['ImageURL']

            response = requests.get(image_url)
            pixmap = None

            if response.status_code == 200:
                # Convertir el contenido de la respuesta en un objeto QPixmap
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(response.content)

            self.lb_name.setText(item)
            self.lb_description.setText(description)

            if pixmap is not None:
                self.lb_img.setPixmap(pixmap)

        # conecta la señal de selección del QListWidget con la función show_details
        self.list_items.currentRowChanged.connect(show_details)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_filtro_search.setText(_translate("Dialog", "Buscar:"))
        self.lb_staticname.setText(_translate("Dialog", "Nombre:"))
        self.lb_staticdescription.setText(_translate("Dialog", "Descripción:"))
        self.lb_details.setText(_translate("Dialog", "Detalles item"))
        self.lb_name.setText(_translate("Dialog", "TextLabel"))
        self.lb_description.setText(_translate("Dialog", "TextLabel"))
        self.lb_category.setText(_translate("Dialog", "Categoría:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_items), _translate("Dialog", "Items"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_Tab1()
    ui.setupUiTab1(w)
    w.show()
    sys.exit(app.exec_())