import customtkinter as tk
import pyodbc
from db_connection import get_connection, set_current_database, get_current_database

# 定義刪除資料庫的視窗
def delete_database_window():
    # 刪除資料庫的功能
    def delete_db():
        try:
            # 檢查是否輸入了資料庫名稱
            if not entry_database.get():
                info_label.configure(text="請輸入資料庫名稱")
                return

            # 連接到 master 資料庫以進行資料庫管理操作
            connection = get_connection("master")
            if connection:
                # 啟用自動提交模式，確保立即執行 SQL 語句
                connection.autocommit = True
                db_name = entry_database.get()

                # 將資料庫設為單一用戶模式以便刪除
                # SINGLE_USER 模式確保只有一個用戶連接，並且中斷其他連接
                # WITH ROLLBACK IMMEDIATE 確保未完成的交易會回滾
                connection.execute(f"""ALTER DATABASE {db_name} SET SINGLE_USER WITH ROLLBACK IMMEDIATE;""")
                # print(f"""ALTER DATABASE {db_name} SET SINGLE_USER WITH ROLLBACK IMMEDIATE;""")
                # 刪除指定名稱的資料庫
                connection.execute(f"DROP DATABASE {db_name}")
                # print(f"DROP DATABASE {db_name}")
                # 如果刪除的資料庫是當前選擇的資料庫，則重置當前資料庫為 None
                if get_current_database() == db_name:
                    set_current_database(None)

                # 顯示成功訊息
                info_label.configure(text=f"刪除資料庫 {db_name} 成功")
            else:
                # 如果連接失敗，顯示錯誤信息
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            # 捕捉刪除操作中的錯誤並顯示詳細錯誤訊息
            info_label.configure(text=f"刪除資料庫失敗: {str(ex)}")

    # 初始化視窗
    app = tk.CTk()
    app.geometry("300x200")  # 設定視窗大小
    app.title("刪除資料庫")  # 設定視窗標題

    # 輸入資料庫名稱的文字框
    entry_database = tk.CTkEntry(app, placeholder_text="請輸入資料庫名稱")
    entry_database.place(relx=0.1, rely=0.2)

    # 刪除資料庫的按鈕，點擊後執行刪除功能
    delete_button = tk.CTkButton(app, text="刪除資料庫", command=delete_db, fg_color="red")
    delete_button.place(relx=0.1, rely=0.4)

    # 顯示操作結果或提示信息的標籤
    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.1, rely=0.6)

    # 啟動視窗的事件循環
    app.mainloop()
