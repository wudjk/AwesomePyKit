# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'imports_check.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_imports_check(object):
    def setupUi(self, imports_check):
        imports_check.setObjectName("imports_check")
        imports_check.setWindowModality(QtCore.Qt.WindowModal)
        imports_check.resize(900, 500)
        self.centralwidget = QtWidgets.QWidget(imports_check)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.centralwidget.setFont(font)
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.le_cip_cur_env = QtWidgets.QLineEdit(self.centralwidget)
        self.le_cip_cur_env.setFrame(False)
        self.le_cip_cur_env.setReadOnly(True)
        self.le_cip_cur_env.setObjectName("le_cip_cur_env")
        self.horizontalLayout_2.addWidget(self.le_cip_cur_env)
        self.horizontalLayout_2.setStretch(1, 9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tw_missing_imports = QtWidgets.QTableWidget(self.centralwidget)
        self.tw_missing_imports.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tw_missing_imports.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tw_missing_imports.setObjectName("tw_missing_imports")
        self.tw_missing_imports.setColumnCount(3)
        self.tw_missing_imports.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_missing_imports.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_missing_imports.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_missing_imports.setHorizontalHeaderItem(2, item)
        self.tw_missing_imports.horizontalHeader().setHighlightSections(False)
        self.tw_missing_imports.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.tw_missing_imports)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pb_install_all_missing = QtWidgets.QPushButton(self.centralwidget)
        self.pb_install_all_missing.setObjectName("pb_install_all_missing")
        self.horizontalLayout.addWidget(self.pb_install_all_missing)
        self.pb_confirm = QtWidgets.QPushButton(self.centralwidget)
        self.pb_confirm.setObjectName("pb_confirm")
        self.horizontalLayout.addWidget(self.pb_confirm)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        imports_check.setCentralWidget(self.centralwidget)

        self.retranslateUi(imports_check)
        QtCore.QMetaObject.connectSlotsByName(imports_check)

    def retranslateUi(self, imports_check):
        _translate = QtCore.QCoreApplication.translate
        imports_check.setWindowTitle(_translate("imports_check", "环境检查"))
        self.label.setText(_translate("imports_check", "当前环境:"))
        item = self.tw_missing_imports.horizontalHeaderItem(0)
        item.setText(_translate("imports_check", "项目文件"))
        item = self.tw_missing_imports.horizontalHeaderItem(1)
        item.setText(_translate("imports_check", "文件导入项"))
        item = self.tw_missing_imports.horizontalHeaderItem(2)
        item.setText(_translate("imports_check", "环境缺失项"))
        self.pb_install_all_missing.setToolTip(_translate("imports_check", "一键安装该环境所有缺失的项目导入项。\n"
"注意，当缺失的导入项无法在该环境安装时，不会有错误提示。"))
        self.pb_install_all_missing.setText(_translate("imports_check", "一键安装"))
        self.pb_confirm.setToolTip(_translate("imports_check", "什么都不做，关闭窗口并返回。"))
        self.pb_confirm.setText(_translate("imports_check", "确定"))
