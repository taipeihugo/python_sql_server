import customtkinter as tk
import pyodbc
from db_connection import get_connection, set_current_database

def create_database_window():
    def create_db():
        try:
            connection = get_connection("master")
            if connection:
                connection.autocommit = True
                db_name = entry_database.get()
                connection.execute(f"CREATE DATABASE {db_name}")
                set_current_database(db_name)
                info_label.configure(text="創建資料庫成功，當前資料庫: " + db_name)
            else:
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            info_label.configure(text="創建資料庫失敗")

    app = tk.CTk()
    app.geometry("300x200")
    app.title("創建資料庫")

    entry_database = tk.CTkEntry(app, placeholder_text="請輸入資料庫名稱")
    entry_database.place(relx=0.1, rely=0.2)

    create_button = tk.CTkButton(app, text="建立資料庫", command=create_db, fg_color="green")
    create_button.place(relx=0.1, rely=0.4)

    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.1, rely=0.6)

    app.mainloop()
