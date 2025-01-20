import customtkinter as tk
import pyodbc
from db_connection import get_connection, get_current_database

def update_data_window():
    """
    提供一個視窗，讓使用者能夠更新指定資料表中的資料。
    """
    def update():
        """
        處理資料更新的邏輯。
        根據使用者輸入的表名稱、ID 及新資料值進行更新。
        """
        try:
            current_db = get_current_database()  # 獲取當前資料庫
            if not current_db:  # 檢查是否選擇了資料庫
                info_label.configure(text="請先創建資料庫")
                return

            connection = get_connection(current_db)  # 建立資料庫連線
            if connection:
                connection.autocommit = True  # 啟用自動提交
                # 執行 UPDATE 語句，根據 ID 更新名字與姓氏
                connection.execute(
                    f"UPDATE {entry_table_name.get()} "
                    f"SET first_name = '{entry_first_name.get()}', last_name = '{entry_last_name.get()}' "
                    f"WHERE id = {entry_id.get()}"
                )
                # print(f"UPDATE {entry_table_name.get()} "
                #    f"SET first_name = '{entry_first_name.get()}', last_name = '{entry_last_name.get()}' "
                #    f"WHERE id = {entry_id.get()}")
                info_label.configure(text="資料更新成功")  # 更新成功訊息
            else:
                info_label.configure(text="連接資料庫失敗")  # 更新失敗訊息
        except pyodbc.Error as ex:  # 捕捉資料庫相關錯誤
            info_label.configure(text="資料更新失敗")
            print("Error:", ex)  # 印出錯誤訊息供除錯

    # 建立主視窗
    app = tk.CTk()
    app.geometry("300x400")  # 設定視窗大小
    app.title("修改資料")      # 設定視窗標題

    # 輸入框：資料表名稱
    entry_table_name = tk.CTkEntry(app, placeholder_text="請輸入工作表名稱")
    entry_table_name.place(relx=0.2, rely=0.1)

    # 輸入框：ID
    entry_id = tk.CTkEntry(app, placeholder_text="請輸入ID")
    entry_id.place(relx=0.2, rely=0.2)

    # 輸入框：新名字
    entry_first_name = tk.CTkEntry(app, placeholder_text="請輸入新名字")
    entry_first_name.place(relx=0.2, rely=0.3)

    # 輸入框：新姓氏
    entry_last_name = tk.CTkEntry(app, placeholder_text="請輸入新姓氏")
    entry_last_name.place(relx=0.2, rely=0.4)

    # 按鈕：執行修改
    update_button = tk.CTkButton(app, text="更新資料", command=update, fg_color="blue")
    update_button.place(relx=0.2, rely=0.5)

    # 資訊標籤：顯示結果
    info_label = tk.CTkLabel(app, text="")
    info_label.place(relx=0.2, rely=0.6)

    # 顯示當前選擇的資料庫
    current_db = get_current_database()
    if current_db:
        current_db_label = tk.CTkLabel(app, text=f"當前資料庫: {current_db}")
        current_db_label.place(relx=0.2, rely=0.7)

    app.mainloop()  # 啟動事件迴圈
