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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.welcomePage = QWidget()
        self.welcomePage.setObjectName(u"welcomePage")
        self.horizontalLayout_4 = QHBoxLayout(self.welcomePage)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mainCard = QFrame(self.welcomePage)
        self.mainCard.setObjectName(u"mainCard")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainCard.sizePolicy().hasHeightForWidth())
        self.mainCard.setSizePolicy(sizePolicy)
        self.mainCard.setMinimumSize(QSize(800, 0))
        self.mainCard.setStyleSheet(u"QFrame#mainCard {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;\n"
"}")
        self.mainCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.mainCard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.mainCard)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.titleLabel = QLabel(self.mainCard)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy1)
        self.titleLabel.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet(u"color: #212121;\n"
"")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.titleLabel)

        self.descriptionLabel = QLabel(self.mainCard)
        self.descriptionLabel.setObjectName(u"descriptionLabel")
        sizePolicy1.setHeightForWidth(self.descriptionLabel.sizePolicy().hasHeightForWidth())
        self.descriptionLabel.setSizePolicy(sizePolicy1)
        self.descriptionLabel.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(False)
        self.descriptionLabel.setFont(font1)
        self.descriptionLabel.setStyleSheet(u"color: #212121;\n"
"")
        self.descriptionLabel.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.descriptionLabel)

        self.choiseLabel = QLabel(self.mainCard)
        self.choiseLabel.setObjectName(u"choiseLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.choiseLabel.sizePolicy().hasHeightForWidth())
        self.choiseLabel.setSizePolicy(sizePolicy2)
        self.choiseLabel.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(16)
        self.choiseLabel.setFont(font2)
        self.choiseLabel.setStyleSheet(u"color: #212121;\n"
"")

        self.verticalLayout.addWidget(self.choiseLabel)


        self.verticalLayout_5.addLayout(self.verticalLayout)

        self.buttonsFrame = QFrame(self.mainCard)
        self.buttonsFrame.setObjectName(u"buttonsFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.buttonsFrame.sizePolicy().hasHeightForWidth())
        self.buttonsFrame.setSizePolicy(sizePolicy3)
        self.buttonsFrame.setMinimumSize(QSize(780, 287))
        self.buttonsFrame.setToolTipDuration(0)
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
        self.layoutWidget = QWidget(self.buttonsFrame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 30, 751, 241))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(35)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.randomButton = QPushButton(self.layoutWidget)
        self.randomButton.setObjectName(u"randomButton")
        self.randomButton.setMinimumSize(QSize(280, 50))
        self.randomButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.randomButton, 2, 0, 1, 1)

        self.startButton = QPushButton(self.layoutWidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setEnabled(True)
        self.startButton.setMinimumSize(QSize(280, 50))
        self.startButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.startButton, 0, 0, 1, 1)

        self.loadButton = QPushButton(self.layoutWidget)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setMinimumSize(QSize(280, 50))
        self.loadButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.loadButton, 0, 1, 1, 1)

        self.aboutButton = QPushButton(self.layoutWidget)
        self.aboutButton.setObjectName(u"aboutButton")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.aboutButton.sizePolicy().hasHeightForWidth())
        self.aboutButton.setSizePolicy(sizePolicy4)
        self.aboutButton.setMinimumSize(QSize(280, 50))
        self.aboutButton.setToolTipDuration(0)
        self.aboutButton.setStyleSheet(u"")

        self.gridLayout.addWidget(self.aboutButton, 2, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.buttonsFrame)


        self.horizontalLayout_4.addWidget(self.mainCard)

        self.stackedWidget.addWidget(self.welcomePage)
        self.startPage = QWidget()
        self.startPage.setObjectName(u"startPage")
        self.verticalLayout_4 = QVBoxLayout(self.startPage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.inputCard = QFrame(self.startPage)
        self.inputCard.setObjectName(u"inputCard")
        self.inputCard.setStyleSheet(u"QFrame#inputCard {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;\n"
"}")
        self.inputCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.inputCard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.inputCard)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, 0, 0)
        self.descriptionParamLabel = QLabel(self.inputCard)
        self.descriptionParamLabel.setObjectName(u"descriptionParamLabel")
        sizePolicy1.setHeightForWidth(self.descriptionParamLabel.sizePolicy().hasHeightForWidth())
        self.descriptionParamLabel.setSizePolicy(sizePolicy1)
        self.descriptionParamLabel.setMinimumSize(QSize(0, 70))
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(False)
        self.descriptionParamLabel.setFont(font3)
        self.descriptionParamLabel.setStyleSheet(u"color: #212121;\n"
"")
        self.descriptionParamLabel.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.descriptionParamLabel.setMargin(11)

        self.verticalLayout_3.addWidget(self.descriptionParamLabel)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(11, -1, 11, -1)
        self.stepsLabel = QLabel(self.inputCard)
        self.stepsLabel.setObjectName(u"stepsLabel")
        sizePolicy1.setHeightForWidth(self.stepsLabel.sizePolicy().hasHeightForWidth())
        self.stepsLabel.setSizePolicy(sizePolicy1)
        self.stepsLabel.setMinimumSize(QSize(0, 50))
        font4 = QFont()
        font4.setPointSize(16)
        font4.setBold(False)
        self.stepsLabel.setFont(font4)
        self.stepsLabel.setStyleSheet(u"color: #212121;\n"
"")
        self.stepsLabel.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.stepsLabel, 4, 0, 1, 1)

        self.beginnigIntLabel = QLabel(self.inputCard)
        self.beginnigIntLabel.setObjectName(u"beginnigIntLabel")
        sizePolicy1.setHeightForWidth(self.beginnigIntLabel.sizePolicy().hasHeightForWidth())
        self.beginnigIntLabel.setSizePolicy(sizePolicy1)
        self.beginnigIntLabel.setMinimumSize(QSize(0, 50))
        self.beginnigIntLabel.setFont(font4)
        self.beginnigIntLabel.setStyleSheet(u"color: #212121;\n"
"")
        self.beginnigIntLabel.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.beginnigIntLabel, 2, 0, 1, 1)

        self.endIntSpinBox = QSpinBox(self.inputCard)
        self.endIntSpinBox.setObjectName(u"endIntSpinBox")
        self.endIntSpinBox.setFont(font4)
        self.endIntSpinBox.setStyleSheet(u"QSpinBox, QDoubleSpinBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus {\n"
"    border: 1px solid rgb(38, 162, 105);\n"
"}")
        self.endIntSpinBox.setMinimum(1)
        self.endIntSpinBox.setMaximum(10)

        self.gridLayout_2.addWidget(self.endIntSpinBox, 3, 1, 1, 1)

        self.degSpinBox = QSpinBox(self.inputCard)
        self.degSpinBox.setObjectName(u"degSpinBox")
        self.degSpinBox.setFont(font4)
        self.degSpinBox.setStyleSheet(u"QSpinBox, QDoubleSpinBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus {\n"
"    border: 1px solid rgb(38, 162, 105);\n"
"}")
        self.degSpinBox.setMinimum(1)
        self.degSpinBox.setMaximum(8)

        self.gridLayout_2.addWidget(self.degSpinBox, 0, 1, 1, 1)

        self.coefLabel = QLabel(self.inputCard)
        self.coefLabel.setObjectName(u"coefLabel")
        sizePolicy1.setHeightForWidth(self.coefLabel.sizePolicy().hasHeightForWidth())
        self.coefLabel.setSizePolicy(sizePolicy1)
        self.coefLabel.setMinimumSize(QSize(0, 50))
        self.coefLabel.setFont(font4)
        self.coefLabel.setStyleSheet(u"color: #212121;\n"
"")
        self.coefLabel.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.coefLabel, 1, 0, 1, 1)

        self.degLabel_ = QLabel(self.inputCard)
        self.degLabel_.setObjectName(u"degLabel_")
        sizePolicy1.setHeightForWidth(self.degLabel_.sizePolicy().hasHeightForWidth())
        self.degLabel_.setSizePolicy(sizePolicy1)
        self.degLabel_.setMinimumSize(QSize(0, 50))
        self.degLabel_.setFont(font4)
        self.degLabel_.setStyleSheet(u"color: #212121;\n"
"")
        self.degLabel_.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.degLabel_, 0, 0, 1, 1)

        self.stepsSpinBox = QSpinBox(self.inputCard)
        self.stepsSpinBox.setObjectName(u"stepsSpinBox")
        self.stepsSpinBox.setFont(font4)
        self.stepsSpinBox.setStyleSheet(u"QSpinBox, QDoubleSpinBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus {\n"
"    border: 1px solid rgb(38, 162, 105);\n"
"}")
        self.stepsSpinBox.setMinimum(10)
        self.stepsSpinBox.setMaximum(35)

        self.gridLayout_2.addWidget(self.stepsSpinBox, 4, 1, 1, 1)

        self.beginnigIntSpinBox = QSpinBox(self.inputCard)
        self.beginnigIntSpinBox.setObjectName(u"beginnigIntSpinBox")
        self.beginnigIntSpinBox.setFont(font4)
        self.beginnigIntSpinBox.setStyleSheet(u"QSpinBox, QDoubleSpinBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #CCCCCC;\n"
"    border-radius: 4px;\n"
"    color: #000000;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QSpinBox:focus, QDoubleSpinBox:focus {\n"
"    border: 1px solid rgb(38, 162, 105);\n"
"}")
        self.beginnigIntSpinBox.setMinimum(-10)
        self.beginnigIntSpinBox.setMaximum(0)

        self.gridLayout_2.addWidget(self.beginnigIntSpinBox, 2, 1, 1, 1)

        self.coefLineEdit = QLineEdit(self.inputCard)
        self.coefLineEdit.setObjectName(u"coefLineEdit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(40)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.coefLineEdit.sizePolicy().hasHeightForWidth())
        self.coefLineEdit.setSizePolicy(sizePolicy5)
        self.coefLineEdit.setMinimumSize(QSize(500, 26))
        self.coefLineEdit.setStyleSheet(u"QLineEdit {\n"
"    background-color: #FFFFFF;    \n"
"    border: 1px solid #DCDCDC; \n"
"    border-radius: 6px;\n"
"    color: #212121;\n"
"    padding: 6px 10px;\n"
"    font-size: 11pt;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(38, 162, 105);\n"
"}")

        self.gridLayout_2.addWidget(self.coefLineEdit, 1, 1, 1, 1)

        self.endIntLabel = QLabel(self.inputCard)
        self.endIntLabel.setObjectName(u"endIntLabel")
        sizePolicy1.setHeightForWidth(self.endIntLabel.sizePolicy().hasHeightForWidth())
        self.endIntLabel.setSizePolicy(sizePolicy1)
        self.endIntLabel.setMinimumSize(QSize(0, 50))
        self.endIntLabel.setFont(font4)
        self.endIntLabel.setStyleSheet(u"color: #212121;\n"
"")
        self.endIntLabel.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.endIntLabel, 3, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(230)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(11, -1, 22, 20)
        self.backButton_1 = QPushButton(self.inputCard)
        self.backButton_1.setObjectName(u"backButton_1")
        self.backButton_1.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.backButton_1.sizePolicy().hasHeightForWidth())
        self.backButton_1.setSizePolicy(sizePolicy4)
        self.backButton_1.setMinimumSize(QSize(280, 50))
        self.backButton_1.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid rgb(224, 27, 36);\n"
