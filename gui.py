from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QGridLayout, QWidget, QLineEdit, QComboBox, QDialog,
    QDialogButtonBox)


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


class LoginWindow(MainWindow):
    def __init__(self, db):
        super().__init__()
        self.login_result = False

        # definindo o banco de dados
        self.db_reciclagem = db

        self.setWindowTitle('Tela de Login')
        self.setFixedSize(QSize(240, 150))

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QGridLayout(central_widget)

        # User Widgets
        text_user = self.text_widget('CPF ou CNPJ:')
        self.input_user = self.text_input_box_widget('Digite seu identificador')

        # Passwords widgets
        text_password = self.text_widget('Senha:')
        self.input_password = self.text_input_box_widget('Digite sua senha', hide_password=True)

        # Type Client widgets
        type_client = ['CPF', 'CNPJ']
        text_type_client = self.text_widget(f'Tipo de Cliente:')
        self.type_client = self.multiples_itens_widget(type_client)

        # Buttons
        login_button = self.add_button_widget('Login', self.on_login_button_clicked)
        registry_button = self.add_button_widget('Cadastrar', self.on_cadastro_button_clicked)

        # Add widgets to layout
        add_widgets_list = [(text_user, 3, 0), (self.input_user, 3, 1), (text_password, 4, 0),
                                    (self.input_password, 4, 1), (text_type_client, 5, 0), (self.type_client, 5, 1),
                                    (login_button, 6, 1), (registry_button, 6, 0)]
        self.add_layout_list(self.layout, add_widgets_list, Qt.AlignHCenter | Qt.AlignVCenter)


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

    def on_cadastro_button_clicked(self):
        print('Botão de Cadastro clicado')
        dlg = RegistryDialog()
        dlg.exec()

    def on_login_button_clicked(self):
        user_answers = self.input_user.text()
        password_answer = self.input_password.text()
        type_client = self.type_client.currentText()
        validate = self.db_reciclagem.select_elements('*', f'clientes{type_client}',
                                                      where=True,
                                                      table_value_filter=f'{type_client} = "{user_answers}"'
                                                                         f' AND senha = "{password_answer}"')
        if validate:
            print('Login realizado com suceso!')
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
        self.layout.addWidget(login_error, 2, 0, 1, 3, Qt.AlignHCenter | Qt.AlignVCenter)
        self.input_password.clear()


class RegistryDialog(QDialog, MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Window Config
        self.setWindowTitle('Tela de Registro')

        type_client = ['CPF', 'CNPJ']
        text_type_client = self.text_widget('Tipo de Cliente:')
        self.type_client = self.multiples_itens_widget(type_client)

        cpf_button = self.add_button_widget('CPF', self.registry_cpf)
        cnpj_button = self.add_button_widget('CNPJ', connect=None)

        # Registry widgets
        # nome ou nomeFantasia
        # nome_text = self.text_widget('Nome ou Nome Fantasia')
        # CPF ou CNPJ
        # senha
        # rua
        # bairro
        # cidade
        # cep

        type_client = ['CPF', 'CNPJ']
        text_type_client = self.text_widget(f'Tipo de Cliente:')
        self.type_client = self.multiples_itens_widget(type_client)

        # Button Config


        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        buttonbox = QDialogButtonBox(buttons)
        buttonbox.accepted.connect(self.accepted)
        buttonbox.rejected.connect(self.rejected)

        #Layout config
        self.layout = QGridLayout()

        self.layout.addWidget(cpf_button, 1, 0)
        self.layout.addWidget(cnpj_button, 1, 1)
        self.layout.addWidget(buttonbox, 10, 0, 1, 2, Qt.AlignHCenter | Qt.AlignVCenter)
        self.setLayout(self.layout)

    def registry_cpf(self):
        # nome ou nomeFantasia
        nome_text = self.text_widget('Nome:')
        nome_input = self.text_input_box_widget('Digite seu nome')

        cpf_text = self.text_widget('CPF:')
        cpf_input = self.text_input_box_widget('Digite seu CPF')
        cpf_input.setMaxLength(11)
        cpf_input.setInputMask('000.000.000-00')

        senha_text = self.text_widget('Senha:')
        senha_input = self.text_input_box_widget('Digite sua senha', hide_password=True)
        senha_input.setMaxLength(18)

        # cep
        cep_text = self.text_widget('cep:')
        cep_input = self.text_input_box_widget('Digite seu cep')
        cep_input.setMaxLength(8)
        cep_input.setInputMask('00000-000')

        # rua
        rua_text = self.text_widget('Rua:')
        rua_input = self.text_input_box_widget('Digite o nome da sua rua')

        # bairro
        bairro_text = self.text_widget('Bairro:')
        bairro_input = self.text_input_box_widget('Digite o nome do seu bairro')

        # cidade
        cidade_text = self.text_widget('Cidade:')
        cidade_input = self.text_input_box_widget('Digite o nome da sua cidade')


        add_list = [(nome_text, 2, 0), (nome_input, 2, 1), (cpf_text, 3, 0), (cpf_input, 3, 1), (senha_text, 4, 0),
                    (senha_input, 4, 1), (cep_text, 5, 0), (cep_input, 5, 1), (rua_text, 6, 0), (rua_input, 6, 1),
                    (bairro_text, 7, 0), (bairro_input, 7, 1), (cidade_text, 8, 0), (cidade_input, 8, 1)]
        self.add_layout_list(self.layout, add_list, Qt.AlignHCenter | Qt.AlignVCenter)

