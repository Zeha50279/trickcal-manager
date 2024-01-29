# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'page_equip_1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

from widgets.wrapper.misc import ExtendedComboBox

class Ui_page_equip_1(object):
    def setupUi(self, page_equip_1):
        if not page_equip_1.objectName():
            page_equip_1.setObjectName(u"page_equip_1")
        page_equip_1.resize(800, 633)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(page_equip_1.sizePolicy().hasHeightForWidth())
        page_equip_1.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(page_equip_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(36, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.hero_select = ExtendedComboBox(page_equip_1)
        self.hero_select.setObjectName(u"hero_select")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.hero_select.sizePolicy().hasHeightForWidth())
        self.hero_select.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font.setPointSize(15)
        self.hero_select.setFont(font)

        self.horizontalLayout_3.addWidget(self.hero_select)

        self.filter_btn = QPushButton(page_equip_1)
        self.filter_btn.setObjectName(u"filter_btn")
        font1 = QFont()
        font1.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font1.setPointSize(12)
        self.filter_btn.setFont(font1)

        self.horizontalLayout_3.addWidget(self.filter_btn)

        self.horizontalSpacer_6 = QSpacerItem(36, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.go_left_btn = QPushButton(page_equip_1)
        self.go_left_btn.setObjectName(u"go_left_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.go_left_btn.sizePolicy().hasHeightForWidth())
        self.go_left_btn.setSizePolicy(sizePolicy2)
        self.go_left_btn.setMaximumSize(QSize(30, 16777215))
        self.go_left_btn.setFont(font)

        self.horizontalLayout.addWidget(self.go_left_btn)

        self.rank_table = QTableWidget(page_equip_1)
        self.rank_table.setObjectName(u"rank_table")
        font2 = QFont()
        font2.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font2.setPointSize(10)
        self.rank_table.setFont(font2)
        self.rank_table.setColumnCount(0)

        self.horizontalLayout.addWidget(self.rank_table)

        self.go_right_btn = QPushButton(page_equip_1)
        self.go_right_btn.setObjectName(u"go_right_btn")
        sizePolicy2.setHeightForWidth(self.go_right_btn.sizePolicy().hasHeightForWidth())
        self.go_right_btn.setSizePolicy(sizePolicy2)
        self.go_right_btn.setMaximumSize(QSize(30, 16777215))
        self.go_right_btn.setFont(font)

        self.horizontalLayout.addWidget(self.go_right_btn)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.groupBox_mode = QGroupBox(page_equip_1)
        self.groupBox_mode.setObjectName(u"groupBox_mode")
        font3 = QFont()
        font3.setFamilies([u"ONE \ubaa8\ubc14\uc77cPOP"])
        font3.setPointSize(11)
        self.groupBox_mode.setFont(font3)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_mode)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.radio_cur_mode = QRadioButton(self.groupBox_mode)
        self.radio_cur_mode.setObjectName(u"radio_cur_mode")
        self.radio_cur_mode.setFont(font3)

        self.horizontalLayout_5.addWidget(self.radio_cur_mode)

        self.radio_goal_mode = QRadioButton(self.groupBox_mode)
        self.radio_goal_mode.setObjectName(u"radio_goal_mode")
        self.radio_goal_mode.setFont(font3)

        self.horizontalLayout_5.addWidget(self.radio_goal_mode)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.widget = QWidget(self.groupBox_mode)
        self.widget.setObjectName(u"widget")
        self.widget.setFont(font3)
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font3)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.cur_goal = QComboBox(self.widget)
        self.cur_goal.setObjectName(u"cur_goal")
        sizePolicy1.setHeightForWidth(self.cur_goal.sizePolicy().hasHeightForWidth())
        self.cur_goal.setSizePolicy(sizePolicy1)
        self.cur_goal.setMinimumSize(QSize(150, 0))
        self.cur_goal.setFont(font1)

        self.horizontalLayout_4.addWidget(self.cur_goal)

        self.goal_setting_btn = QPushButton(self.widget)
        self.goal_setting_btn.setObjectName(u"goal_setting_btn")
        self.goal_setting_btn.setFont(font1)

        self.horizontalLayout_4.addWidget(self.goal_setting_btn)


        self.horizontalLayout_5.addWidget(self.widget)


        self.horizontalLayout_7.addWidget(self.groupBox_mode)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_setAll = QGroupBox(page_equip_1)
        self.groupBox_setAll.setObjectName(u"groupBox_setAll")
        self.groupBox_setAll.setFont(font3)
        self.verticalLayout = QVBoxLayout(self.groupBox_setAll)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.widget_2 = QWidget(self.groupBox_setAll)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label)

        self.combo_set_goal = QComboBox(self.widget_2)
        self.combo_set_goal.setObjectName(u"combo_set_goal")
        self.combo_set_goal.setFont(font3)

        self.horizontalLayout_2.addWidget(self.combo_set_goal)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.set_check_btn = QPushButton(self.widget_2)
        self.set_check_btn.setObjectName(u"set_check_btn")
        self.set_check_btn.setFont(font3)

        self.horizontalLayout_2.addWidget(self.set_check_btn)


        self.horizontalLayout_6.addWidget(self.widget_2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.set_goal_w_stat_btn = QPushButton(self.groupBox_setAll)
        self.set_goal_w_stat_btn.setObjectName(u"set_goal_w_stat_btn")
        self.set_goal_w_stat_btn.setFont(font3)

        self.verticalLayout.addWidget(self.set_goal_w_stat_btn)


        self.horizontalLayout_8.addWidget(self.groupBox_setAll)

        self.groupBox_save_undo = QGroupBox(page_equip_1)
        self.groupBox_save_undo.setObjectName(u"groupBox_save_undo")
        sizePolicy.setHeightForWidth(self.groupBox_save_undo.sizePolicy().hasHeightForWidth())
        self.groupBox_save_undo.setSizePolicy(sizePolicy)
        self.groupBox_save_undo.setFont(font3)
        self.gridLayout = QGridLayout(self.groupBox_save_undo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.undo_cur_btn = QPushButton(self.groupBox_save_undo)
        self.undo_cur_btn.setObjectName(u"undo_cur_btn")
        self.undo_cur_btn.setFont(font3)

        self.gridLayout.addWidget(self.undo_cur_btn, 1, 1, 1, 1)

        self.save_all_btn = QPushButton(self.groupBox_save_undo)
        self.save_all_btn.setObjectName(u"save_all_btn")
        self.save_all_btn.setFont(font3)

        self.gridLayout.addWidget(self.save_all_btn, 0, 0, 1, 1)

        self.save_cur_btn = QPushButton(self.groupBox_save_undo)
        self.save_cur_btn.setObjectName(u"save_cur_btn")
        self.save_cur_btn.setFont(font3)

        self.gridLayout.addWidget(self.save_cur_btn, 0, 1, 1, 1)

        self.undo_all_btn = QPushButton(self.groupBox_save_undo)
        self.undo_all_btn.setObjectName(u"undo_all_btn")
        self.undo_all_btn.setFont(font3)

        self.gridLayout.addWidget(self.undo_all_btn, 1, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.groupBox_save_undo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)


        self.retranslateUi(page_equip_1)

        QMetaObject.connectSlotsByName(page_equip_1)
    # setupUi

    def retranslateUi(self, page_equip_1):
        page_equip_1.setWindowTitle(QCoreApplication.translate("page_equip_1", u"Form", None))
        self.filter_btn.setText(QCoreApplication.translate("page_equip_1", u" \uc0ac\ub3c4 \ubaa9\ub85d \ud544\ud130 ", None))
        self.go_left_btn.setText(QCoreApplication.translate("page_equip_1", u"<", None))
        self.go_right_btn.setText(QCoreApplication.translate("page_equip_1", u">", None))
        self.groupBox_mode.setTitle(QCoreApplication.translate("page_equip_1", u"\ubaa8\ub4dc", None))
        self.radio_cur_mode.setText(QCoreApplication.translate("page_equip_1", u"\ucc29\uc6a9 \uc7a5\ube44 \uae30\ub85d", None))
        self.radio_goal_mode.setText(QCoreApplication.translate("page_equip_1", u"\ubaa9\ud45c \uc124\uc815", None))
        self.label_3.setText(QCoreApplication.translate("page_equip_1", u"\ud604\uc7ac \ubaa9\ud45c : ", None))
        self.goal_setting_btn.setText(QCoreApplication.translate("page_equip_1", u" \ubaa9\ud45c \uc218\uc815/\uc0ad\uc81c ", None))
        self.groupBox_setAll.setTitle(QCoreApplication.translate("page_equip_1", u"\uc77c\uad04 \uc124\uc815\ud558\uae30", None))
        self.label.setText(QCoreApplication.translate("page_equip_1", u"\uc804\uccb4 \uc0ac\ub3c4", None))
        self.label_2.setText(QCoreApplication.translate("page_equip_1", u"\ub7ad\ud06c\uae4c\uc9c0", None))
        self.set_check_btn.setText(QCoreApplication.translate("page_equip_1", u"\uccb4\ud06c", None))
        self.set_goal_w_stat_btn.setText(QCoreApplication.translate("page_equip_1", u"\uc2a4\ud0ef \ubcc4 \ub7ad\ud06c\uc791 \ubaa9\ud45c \uc77c\uad04 \uc124\uc815", None))
        self.groupBox_save_undo.setTitle(QCoreApplication.translate("page_equip_1", u"\uc800\uc7a5 / \ucde8\uc18c", None))
        self.undo_cur_btn.setText(QCoreApplication.translate("page_equip_1", u"\ud604\uc7ac \ud398\uc774\uc9c0 \ubcc0\uacbd\uc0ac\ud56d \ucde8\uc18c", None))
        self.save_all_btn.setText(QCoreApplication.translate("page_equip_1", u"\ubaa8\ub450 \uc800\uc7a5", None))
        self.save_cur_btn.setText(QCoreApplication.translate("page_equip_1", u"\ud604\uc7ac \ud398\uc774\uc9c0 \uc800\uc7a5", None))
        self.undo_all_btn.setText(QCoreApplication.translate("page_equip_1", u"\ubcc0\uacbd\uc0ac\ud56d \ubaa8\ub450 \ucde8\uc18c", None))
    # retranslateUi

