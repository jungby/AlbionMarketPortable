# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
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
        self.tab_cities = QtWidgets.QWidget()
        self.tab_cities.setObjectName("tab_cities")
        self.fr_general_cities = QtWidgets.QFrame(self.tab_cities)
        self.fr_general_cities.setGeometry(QtCore.QRect(0, 0, 681, 341))
        self.fr_general_cities.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_general_cities.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_general_cities.setObjectName("fr_general_cities")
        self.list_cities = QtWidgets.QListWidget(self.fr_general_cities)
        self.list_cities.setGeometry(QtCore.QRect(10, 40, 321, 291))
        self.list_cities.setObjectName("list_cities")
        self.lb_filtro_city = QtWidgets.QLabel(self.fr_general_cities)
        self.lb_filtro_city.setGeometry(QtCore.QRect(10, 10, 55, 16))
        self.lb_filtro_city.setObjectName("lb_filtro_city")
        self.entry_search_city = QtWidgets.QLineEdit(self.fr_general_cities)
        self.entry_search_city.setGeometry(QtCore.QRect(70, 10, 261, 22))
        self.entry_search_city.setObjectName("entry_search_city")
        self.fr_details__city = QtWidgets.QFrame(self.fr_general_cities)
        self.fr_details__city.setGeometry(QtCore.QRect(360, 10, 321, 321))
        self.fr_details__city.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_details__city.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_details__city.setObjectName("fr_details__city")
        self.lb_staticname_city = QtWidgets.QLabel(self.fr_details__city)
        self.lb_staticname_city.setGeometry(QtCore.QRect(10, 170, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.lb_staticname_city.setFont(font)
        self.lb_staticname_city.setObjectName("lb_staticname_city")
        self.lb_staticdescription_city = QtWidgets.QLabel(self.fr_details__city)
        self.lb_staticdescription_city.setGeometry(QtCore.QRect(10, 220, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setBold(True)
        font.setWeight(75)
        self.lb_staticdescription_city.setFont(font)
        self.lb_staticdescription_city.setObjectName("lb_staticdescription_city")
        self.lb_img_city = QtWidgets.QLabel(self.fr_details__city)
        self.lb_img_city.setGeometry(QtCore.QRect(10, 40, 111, 111))
        self.lb_img_city.setText("")
        self.lb_img_city.setPixmap(QtGui.QPixmap("../../../../../Pictures/reactions/bb72016e-a8f2-407a-8ee9-854823e4f28c.png"))
        self.lb_img_city.setScaledContents(True)
        self.lb_img_city.setObjectName("lb_img_city")
        self.lb_details_city = QtWidgets.QLabel(self.fr_details__city)
        self.lb_details_city.setGeometry(QtCore.QRect(10, 10, 301, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lb_details_city.setFont(font)
        self.lb_details_city.setObjectName("lb_details_city")
        self.lb_name_city = QtWidgets.QLabel(self.fr_details__city)
        self.lb_name_city.setGeometry(QtCore.QRect(10, 190, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.lb_name_city.setFont(font)
        self.lb_name_city.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_name_city.setWordWrap(True)
        self.lb_name_city.setObjectName("lb_name_city")
        self.lb_description_city = QtWidgets.QLabel(self.fr_details__city)
        self.lb_description_city.setGeometry(QtCore.QRect(10, 240, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.lb_description_city.setFont(font)
        self.lb_description_city.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_description_city.setWordWrap(True)
        self.lb_description_city.setObjectName("lb_description_city")
        self.tabWidget.addTab(self.tab_cities, "")

        #------------ don't touch ------------#
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #------------ before blowing it up ---------------#
        for city_unique_name, city_info in sorted(source.city_sp_dict.items()):
            city_text = f"{city_unique_name}"
            self.list_cities.addItem(city_text)

        def filter_cities():
            # Get the text entered in the QLineEdit
            search_text = self.entry_search_city.text().lower()

            # Disable resizing of the QListWidget
            self.list_cities.setUpdatesEnabled(False)

            # Store the current scroll position
            scroll_pos = self.list_cities.verticalScrollBar().value()

            # Iterate over all items in the QListWidget
            for row in range(self.list_cities.count()):
                city = self.list_cities.item(row)

                # Get the item text
                city_text = city.text().lower()

                # If the search text is in the item text, show the item; otherwise, hide it
                if search_text in city_text:
                    city.setHidden(False)
                else:
                    city.setHidden(True)

            # Re-enable resizing of the QListWidget
            self.list_cities.setUpdatesEnabled(True)
            self.list_cities.update()

            # Connect to the scrollbar's valueChanged signal and update the position
            def update_scrollbar(value):
                self.list_cities.verticalScrollBar().setValue(scroll_pos)
            self.list_cities.verticalScrollBar().valueChanged.connect(update_scrollbar)

        # Connect the filter_cities function to the textChanged signal of the QLineEdit
        self.entry_search_city.textChanged.connect(filter_cities)

        
        def show_details():
            # Get the index of the currently selected city in the list
            index = self.list_cities.currentRow()

            # Get the text of the currently selected city
            city_name = self.list_cities.item(index).text()

            # Retrieve city information from dictionary using Name
            city_info = source.city_sp_dict.get(city_name)

            if city_info is not None:
                # Get the city's description and image URL from the dictionary
                description = city_info['description']
                # image_url = city_info['image']

                # Update the QLabel widgets with the city's name, description, and image
                self.lb_name_city.setText(city_name)
                self.lb_description_city.setText(description)

                # # Download the image data from the URL
                # response = requests.get(image_url)
                # pixmap = None

                # if response.status_code == 200:
                #     # Convert the image data into a QPixmap object
                #     pixmap = QtGui.QPixmap()
                #     pixmap.loadFromData(response.content)

                #     # Update the QLabel widgets with the item's name, description, and image
                #     self.lb_name.setText(city_name)
                #     self.lb_description.setText(description)

                #     self.lb_img.clear()
                #     self.lb_img.setPixmap(pixmap)
                # else:
                #     print("Failed to load image for item:", city_name)

        # Connect the show_details function to the currentRowChanged signal of the QListWidget
        self.list_cities.currentRowChanged.connect(show_details)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb_filtro_city.setText(_translate("Dialog", "Buscar:"))
        self.lb_staticname_city.setText(_translate("Dialog", "Nombre:"))
        self.lb_staticdescription_city.setText(_translate("Dialog", "Descripción:"))
        self.lb_details_city.setText(_translate("Dialog", "Detalles de ciudad"))
        self.lb_name_city.setText(_translate("Dialog", "TextLabel"))
        self.lb_description_city.setText(_translate("Dialog", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cities), _translate("Dialog", "Ciudades"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())