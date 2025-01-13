import pyodbc
import customtkinter as tk

# 全域變數儲存資料庫名稱
current_database = None

def get_connection(database_name):
    try:
        return pyodbc.connect(
            'DRIVER={SQL Server};' +
            f'SERVER=vm-hungtao;DATABASE={database_name};' +
            'Trusted_Connection=True;'
        )
    except pyodbc.Error as ex:
        return None

def create_database_window():
    def create_db():
        global current_database
        try:
            connection = get_connection("master")
            if connection:
                connection.autocommit = True
                connection.execute(f"CREATE DATABASE {entry_database.get()}")
                current_database = entry_database.get()
                info_label.configure(text="創建資料庫成功，當前資料庫: " + current_database)
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

def create_table_window():
    def create():
        try:
            if not current_database:
                info_label.configure(text="請先創建資料庫")
                return

            if not radio_var_col1.get() or not radio_var_col2.get() or not radio_var_col3.get():
                info_label.configure(text="請為所有欄位選擇資料型態")
                return

            connection = get_connection(current_database)
            if connection:
                connection.autocommit = True
                sql_stmt = (
                    f"CREATE TABLE {entry_table_name.get()} ("
                    f"{entry_column1.get()} {radio_var_col1.get()}, "
                    f"{entry_column2.get()} {radio_var_col2.get()}, "
                    f"{entry_column3.get()} {radio_var_col3.get()})"
                )
                print("Generated SQL:", sql_stmt)  # Debugging line
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

    app.mainloop()

def insert_data_window():
    def insert():
        try:
            if not current_database:
                info_label.configure(text="請先創建資料庫")
                return

            connection = get_connection(current_database)
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

    app.mainloop()

def select_data_window():
    def select():
        try:
            if not current_database:
                info_label.configure(text="請先創建資料庫")
                return

            connection = get_connection(current_database)
            if connection:
                cursor = connection.cursor()
                cursor.execute(f"SELECT * FROM {entry_table_name.get()} WHERE id = {entry_id.get()}")
                result = ""
                for data in cursor:
                    result += f"{data[0]} {data[1]} {data[2]}\n"
                info_label.configure(text=result if result else "查無資料")
            else:
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            info_label.configure(text="查無資料或工作表")

    app = tk.CTk()
    app.geometry("300x300")
    app.title("查詢資料")

    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱")
    entry_table_name.place(relx=0.2, rely=0.1)
    entry_id = tk.CTkEntry(app, placeholder_text="請輸入ID")
    entry_id.place(relx=0.2, rely=0.2)

    select_button = tk.CTkButton(app, text="查詢", command=select, fg_color="green")
    select_button.place(relx=0.2, rely=0.3)

    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.2, rely=0.4)

    app.mainloop()

def delete_data_window():
    def delete():
        try:
            if not current_database:
                info_label.configure(text="請先創建資料庫")
                return

            connection = get_connection(current_database)
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

    app.mainloop()

def between_data_window():
    def select():
        try:
            if not current_database:
                info_label.configure(text="請先創建資料庫")
                return

            connection = get_connection(current_database)
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

    app.mainloop()

def delete_database_window():
    def delete_db():
        global current_database
        try:
            if not entry_database.get():
                info_label.configure(text="請輸入資料庫名稱")
                return

            connection = get_connection("master")
            if connection:
                connection.autocommit = True
                db_name = entry_database.get()
                connection.execute(f"DROP DATABASE [{db_name}]")
                if current_database == db_name:
                    current_database = None
                info_label.configure(text=f"刪除資料庫 {db_name} 成功")
            else:
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            info_label.configure(text=f"刪除資料庫失敗: {ex}")

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


def main_window():
    app = tk.CTk()
    app.geometry("400x400")
    app.title("資料庫管理系統")

    tk.CTkButton(app, text="創建資料庫", command=create_database_window).pack(pady=10)
    tk.CTkButton(app, text="創建工作表", command=create_table_window).pack(pady=10)
    tk.CTkButton(app, text="新增資料", command=insert_data_window).pack(pady=10)
    tk.CTkButton(app, text="查詢資料", command=select_data_window).pack(pady=10)
    tk.CTkButton(app, text="刪除資料", command=delete_data_window).pack(pady=10)
    tk.CTkButton(app, text="範圍查詢", command=between_data_window).pack(pady=10)
    tk.CTkButton(app, text="刪除資料庫", command=delete_database_window).pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    main_window()
