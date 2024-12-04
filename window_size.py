
def window_size(root):
    # 设置窗口是否可调整大小
    root.resizable(True, True)  # 可以调整大小

    # 可选：根据内容调整窗口大小
    root.update_idletasks()  # 更新窗口内容
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    root.geometry(f"{window_width}x{window_height}")