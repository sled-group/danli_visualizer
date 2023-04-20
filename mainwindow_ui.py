# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/data/simbot/simbot_visualizer/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1084, 853)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.rawObservationText = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rawObservationText.sizePolicy().hasHeightForWidth())
        self.rawObservationText.setSizePolicy(sizePolicy)
        self.rawObservationText.setObjectName("rawObservationText")
        self.verticalLayout.addWidget(self.rawObservationText)
        self.rawObservationDisplay = ScaledLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rawObservationDisplay.sizePolicy().hasHeightForWidth())
        self.rawObservationDisplay.setSizePolicy(sizePolicy)
        self.rawObservationDisplay.setMinimumSize(QtCore.QSize(600, 300))
        self.rawObservationDisplay.setObjectName("rawObservationDisplay")
        self.verticalLayout.addWidget(self.rawObservationDisplay)
        self.verticalLayout_10.addLayout(self.verticalLayout)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_10.addWidget(self.line_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.voxelSideViewText = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voxelSideViewText.sizePolicy().hasHeightForWidth())
        self.voxelSideViewText.setSizePolicy(sizePolicy)
        self.voxelSideViewText.setObjectName("voxelSideViewText")
        self.verticalLayout_11.addWidget(self.voxelSideViewText)
        self.voxelSideViewDisplay = ScaledLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voxelSideViewDisplay.sizePolicy().hasHeightForWidth())
        self.voxelSideViewDisplay.setSizePolicy(sizePolicy)
        self.voxelSideViewDisplay.setMinimumSize(QtCore.QSize(300, 300))
        self.voxelSideViewDisplay.setObjectName("voxelSideViewDisplay")
        self.verticalLayout_11.addWidget(self.voxelSideViewDisplay)
        self.horizontalLayout_5.addLayout(self.verticalLayout_11)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_12.addWidget(self.label_8)
        self.voxelTopViewDisplay = ScaledLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voxelTopViewDisplay.sizePolicy().hasHeightForWidth())
        self.voxelTopViewDisplay.setSizePolicy(sizePolicy)
        self.voxelTopViewDisplay.setMinimumSize(QtCore.QSize(300, 300))
        self.voxelTopViewDisplay.setObjectName("voxelTopViewDisplay")
        self.verticalLayout_12.addWidget(self.voxelTopViewDisplay)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.step_label = QtWidgets.QLabel(self.frame_2)
        self.step_label.setObjectName("step_label")
        self.horizontalLayout_2.addWidget(self.step_label)
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.stage_label = QtWidgets.QLabel(self.frame_2)
        self.stage_label.setObjectName("stage_label")
        self.horizontalLayout_2.addWidget(self.stage_label)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.line_4 = QtWidgets.QFrame(self.frame)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_2.addWidget(self.line_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.dialog_textBrowser = QtWidgets.QTextBrowser(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dialog_textBrowser.sizePolicy().hasHeightForWidth())
        self.dialog_textBrowser.setSizePolicy(sizePolicy)
        self.dialog_textBrowser.setObjectName("dialog_textBrowser")
        self.verticalLayout_3.addWidget(self.dialog_textBrowser)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.line_6 = QtWidgets.QFrame(self.frame)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_3.addWidget(self.line_6)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_15.addWidget(self.label_4)
        self.last_action_textBrowser = QtWidgets.QTextBrowser(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.last_action_textBrowser.sizePolicy().hasHeightForWidth())
        self.last_action_textBrowser.setSizePolicy(sizePolicy)
        self.last_action_textBrowser.setObjectName("last_action_textBrowser")
        self.verticalLayout_15.addWidget(self.last_action_textBrowser)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_15.addWidget(self.label_3)
        self.action_to_take_textBrowser = QtWidgets.QTextBrowser(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.action_to_take_textBrowser.sizePolicy().hasHeightForWidth())
        self.action_to_take_textBrowser.setSizePolicy(sizePolicy)
        self.action_to_take_textBrowser.setObjectName("action_to_take_textBrowser")
        self.verticalLayout_15.addWidget(self.action_to_take_textBrowser)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_15)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.subgoal_textBrowser = QtWidgets.QTextBrowser(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subgoal_textBrowser.sizePolicy().hasHeightForWidth())
        self.subgoal_textBrowser.setSizePolicy(sizePolicy)
        self.subgoal_textBrowser.setMinimumSize(QtCore.QSize(158, 0))
        self.subgoal_textBrowser.setObjectName("subgoal_textBrowser")
        self.verticalLayout_4.addWidget(self.subgoal_textBrowser)
        self.horizontalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_13.addWidget(self.label_2)
        self.plan_textBrowser = QtWidgets.QTextBrowser(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plan_textBrowser.sizePolicy().hasHeightForWidth())
        self.plan_textBrowser.setSizePolicy(sizePolicy)
        self.plan_textBrowser.setObjectName("plan_textBrowser")
        self.verticalLayout_13.addWidget(self.plan_textBrowser)
        self.horizontalLayout_9.addLayout(self.verticalLayout_13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.line_5 = QtWidgets.QFrame(self.frame)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_2.addWidget(self.line_5)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.events_textBrowser = QtWidgets.QTextBrowser(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.events_textBrowser.sizePolicy().hasHeightForWidth())
        self.events_textBrowser.setSizePolicy(sizePolicy)
        self.events_textBrowser.setObjectName("events_textBrowser")
        self.verticalLayout_2.addWidget(self.events_textBrowser)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.previous_button = QtWidgets.QPushButton(self.frame)
        self.previous_button.setObjectName("previous_button")
        self.horizontalLayout.addWidget(self.previous_button)
        self.next_button = QtWidgets.QPushButton(self.frame)
        self.next_button.setObjectName("next_button")
        self.horizontalLayout.addWidget(self.next_button)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_9)
        self.horizontalLayout_4.addWidget(self.frame)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Visualizer"))
        self.rawObservationText.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Raw Observation &amp; Panoptic Segmentation:</span></p></body></html>"))
        self.rawObservationDisplay.setText(_translate("MainWindow", "rawObservationDisplay"))
        self.voxelSideViewText.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Voxel Map Side View:</span></p></body></html>"))
        self.voxelSideViewDisplay.setText(_translate("MainWindow", "voxelSideViewDisplay"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Voxel Map Top View:</span></p></body></html>"))
        self.voxelTopViewDisplay.setText(_translate("MainWindow", "voxelTopViewDisplay"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Step:</span></p></body></html>"))
        self.step_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Stage:</span></p></body></html>"))
        self.stage_label.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Dialog:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Last Action:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Next Action:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Subgoals:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Plan for current subgoal:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:700;\">Events:</span></p></body></html>"))
        self.previous_button.setText(_translate("MainWindow", "Previous"))
        self.next_button.setText(_translate("MainWindow", "Next"))
from main import ScaledLabel
