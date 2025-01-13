import customtkinter as tk
import pyodbc
from db_connection import get_connection, get_current_database

def delete_data_window():
    def delete():
        try:
            current_db = get_current_database()
            if not current_db:
                info_label.configure(text="請先創建資料庫")
                return

            connection = get_connection(current_db)
            if connection:
                connection.autocommit = True
                connection.execute(f"DELETE FROM {entry_table_name.get()} WHERE id = {entry_id.get()}")
                info_label.configure(text="刪除成功")
            else:
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            info_label.configure(text="刪除失敗")

    app = tk.CTk()
    app.geometry("300x300")
    app.title("刪除資料")

    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱")
    entry_table_name.place(relx=0.2, rely=0.1)
    entry_id = tk.CTkEntry(app, placeholder_text="請輸入ID")
    entry_id.place(relx=0.2, rely=0.2)

    delete_button = tk.CTkButton(app, text="刪除", command=delete, fg_color="red")
    delete_button.place(relx=0.2, rely=0.4)

    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.2, rely=0.5)

    # 顯示當前選擇的資料庫
    current_db = get_current_database()
    if current_db:
        current_db_label = tk.CTkLabel(app, text=f"當前資料庫: {current_db}")
        current_db_label.place(relx=0.2, rely=0.6)

    app.mainloop()
