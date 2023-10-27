import sys
from utils import StrManipulate
from PySide6.QtCore import QUrl, Signal, Qt
from PySide6.QtGui import QDesktopServices, QMouseEvent
from PySide6.QtWidgets import QApplication, QWidget, QLabel
from ui_form import Ui_Widget


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setFixedSize(750, 600)

        # Quit button
        quit_button = self.ui.btn_toggle
        quit_button.clicked.connect(self.on_quit_button_clicked)

        # Buttons left menu
        button_ponto_de_coleta_page = self.ui.bttn_ponto_de_coleta
        button_meu_oleo_usado_page = self.ui.bttn_meu_oleo_usado
        button_calculadora_page = self.ui.bttn_calculadora
        button_beneficios_reciclagem_page = self.ui.bttn_beneficios_reciclagem
        button_suporte_page = self.ui.bttn_suporte
        button_sobre_page = self.ui.bttn_sobre

        # Action left buttons
        button_ponto_de_coleta_page.clicked.connect(self.on_ponto_de_coleta_bttn_clicked)
        button_meu_oleo_usado_page.clicked.connect(self.on_meu_oleo_usado_bttn_clicked)
        button_calculadora_page.clicked.connect(self.on_calculadora_bttn_clicked)
        button_beneficios_reciclagem_page.clicked.connect(self.on_beneficios_reciclagem_bttn_clicked)
        button_suporte_page.clicked.connect(self.on_suporte_bttn_clicked)
        button_sobre_page.clicked.connect(self.on_sobre_bttn_clicked)

        # Ponto de Coleta Page
        # Open URL recicla sampa
        buscar_ponto_coleta = self.ui.LinkReciclaSampa
        recicla_sampa = buscar_ponto_coleta.text()
        self.url_recicla_sampa = StrManipulate.split_url_in_string(recicla_sampa)
        self.qlabel_as_a_link_interaction(buscar_ponto_coleta, self.on_buscar_ponto_coleta_clicked)

    def qlabel_as_a_link_interaction(self, qlabel, action):
        qlabel.setOpenExternalLinks(True)
        qlabel.setTextInteractionFlags(Qt.TextBrowserInteraction)
        qlabel.linkActivated.connect(action)

    def on_quit_button_clicked(self):
        self.close()

    def open_url(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def on_buscar_ponto_coleta_clicked(self):
        self.open_url(self.url_recicla_sampa)

    def set_mainpage(self, index):
        self.ui.pages_stack.setCurrentIndex(index)

    def on_ponto_de_coleta_bttn_clicked(self):
        self.set_mainpage(0)

    def on_meu_oleo_usado_bttn_clicked(self):
        self.set_mainpage(5)

    def on_calculadora_bttn_clicked(self):
        self.set_mainpage(1)

    def on_beneficios_reciclagem_bttn_clicked(self):
        self.set_mainpage(2)

    def on_suporte_bttn_clicked(self):
        self.set_mainpage(3)

    def on_sobre_bttn_clicked(self):
        self.set_mainpage(4)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
