import customtkinter as tk
import pyodbc
from db_connection import get_connection, get_current_database

def create_table_window():
    """
    建立一個 GUI 視窗，提供創建資料表的功能。
    使用者可以輸入資料表名稱、欄位名稱並選擇資料型態，完成後會將表格創建到當前選擇的資料庫。
    """
    def create():
        """
        處理資料表創建的邏輯，包括檢查使用者輸入和執行 SQL 語句。
        """
        try:
            # 獲取當前選擇的資料庫
            current_db = get_current_database()
            if not current_db:
                info_label.configure(text="請先創建資料庫")  # 當前沒有選擇資料庫時提示
                return

            # 檢查是否為所有欄位選擇了資料型態
            if not radio_var_col1.get() or not radio_var_col2.get() or not radio_var_col3.get():
                info_label.configure(text="請為所有欄位選擇資料型態")
                return

            # 嘗試連接到當前資料庫
            connection = get_connection(current_db)
            if connection:
                connection.autocommit = True  # 開啟自動提交模式

                # 組合 SQL 語句，用於創建資料表
                sql_stmt = (
                    f"CREATE TABLE {entry_table_name.get()} ("  # 資料表名稱
                    f"{entry_column1.get()} {radio_var_col1.get()}, "  # 第一欄位名稱與型態
                    f"{entry_column2.get()} {radio_var_col2.get()}, "  # 第二欄位名稱與型態
                    f"{entry_column3.get()} {radio_var_col3.get()})"   # 第三欄位名稱與型態
                )
                connection.execute(sql_stmt)  # 執行 SQL 語句
                info_label.configure(text="創建資料表成功")  # 成功訊息
            else:
                info_label.configure(text="連接資料庫失敗")  # 連接失敗訊息
        except pyodbc.Error as ex:
            info_label.configure(text="創建資料表失敗")  # 創建失敗訊息
            print("Error:", ex)  # 印出錯誤訊息以供除錯

    # 建立主視窗
    app = tk.CTk()
    app.geometry("600x400")  # 設定視窗大小
    app.title("創建工作表")  # 設定視窗標題

    # 輸入資料表名稱
    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱", width=200)
    entry_table_name.place(relx=0.1, rely=0.1)  # 定位輸入框

    # 輸入第一欄位名稱
    entry_column1 = tk.CTkEntry(app, placeholder_text="column1", width=200)
    entry_column1.place(relx=0.1, rely=0.2)

    # 輸入第二欄位名稱
    entry_column2 = tk.CTkEntry(app, placeholder_text="column2", width=200)
    entry_column2.place(relx=0.1, rely=0.3)

    # 輸入第三欄位名稱
    entry_column3 = tk.CTkEntry(app, placeholder_text="column3", width=200)
    entry_column3.place(relx=0.1, rely=0.4)

    # 第一欄位型態選擇
    radio_var_col1 = tk.StringVar(value="")
    tk.CTkRadioButton(app, text="VARCHAR(50)", variable=radio_var_col1, value="VARCHAR(50)").place(relx=0.5, rely=0.2)
    tk.CTkRadioButton(app, text="INTEGER", variable=radio_var_col1, value="INTEGER").place(relx=0.7, rely=0.2)

    # 第二欄位型態選擇
    radio_var_col2 = tk.StringVar(value="")
    tk.CTkRadioButton(app, text="VARCHAR(50)", variable=radio_var_col2, value="VARCHAR(50)").place(relx=0.5, rely=0.3)
    tk.CTkRadioButton(app, text="INTEGER", variable=radio_var_col2, value="INTEGER").place(relx=0.7, rely=0.3)

    # 第三欄位型態選擇
    radio_var_col3 = tk.StringVar(value="")
    tk.CTkRadioButton(app, text="VARCHAR(50)", variable=radio_var_col3, value="VARCHAR(50)").place(relx=0.5, rely=0.4)
    tk.CTkRadioButton(app, text="INTEGER", variable=radio_var_col3, value="INTEGER").place(relx=0.7, rely=0.4)

    # 創建資料表按鈕
    create_button = tk.CTkButton(app, text="建立工作表", command=create)
    create_button.place(relx=0.1, rely=0.5)

    # 資訊標籤，用於顯示操作結果
    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.1, rely=0.6)

    # 顯示當前選擇的資料庫
    current_db = get_current_database()
    if current_db:
        current_db_label = tk.CTkLabel(app, text=f"當前資料庫: {current_db}")
        current_db_label.place(relx=0.1, rely=0.7)

    # 啟動視窗事件迴圈
    app.mainloop()
