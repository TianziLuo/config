import tkinter as tk
from online_order import online_order
from mysql_string import mysql_string
from ip_config import ip_config
from store_info import store_info

# Decorator to safely execute functions, catching errors
def safe_execute(func):
    def wrapper():
        try:
            func()
        except Exception as e:
            print(f"Error executing {func.__name__}: {e}")
    return wrapper

def main():
    # Create the main window
    root = tk.Tk()
    root.title("SetUp Panel")  # Set window title
    root.geometry("400x240")  # Set window size
    root.configure(bg="#162A3B")  

    # Button style configuration
    button_style = {
        "width": 23,  
        "font": ("Arial", 13, "bold"),  
        "bg": "#305D82",  
        "fg": "white",  
        "activebackground": "#84AED1",  
        "activeforeground": "white",  
    }

    # Function to create a button with specific text and command
    def create_button(text, command):
        return tk.Button(root, text=text, command=safe_execute(command), **button_style)

    # Create buttons for different functionalities
    store_info_button = create_button("Store Info", store_info)
    mysql_string_button = create_button("MySQL String", mysql_string)
    config_file_button = create_button("Config File", ip_config)
    online_order_button = create_button("Online Order", online_order)

    # Pack the "Store Info" button with padding at the top and bottom
    store_info_button.pack(pady=(20, 10))

    # Pack the other buttons with padding and some space on the sides
    for button in [mysql_string_button, config_file_button, online_order_button]:
        button.pack(pady=8, padx=50)  # Vertical padding of 8, horizontal padding of 50

    # Start the Tkinter event loop to display the window
    root.mainloop()

if __name__ == "__main__":
    main()
