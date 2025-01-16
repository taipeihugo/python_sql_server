import customtkinter as tk
# 匯入 customtkinter 作為 tk，用於建立具有自訂樣式的 GUI 應用程式

# 匯入各個功能模組的視窗函式
from create_database import create_database_window  # 創建資料庫的視窗函式
from create_table import create_table_window        # 創建資料表的視窗函式
from insert_data import insert_data_window          # 新增資料的視窗函式
from select_data import select_data_window          # 查詢資料的視窗函式
from delete_data import delete_data_window          # 刪除資料的視窗函式
from between_data import between_data_window        # 範圍查詢的視窗函式
from delete_database import delete_database_window  # 刪除資料庫的視窗函式

def main_window():
    """
    建立資料庫管理系統的主視窗，並添加多個功能按鈕，讓使用者執行不同的資料庫操作。
    """
    app = tk.CTk()              # 建立主視窗物件
    app.geometry("300x400")     # 設定視窗大小為 400x400 像素
    app.title("資料庫管理系統")  # 設定視窗標題為 "資料庫管理系統"

    # 添加功能按鈕，並綁定到對應的功能視窗函式
    tk.CTkButton(app, text="創建資料庫", command=create_database_window).pack(pady=10)  # 按鈕：創建資料庫
    tk.CTkButton(app, text="創建工作表", command=create_table_window).pack(pady=10)    # 按鈕：創建工作表
    tk.CTkButton(app, text="新增資料", command=insert_data_window).pack(pady=10)       # 按鈕：新增資料
    tk.CTkButton(app, text="查詢資料", command=select_data_window).pack(pady=10)       # 按鈕：查詢資料
    tk.CTkButton(app, text="範圍查詢", command=between_data_window).pack(pady=10)      # 按鈕：範圍查詢
    tk.CTkButton(app, text="刪除資料", command=delete_data_window).pack(pady=10)       # 按鈕：刪除資料
    tk.CTkButton(app, text="刪除資料庫", command=delete_database_window).pack(pady=10)  # 按鈕：刪除資料庫

    app.mainloop()  # 啟動事件迴圈，讓視窗保持運行，等待使用者互動

if __name__ == "__main__":
    """
    若此程式是直接執行，則啟動 main_window() 函式來開啟主視窗。
    """
    main_window()
