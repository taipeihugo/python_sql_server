import pyodbc  # 匯入 pyodbc 模組，用於與 SQL Server 進行連接

# 全域變數用於儲存目前選定的資料庫名稱
current_database = None

def get_connection(database_name):
    """
    建立與指定資料庫的連線。
    參數：database_name (str): 要連接的資料庫名稱。        
    回傳：pyodbc.Connection 或 None: 成功時回傳資料庫連線物件，失敗時回傳 None。
    """
    try:
        # 使用 pyodbc 建立與 SQL Server 的連線
        return pyodbc.connect(
             'DRIVER={SQL Server};' +       # 使用 SQL Server 驅動程式
             'SERVER=tao-nuc11;' +          # 修改成自己的主機名稱
            f'DATABASE={database_name};' +  # 指定伺服器名稱和資料庫
             'Trusted_Connection=True;'
        )
    except pyodbc.Error as ex:
        # 若連線失敗，回傳 None
        return None

def set_current_database(db_name):
    """
    設定全域變數 current_database 的值。
    參數：db_name (str): 要設定的資料庫名稱。
    """
    global current_database  # 使用 global 關鍵字，修改全域變數
    current_database = db_name  # 更新目前的資料庫名稱

def get_current_database():
    """
    取得目前設定的資料庫名稱。
    回傳：儲存在全域變數中的資料庫名稱，若未設定則回傳 None。
    """
    return current_database