"    border-radius: 8px;\n"
"    color: #212121;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 176, 176);\n"
"    border: 1px solid rgb(224, 27, 36);\n"
"    color: rgb(224, 27, 36);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 27, 36);\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_2.addWidget(self.backButton_1)

        self.nextButton_1 = QPushButton(self.inputCard)
        self.nextButton_1.setObjectName(u"nextButton_1")
        sizePolicy4.setHeightForWidth(self.nextButton_1.sizePolicy().hasHeightForWidth())
        self.nextButton_1.setSizePolicy(sizePolicy4)
        self.nextButton_1.setMinimumSize(QSize(280, 50))
        self.nextButton_1.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid rgb(38, 162, 105);\n"
"    border-radius: 8px;\n"
"    color: #212121;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color:rgb(206, 255, 232);\n"
"    border: 1px solid rgb(38, 162, 105);\n"
"    color: rgb(38, 162, 105);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(38, 162, 105);\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_2.addWidget(self.nextButton_1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.inputCard)

        self.stackedWidget.addWidget(self.startPage)
        self.aboutPage = QWidget()
        self.aboutPage.setObjectName(u"aboutPage")
        self.aboutCard = QFrame(self.aboutPage)
        self.aboutCard.setObjectName(u"aboutCard")
        self.aboutCard.setGeometry(QRect(0, 0, 800, 600))
        self.aboutCard.setStyleSheet(u"QFrame#aboutCard {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #E0E0E0;\n"
"}")
        self.aboutCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.aboutCard.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.aboutCard)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.descriptionParamLabel_2 = QLabel(self.aboutCard)
        self.descriptionParamLabel_2.setObjectName(u"descriptionParamLabel_2")
        sizePolicy1.setHeightForWidth(self.descriptionParamLabel_2.sizePolicy().hasHeightForWidth())
        self.descriptionParamLabel_2.setSizePolicy(sizePolicy1)
        self.descriptionParamLabel_2.setMinimumSize(QSize(0, 70))
        self.descriptionParamLabel_2.setFont(font3)
        self.descriptionParamLabel_2.setStyleSheet(u"color: #212121;\n"
"")
        self.descriptionParamLabel_2.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.descriptionParamLabel_2.setMargin(11)

        self.verticalLayout_10.addWidget(self.descriptionParamLabel_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)

        self.verticalSpacer_3 = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.taskDescription = QLabel(self.aboutCard)
        self.taskDescription.setObjectName(u"taskDescription")
        self.taskDescription.setFont(font2)
        self.taskDescription.setStyleSheet(u"color: #212121;\n"
"")
        self.taskDescription.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_9.addWidget(self.taskDescription)

        self.authors = QLabel(self.aboutCard)
        self.authors.setObjectName(u"authors")
        self.authors.setFont(font2)
        self.authors.setStyleSheet(u"color: #212121;\n"
"")

        self.verticalLayout_9.addWidget(self.authors)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(6, -1, 0, 20)
        self.backButton_2 = QPushButton(self.aboutCard)
        self.backButton_2.setObjectName(u"backButton_2")
        self.backButton_2.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.backButton_2.sizePolicy().hasHeightForWidth())
        self.backButton_2.setSizePolicy(sizePolicy3)
        self.backButton_2.setMinimumSize(QSize(280, 50))
        self.backButton_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.backButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid rgb(224, 27, 36);\n"
