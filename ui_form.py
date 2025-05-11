# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(978, 755)
        Widget.setMouseTracking(True)
        Widget.setStyleSheet(u"\n"
"        background-color: #ccc;    /* White background for table cells */\n"
"        color: #000;               /* Black text in cells */\n"
"        font-family: \"Segoe UI\";\n"
"        font-size: 10pt;\n"
"    ")
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(670, 30, 80, 25))
        self.pushButton.setStyleSheet(u"\n"
"    color: #000;              /* black text */\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;")
        self.tableWidget = QTableWidget(Widget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(50, 80, 901, 651))
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setStyleSheet(u" background-color: #fff;    /* White background for table cells */")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(480, 30, 181, 25))
        self.lineEdit.setStyleSheet(u"background-color: #fff;   /* white background */\n"
"    color: #000;              /* black text */\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;")
        self.pushButton_SelectFile = QPushButton(Widget)
        self.pushButton_SelectFile.setObjectName(u"pushButton_SelectFile")
        self.pushButton_SelectFile.setGeometry(QRect(240, 30, 111, 25))
        self.lineEdit_2 = QLineEdit(Widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 30, 181, 25))
        self.lineEdit_2.setStyleSheet(u"background-color: #fff;   /* white background */\n"
"    color: #000;              /* black text */\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12pt;")

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Search", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Sheet", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Summary", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Widget", u"Price", None));
        self.pushButton_SelectFile.setText(QCoreApplication.translate("Widget", u"Select File", None))
    # retranslateUi

