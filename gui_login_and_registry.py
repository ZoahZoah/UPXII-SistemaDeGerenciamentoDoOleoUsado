from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QGridLayout, QWidget, QLineEdit, QComboBox, QDialog,
    QDialogButtonBox)
from utils import Validate
import re

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    @staticmethod
    def text_widget(texto):
        texto_widget = QLabel(texto)
        return texto_widget

    @staticmethod
    def text_input_box_widget(text, hide_password=False):
        input_widget = QLineEdit()
        if hide_password:
            input_widget.setEchoMode(QLineEdit.Password)
        if text:
            input_widget.setPlaceholderText(text)
        return input_widget

    @staticmethod
    def multiples_itens_widget(itens):
        combo = QComboBox()
        combo.addItems(itens)
        return combo

    @staticmethod
    def add_button_widget(text, connect):
        button = QPushButton(text)
        button.setCheckable(True)
        button.clicked.connect(connect)
        return button

    @staticmethod
    def add_layout_list(layout, list, alignment=None):
        for x, y, z in list:
            layout.addWidget(x, y, z, alignment)

    @staticmethod
    def clearLayout(layout):
        if layout is not None:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget() is not None:
                    child.widget().deleteLater()
                elif child.layout() is not None:
                    clearLayout(child.layout())


class LoginWindow(MainWindow):
    def __init__(self, db):
        super().__init__()
        self.login_result = False

        # User information
        self.__login_user = ''
        self.__system_type = ''

        # definindo o banco de dados
        self.db_reciclagem = db

        self.setWindowTitle('Tela de Login')
        self.setFixedSize(QSize(240, 150))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QGridLayout(central_widget)
        self.login_cpf()

    @property
    def login_user(self):
        return self.__login_user

    @login_user.setter
    def login_user(self, new_information):
        self.__login_user = new_information

    @property
    def system_type(self):
        return self.__system_type

    @system_type.setter
    def system_type(self, new_system):
        self.__system_type = new_system

    def login_cpf(self):
        self.login(False)

    def login_cnpj(self):
        self.login(True)

    def login(self, is_cnpj=False):
        self.clearLayout(self.layout)

        # Buttons
        cpf_button = self.add_button_widget('CPF', self.login_cpf)
        cnpj_button = self.add_button_widget('CNPJ', self.login_cnpj)

        # cnpj ou cpf
        self.documento_text = self.text_widget('CNPJ' if is_cnpj else 'CPF')
        self.documento_input = self.text_input_box_widget('Digite seu CNPJ' if is_cnpj else 'Digite seu CPF')
        self.documento_input.setMaxLength(14 if is_cnpj else 11)
        self.documento_input.setInputMask('00.000.000/0000-00' if is_cnpj else '000.000.000-00')

        # senha
        senha_text = self.text_widget('Senha:')
        self.senha_input = self.text_input_box_widget('Digite sua senha', hide_password=True)
        self.senha_input.setMaxLength(18)

        # Buttons
        login_button = self.add_button_widget('Login', self.on_login_button_clicked)
        registry_button = self.add_button_widget('Cadastrar', self.on_cadastro_button_clicked)

        # Add widgets to layout
        add_widgets_list = [(cpf_button, 1, 0), (cnpj_button, 1, 1), (self.documento_text, 2, 0),
                            (self.documento_input, 2, 1), (senha_text, 3, 0), (self.senha_input, 3, 1),
                            (login_button, 4, 1), (registry_button, 4, 0)]
        self.add_layout_list(self.layout, add_widgets_list, Qt.AlignHCenter | Qt.AlignVCenter)

    def on_cadastro_button_clicked(self):
        print('Botão de Cadastro clicado')
        dlg = RegistryDialog(self.db_reciclagem)
        dlg.exec()

    def on_login_button_clicked(self):
        user_answers = self.documento_input.text()
        password_answer = self.senha_input.text()
        type_client = self.documento_text.text()
        validate = self.db_reciclagem.select_elements('*', f'clientes{type_client}',
                                                      where=True,
                                                      table_value_filter=f'{type_client} = "{user_answers}"'
                                                                         f' AND senha = "{password_answer}"')

        if validate:
            print('Login realizado com suceso!')
            self.login_user = user_answers
            match type_client:
                case 'CPF':
                    self.system_type = 'CPF'
                case 'CNPJ':
                    self.system_type = 'CNPJ'
            self.window().close()
        elif not validate:
            self.show_login_error_message()
        self.login_result = bool(validate)


    def show_login_error_message(self):
        # Add widget
        login_error = QLabel('Usuario ou senha incorreto!')

        # Set color font
        palette = QPalette()
        palette.setColor(QPalette.WindowText, Qt.red)
        login_error.setPalette(palette)

        # Add widget in the layout
        self.layout.addWidget(login_error, 0, 0, 1, 3, Qt.AlignHCenter | Qt.AlignVCenter)
        self.senha_input.clear()


