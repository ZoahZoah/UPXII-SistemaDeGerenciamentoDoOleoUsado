from banco_de_dados import BancoDeDados
from gui_login_and_registry import LoginWindow
from gui_cpf import CpfInterface
from PySide6.QtCore import QCoreApplication
from PySide6.QtWidgets import (
    QApplication, QMainWindow)

# Do you need to create a DataBase Local
db_reciclagem = BancoDeDados('localhost', 'root', '93100', 'reciclagem')
app = QApplication([])
login_window = LoginWindow(db_reciclagem)
login_window.show()
app.exec()

if login_window.login_result:
    match login_window.system_type:
        case 'CPF':
            login_cpf = CpfInterface(db_reciclagem, login_window.login_user, login_window.system_type)
            login_cpf.show()
            app.exec()
        case 'CNPJ':
            pass



