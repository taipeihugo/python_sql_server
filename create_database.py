import customtkinter as tk
# 匯入 customtkinter 作為 tk，用於建立具有自訂樣式的 GUI 視窗
import pyodbc  # 匯入 pyodbc 模組，用於與 SQL Server 資料庫進行連線
from db_connection import get_connection, set_current_database
# 匯入自定義的資料庫連線函式和設定當前資料庫的函式

def create_database_window():
    """
    建立創建資料庫的視窗，讓使用者輸入資料庫名稱，並執行創建動作。
    """
    def create_db():
        """
        創建資料庫的內部邏輯，包含輸入驗證與連線操作。
        """
        try:
            # 嘗試連接到 SQL Server 的 master 資料庫
            connection = get_connection("master")
            if connection:
                connection.autocommit = True  # 啟用自動提交模式
                db_name = entry_database.get()  # 從輸入欄獲取資料庫名稱
                
                # 驗證資料庫名稱是否為空
                if not db_name.strip():
                    info_label.configure(text="資料庫名稱不可為空")  # 顯示錯誤訊息
                    return
                
                # 執行 SQL 語句以創建新資料庫
                connection.execute(f"CREATE DATABASE {db_name}")
                set_current_database(db_name)  # 設定當前資料庫為新創建的資料庫
                
                # 更新標籤以顯示成功訊息
                info_label.configure(text="創建資料庫成功，當前資料庫: " + db_name)
            else:
                # 無法連接到資料庫時，顯示錯誤訊息
                info_label.configure(text="連接資料庫失敗")
        except pyodbc.Error as ex:
            # 捕捉資料庫操作的例外，並顯示詳細錯誤訊息
            info_label.configure(text=f"創建資料庫失敗: {ex}")

    # 創建主視窗
    app = tk.CTk()
    app.geometry("300x200")  # 設定視窗大小為 300x200 像素
    app.title("創建資料庫")  # 設定視窗標題

    # 資料庫名稱輸入欄位
    entry_database = tk.CTkEntry(app, placeholder_text="請輸入資料庫名稱")
    entry_database.place(relx=0.1, rely=0.2)  # 設定位置於視窗內的相對位置

    # 創建資料庫按鈕
    create_button = tk.CTkButton(app, text="建立資料庫", command=create_db, fg_color="green")
    create_button.place(relx=0.1, rely=0.4)  # 設定按鈕位置於視窗內的相對位置

    # 資訊標籤，用於顯示操作結果（成功或失敗）
    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.1, rely=0.6)  # 設定標籤位置於視窗內的相對位置

    # 啟動視窗事件迴圈，讓視窗保持開啟狀態
    app.mainloop()
