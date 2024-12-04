import tkinter as tk
from online_order import online_order
from mysql_string import mysql_string
from master_server_check import configs
from store_info import store_info

def main():
    # Function for "Store Info" button click
    def show_store_info():
        store_info()

    # Function for "MySQL String" button click
    def show_mysql_string():
        mysql_string()

    # Function for "Config File" button click
    def show_config_file():
        configs()

    # Function for "Online Order" button click
    def show_online_order():
        online_order()

    root = tk.Tk()
    root.title("Configuration Panel")
    root.geometry("300x300")  # Window size

    # Create buttons and attach the corresponding functions
    store_info_button = tk.Button(root, text="Store Info", width=20, command=show_store_info)
    store_info_button.pack(pady=10)

    mysql_string_button = tk.Button(root, text="MySQL String", width=20, command=show_mysql_string)
    mysql_string_button.pack(pady=10)

    config_file_button = tk.Button(root, text="Config File", width=20, command=show_config_file)
    config_file_button.pack(pady=10)

    online_order_button = tk.Button(root, text="Online Order", width=20, command=show_online_order)
    online_order_button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()