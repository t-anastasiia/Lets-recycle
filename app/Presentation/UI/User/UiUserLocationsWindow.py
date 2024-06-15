from PyQt6 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_UserLocationsWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.placeForMap = QtWebEngineWidgets.QWebEngineView(parent=self.centralwidget)
        self.placeForMap.setObjectName("placeForMap")
        self.verticalLayout.addWidget(self.placeForMap)

        self.backButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(650, 10, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(11)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LocationWindow"))
        self.backButton.setText(_translate("MainWindow", "BACK"))
