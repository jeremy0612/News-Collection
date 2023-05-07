# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceXWBhev.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
import os
import resources_rc
import openai


class Ui_MainWindow(object):
    def __ini__(self):
        super().__init__()
        self.data = None
        self.connection = None
        
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(843, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
      
        
        
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border : none;\n"
"	background-color: transparent;\n"
"	background:transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	\n"
"	color:rgb(25, 25, 25);\n"
"	font-family : Tahoma;\n"
"	\n"
"}\n"
"\n"
"#centralwidget{\n"
" 	background-color:rgb(37, 75, 55);\n"
"}\n"
"#leftMenuSubContainer{\n"
"	background-color: rgb(78, 158, 117);\n"
"}\n"
"#leftMenuSubContainer QPushButton {\n"
"	text-align: left;\n"
"	padding: 5px 10px;\n"
"	\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuSubContainer{\n"
"	background-color: rgb(60, 121, 89);\n"
"}\n"
"#frame_5{\n"
" background-color: rgb(78, 158, 117);\n"
"border-radius: 10px;\n"
"}\n"
"#headerContainer{\n"
" background-color:rgb(78, 158, 117);\n"
"}\n"
"/*///////////////QPushButton///////*/\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
""
                        "    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59,"
                        " 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(124, 249, 185);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"/* QPlainTextEdit/////////////////////////////"
                        "//////////////////////////////////////////////////*/\n"
"QPlainTextEdit {\n"
"	background-color:rgb(216, 216, 216);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	opacity: 0.8; /* Gi\u1ea3m \u0111\u1ed9 trong su\u1ed1t khi di chu\u1ed9t \u0111\u1ebfn \u0111\u1ed1i t\u01b0\u1ee3ng */\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"	opacity: 1.0; /* Kh\u00f4i ph\u1ee5c \u0111\u1ed9 trong su\u1ed1t khi \u0111\u1ed1i t\u01b0\u1ee3ng \u0111\u01b0\u1ee3c focus */\n"
"}\n"
"\n"
"\n"
"\n"
"#finding_data{\n"
"	background-color:rgb(66, 150, 105)\n"
"}\n"
"QPushButton:hover{\n"
" background-color: ;\n"
"cursor: pointer;\n"
"opacity: 0.8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"backgr"
                        "ound-color: rgb(105, 255, 185);\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(78, 158, 117);\n"
"	border-bottom: 1px solid rgbrgb(78, 158, 117);\n"
"       color: rgb(255 ,255,255);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(78, 158, 117);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(78, 158, 117);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(127, 255, 189);\n"
"       color: rgb(0,0,0);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(63, 126, 93);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(63, 126, 93);\n"
"}\n"
"\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33,"
                        " 37, 43);\n"
"	background-color: rgb(63, 126, 93);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"/*QTextBrowser/////////////////////////////////////////////////////////////////*/\n"
"\n"
"QTextBrowser{\n"
"	background-color:rgb(216, 216, 216);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QTextBrowser  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QTextBrowser QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QTextBrowser:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"	opacity: 0.8; /* Gi\u1ea3m \u0111\u1ed9 trong su\u1ed1t khi di chu\u1ed9t \u0111\u1ebfn \u0111\u1ed1i t\u01b0\u1ee3ng */\n"
"}\n"
"QTextBrowser:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"	opacity: 1.0; /* Kh\u00f4i ph\u1ee5c \u0111\u1ed9 trong su\u1ed1t khi \u0111\u1ed1"
                        "i t\u01b0\u1ee3ng \u0111\u01b0\u1ee3c focus */\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame)
        self.menuButton.setObjectName(u"menuButton")
        icon = QIcon()
        icon.addFile(u":/icons/images/feather/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuButton)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 9, 0, 0)
        self.homeButton = QPushButton(self.frame_2)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setStyleSheet(u"	/*background-color: rgb(66, 199, 199);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/feather/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeButton.setIcon(icon1)
        self.homeButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.homeButton)

        self.findButton = QPushButton(self.frame_2)
        self.findButton.setObjectName(u"findButton")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/feather/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.findButton.setIcon(icon2)
        self.findButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.findButton)

        self.dataButton = QPushButton(self.frame_2)
        self.dataButton.setObjectName(u"dataButton")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/feather/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dataButton.setIcon(icon3)
        self.dataButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.dataButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.settingButton = QPushButton(self.frame_2)
        self.settingButton.setObjectName(u"settingButton")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/feather/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingButton.setIcon(icon4)
        self.settingButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.settingButton)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 9, 9)
        self.infoButton = QPushButton(self.frame_3)
        self.infoButton.setObjectName(u"infoButton")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/feather/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoButton.setIcon(icon5)
        self.infoButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.infoButton)

        self.helpButton = QPushButton(self.frame_3)
        self.helpButton.setObjectName(u"helpButton")
        icon6 = QIcon()
        icon6.addFile(u":/icons/images/feather/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon6)
        self.helpButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpButton)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.mainBodyContainner = QWidget(self.centralwidget)
        self.mainBodyContainner.setObjectName(u"mainBodyContainner")
        sizePolicy.setHeightForWidth(self.mainBodyContainner.sizePolicy().hasHeightForWidth())
        self.mainBodyContainner.setSizePolicy(sizePolicy)
        self.mainBodyContainner.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.mainBodyContainner)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainner)
        self.headerContainer.setObjectName(u"headerContainer")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(15)
        self.headerContainer.setFont(font)
        self.horizontalLayout_5 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.headerContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 60))
        self.label_5.setPixmap(QPixmap(u":/images/images/zyro-image (2).png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamily(u"Tahoma")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_6)


        self.horizontalLayout_5.addWidget(self.frame_4, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon7 = QIcon()
        icon7.addFile(u":/icons/feather/share-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon8 = QIcon()
        icon8.addFile(u":/icons/feather/book.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_5)


        self.horizontalLayout_5.addWidget(self.frame_6, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.frame_7)
        self.minimizeButton.setObjectName(u"minimizeButton")
        icon9 = QIcon()
        icon9.addFile(u":/icons/feather/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon9)

        self.horizontalLayout_3.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.frame_7)
        self.restoreButton.setObjectName(u"restoreButton")
        icon10 = QIcon()
        icon10.addFile(u":/icons/feather/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon10)

        self.horizontalLayout_3.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.frame_7)
        self.closeButton.setObjectName(u"closeButton")
        icon11 = QIcon()
        icon11.addFile(u":/icons/feather/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon11)

        self.horizontalLayout_3.addWidget(self.closeButton)


        self.horizontalLayout_5.addWidget(self.frame_7, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.bodyContent = QWidget(self.mainBodyContainner)
        self.bodyContent.setObjectName(u"bodyContent")
        sizePolicy1.setHeightForWidth(self.bodyContent.sizePolicy().hasHeightForWidth())
        self.bodyContent.setSizePolicy(sizePolicy1)
        self.verticalLayout_9 = QVBoxLayout(self.bodyContent)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.bodyContent)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_10 = QVBoxLayout(self.home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.home)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(500, 500))
        self.label_7.setPixmap(QPixmap(u":/images/images/monleoto.png"))
        self.label_7.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_7)

        self.stackedWidget_2.addWidget(self.home)
        self.find_data = QWidget()
        self.find_data.setObjectName(u"find_data")
        self.verticalLayout_13 = QVBoxLayout(self.find_data)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.finding_data = QWidget(self.find_data)
        self.finding_data.setObjectName(u"finding_data")
        self.horizontalLayout_8 = QHBoxLayout(self.finding_data)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.findDataContaner = QWidget(self.finding_data)
        self.findDataContaner.setObjectName(u"findDataContaner")
        self.findDataContaner.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.findDataContaner)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_8 = QFrame(self.findDataContaner)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_8)
        self.label_8.setObjectName(u"label_8")
        font2 = QFont()
        font2.setFamily(u"Tahoma")
        font2.setPointSize(13)
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_8)


        self.verticalLayout_14.addWidget(self.frame_8)

        self.input_box = QFrame(self.findDataContaner)
        self.input_box.setObjectName(u"input_box")
        self.input_box.setStyleSheet(u"")
        self.input_box.setFrameShape(QFrame.StyledPanel)
        self.input_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.input_box)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.plainTextEdit = QPlainTextEdit(self.input_box)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout_14.addWidget(self.plainTextEdit)

        self.verticalScrollBar = QScrollBar(self.input_box)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.horizontalLayout_14.addWidget(self.verticalScrollBar)


        self.verticalLayout_14.addWidget(self.input_box)

        self.frame_10 = QFrame(self.findDataContaner)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        
        font3 = QFont()
        font3.setFamily(u"Tahoma")
        font3.setPointSize(12)
        
        icon12 = QIcon()
        icon12.addFile(u":/icons/feather/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        


        self.verticalLayout_14.addWidget(self.frame_10)


        self.horizontalLayout_8.addWidget(self.findDataContaner, 0, Qt.AlignLeft)

        self.data_response = QWidget(self.finding_data)
        self.data_response.setObjectName(u"data_response")
        self.data_response.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.data_response)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_9 = QFrame(self.data_response)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setFamily(u"Tahoma")
        font4.setPointSize(15)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setUnderline(False)
        font4.setWeight(50)
        font4.setStrikeOut(False)
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_9)


        self.verticalLayout_16.addWidget(self.frame_9, 0, Qt.AlignTop)

        self.frame_11 = QFrame(self.data_response)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.frame_11)
        self.textBrowser.setObjectName(u"textBrowser")

        self.horizontalLayout_13.addWidget(self.textBrowser)

        self.verticalScrollBar_2 = QScrollBar(self.frame_11)
        self.verticalScrollBar_2.setObjectName(u"verticalScrollBar_2")
        self.verticalScrollBar_2.setOrientation(Qt.Vertical)

        self.horizontalLayout_13.addWidget(self.verticalScrollBar_2)


        self.verticalLayout_16.addWidget(self.frame_11)


        self.horizontalLayout_8.addWidget(self.data_response)


        self.verticalLayout_13.addWidget(self.finding_data)

        self.widget_2 = QWidget(self.find_data)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_15 = QVBoxLayout(self.widget_2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.table_data = QTableWidget(self.widget_3)
        if (self.table_data.columnCount() < 5):
            self.table_data.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_data.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.table_data.rowCount() < 10):
            self.table_data.setRowCount(10)
        font5 = QFont()
        font5.setPointSize(12)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5)
        self.table_data.setItem(0, 0, __qtablewidgetitem4)
        self.table_data.setObjectName(u"table_data")
        self.table_data.setShowGrid(True)
        self.table_data.setSortingEnabled(False)
        self.table_data.setRowCount(10)
        self.table_data.setColumnCount(5)
        self.table_data.horizontalHeader().setVisible(True)
        self.table_data.horizontalHeader().setCascadingSectionResizes(True)
        self.table_data.verticalHeader().setVisible(True)
        #self.table_data.resizeRowsToContents()
        #self.table_data.resizeColumnsToContents()
        
        self.horizontalLayout_12.addWidget(self.table_data)
        self.widget_3.setLayout(self.horizontalLayout_12)
        
        self.verticalLayout_15.addWidget(self.widget_3)


        self.verticalLayout_13.addWidget(self.widget_2)

        self.stackedWidget_2.addWidget(self.find_data)

        self.verticalLayout_9.addWidget(self.stackedWidget_2)


        self.verticalLayout_8.addWidget(self.bodyContent)


        self.horizontalLayout.addWidget(self.mainBodyContainner)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
         #///////////BACK--END///////////////////////////////////////
        self.homeButton.clicked.connect(self.switch_widget1)
        self.findButton.clicked.connect(self.search_machine)
        self.dataButton.clicked.connect(self.summarise)
        #self.generate_table(self.data)

        #//////////////////////////////////////////////////////HÀM XỬ LÝ NÚT NHẤN/////////////////////////////////////////////////////////////

    def generate_table(self,data):
        for i, row in enumerate(data):
            item = QTableWidgetItem(str(row["Title"]))
            self.table_data.setItem(i, 0, item)
            item = QTableWidgetItem(str(row["Publish_Time"]))
            self.table_data.setItem(i, 1, item)
            item = QTableWidgetItem(str(row["Genre"]))
            self.table_data.setItem(i, 2, item)
            item = QTableWidgetItem(str(row["Content"]))
            self.table_data.setItem(i, 3, item)
            item = QTableWidgetItem(str(row["Author_Name"]))
            self.table_data.setItem(i, 4, item)
                # hiển thị widget bảng
        
    def search_machine(self):
        self.table_data.clearContents()
        search = self.plainTextEdit.toPlainText()
        query = "SELECT * FROM article WHERE Author_Name LIKE %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (search + '%',))
        result = cursor.fetchall()
        self.generate_table(result)
        # process the result
    def switch_widget1(self):
        current_index = int(self.stackedWidget_2.indexOf(self.find_data))
        self.stackedWidget_2.setCurrentIndex(current_index)
    def summarise(self):
        print("You are finding content relate : ",self.plainTextEdit.toPlainText())
        search = self.plainTextEdit.toPlainText()
     
        os.environ["OPENAI_API_KEY"] = "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"
        openai.api_key = os.getenv("OPENAI_API_KEY")

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Q:sumary " + search + "?\n A:",
        temperature=0,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
        )

        #print(response)
        result =response['choices'][0]['text']
        self.plainTextEdit.clear()
        self.textBrowser.setHtml(result)
    

    # thêm dữ liệu vào từng ô của bảng
    

        
        

    
    
    
    
    
    
    
    
    
    # setupUi


    def retranslateUi(self, MainWindow):
        
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuButton.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuButton.setText(QCoreApplication.translate("MainWindow", u"Menu ", None))
#if QT_CONFIG(tooltip)
        self.homeButton.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.findButton.setToolTip(QCoreApplication.translate("MainWindow", u"Find", None))