"    border-radius: 8px;\n"
"    color: #212121;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 176, 176);\n"
"    border: 1px solid rgb(224, 27, 36);\n"
"    color: rgb(224, 27, 36);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(224, 27, 36);\n"
"    color: #FFFFFF;\n"
"}")

        self.horizontalLayout_3.addWidget(self.backButton_2, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.stackedWidget.addWidget(self.aboutPage)
        self.algoritmPage = QWidget()
        self.algoritmPage.setObjectName(u"algoritmPage")
        self.stackedWidget.addWidget(self.algoritmPage)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u043b\u0438\u0436\u0435\u043d\u0438\u0435 \u0441\u0442\u0443\u043f\u0435\u043d\u0447\u0430\u0442\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0435\u0439", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0431\u043b\u0438\u0436\u0435\u043d\u0438\u0435 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0438\u0430\u043b\u044c\u043d\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 \u0441\u0442\u0443\u043f\u0435\u043d\u0447\u0430\u0442\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0435\u0439", None))
        self.descriptionLabel.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430 \u043f\u0440\u0435\u0434\u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0430 \u0434\u043b\u044f \u043f\u043e\u0438\u0441\u043a\u0430 \u0441\u0442\u0443\u043f\u0435\u043d\u0447\u0430\u0442\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438, \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u043e\n"
