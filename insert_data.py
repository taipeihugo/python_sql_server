import customtkinter as tk
import pyodbc
from db_connection import get_connection, get_current_database

def insert_data_window():
    def insert():
        try:
            current_db = get_current_database()
            if not current_db:
                info_label.configure(text="請先創建資料庫")
                return

            connection = get_connection(current_db)
            if connection:
                connection.autocommit = True
                connection.execute(f"INSERT INTO {entry_table_name.get()} VALUES ({entry_id.get()}, '{entry_first_name.get()}', '{entry_last_name.get()}')")
                info_label.configure(text="新增資料成功")
            else:
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            info_label.configure(text="新增資料失敗")

    app = tk.CTk()
    app.geometry("300x400")
    app.title("新增資料")

    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱")
    entry_table_name.place(relx=0.2, rely=0.1)
    entry_id = tk.CTkEntry(app, placeholder_text="請輸入ID")
    entry_id.place(relx=0.2, rely=0.2)
    entry_first_name = tk.CTkEntry(app, placeholder_text="請輸入名字")
    entry_first_name.place(relx=0.2, rely=0.3)
    entry_last_name = tk.CTkEntry(app, placeholder_text="請輸入姓氏")
    entry_last_name.place(relx=0.2, rely=0.4)

    insert_button = tk.CTkButton(app, text="新增資料", command=insert, fg_color="green")
    insert_button.place(relx=0.2, rely=0.5)

    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.2, rely=0.6)

    # 顯示當前選擇的資料庫
    current_db = get_current_database()
    if current_db:
        current_db_label = tk.CTkLabel(app, text=f"當前資料庫: {current_db}")
        current_db_label.place(relx=0.2, rely=0.7)

    app.mainloop()
