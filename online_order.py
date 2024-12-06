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
    print("The online order setting has been updated.")


def online_order():
    # File path
    file_path = r"C:\uServePro\Server\uServeService.exe.config"
    
    def on_submit():
        token = token_entry.get()
        store_id = store_id_entry.get()
        if token and store_id:
            update_config(file_path, token, store_id)
            # Show a success message
            messagebox.showinfo("Success", "The config has been updated successfully!")
        else:
            # Show an error message if either field is empty
            messagebox.showerror("Error", "Please fill in both fields.")

    # Create the Tkinter GUI
    root = tk.Tk()
    root.title("OO Config")
    root.geometry("300x180")  # Window size
    root.configure(bg="#305D82")

    # Center the window on the screen
    window_width = 300
    window_height = 150
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    # Token Label and Entry
    token_label = tk.Label(root, text="API Key:", font=("Arial", 12, "bold"), bg="#305D82", fg="white")
    token_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    token_entry = tk.Entry(root, justify='center', font=("Arial", 12),bg="#e9f4f7")
    token_entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    # Store ID Label and Entry
    store_id_label = tk.Label(root, text="Store ID:", font=("Arial", 12, "bold"), bg="#305D82", fg="white")
    store_id_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    store_id_entry = tk.Entry(root, justify='center', font=("Arial", 12), bg="#e9f4f7")
    store_id_entry.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Submit Button
    submit_button = tk.Button(root, text="Submit", command=on_submit, bg="#84AED1", fg="black", font=("Arial", 12, "bold"))
    submit_button.grid(row=2, column=0, columnspan=2, pady=15)

    # Start Tkinter main loop
    root.mainloop()

'''
if __name__ == "__main__":
    online_order()
'''