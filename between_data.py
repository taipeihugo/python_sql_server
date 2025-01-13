import customtkinter as tk
import pyodbc
from db_connection import get_connection, get_current_database

def between_data_window():
    def select():
        try:
            current_db = get_current_database()
            if not current_db:
                info_label.configure(text="請先創建資料庫")
                return

            connection = get_connection(current_db)
            if connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT * FROM {entry_table_name.get()} WHERE id BETWEEN {entry_id_1.get()} AND {entry_id_2.get()}")
                result = ""
                for data in cursor:
                    result += f"{data[0]} {data[1]} {data[2]}\n"
                info_label.configure(text=result if result else "查無資料")
            else:
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            info_label.configure(text="查無資料或工作表")

    app = tk.CTk()
    app.geometry("400x300")
    app.title("範圍查詢")

    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱")
    entry_table_name.place(relx=0.2, rely=0.1)
    entry_id_1 = tk.CTkEntry(app, placeholder_text="請輸入起始ID")
    entry_id_1.place(relx=0.2, rely=0.2)
    entry_id_2 = tk.CTkEntry(app, placeholder_text="請輸入結束ID")
    entry_id_2.place(relx=0.2, rely=0.3)

    select_button = tk.CTkButton(app, text="查詢", command=select, fg_color="green")
    select_button.place(relx=0.2, rely=0.4)

    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.2, rely=0.5)

    # 顯示當前選擇的資料庫
    current_db = get_current_database()
    if current_db:
        current_db_label = tk.CTkLabel(app, text=f"當前資料庫: {current_db}")
        current_db_label.place(relx=0.2, rely=0.6)

    app.mainloop()
