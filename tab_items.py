# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import logic as source
import requests

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
        self.lb_staticname.setGeometry(QtCore.QRect(10, 150, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.lb_staticname.setFont(font)
        self.lb_staticname.setObjectName("lb_staticname")
        self.lb_staticdescription = QtWidgets.QLabel(self.fr_details)
        self.lb_staticdescription.setGeometry(QtCore.QRect(10, 200, 81, 16))
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
        self.lb_name.setGeometry(QtCore.QRect(10, 170, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.lb_name.setFont(font)
        self.lb_name.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_name.setWordWrap(True)
        self.lb_name.setObjectName("lb_name")
        self.lb_description = QtWidgets.QLabel(self.fr_details)
        self.lb_description.setGeometry(QtCore.QRect(10, 220, 301, 61))
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

        #------------ don't touch ------------#
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #------------ before blowing it up ---------------#
        for item_unique_name, item_info in source.item_sp_dict.items():
            item_name = item_info['name']
            item_text = f"{item_name} ({item_unique_name})"
            self.list_items.addItem(item_text)
        self.combo_category.addItems(source.unique_tags)


        def combo_changed():
            tag_selected = self.combo_category.currentText().lower()
            filter_items()

        self.combo_category.currentIndexChanged.connect(combo_changed)
        
        def filter_items():
            # Get the text entered in the QLineEdit
            search_text = self.entry_search.text().lower()

            # Disable resizing of the QListWidget
            self.list_items.setUpdatesEnabled(False)

            # Store the current scroll position
            scroll_pos = self.list_items.verticalScrollBar().value()

            # Iterate over all items in the QListWidget
            for row in range(self.list_items.count()):
                item = self.list_items.item(row)
                item_name2 = item.text()
                # Get the item text
                item_text = item.text().lower()
                # Retrieve item information from dictionary using Name
                # Split item_name into its name and unique name components
                if item_name2.count('(') == 2:
                    item_name2, item_unique_name = item_name2.rsplit(' (', 1)
                else:
                    item_name2, item_unique_name = item_name2.split(' (', 1)

                item_unique_name = item_unique_name[:-1]
                item_info = source.item_sp_dict.get(item_unique_name)
                if item_info is not None:
                    # Get the item's description and image URL from the dictionary
                    tag = item_info['tag']
                    # If the search text is in the item text, show the item; otherwise, hide it
                    if (self.combo_category.currentText() != 'Any'):
                        if (search_text in item_text) and (tag == self.combo_category.currentText()):
                            item.setHidden(False)
                        else:
                            item.setHidden(True)

                    else:
                        if (search_text in item_text):
                            item.setHidden(False)
                        else:
                            item.setHidden(True)

            # Re-enable resizing of the QListWidget
            self.list_items.setUpdatesEnabled(True)
            self.list_items.update()

            # Set the scroll position to the top of the list
            self.list_items.verticalScrollBar().setValue(0)
            

        # Connect the filter_items function to the textChanged signal of the QLineEdit
        self.entry_search.textChanged.connect(filter_items)

        
        def show_details():
            # Get the index of the currently selected item in the list
            index = self.list_items.currentRow()

            # Get the text of the currently selected item
            item_name = self.list_items.item(index).text()

            # Retrieve item information from dictionary using Name
            # Split item_name into its name and unique name components
            if item_name.count('(') == 2:
                item_name, item_unique_name = item_name.rsplit(' (', 1)
            else:
                item_name, item_unique_name = item_name.split(' (', 1)

            item_unique_name = item_unique_name[:-1]
            item_info = source.item_sp_dict.get(item_unique_name)

            if item_info is not None:
                # Get the item's description and image URL from the dictionary
                tag = item_info['tag']
                description = item_info['description']
                image_url = item_info['image']

                # Download the image data from the URL
                response = requests.get(image_url)
                pixmap = None

                if response.status_code == 200:
                    # Convert the image data into a QPixmap object
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(response.content)

                    # Update the QLabel widgets with the item's name, description, and image
                    self.lb_name.setText(item_name)
                    self.lb_description.setText(description)

                    self.lb_img.clear()
                    self.lb_img.setPixmap(pixmap)
                else:
                    print("Failed to load image for item:", item_name)

        # Connect the show_details function to the currentRowChanged signal of the QListWidget
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
    ui = Ui_Dialog()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())