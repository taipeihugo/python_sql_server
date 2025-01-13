import customtkinter as tk
import pyodbc
from db_connection import get_connection, set_current_database, get_current_database

def delete_database_window():
    def delete_db():
        try:
            if not entry_database.get():
                info_label.configure(text="請輸入資料庫名稱")
                return

            connection = get_connection("master")
            if connection:
                connection.autocommit = True
                db_name = entry_database.get()
                
                # 首先將資料庫設為單一用戶模式
                
                # SINGLE_USER 將資料庫設為單一用戶模式
                # WITH ROLLBACK IMMEDIATE 會立即中斷所有現有的連接並回滾未完成的交易
                
                connection.execute(f"""
                    ALTER DATABASE [{db_name}] SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
                """)
                
                # 然後刪除資料庫
                connection.execute(f"DROP DATABASE [{db_name}]")
                
                if get_current_database() == db_name:
                    set_current_database(None)
                info_label.configure(text=f"刪除資料庫 {db_name} 成功")
            else:
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            info_label.configure(text=f"刪除資料庫失敗: {str(ex)}")

    app = tk.CTk()
    app.geometry("300x200")
    app.title("刪除資料庫")

    entry_database = tk.CTkEntry(app, placeholder_text="請輸入資料庫名稱")
    entry_database.place(relx=0.1, rely=0.2)

    delete_button = tk.CTkButton(app, text="刪除資料庫", command=delete_db, fg_color="red")
    delete_button.place(relx=0.1, rely=0.4)

    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.1, rely=0.6)

    app.mainloop()
