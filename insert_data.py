import customtkinter as tk
import pyodbc
from db_connection import get_connection, get_current_database

def insert_data_window():
    """
    建立一個 GUI 視窗，提供插入資料的功能。
    使用者可輸入資料表名稱、ID、名字與姓氏，並將資料新增至當前選擇的資料庫。
    """
    def insert():
        """
        處理資料插入的邏輯，包括檢查使用者輸入和執行 SQL 語句。
        防止重複插入相同的資料。
        """
        try:
            # 獲取當前選擇的資料庫
            current_db = get_current_database()
            if not current_db:
                info_label.configure(text="請先創建資料庫")  # 提示未選擇資料庫
                return

            # 嘗試連接到當前資料庫
            connection = get_connection(current_db)
            if connection:
                cursor = connection.cursor()  # 建立游標
                # 檢查是否已存在相同的資料
                cursor.execute(
                    f"SELECT COUNT(*) FROM {entry_table_name.get()} WHERE id = {entry_id.get()}"
                )
                # print(f"SELECT COUNT(*) FROM {entry_table_name.get()} WHERE id = {entry_id.get()}")
                # fetchone()讀取1行
                if cursor.fetchone()[0] > 0:
                    info_label.configure(text="資料已存在，請勿重複新增")  # 資料已存在提示
                    return

                # 若資料不存在，執行插入資料的 SQL 語句
                connection.autocommit = True  # 開啟自動提交模式
                connection.execute(
                    f"INSERT INTO {entry_table_name.get()} "
                    f"VALUES ({entry_id.get()}, '{entry_first_name.get()}', '{entry_last_name.get()}')"
                )
                info_label.configure(text="新增資料成功："+entry_id.get())  # 顯示成功訊息
            else:
                info_label.configure(text="連接資料庫失敗")  # 連接失敗提示
        except pyodbc.Error as ex:
            info_label.configure(text="新增資料失敗")  # 新增失敗提示
            print("Error:", ex)  # 印出錯誤訊息以供除錯

    # 建立主視窗
    app = tk.CTk()
    app.geometry("300x400")  # 設定視窗大小
    app.title("新增資料")  # 設定視窗標題

    # 資料表名稱輸入框
    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱")
    entry_table_name.place(relx=0.2, rely=0.1)  # 定位輸入框

    # ID 輸入框
    entry_id = tk.CTkEntry(app, placeholder_text="請輸入ID")
    entry_id.place(relx=0.2, rely=0.2)

    # 名字輸入框
    entry_first_name = tk.CTkEntry(app, placeholder_text="請輸入名字")
    entry_first_name.place(relx=0.2, rely=0.3)

    # 姓氏輸入框
    entry_last_name = tk.CTkEntry(app, placeholder_text="請輸入姓氏")
    entry_last_name.place(relx=0.2, rely=0.4)

    # 新增資料按鈕
    insert_button = tk.CTkButton(app, text="新增資料", command=insert, fg_color="green")
    insert_button.place(relx=0.2, rely=0.5)

    # 資訊標籤，用於顯示操作結果
    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.2, rely=0.6)

    # 顯示當前選擇的資料庫
    current_db = get_current_database()
    if current_db:
        current_db_label = tk.CTkLabel(app, text=f"當前資料庫: {current_db}")
        current_db_label.place(relx=0.2, rely=0.7)

    # 啟動視窗事件迴圈
    app.mainloop()
