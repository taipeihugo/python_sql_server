import customtkinter as tk
import pyodbc
from db_connection import get_connection, get_current_database

def create_table_window():
    def create():
        try:
            current_db = get_current_database()
            if not current_db:
                info_label.configure(text="請先創建資料庫")
                return

            if not radio_var_col1.get() or not radio_var_col2.get() or not radio_var_col3.get():
                info_label.configure(text="請為所有欄位選擇資料型態")
                return

            connection = get_connection(current_db)
            if connection:
                connection.autocommit = True
                sql_stmt = (
                    f"CREATE TABLE {entry_table_name.get()} ("
                    f"{entry_column1.get()} {radio_var_col1.get()}, "
                    f"{entry_column2.get()} {radio_var_col2.get()}, "
                    f"{entry_column3.get()} {radio_var_col3.get()})"
                )
                connection.execute(sql_stmt)
                info_label.configure(text="創建資料表成功")
            else:
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            info_label.configure(text="創建資料表失敗")
            print("Error:", ex)

    app = tk.CTk()
    app.geometry("600x400")
    app.title("創建工作表")

    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱", width=200)
    entry_table_name.place(relx=0.1, rely=0.1)

    entry_column1 = tk.CTkEntry(app, placeholder_text="column1", width=200)
    entry_column1.place(relx=0.1, rely=0.2)
    entry_column2 = tk.CTkEntry(app, placeholder_text="column2", width=200)
    entry_column2.place(relx=0.1, rely=0.3)
    entry_column3 = tk.CTkEntry(app, placeholder_text="column3", width=200)
    entry_column3.place(relx=0.1, rely=0.4)

    radio_var_col1 = tk.StringVar(value="")
    tk.CTkRadioButton(app, text="VARCHAR(50)", variable=radio_var_col1, value="VARCHAR(50)").place(relx=0.5, rely=0.2)
    tk.CTkRadioButton(app, text="INTEGER", variable=radio_var_col1, value="INTEGER").place(relx=0.7, rely=0.2)

    radio_var_col2 = tk.StringVar(value="")
    tk.CTkRadioButton(app, text="VARCHAR(50)", variable=radio_var_col2, value="VARCHAR(50)").place(relx=0.5, rely=0.3)
    tk.CTkRadioButton(app, text="INTEGER", variable=radio_var_col2, value="INTEGER").place(relx=0.7, rely=0.3)

    radio_var_col3 = tk.StringVar(value="")
    tk.CTkRadioButton(app, text="VARCHAR(50)", variable=radio_var_col3, value="VARCHAR(50)").place(relx=0.5, rely=0.4)
    tk.CTkRadioButton(app, text="INTEGER", variable=radio_var_col3, value="INTEGER").place(relx=0.7, rely=0.4)

    create_button = tk.CTkButton(app, text="建立工作表", command=create)
    create_button.place(relx=0.1, rely=0.5)

    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.1, rely=0.6)

    # 顯示當前選擇的資料庫
    current_db = get_current_database()
    if current_db:
        current_db_label = tk.CTkLabel(app, text=f"當前資料庫: {current_db}")
        current_db_label.place(relx=0.1, rely=0.7)

    app.mainloop()
