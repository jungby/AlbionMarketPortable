# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import logic as source

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(705, 388)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        Dialog.setFont(font)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 691, 371))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_prices = QtWidgets.QWidget()
        self.tab_prices.setObjectName("tab_prices")
        self.frame = QtWidgets.QFrame(self.tab_prices)
        self.frame.setGeometry(QtCore.QRect(0, 0, 681, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.list_items_prices = QtWidgets.QListWidget(self.frame)
        self.list_items_prices.setGeometry(QtCore.QRect(10, 50, 341, 281))
        self.list_items_prices.setObjectName("list_items_prices")
        self.entry_search_prices = QtWidgets.QLineEdit(self.frame)
        self.entry_search_prices.setGeometry(QtCore.QRect(10, 10, 241, 21))
        self.entry_search_prices.setObjectName("entry_search_prices")
        self.fr_prices = QtWidgets.QFrame(self.frame)
        self.fr_prices.setGeometry(QtCore.QRect(390, 40, 291, 291))
        self.fr_prices.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_prices.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_prices.setObjectName("fr_prices")
        self.lb_details_prices = QtWidgets.QLabel(self.fr_prices)
        self.lb_details_prices.setGeometry(QtCore.QRect(10, 20, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_details_prices.setFont(font)
        self.lb_details_prices.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_details_prices.setObjectName("lb_details_prices")
        self.table_prices = QtWidgets.QTableWidget(self.fr_prices)
        self.table_prices.setGeometry(QtCore.QRect(10, 50, 261, 231))
        self.table_prices.setObjectName("table_prices")
        self.table_prices.setColumnCount(2)
        self.table_prices.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_prices.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_prices.setHorizontalHeaderItem(1, item)
        self.lb_category_prices = QtWidgets.QLabel(self.frame)
        self.lb_category_prices.setGeometry(QtCore.QRect(390, 10, 71, 16))
        self.lb_category_prices.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_category_prices.setObjectName("lb_category_prices")
        self.combo_category_prices = QtWidgets.QComboBox(self.frame)
        self.combo_category_prices.setGeometry(QtCore.QRect(470, 10, 201, 22))
        self.combo_category_prices.setObjectName("combo_category_prices")
        self.bttn_search = QtWidgets.QPushButton(self.frame)
        self.bttn_search.setGeometry(QtCore.QRect(260, 10, 93, 28))
        self.bttn_search.setObjectName("bttn_search")
        self.tabWidget.addTab(self.tab_prices, "")

        #------------ don't touch ------------#
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #------------ before blowing it up ---------------#
        source.city_names
        for item_name in source.item_names:
            self.list_items_prices.addItem(item_name)
        self.combo_category_prices.addItems(source.unique_tags)
        
        def redirectFilter():
            filterItems()

        #------------ triggers ---------------#
        self.bttn_search.clicked.connect(self.get_price)
        self.entry_search_prices.textChanged.connect(redirectFilter)
        self.combo_category_prices.currentIndexChanged.connect(redirectFilter)

        def filterItems():
            # Get the text entered in the QLineEdit
            search_text = self.entry_search_prices.text().lower()
            # Disable resizing of the QListWidget
            self.list_items_prices.setUpdatesEnabled(True)
            self.list_items_prices.update()


            # Get the number of items in the list
            count = self.list_items_prices.count()

            # Loop through each item in the list
            for i in range(count):
                item = self.list_items_prices.item(i)
                item_unique_name = item.text()
                item_info = source.item_sp_dict.get(item_unique_name)
                if item_info is not None:
                    # Get the item's description and image URL from the dictionary
                    tag = item_info['tag']
                    if (self.combo_category_prices.currentText() != 'Any'):
                        # If the search text is in the item text, show the item; otherwise, hide it
                        if (search_text in item.text().lower()) and (tag == self.combo_category_prices.currentText()):
                            item.setHidden(False)
                        else:
                            item.setHidden(True)

                    else:
                        if (search_text in item.text().lower()):
                            item.setHidden(False)
                        else:
                            item.setHidden(True)

            # Re-enable resizing of the QListWidget
            self.list_items_prices.setUpdatesEnabled(True)
            self.list_items_prices.update()

            self.list_items_prices.verticalScrollBar().setValue(0)

    def get_price(self):

        if self.list_items_prices.currentItem() is None:
            QMessageBox.warning(self.frame, 'Error', 'Debes seleccionar un item de la lista')
            return
        
        item_name = self.list_items_prices.currentItem().text()      
        # Clear the table rows
        self.table_prices.clearContents()
        self.table_prices.setRowCount(0)

        for city_name in source.city_names:
            # Parameters for the request
            params = {
                'item': item_name,
                'locations': city_name,
                'qualities': '1'
            }
            # Trying to obtain the prices
            response = source.requests.get(f'{source.BASE_URL}{item_name}.json', params=params)
            data = response.json()
            if response.status_code == 200:
                for item_data in data:
                    # Extract the price data from the dictionary
                    price = item_data.get('sell_price_min')

                    # Add city and price to the table
                    row_position = self.table_prices.rowCount()
                    self.table_prices.insertRow(row_position)
                    self.table_prices.setItem(row_position, 0, QtWidgets.QTableWidgetItem(city_name))
                    self.table_prices.setItem(row_position, 1, QtWidgets.QTableWidgetItem(str(price)))
            else:
                return None


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_details_prices.setText(_translate("Dialog", "Detalles de precios"))
        item = self.table_prices.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Ciudad"))
        item = self.table_prices.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Precio"))
        self.lb_category_prices.setText(_translate("Dialog", "Categoría:"))
        self.bttn_search.setText(_translate("Dialog", "Buscar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_prices), _translate("Dialog", "Precios"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())