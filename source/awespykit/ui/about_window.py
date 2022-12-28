# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_about_window(object):
    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.setWindowModality(QtCore.Qt.WindowModal)
        about_window.resize(428, 476)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        about_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(about_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.uiGroupBox_app_name = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.uiGroupBox_app_name.setFont(font)
        self.uiGroupBox_app_name.setObjectName("uiGroupBox_app_name")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiGroupBox_app_name)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_app_description = QtWidgets.QLabel(self.uiGroupBox_app_name)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_app_description.setFont(font)
        self.label_app_description.setWordWrap(True)
        self.label_app_description.setObjectName("label_app_description")
        self.verticalLayout.addWidget(self.label_app_description)
        self.line = QtWidgets.QFrame(self.uiGroupBox_app_name)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.uiGroupBox_app_name)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.uiLabel_app_version = QtWidgets.QLabel(self.uiGroupBox_app_name)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.uiLabel_app_version.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.uiLabel_app_version.setFont(font)
        self.uiLabel_app_version.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uiLabel_app_version.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.uiLabel_app_version.setObjectName("uiLabel_app_version")
        self.gridLayout.addWidget(self.uiLabel_app_version, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.uiGroupBox_app_name)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.uiLabel_authors = QtWidgets.QLabel(self.uiGroupBox_app_name)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.uiLabel_authors.setFont(font)
        self.uiLabel_authors.setObjectName("uiLabel_authors")
        self.gridLayout.addWidget(self.uiLabel_authors, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.uiGroupBox_app_name)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.uiLabel_license = QtWidgets.QLabel(self.uiGroupBox_app_name)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.uiLabel_license.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.uiLabel_license.setFont(font)
        self.uiLabel_license.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uiLabel_license.setObjectName("uiLabel_license")
        self.gridLayout.addWidget(self.uiLabel_license, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.uiGroupBox_app_name)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiLabel_source_github = QtWidgets.QLabel(self.uiGroupBox_app_name)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.uiLabel_source_github.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.uiLabel_source_github.setFont(font)
        self.uiLabel_source_github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uiLabel_source_github.setObjectName("uiLabel_source_github")
        self.horizontalLayout.addWidget(self.uiLabel_source_github)
        self.uiLabel_source_gitee = QtWidgets.QLabel(self.uiGroupBox_app_name)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.uiLabel_source_gitee.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.uiLabel_source_gitee.setFont(font)
        self.uiLabel_source_gitee.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uiLabel_source_gitee.setObjectName("uiLabel_source_gitee")
        self.horizontalLayout.addWidget(self.uiLabel_source_gitee)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.uiGroupBox_app_name)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiLabel_issue_github = QtWidgets.QLabel(self.uiGroupBox_app_name)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.uiLabel_issue_github.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.uiLabel_issue_github.setFont(font)
        self.uiLabel_issue_github.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uiLabel_issue_github.setObjectName("uiLabel_issue_github")
        self.horizontalLayout_2.addWidget(self.uiLabel_issue_github)
        self.uiLabel_issue_gitee = QtWidgets.QLabel(self.uiGroupBox_app_name)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.uiLabel_issue_gitee.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.uiLabel_issue_gitee.setFont(font)
        self.uiLabel_issue_gitee.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.uiLabel_issue_gitee.setObjectName("uiLabel_issue_gitee")
        self.horizontalLayout_2.addWidget(self.uiLabel_issue_gitee)
        self.horizontalLayout_2.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 4, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.uiGroupBox_app_name)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.uiPlainTextEdit_open_packages = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.uiPlainTextEdit_open_packages.setFont(font)
        self.uiPlainTextEdit_open_packages.setReadOnly(True)
        self.uiPlainTextEdit_open_packages.setObjectName("uiPlainTextEdit_open_packages")
        self.verticalLayout_2.addWidget(self.uiPlainTextEdit_open_packages)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        about_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "关于"))
        self.uiGroupBox_app_name.setTitle(_translate("about_window", "Awespykit"))
        self.label_app_description.setText(_translate("about_window", "Awespykit 是一个关于 Python 的工具箱程序，主要是为 Python 的包管理工具 pip 和 Python 程序打包工具 PyInstaller 封装图形用户界面，目前提供了 4 个工具：Python 包管理器、程序打包工具、Pip 源设置工具、模块安装包下载器。"))
        self.label.setText(_translate("about_window", "程序版本："))
        self.uiLabel_app_version.setText(_translate("about_window", "Awespykit - 1.0.0"))
        self.label_3.setText(_translate("about_window", "作者："))
        self.uiLabel_authors.setText(_translate("about_window", "hrpzcf"))
        self.label_2.setText(_translate("about_window", "开源协议："))
        self.uiLabel_license.setText(_translate("about_window", "GNU General Public License v3"))
        self.label_7.setText(_translate("about_window", "源代码："))
        self.uiLabel_source_github.setText(_translate("about_window", "GitHub、"))
        self.uiLabel_source_gitee.setText(_translate("about_window", "Gitee"))
        self.label_8.setText(_translate("about_window", "问题反馈："))
        self.uiLabel_issue_github.setText(_translate("about_window", "GitHub Issues、"))
        self.uiLabel_issue_gitee.setText(_translate("about_window", "Gitee Issues"))
        self.label_11.setText(_translate("about_window", "使用的开源库："))
        self.uiPlainTextEdit_open_packages.setPlainText(_translate("about_window", "名称：chardet\n"
"版本：>=4.0.0\n"
"开源协议：LGPL-2.1 license\n"
"主页：https://github.com/chardet/chardet\n"
"描述：用于探测编码不明的文本文件的正确编码\n"
"\n"
"名称：PyQt5\n"
"版本：>=5.15.2,<6.0\n"
"开源协议：GPL v3\n"
"主页：https://www.riverbankcomputing.com/software/pyqt/\n"
"描述：用于构建本程序界面的图形界面库\n"
"\n"
"名称：fastpip\n"
"版本：>=1.6.0,<2.0\n"
"开源协议：MIT License\n"
"主页：https://github.com/hrpzcf/fastpip\n"
"描述：封装 Python 环境及包管理工具 Pip\n"
"\n"
"名称：pywin32\n"
"版本：>=224\n"
"开源协议：Python Software Foundation License\n"
"主页：https://github.com/mhammond/pywin32\n"
"描述：用于在 Windows 系统上调用系统接口打开资源管理器\n"
"\n"
"名称：qt-material\n"
"版本：>=2.12\n"
"开源协议：BSD-2-Clause License\n"
"主页：https://github.com/UN-GCPDS/qt-material\n"
"描述：PyQt 样式库（本程序主题菜单中名称以 \'dark_\' 和 \'light_\' 起始的主题的出处）\n"
"如果您以 pip 命令的方式安装本程序，主题菜单中没有以上括号内描述的主题，请安装 qt-material 包到本程序的运行环境中后重启本程序\n"
"\n"
"名称：QDarkStyle\n"
"版本：>=3.1\n"
"开源协议：MIT License\n"
"主页：https://github.com/ColinDuquesnoy/QDarkStyleSheet\n"
"描述：PyQt 样式库（本程序主题菜单中名称 QDarkStyle 主题的出处）\n"
"如果您以 pip 命令的方式安装本程序，主题菜单中没有 QDarkStyle 主题，请安装 QDarkStyle 包到本程序的运行环境中后重启本程序"))
