import tkinter as tk
from tkinter import simpledialog
from lxml import etree

def mysql_string():
# 文件路径
    file_path = r"C:\uServePro\Server\uServeService.exe.config"

    # 创建一个 Tkinter 根窗口
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    # 弹出输入框，获取新的 value 内容
    new_value = simpledialog.askstring("Input mySQL String", "please Input the mySQL String:")

    # 如果用户输入了新的值，进行替换
    if new_value is not None and new_value.strip():
            # Parse the XML file
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(file_path, parser)
        root_elem = tree.getroot()

            # Find and update the target node
        for add_element in root_elem.xpath("//add[@name='mysql']"):
            add_element.attrib['connectionString'] = new_value.strip()

        # 保存修改后的文件
    tree.write(file_path, encoding="utf-8", xml_declaration=True, pretty_print=True)
