# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QToolBox, QVBoxLayout, QWidget)
import rc_arquivo_recursos

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(827, 611)
        Widget.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.horizontalLayout = QHBoxLayout(Widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(Widget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMinimumSize(QSize(175, 0))
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setStyleSheet(u"\n"
"background-color: rgb(170, 170, 255);")
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.left_container)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.toolBox = QToolBox(self.left_container)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 159, 477))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.bttn_ponto_de_coleta = QPushButton(self.page)
        self.bttn_ponto_de_coleta.setObjectName(u"bttn_ponto_de_coleta")

        self.verticalLayout_4.addWidget(self.bttn_ponto_de_coleta)

        self.bttn_meu_oleo_usado = QPushButton(self.page)
        self.bttn_meu_oleo_usado.setObjectName(u"bttn_meu_oleo_usado")

        self.verticalLayout_4.addWidget(self.bttn_meu_oleo_usado)

        self.bttn_calculadora = QPushButton(self.page)
        self.bttn_calculadora.setObjectName(u"bttn_calculadora")

        self.verticalLayout_4.addWidget(self.bttn_calculadora)

        self.bttn_beneficios_reciclagem = QPushButton(self.page)
        self.bttn_beneficios_reciclagem.setObjectName(u"bttn_beneficios_reciclagem")

        self.verticalLayout_4.addWidget(self.bttn_beneficios_reciclagem)

        self.bttn_suporte = QPushButton(self.page)
        self.bttn_suporte.setObjectName(u"bttn_suporte")

        self.verticalLayout_4.addWidget(self.bttn_suporte)

        self.bttn_sobre = QPushButton(self.page)
        self.bttn_sobre.setObjectName(u"bttn_sobre")

        self.verticalLayout_4.addWidget(self.bttn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Page 1")
        self.User_Informations = QWidget()
        self.User_Informations.setObjectName(u"User_Informations")
        self.User_Informations.setGeometry(QRect(0, 0, 181, 477))
        self.verticalLayout_5 = QVBoxLayout(self.User_Informations)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame = QFrame(self.User_Informations)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.user_qlabel_text = QLabel(self.frame_2)
        self.user_qlabel_text.setObjectName(u"user_qlabel_text")

        self.verticalLayout_6.addWidget(self.user_qlabel_text)

        self.system_qlabel_text = QLabel(self.frame_2)
        self.system_qlabel_text.setObjectName(u"system_qlabel_text")

        self.verticalLayout_6.addWidget(self.system_qlabel_text)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.user_qlabel = QLabel(self.frame_3)
        self.user_qlabel.setObjectName(u"user_qlabel")

        self.verticalLayout_7.addWidget(self.user_qlabel)

        self.system_qlabel = QLabel(self.frame_3)
        self.system_qlabel.setObjectName(u"system_qlabel")

        self.verticalLayout_7.addWidget(self.system_qlabel)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.verticalLayout_5.addWidget(self.frame)

        self.toolBox.addItem(self.User_Informations, u"Page 2")

        self.verticalLayout_3.addWidget(self.toolBox)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(Widget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u"background-color: rgb(170, 255, 127);")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_2.addWidget(self.btn_toggle)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.main_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.pages_stack = QStackedWidget(self.main_frame)
        self.pages_stack.setObjectName(u"pages_stack")
        self.PagePontoDeColeta = QWidget()
        self.PagePontoDeColeta.setObjectName(u"PagePontoDeColeta")
        self.verticalLayout_9 = QVBoxLayout(self.PagePontoDeColeta)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.LinkReciclaSampa = QLabel(self.PagePontoDeColeta)
        self.LinkReciclaSampa.setObjectName(u"LinkReciclaSampa")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LinkReciclaSampa.sizePolicy().hasHeightForWidth())
        self.LinkReciclaSampa.setSizePolicy(sizePolicy1)
        self.LinkReciclaSampa.setAutoFillBackground(False)
        self.LinkReciclaSampa.setStyleSheet(u"")
        self.LinkReciclaSampa.setAlignment(Qt.AlignCenter)
        self.LinkReciclaSampa.setOpenExternalLinks(True)

        self.verticalLayout_9.addWidget(self.LinkReciclaSampa)

        self.pages_stack.addWidget(self.PagePontoDeColeta)
        self.PageCalculadora = QWidget()
        self.PageCalculadora.setObjectName(u"PageCalculadora")
        self.verticalLayout_12 = QVBoxLayout(self.PageCalculadora)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_4 = QFrame(self.PageCalculadora)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_16.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_16.addWidget(self.label_17)


        self.verticalLayout_12.addWidget(self.frame_4)

        self.Calculadora = QFrame(self.PageCalculadora)
        self.Calculadora.setObjectName(u"Calculadora")
        self.Calculadora.setMaximumSize(QSize(16777215, 125))
        self.Calculadora.setFrameShape(QFrame.StyledPanel)
        self.Calculadora.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.Calculadora)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.AreaCalculadora = QFrame(self.Calculadora)
        self.AreaCalculadora.setObjectName(u"AreaCalculadora")
        self.AreaCalculadora.setFrameShape(QFrame.StyledPanel)
        self.AreaCalculadora.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.AreaCalculadora)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.AreaTextos = QFrame(self.AreaCalculadora)
        self.AreaTextos.setObjectName(u"AreaTextos")
        self.AreaTextos.setMinimumSize(QSize(150, 70))
        self.AreaTextos.setMaximumSize(QSize(150, 70))
        self.AreaTextos.setFrameShape(QFrame.StyledPanel)
        self.AreaTextos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.AreaTextos)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.TextoPesoKg = QLabel(self.AreaTextos)
        self.TextoPesoKg.setObjectName(u"TextoPesoKg")

        self.verticalLayout_14.addWidget(self.TextoPesoKg)

        self.TextoPrecoPorKg = QLabel(self.AreaTextos)
        self.TextoPrecoPorKg.setObjectName(u"TextoPrecoPorKg")

        self.verticalLayout_14.addWidget(self.TextoPrecoPorKg)


        self.horizontalLayout_5.addWidget(self.AreaTextos)

        self.AreaCalculo = QFrame(self.AreaCalculadora)
        self.AreaCalculo.setObjectName(u"AreaCalculo")
        self.AreaCalculo.setMinimumSize(QSize(140, 80))
        self.AreaCalculo.setMaximumSize(QSize(140, 80))
        self.AreaCalculo.setFrameShape(QFrame.StyledPanel)
        self.AreaCalculo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.AreaCalculo)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.PesoProdutoKg = QLineEdit(self.AreaCalculo)
        self.PesoProdutoKg.setObjectName(u"PesoProdutoKg")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PesoProdutoKg.sizePolicy().hasHeightForWidth())
        self.PesoProdutoKg.setSizePolicy(sizePolicy2)
        self.PesoProdutoKg.setMaximumSize(QSize(150, 20))
        self.PesoProdutoKg.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.PesoProdutoKg.setClearButtonEnabled(True)

        self.verticalLayout_15.addWidget(self.PesoProdutoKg)

        self.PrecoOleoUsado = QLabel(self.AreaCalculo)
        self.PrecoOleoUsado.setObjectName(u"PrecoOleoUsado")

        self.verticalLayout_15.addWidget(self.PrecoOleoUsado)


        self.horizontalLayout_5.addWidget(self.AreaCalculo)


        self.verticalLayout_13.addWidget(self.AreaCalculadora)

        self.pushButton = QPushButton(self.Calculadora)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_13.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_12.addWidget(self.Calculadora)

        self.pages_stack.addWidget(self.PageCalculadora)
        self.PageBeneficiosReciclagem = QWidget()
        self.PageBeneficiosReciclagem.setObjectName(u"PageBeneficiosReciclagem")
        self.verticalLayout_11 = QVBoxLayout(self.PageBeneficiosReciclagem)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.PageBeneficiosReciclagem)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.label_9)

        self.label_10 = QLabel(self.PageBeneficiosReciclagem)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_11.addWidget(self.label_10)

        self.label_11 = QLabel(self.PageBeneficiosReciclagem)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_11.addWidget(self.label_11)

        self.label_12 = QLabel(self.PageBeneficiosReciclagem)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_11.addWidget(self.label_12)

        self.label_13 = QLabel(self.PageBeneficiosReciclagem)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_11.addWidget(self.label_13)

        self.label_14 = QLabel(self.PageBeneficiosReciclagem)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_11.addWidget(self.label_14)

        self.label_15 = QLabel(self.PageBeneficiosReciclagem)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_11.addWidget(self.label_15)

        self.pages_stack.addWidget(self.PageBeneficiosReciclagem)
        self.PageSuporte = QWidget()
        self.PageSuporte.setObjectName(u"PageSuporte")
        self.verticalLayout_2 = QVBoxLayout(self.PageSuporte)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.PageSuporte)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_2.addWidget(self.label_4)

        self.WppIvan = QLabel(self.PageSuporte)
        self.WppIvan.setObjectName(u"WppIvan")
        self.WppIvan.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.WppIvan)

        self.WppMurilo = QLabel(self.PageSuporte)
        self.WppMurilo.setObjectName(u"WppMurilo")
        self.WppMurilo.setOpenExternalLinks(True)

        self.verticalLayout_2.addWidget(self.WppMurilo)

        self.label_8 = QLabel(self.PageSuporte)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.pages_stack.addWidget(self.PageSuporte)
        self.PageSobre = QWidget()
        self.PageSobre.setObjectName(u"PageSobre")
        self.verticalLayout_10 = QVBoxLayout(self.PageSobre)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.TextSobreNos = QLabel(self.PageSobre)
        self.TextSobreNos.setObjectName(u"TextSobreNos")

        self.verticalLayout_10.addWidget(self.TextSobreNos)

        self.EathChanImage = QLabel(self.PageSobre)
        self.EathChanImage.setObjectName(u"EathChanImage")
        self.EathChanImage.setPixmap(QPixmap(u":/imgs/dbxedds-8681688a-e7af-428a-89b7-ab8ae2adf228.png"))
        self.EathChanImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.EathChanImage)

        self.pages_stack.addWidget(self.PageSobre)
        self.PageMeuOleoUsado = QWidget()
        self.PageMeuOleoUsado.setObjectName(u"PageMeuOleoUsado")
        self.verticalLayout_17 = QVBoxLayout(self.PageMeuOleoUsado)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_18 = QLabel(self.PageMeuOleoUsado)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_17.addWidget(self.label_18)

        self.frame_5 = QFrame(self.PageMeuOleoUsado)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_19 = QLabel(self.frame_5)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_18.addWidget(self.label_19)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_20 = QLabel(self.frame_7)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_6.addWidget(self.label_20)

        self.AnuncioKg = QLineEdit(self.frame_7)
        self.AnuncioKg.setObjectName(u"AnuncioKg")
        self.AnuncioKg.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_6.addWidget(self.AnuncioKg)


        self.verticalLayout_18.addWidget(self.frame_7)

        self.BttnAnunciar = QPushButton(self.frame_5)
        self.BttnAnunciar.setObjectName(u"BttnAnunciar")
        self.BttnAnunciar.setMaximumSize(QSize(150, 25))
        self.BttnAnunciar.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout_18.addWidget(self.BttnAnunciar, 0, Qt.AlignHCenter)


        self.verticalLayout_17.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.PageMeuOleoUsado)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_6)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_19.addWidget(self.label_21)

        self.MeusAnuncios = QLabel(self.frame_6)
        self.MeusAnuncios.setObjectName(u"MeusAnuncios")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.MeusAnuncios.sizePolicy().hasHeightForWidth())
        self.MeusAnuncios.setSizePolicy(sizePolicy3)
        self.MeusAnuncios.setMinimumSize(QSize(550, 150))
        self.MeusAnuncios.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_19.addWidget(self.MeusAnuncios, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_17.addWidget(self.frame_6)

        self.pages_stack.addWidget(self.PageMeuOleoUsado)

        self.verticalLayout_8.addWidget(self.pages_stack)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        sizePolicy3.setHeightForWidth(self.footer_frame.sizePolicy().hasHeightForWidth())
        self.footer_frame.setSizePolicy(sizePolicy3)
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.footer_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(25, 25))
        self.label_5.setMaximumSize(QSize(25, 25))
        self.label_5.setStyleSheet(u"image: url(:/imgs/46080.png);")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_4.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)


        self.retranslateUi(Widget)

        self.toolBox.setCurrentIndex(0)
        self.pages_stack.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"SGROU", None))
        self.bttn_ponto_de_coleta.setText(QCoreApplication.translate("Widget", u"Pontos de Coleta", None))
        self.bttn_meu_oleo_usado.setText(QCoreApplication.translate("Widget", u"Meu \u00f3leo usado", None))
        self.bttn_calculadora.setText(QCoreApplication.translate("Widget", u"Calculadora custo/kg", None))
        self.bttn_beneficios_reciclagem.setText(QCoreApplication.translate("Widget", u"Benef\u00edcios da Reciclagem", None))
        self.bttn_suporte.setText(QCoreApplication.translate("Widget", u"Suporte", None))
        self.bttn_sobre.setText(QCoreApplication.translate("Widget", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Widget", u"Page 1", None))
        self.user_qlabel_text.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-weight:700;\">User:</span></p></body></html>", None))
        self.system_qlabel_text.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-weight:700;\">Sistema:</span></p></body></html>", None))
        self.user_qlabel.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.system_qlabel.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.User_Informations), QCoreApplication.translate("Widget", u"Page 2", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Sistema de Gerenciamento de Reciclagem do \u00d3leo Usado</span></p></body></html>", None))
        self.btn_toggle.setText(QCoreApplication.translate("Widget", u"Sair", None))
        self.LinkReciclaSampa.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/861143.png\"/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Pontos de Coleta:</span><br/><a href=\"https://www.reciclasampa.com.br/pontos-de-coleta\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">Buscar Pontos de Coleta</span></a></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/4341087.png\"/><span style=\" font-size:20pt; font-weight:700; text-decoration: underline; vertical-align:super;\">Calculadora</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\">Bem-vindo \u00e0 nossa Calculadora de \u00d3leo de Cozinha Usado! Aqui est\u00e1 como funciona:</p><p align=\"center\"><span style=\" font-weight:700;\">1.</span> Insira a quantidade de \u00f3leo de cozinha usado: Voc\u00ea pode medir isso em <span style=\" font-weight:700;\">Kg</span>. Se voc\u00ea n\u00e3o tiver <br/>certeza, uma estimativa aproximada tamb\u00e9m funciona. </p><p align=\"center\"><span style=\" font-weight:700;\">2.</span> Clique em <span style=\" font-weight:700;\">&quot;Calcular&quot;</span> e pronto!</p></body></html>", None))
        self.TextoPesoKg.setText(QCoreApplication.translate("Widget", u"Peso do Produto em Kg", None))
        self.TextoPrecoPorKg.setText(QCoreApplication.translate("Widget", u"Pre\u00e7o do \u00d3leo Atual/kg", None))
        self.PesoProdutoKg.setInputMask(QCoreApplication.translate("Widget", u"999.999", None))
        self.PesoProdutoKg.setPlaceholderText(QCoreApplication.translate("Widget", u"Digite o peso do \u00f2leo", None))
        self.PrecoOleoUsado.setText(QCoreApplication.translate("Widget", u"R$ 2.00", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Calcular", None))
        self.label_9.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Benef\u00edcios da Reciclagem do \u00d3leo de Cozinha Usado</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Redu\u00e7\u00e3o da polui\u00e7\u00e3o ambiental:</span> O descarte inadequado de \u00f3leo de cozinha usado em pias<br/>e ralos pode causar entupimentos em sistemas de esgoto e danos ao meio ambiente,<br/>poluindo rios, lagos e solos. A reciclagem evita essa polui\u00e7\u00e3o.</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Conserva\u00e7\u00e3o de recursos naturais:</span> A reciclagem de \u00f3leo de cozinha usado ajuda a conservar <br/>os recursos naturais, uma vez que ele pode ser transformado em biodiesel, uma fonte de energia <br/>renov\u00e1vel.</p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Redu\u00e7\u00e3o das emiss\u00f5es de gases de efeito estufa:</span> A produ\u00e7\u00e3o de biodiesel a partir de \u00f3leo de <br/>cozinha usado emite menos gases de efeito estufa em compara\u00e7\u00e3o com o diesel convencional,<br/> contribuindo para a redu\u00e7\u00e3o das mudan\u00e7as clim\u00e1ticas.</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Est\u00edmulo \u00e0 economia local:</span> A reciclagem de \u00f3leo de cozinha usado pode criar empregos locais <br/>na coleta, processamento e fabrica\u00e7\u00e3o de biodiesel.</p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Preven\u00e7\u00e3o de entupimentos em sistemas de esgoto:</span> O descarte inadequado de \u00f3leo de cozinha <br/>pode causar entupimentos caros em sistemas de esgoto, e a reciclagem ajuda a evitar esses <br/>problemas.</p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Redu\u00e7\u00e3o da depend\u00eancia de combust\u00edveis f\u00f3sseis:</span> A produ\u00e7\u00e3o de biodiesel a partir do \u00f3leo de <br/>cozinha usado contribui para a diversifica\u00e7\u00e3o da matriz energ\u00e9tica, reduzindo a depend\u00eancia de <br/>combust\u00edveis f\u00f3sseis.</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:700; vertical-align:super;\">Contatos</span></p></body></html>", None))
        self.WppIvan.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/whatsApp.png\"/><span style=\" font-size:18pt; font-weight:700; vertical-align:super;\">Ivan Mendonca</span></p><p align=\"center\"><a href=\"https://wa.me/11931004219\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">(11) 93100-4219</span></a></p></body></html>", None))
        self.WppMurilo.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/whatsApp.png\"/><span style=\" font-size:18pt; font-weight:700; vertical-align:super;\">Murilo Sene</span></p><p align=\"center\"><a href=\"https://wa.me/11944803198\"><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">(11) 94480-3198</span></a></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/email.png\"/><span style=\" font-size:18pt; vertical-align:super;\">suporte@sgrou.br</span></p></body></html>", None))
        self.TextSobreNos.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Sobre n\u00f3s</span><br/><br/>N\u00f3s da<span style=\" font-weight:700;\"> SGROU</span> acreditamos que a reciclagem \u00e9 mais do que uma obriga\u00e7\u00e3o, \u00e9 uma oportunidade de criar<br/>um mundo melhor para as presentes e futuras gera\u00e7\u00f5es. Por isso, n\u00f3s convidamos voc\u00ea a se juntar a n\u00f3s <br/>nessa miss\u00e3o. Entre em contato conosco e saiba como podemos ajudar voc\u00ea a reciclar mais e melhor. <br/>Juntos, podemos fazer a diferen\u00e7a!</p></body></html>", None))
        self.EathChanImage.setText("")
        self.label_18.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">Anuncie seu \u00d3leo Usado</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">Passo a Passo:</span><br/><br/><span style=\" font-weight:700;\">1.</span> Digite o peso em <span style=\" font-weight:700;\">kg</span> correspondente ao peso de \u00f3leo que voc\u00ea possui.<br/><br/><span style=\" font-weight:700;\">2.</span> Clice em &quot;Anunciar&quot; e pronto, est\u00e1 anunciado!</p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("Widget", u"Kg do \u00d3leo:", None))
        self.AnuncioKg.setInputMask(QCoreApplication.translate("Widget", u"999.999", None))
        self.BttnAnunciar.setText(QCoreApplication.translate("Widget", u"Anunciar!", None))
        self.label_21.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">Meus an\u00fancios</span></p></body></html>", None))
        self.MeusAnuncios.setText(QCoreApplication.translate("Widget", u"Meus an\u00fancios", None))
        self.label_5.setText("")
        self.label_2.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">SGROU</span></p></body></html>", None))
    # retranslateUi