"\u043f\u0440\u0438\u0431\u043b\u0438\u0436\u0430\u044e\u0449\u0435\u0439 \u0437\u0430\u0434\u0430\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u0438\u043d\u043e\u043c \u0441 \u043f\u043e\u043c\u043e\u0449\u044c\u044e \u0433\u0435\u043d\u0435\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0430\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u0430.", None))
        self.choiseLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0434\u043d\u0443 \u0438\u0437 \u043e\u043f\u0446\u0438\u0439:", None))
        self.randomButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u0443\u0447\u0430\u0439\u043d\u0430\u044f \u0433\u0435\u043d\u0435\u0440\u0430\u0446\u0438\u044f \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0432\u0440\u0443\u0447\u043d\u0443\u044e", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0434\u0430\u043d\u043d\u044b\u0435 \u0438\u0437 \u0444\u0430\u0439\u043b\u0430", None))
        self.aboutButton.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435", None))
        self.descriptionParamLabel.setText(QCoreApplication.translate("MainWindow", u" \u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0437\u0430\u0434\u0430\u0447\u0438:", None))
        self.stepsLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439:", None))
        self.beginnigIntLabel.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u043e \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430:", None))
        self.coefLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u044d\u0444\u0444\u0438\u0446\u0438\u0435\u043d\u0442\u044b:", None))
        self.degLabel_.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0435\u043f\u0435\u043d\u044c \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430:", None))
        self.coefLineEdit.setText("")
        self.endIntLabel.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043d\u0435\u0446 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0430:", None))
        self.backButton_1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.nextButton_1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043f\u0435\u0440\u0435\u0434", None))
        self.descriptionParamLabel_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0435:", None))
        self.taskDescription.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0441\u043b\u043e\u0432\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438: \n"
