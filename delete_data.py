import customtkinter as tk
import pyodbc
from db_connection import get_connection, get_current_database

# 定義刪除資料的視窗
def delete_data_window():
    # 刪除功能
    def delete():
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
                # 啟用自動提交模式以執行刪除操作
                connection.autocommit = True
                # 執行刪除 SQL 語句
                connection.execute(f"DELETE FROM {entry_table_name.get()} WHERE id = {entry_id.get()}")
                # print(f"DELETE FROM {entry_table_name.get()} WHERE id = {entry_id.get()}")
                # 刪除成功後更新提示信息
                info_label.configure(text="刪除成功")
            else:
                # 如果連接失敗，顯示錯誤信息
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            # 捕捉刪除操作中的錯誤並顯示提示
            info_label.configure(text="刪除失敗")

    # 初始化視窗
    app = tk.CTk()
    app.geometry("300x300")  # 設定視窗大小
    app.title("刪除資料")  # 設定視窗標題

    # 輸入工作表名稱的文字框
    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱")
    entry_table_name.place(relx=0.2, rely=0.1)

    # 輸入 ID 的文字框
    entry_id = tk.CTkEntry(app, placeholder_text="請輸入ID")
    entry_id.place(relx=0.2, rely=0.2)

    # 刪除按鈕，點擊後執行刪除功能
    delete_button = tk.CTkButton(app, text="刪除", command=delete, fg_color="red")
    delete_button.place(relx=0.2, rely=0.4)

    # 顯示操作結果或提示信息的標籤
    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.2, rely=0.5)

    # 顯示當前選擇的資料庫
    current_db = get_current_database()
    if current_db:
        current_db_label = tk.CTkLabel(app, text=f"當前資料庫: {current_db}")
        current_db_label.place(relx=0.2, rely=0.6)

    # 啟動視窗的事件循環
    app.mainloop()
