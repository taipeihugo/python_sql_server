import customtkinter as tk
import pyodbc
from db_connection import get_connection, get_current_database

# 定義範圍查詢的視窗
def between_data_window():
    # 查詢功能
    def select():
        try:
            # 獲取當前使用的資料庫名稱
            current_db = get_current_database()
            if not current_db:
                # 如果沒有選擇資料庫，提示用戶先創建資料庫
                info_label.configure(text="請先創建資料庫")
                return

            # 建立資料庫連接
            connection = get_connection(current_db)
            if connection:
                # 執行 SQL 查詢
                cursor = connection.cursor()
                cursor.execute(f"SELECT * FROM {entry_table_name.get()} WHERE id BETWEEN {entry_id_1.get()} AND {entry_id_2.get()}")
                
                # 解析查詢結果
                result = ""
                for data in cursor:
                    result += f"{data[0]} {data[1]} {data[2]}\n"  # 假設每筆資料有三個欄位
                
                # 如果有查詢結果，顯示結果，否則顯示查無資料
                info_label.configure(text=result if result else "查無資料")
            else:
                # 如果連接失敗，顯示錯誤信息
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            # 捕捉資料庫查詢錯誤並顯示提示
            info_label.configure(text="查無資料或工作表")

    # 初始化視窗
    app = tk.CTk()
    app.geometry("400x300")  # 設定視窗大小
    app.title("範圍查詢")  # 設定視窗標題

    # 輸入工作表名稱的文字框
    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱")
    entry_table_name.place(relx=0.2, rely=0.1)

    # 輸入起始 ID 的文字框
    entry_id_1 = tk.CTkEntry(app, placeholder_text="請輸入起始ID")
    entry_id_1.place(relx=0.2, rely=0.2)

    # 輸入結束 ID 的文字框
    entry_id_2 = tk.CTkEntry(app, placeholder_text="請輸入結束ID")
    entry_id_2.place(relx=0.2, rely=0.3)

    # 查詢按鈕，點擊後執行查詢功能
    select_button = tk.CTkButton(app, text="查詢", command=select, fg_color="green")
    select_button.place(relx=0.2, rely=0.4)

    # 顯示查詢結果或提示信息的標籤
    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.2, rely=0.5)

    # 顯示當前選擇的資料庫
    current_db = get_current_database()
    if current_db:
        current_db_label = tk.CTkLabel(app, text=f"當前資料庫: {current_db}")
        current_db_label.place(relx=0.2, rely=0.6)

    # 啟動視窗的事件循環
    app.mainloop()
