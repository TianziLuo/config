import tkinter as tk
from tkinter import messagebox
from lxml import etree


def update_config(file_path, token, store_id):

    # Parse the XML file
    parser = etree.XMLParser(remove_blank_text=True)  # Preserve formatting
    tree = etree.parse(file_path, parser)
    root_elem = tree.getroot()

    # Update the relevant XML nodes
    for add_element in root_elem.xpath("//add[@key='online_order']"):
        add_element.attrib['value'] = "true"
    for add_element in root_elem.xpath("//add[@key='token']"):
        add_element.attrib['value'] = token
    for add_element in root_elem.xpath("//add[@key='store_id']"):
        add_element.attrib['value'] = store_id

    # Save the modified file
    tree.write(file_path, encoding="utf-8", xml_declaration=True, pretty_print=True)
    messagebox.showinfo("Success", "The online order setting has been updated successfully.")
 
      
def online_order():
    # File path
    file_path = r"C:\uServePro\Server\uServeService.exe.config"
    
    def on_submit():
        token = token_entry.get()
        store_id = store_id_entry.get()
        if token and store_id:
            update_config(file_path, token, store_id)

    # Create the Tkinter GUI
    root = tk.Tk()
    root.title("OO config")
    root.geometry("250x100")  # 窗口大小
  
    # Token Label and Entry
    tk.Label(root, text="Token:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    token_entry = tk.Entry(root, justify='center')
    token_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    # Store ID Label and Entry
    tk.Label(root, text="Store ID:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    store_id_entry = tk.Entry(root, justify='center')
    store_id_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    # Submit Button
    submit_button = tk.Button(root, text="Update Config", command = on_submit)  # command为空，待定义
    submit_button.grid(row=2, column=0, columnspan=2, pady=10)

    # 启动Tkinter主循环
    root.mainloop()

'''
if __name__ == "__main__":
    online_order()
'''
