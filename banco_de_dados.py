import mysql.connector

class BancoDeDados:
    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.mycursor = self.mydb.cursor()

    def create_table(self, table_name, table):
        self.mycursor.execute(f'CREATE TABLE {table_name} ({table})')


    def drop_table(self, table_name):
        self.mycursor.execute(f'DROP TABLE {table_name}')

    def insert_into(self, table_name, table_columns, value_columns):
        self.mycursor.execute(f'INSERT INTO {table_name}({table_columns}) VALUES ({value_columns})')
        self.mydb.commit()

    def select_elements(self, whats_you_want_select, table_name, where=False, like=False, table_value_filter=None):
        if not where:
            self.mycursor.execute(f'SELECT {whats_you_want_select} FROM {table_name}')
        elif where:
            self.mycursor.execute(f'SELECT {whats_you_want_select} FROM {table_name} '
                                  f'WHERE {table_value_filter}')

        elif where and like:
            self.mycursor.execute(f'SELECT {whats_you_want_select} FROM {table_name} '
                                  f'WHERE {table_column} LIKE {value_filter}')
        myresult = self.mycursor.fetchall()
        return myresult

    def selec_elements_order_by(self, whats_you_want_select, table_name, table_column, desc=False):
        if not desc:
            self.mycursor.execute(f'SELECT {whats_you_want_select} FROM {table_name} ORDER BY {table_column}')
        elif desc:
            self.mycursor.execute(f'SELECT {whats_you_want_select} FROM {table_name} ORDER BY {table_column} DESC')
        myresult = self.mycursor.fetchall()

    def delete_user(self, table_name, table_columns, value_columns):
        self.mycursor.execute(f'DELETE FROM {table_name} WHERE {table_columns} = {value_columns}')
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) deleted")

    def update_user(self, table_name, table_column, new_value_column, another_column, value_column):
        self.mycursor.execute(f'UPDATE {table_name} SET {table_column} = {new_value_column} '
                              f'WHERE {another_column} = {value_column}')
        self.mydb.commit()
        print(self.mycursor.rowcount, 'record(s) affected')