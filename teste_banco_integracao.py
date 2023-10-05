from banco_de_dados import BancoDeDados

host='localhost'
user='root'
password='93100'
database='reciclagem'

reciclagem_bd = BancoDeDados(host, user, password, database)
#reciclagem_bd.insert_into('pessoa_fisica', 'Nome, UltimoNome, Usuario, Senha, CPF', '"Wabakat", "Trapper", "dororo", 183156, 448593')
reciclagem_bd.selec_elements_order_by('*', 'pessoa_fisica', 'Nome')

