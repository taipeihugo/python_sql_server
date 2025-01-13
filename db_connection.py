import pyodbc

# 全域變數儲存資料庫名稱
current_database = None

def get_connection(database_name):
    try:
        return pyodbc.connect(
            'DRIVER={SQL Server};' +
            f'SERVER=vm-hungtao;DATABASE={database_name};' +
            'Trusted_Connection=True;'
        )
    except pyodbc.Error as ex:
        return None

def set_current_database(db_name):
    global current_database
    current_database = db_name

def get_current_database():
    return current_database