class RegistryDialog(QDialog, MainWindow):
    def __init__(self, database, parent=None):
        super().__init__(parent)

        self.db = database
        self.dlg = RegistryDialog

        # Window Config
        self.setWindowTitle('Tela de Registro')

        #Layout config
        self.layout = QGridLayout()
        self.registry()
        self.setLayout(self.layout)
        self.cpf = True

    def registry_cpf(self):
        self.registry(False)

    def registry_cnpj(self):
        self.registry(True)

    def registry(self, is_cnpj=False):
        # Clear layout
        self.clearLayout(self.layout)

        # nome ou nomeFantasia
        nome_text = self.text_widget('Nome Fantasia:' if is_cnpj else 'Nome:')
        self.nome_input = self.text_input_box_widget('Digite o nome da empresa' if is_cnpj else 'Digite seu nome')

        # cnpj ou cpf
        self.documento_text = self.text_widget('CNPJ:' if is_cnpj else 'CPF:')
        self.documento_input = self.text_input_box_widget('Digite seu CNPJ' if is_cnpj else 'Digite seu CPF')
        self.documento_input.setMaxLength(14 if is_cnpj else 11)
        self.documento_input.setInputMask('00.000.000/0000-00' if is_cnpj else '000.000.000-00')

        # senha
        senha_text = self.text_widget('Senha:')
        self.senha_input = self.text_input_box_widget('Digite sua senha', hide_password=True)
        self.senha_input.setMaxLength(18)

        # cep
        cep_text = self.text_widget('cep:')
        self.cep_input = self.text_input_box_widget('Digite seu cep')
        self.cep_input.setMaxLength(8)
        self.cep_input.setInputMask('00000-000')

        # rua
        rua_text = self.text_widget('Rua:')
        self.rua_input = self.text_input_box_widget('Digite o nome da sua rua')

        # bairro
        bairro_text = self.text_widget('Bairro:')
        self.bairro_input = self.text_input_box_widget('Digite o nome do seu bairro')

        # cidade
        cidade_text = self.text_widget('Cidade:')
        self.cidade_input = self.text_input_box_widget('Digite o nome da sua cidade')

        # Buttons
        cpf_button = self.add_button_widget('CPF', self.registry_cpf)
        cnpj_button = self.add_button_widget('CNPJ', self.registry_cnpj)
        verify_cep = self.add_button_widget('CEP', self.on_verifycep_button_clicked)

        registry_button = self.add_button_widget('Cadastrar', self.on_okay_button_clicked)
        quit_button = self.add_button_widget('Sair', self.on_cancel_button_clicked)

        # Add layout
        add_list = [(cpf_button, 1, 0), (cnpj_button, 1, 1), (nome_text, 2, 0),
                    (self.nome_input, 2, 1), (self.documento_text, 3, 0), (self.documento_input, 3, 1),
                    (senha_text, 4, 0), (self.senha_input, 4, 1), (cep_text, 5, 0), (self.cep_input, 5, 1),
                    (verify_cep, 5, 2), (rua_text, 6, 0), (self.rua_input, 6, 1), (bairro_text, 7, 0),
                    (self.bairro_input, 7, 1), (cidade_text, 8, 0), (self.cidade_input, 8, 1),
                    (quit_button, 10, 2)]
        self.add_layout_list(self.layout, add_list, Qt.AlignHCenter | Qt.AlignVCenter)
        self.layout.addWidget(registry_button, 10, 0, 1, 2)

    def on_verifycep_button_clicked(self):
        rua = ''
        bairro = ''
        cidade = ''
        validate = Validate()
        cep_input = self.cep_input.text()

        cep = validate.validate_cep(cep_input)
        if cep:
            print('Cep válido')
            cep_validate, rua, bairro, cidade = cep
            self.rua_input.setText(rua)
            self.bairro_input.setText(bairro)
            self.cidade_input.setText(cidade)
        else:
            print('cep inválido')

    def on_cancel_button_clicked(self):
        self.dlg.close(self)

    def on_okay_button_clicked(self):
        validate = Validate()
        type_client = self.documento_text.text()
        name_input = self.nome_input.text()
        document_input = self.documento_input.text()
        document_verify = validate.validate_cpfcnpj(document_input)
        senha_input = self.senha_input.text()
        cep_input = self.cep_input.text()
        cep_verify = validate.validate_cep(cep_input)
        rua_input = self.rua_input.text()
        bairro_input = self.bairro_input.text()
        cidade_input = self.bairro_input.text()

        if document_verify and cep_verify:
            match type_client:
                case 'CPF:':
                        selection = self.db.select_elements('*', 'clientesCPF', where=True,
                                                            table_value_filter=f'CPF = "{document_input}"')
                        if not selection:
                            self.db.insert_into('clientesCPF', 'Nome, CPF, senha, cep, Rua, Bairro, Cidade',
                                                f"'{name_input}', '{document_input}', '{senha_input}', '{cep_input}', "
                                                f"'{rua_input}', '{bairro_input}', '{cidade_input}'")
                            self.dlg.close(self)
                        elif selection:
                            self.warning_message('Usuário já cadastrado', 3, 2)
                case 'CNPJ:':
                        selection = self.db.select_elements('*', 'clientesCNPJ', where=True,
                                                            table_value_filter=f'CNPJ = "{document_input}"')
                        if not selection:
                            self.db.insert_into('clientesCNPJ', 'NomeFantasia, CNPJ, senha, cep, Rua, Bairro, Cidade',
                                                f"'{name_input}', '{document_input}', '{senha_input}', '{cep_input}', "
                                                f"'{rua_input}', '{bairro_input}', '{cidade_input}'")
                            self.dlg.close(self)
                        elif selection:
                            self.already_registry('CNPJ já cadastrado!', 3, 2)

        else:
            self.warning_message('Documento inválido', 0, 1)

    def warning_message(self, message, x, y):
        print(message)
        already_registry = QLabel(message)
        palette = QPalette()
        palette.setColor(QPalette.WindowText, Qt.red)
        already_registry.setPalette(palette)
        self.layout.addWidget(already_registry, x, y)

