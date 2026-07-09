# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(831, 590)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.horizontalLayout_4 = QHBoxLayout(self.page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.mainCard = QFrame(self.page)
        self.mainCard.setObjectName(u"mainCard")
        self.mainCard.setStyleSheet(u"QFrame#mainCard {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;\n"
"}")
        self.mainCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainCard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.mainCard)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 9)
        self.titleLabel = QLabel(self.mainCard)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"color: #212121;\n"
"")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.titleLabel)

        self.descriptionLabel = QLabel(self.mainCard)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        sizePolicy.setHeightForWidth(self.descriptionLabel.sizePolicy().hasHeightForWidth())
        self.descriptionLabel.setSizePolicy(sizePolicy)
        self.descriptionLabel.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        self.descriptionLabel.setFont(font1)
        self.descriptionLabel.setStyleSheet(u"color: #212121;\n"
"")
        self.descriptionLabel.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_2.addWidget(self.descriptionLabel)

        self.choiseLabel = QLabel(self.mainCard)
        self.choiseLabel.setObjectName(u"choiseLabel")
        sizePolicy.setHeightForWidth(self.choiseLabel.sizePolicy().hasHeightForWidth())
        self.choiseLabel.setSizePolicy(sizePolicy)
        self.choiseLabel.setMinimumSize(QSize(773, 0))
        font2 = QFont()
        font2.setPointSize(16)
        self.choiseLabel.setFont(font2)
        self.choiseLabel.setStyleSheet(u"color: #212121;\n"
"")

        self.verticalLayout_2.addWidget(self.choiseLabel)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.buttonsFrame = QFrame(self.mainCard)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        self.buttonsFrame.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;\n"
"    border-radius: 8px;\n"
"    color: #212121;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #F0F8FF;\n"
"    border: 1px solid #0078D7;\n"
"    color: #0078D7;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #0078D7;\n"
"    color: #FFFFFF;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.buttonsFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.startButton = QPushButton(self.buttonsFrame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(True)
        self.startButton.setMinimumSize(QSize(280, 50))
        self.startButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.startButton, 0, 0, 1, 1)

        self.loadButton = QPushButton(self.buttonsFrame)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setMinimumSize(QSize(280, 50))
        self.loadButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.loadButton, 0, 1, 1, 1)

        self.randomButton = QPushButton(self.buttonsFrame)
        self.randomButton.setObjectName(u"randomButton")
        self.randomButton.setMinimumSize(QSize(280, 50))
        self.randomButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.randomButton, 1, 0, 1, 1)

        self.aboutButton = QPushButton(self.buttonsFrame)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setMinimumSize(QSize(280, 50))
        self.aboutButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.aboutButton, 1, 1, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.buttonsFrame)


        self.horizontalLayout_4.addWidget(self.mainCard)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u043b\u0438\u0436\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u0441\u0442\u0443\u043f\u0435\u043d\u0447\u0430\u0442\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0435\u0439", None))
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0430 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u0441\u0442\u0443\u043f\u0435\u043d\u0447\u0430\u0442\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438, \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\n"
"\u043f\u0440\u0438\u0431\u043b\u0438\u0436\u0430\u044e\u0449\u0435\u0439 \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u0438\u043d\u043e\u043c \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0433\u0435\u043d\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430.", None))
        self.choiseLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0434\u043d\u0443 \u0438\u0437 \u043e\u043f\u0446\u0438\u0439:", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0432\u0440\u0443\u0447\u043d\u0443\u044e", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.randomButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u0430\u044f \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.aboutButton.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
    # retranslateUi