" \u0414\u043b\u044f \u0437\u0430\u0434\u0430\u043d\u043d\u043e\u0433\u043e \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0430 f(x) (\u0441\u0442\u0435\u043f\u0435\u043d\u044c \u043d\u0435 \u0431\u043e\u043b\u044c\u0448\u0435 8) \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043d\u0430\u0439\u0442\u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b\n"
" \u0441\u0442\u0443\u043f\u0435\u043d\u0447\u0430\u0442\u043e\u0439 \u0444\u0443\u043d\u043a\u0446\u0438\u0438 g(x) (\u0432\u044b\u0441\u043e\u0442\u0430 \u201c\u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439\u201d), \u043a\u043e\u0442\u043e\u0440\u0430\u044f \u043f\u0440\u0438\u0431\u043b\u0438\u0436\u0430\u0435\u0442 \u043f\u043e\u043b\u0438\u043d\u043e\u043c\u0438\u0430\u043b\u044c\u043d\u0443\u044e\n"
" \u0444\u0443\u043d\u043a\u0446\u0438\u044e, \u0442\u043e \u0435\u0441\u0442\u044c \u043c\u0438\u043d\u0438\u043c\u0438\u0437\u0438\u0440\u043e\u0432\u0430"
                        "\u0442\u044c \u0440\u0430\u0441\u0441\u0442\u043e\u044f\u043d\u0438\u0435 |f(x) - g(x)| \u043c\u0435\u0436\u0434\u0443 \u0444\u0443\u043d\u043a\u0446\u0438\u044f\u043c\u0438 \u043d\u0430\n"
" \u0437\u0430\u0434\u0430\u043d\u043d\u043e\u043c \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b\u0435 [l, r]. \u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0443\u043f\u0435\u043d\u0435\u0439 \u0432\u0432\u043e\u0434\u044f\u0442\u0441\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u043c.\n"
"", None))
        self.authors.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u0440\u044b: \n"
" \u0413\u0430\u0432\u0440\u0438\u0448 \u041c\u0430\u0442\u0432\u0435\u0439 - SuperNeonZ\n"
" \u0422\u0440\u0443\u0448\u043a\u0438\u043d \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 - Trushkin-Alexandr\n"
" \u0428\u0443\u0432\u0430\u043b\u043e\u0432 \u0410\u043b\u0435\u043a\u0441\u0435\u0439 - AlekseyShuvalov", None))
        self.backButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi