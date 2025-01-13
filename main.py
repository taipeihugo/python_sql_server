import customtkinter as tk
from create_database import create_database_window
from create_table import create_table_window
from insert_data import insert_data_window
from select_data import select_data_window
from delete_data import delete_data_window
from between_data import between_data_window
from delete_database import delete_database_window

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