#endif // QT_CONFIG(tooltip)
        self.findButton.setText(QCoreApplication.translate("MainWindow", u"Find Document", None))
#if QT_CONFIG(tooltip)
        self.dataButton.setToolTip(QCoreApplication.translate("MainWindow", u"analyst", None))
#endif // QT_CONFIG(tooltip)
        self.dataButton.setText(QCoreApplication.translate("MainWindow", u"Data analyst", None))
#if QT_CONFIG(tooltip)
        self.settingButton.setToolTip(QCoreApplication.translate("MainWindow", u"setting", None))
#endif // QT_CONFIG(tooltip)
        self.settingButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.frame_3.setToolTip(QCoreApplication.translate("MainWindow", u"help", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.infoButton.setToolTip(QCoreApplication.translate("MainWindow", u"info", None))
#endif // QT_CONFIG(tooltip)
        self.infoButton.setText(QCoreApplication.translate("MainWindow", u"Infomation", None))
        self.helpButton.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"TEAM \u0110\u1ea6N", None))
        self.pushButton_4.setText("")
        self.pushButton_5.setText("")
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.label_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Input Box", None))
        self.plainTextEdit.setPlainText("")
        
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Output Box", None))
        ___qtablewidgetitem = self.table_data.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Title", None));
        ___qtablewidgetitem1 = self.table_data.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Publish Time", None));
        ___qtablewidgetitem2 = self.table_data.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtablewidgetitem3 = self.table_data.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Content", None));
        ___qtablewidgetitem4 = self.table_data.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Author", None));

        __sortingEnabled = self.table_data.isSortingEnabled()
        self.table_data.setSortingEnabled(False)
        self.table_data.setSortingEnabled(__sortingEnabled)


    # retranslateUi

