import re
import sys
from tabulate import tabulate
from utils import StrManipulate
from PySide6.QtCore import QUrl, Signal, Qt
from PySide6.QtGui import QDesktopServices, QMouseEvent, QFont
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QDialog
from ui_form import Ui_Widget
from banco_de_dados import BancoDeDados

class CpfInterface(QWidget):
    def __init__(self, database, user, system_type):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setFixedSize(750, 600)

        # Database config
        self.db = database

        # user and system
        self.user = user
        self.system = system_type
        self.ui.user_qlabel.setText(self.user)
        self.ui.system_qlabel.setText(self.system)

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

        # Anunciar button
        button_anunciar = self.ui.BttnAnunciar
        button_anunciar.clicked.connect(self.on_anunciar_bttn_clicked)

        # Action left buttons
        button_ponto_de_coleta_page.clicked.connect(self.on_ponto_de_coleta_bttn_clicked)
        button_meu_oleo_usado_page.clicked.connect(self.on_meu_oleo_usado_bttn_clicked)
        button_calculadora_page.clicked.connect(self.on_calculadora_bttn_clicked)
        button_beneficios_reciclagem_page.clicked.connect(self.on_beneficios_reciclagem_bttn_clicked)
        button_suporte_page.clicked.connect(self.on_suporte_bttn_clicked)
        button_sobre_page.clicked.connect(self.on_sobre_bttn_clicked)

        # Button Calculadora Page
        button_calculadora = self.ui.pushButton
        button_calculadora.clicked.connect(self.on_calculadora_button_clicked)

    def result_calculator(self):
        peso_oleo = self.ui.PesoProdutoKg.text()
        result = float(peso_oleo) * 2
        return result

    def on_calculadora_button_clicked(self):
        result = self.result_calculator()
        dlg = ResultDialog(result)
        dlg.exec()

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

    def on_anunciar_bttn_clicked(self):
        quantity_kg = self.ui.AnuncioKg.text()
        data_person = self.db.select_elements(
                            'ID, Nome, CPF, CEP, Rua, Bairro, Cidade',
                                                'clientescpf', where=True,
                                                table_value_filter=f'CPF = "{self.user}"')
        id = data_person[0][0]
        nome = data_person[0][1]
        cpf = data_person[0][2]
        cep = data_person[0][3]
        rua = data_person[0][4]
        bairro = data_person[0][5]
        cidade = data_person[0][6]

        if quantity_kg != '.':
            quantity_kg = float(quantity_kg)
            if quantity_kg > 0:
                self.db.insert_into('anuncio_cliente_cpf',
                                'ID, Nome, CPF, CEP, Rua, Bairro, Cidade, disponivel, QuantidadeKg',
                                f'"{id}", "{nome}", "{cpf}", "{cep}", "{rua}", "{bairro}", "{cidade}",'
                                f'"Sim", "{quantity_kg:.2f}"')
            else:
                dlg = ErrorDialog('O valor deve ser maior que 0 (Zero).')
                dlg.exec()
        else:
            dlg = ErrorDialog('Valor não digitado')
            dlg.exec()

        my_announce = self.db.select_elements('ID, Nome, CPF, CEP, disponivel, QuantidadeKg, data_de_registro',
                                                'anuncio_cliente_cpf', where=True,
                                                table_value_filter=f'CPF = "{cpf}" and disponivel = "Sim"'
                                                                   'ORDER BY data_de_registro DESC LIMIT 3')
        my_announce_label = self.ui.MeusAnuncios
        my_announce_label.setFont(QFont('Arial', 8))
        my_announce_label.setText(self.view_my_announce_with_three_itens(my_announce))

    def view_my_announce_with_three_itens(self, my_announce):
        columns = ['ID', 'Nome', 'CPF', 'CEP', 'disponivel', 'QuantidadeKg', 'data_de_registro']
        tabela = tabulate(my_announce, columns, tablefmt='fancy_grid')
        return tabela


class ResultDialog(QDialog):
    def __init__(self, result, parent=None):
        super().__init__(parent)

        # Window Config
        self.setWindowTitle('Resultado')

        # Layout config
        self.layout = QVBoxLayout()
        ok_button = QPushButton('Okay')
        self.result_label = QLabel()
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(ok_button)
        self.setLayout(self.layout)

        # Initialize the result label
        self.update_result(result)

        ok_button.clicked.connect(self.accept)

    def update_result(self, result):
        self.result_label.setText(f'Seu resultado é: R${result:.2f}')

class ErrorDialog(QDialog):
    def __init__(self, message, parent=None):
        super().__init__(parent)

        # Window Config
        self.message = message
        self.setWindowTitle('Error')
        # Layout config

        self.layout = QVBoxLayout()
        ok_button = QPushButton('Okay')
        self.error_message = QLabel(self.message)
        self.layout.addWidget(self.error_message)
        self.layout.addWidget(ok_button)
        self.setLayout(self.layout)
        ok_button.clicked.connect(self.accept)

