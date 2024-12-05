import tkinter as tk
from online_order import online_order
from mysql_string import mysql_string
from ip_config import ip_config
from store_info import store_info

def safe_execute(func):
    def wrapper():
        try:
            func()
        except Exception as e:
            print(f"Error executing {func.__name__}: {e}")
    return wrapper

def main():
    root = tk.Tk()
    root.title("Configuration Panel")
    root.geometry("400x240")  # 窗口大小
    root.configure(bg="#f0f0f0")  # 窗口背景颜色

    # 美化按钮样式
    button_style = {
        "width": 23,  # 按钮宽度（字符数）
        "font": ("Arial", 13, "bold"),
        "bg": "#FA8072",
        "fg": "white",
        "activebackground": "#FA9972",
        "activeforeground": "white",
    }

    # 按钮生成函数
    def create_button(text, command):
        return tk.Button(root, text=text, command=safe_execute(command), **button_style)

    # 按钮组件
    store_info_button = create_button("Store Info", store_info)
    mysql_string_button = create_button("MySQL String", mysql_string)
    config_file_button = create_button("Config File", ip_config)
    online_order_button = create_button("Online Order", online_order)

    store_info_button.pack(pady=(20, 10))
    # 布局（左右留白和上下间距）
    for button in [mysql_string_button, config_file_button, online_order_button]:
        button.pack(pady=8, padx=50)  # 上下间距为10，左右留白50

    # 启动主窗口
    root.mainloop()

if __name__ == "__main__":
    main()
