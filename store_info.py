import tkinter as tk
from tkinter import simpledialog
from lxml import etree

def store_info():
    # 文件路径
    file_path = r"C:\uServePro\Server\uServeService.exe.config"

    # 创建一个 Tkinter 根窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 弹出输入框，获取新的 value 内容
    new_value = simpledialog.askstring("Input Store Info", "please Input Store Info String:")

    # 如果用户输入了新的值，进行替换
    if new_value is not None:
        # 解析 XML 文件
        parser = etree.XMLParser(remove_blank_text=True)  # 保留格式
        tree = etree.parse(file_path, parser)
        root = tree.getroot()

        # 定位到需要修改的节点并替换 value
        for add_element in root.xpath("//add[@key='store']"):
            add_element.attrib['value'] = new_value  # 替换为用户输入的值

        # 保存修改后的文件
        tree.write(file_path, encoding="utf-8", xml_declaration=True, pretty_print=True)
