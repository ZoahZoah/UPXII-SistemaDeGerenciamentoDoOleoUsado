from banco_de_dados import BancoDeDados
from gui import LoginWindow
from PySide6.QtWidgets import (
    QApplication)

db_reciclagem = BancoDeDados('localhost', 'root', '93100', 'reciclagem')
app = QApplication([])
login_window = LoginWindow(db_reciclagem)
login_window.show()
app.exec()

if login_window.login_result:
    print('oi')


