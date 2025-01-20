import customtkinter as tk
import pyodbc
from db_connection import get_connection, get_current_database

def select_data_window():
    """
    建立一個 GUI 視窗，提供查詢資料功能。
    使用者可輸入資料表名稱及 ID 進行資料查詢，顯示對應的結果。
    """
    def select():
        """
        處理資料查詢邏輯，根據使用者輸入的表名稱和 ID 查詢資料表中的記錄。
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
                # 執行查詢語句，根據表名和 ID 查詢
                cursor.execute(f"SELECT * FROM {entry_table_name.get()} WHERE id = {entry_id.get()}")
                # print(f"SELECT * FROM {entry_table_name.get()} WHERE id = {entry_id.get()}")
                result = ""
                # 遍歷查詢結果，將記錄格式化為字串
                for data in cursor:
                    result += f"{data[0]} {data[1]} {data[2]}\n"
                # 如果有結果，顯示記錄；否則提示查無資料
                info_label.configure(text=result if result else "查無資料")
            else:
                info_label.configure(text="連接資料庫失敗")  # 連接失敗提示
        except pyodbc.Error as ex:
            info_label.configure(text="查無資料或工作表")  # 查詢失敗提示
            print("Error:", ex)  # 印出錯誤訊息以供除錯

    # 建立主視窗
    app = tk.CTk()
    app.geometry("300x300")  # 設定視窗大小
    app.title("查詢資料")  # 設定視窗標題

    # 資料表名稱輸入框
    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱")
    entry_table_name.place(relx=0.2, rely=0.1)  # 定位輸入框

    # ID 輸入框
    entry_id = tk.CTkEntry(app, placeholder_text="請輸入ID")
    entry_id.place(relx=0.2, rely=0.2)

    # 查詢按鈕
    select_button = tk.CTkButton(app, text="查詢", command=select, fg_color="green")
    select_button.place(relx=0.2, rely=0.3)

    # 資訊標籤，用於顯示查詢結果或錯誤提示
    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.2, rely=0.4)

    # 顯示當前選擇的資料庫
    current_db = get_current_database()
    if current_db:
        current_db_label = tk.CTkLabel(app, text=f"當前資料庫: {current_db}")
        current_db_label.place(relx=0.2, rely=0.5)

    # 啟動視窗事件迴圈
    app.mainloop()