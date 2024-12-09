import tkinter as tk
from tkinter import simpledialog
from master_ip_main import master_ip_main
from server_ip_main import server_ip_main
from Master_ip.get_ip import get_ipconfig_ip

def ip_config():

    # Function to create the main window for "Master Serve" selection
    def master_serve_window():
        root = tk.Toplevel()
        root.title("Master Serve")  # Set the window title
        root.geometry("300x230")
        root.configure(bg="#305D82")  # Set background color

        # Label with increased font size and color
        label = tk.Label(root, text="Are you the master serve?", font=("Arial", 14), bg="#305D82", fg="white")
        label.pack(pady=20)

        master_serve_var = tk.IntVar(value=-1)  # Default value is -1 (no selection)

        tk.Radiobutton(root, text="Yes, I am the master serve", variable=master_serve_var, value=1, font=("Arial", 12), bg="#305D82", fg="white").pack(pady=10)
        tk.Radiobutton(root, text="No, I am not the master serve", variable=master_serve_var, value=0, font=("Arial", 12), bg="#305D82", fg="white").pack(pady=10)
        
        submit_button = tk.Button(
            root,
            text="Next",
            command=lambda: handle_master_serve(master_serve_var.get(), root),
            font=("Arial", 12, "bold"), 
            bg="#84AED1", 
            fg="black"
        )
        submit_button.pack(pady=10)

        root.mainloop()

    # Function to handle the next step based on "Master Serve" selection
    def handle_master_serve(is_master, root):
        if is_master == 1:
            root.destroy()  # Close the current window
            other_serves_window()
        elif is_master == 0:
            main_ip_address = simpledialog.askstring("Input", "Please enter the main server IP address:")
            if main_ip_address:
                server_ip_main(main_ip_address)  # Call the server_ip_main function with the provided IP
                print("Other se")
            root.destroy()
        else:
            print("Please select an option.")  # Print an error message if no option is selected

    # Function to create a window asking about additional serves
    def other_serves_window():
        window = tk.Toplevel()
        window.title("Other Serves")  # Set the window title
        window.geometry("300x230")
        window.configure(bg="#305D82")  # Set background color

        # Label with increased font size and color
        label = tk.Label(window, text="Are there any other serves?", font=("Arial", 14), bg="#305D82", fg="white")
        label.pack(pady=20)

        other_serves_var = tk.IntVar(value=-1)  # Default value is -1 (no selection)

        # Radiobuttons with increased font size
        tk.Radiobutton(window, text="Yes, there are other serves", variable=other_serves_var, value=1, font=("Arial", 12), bg="#305D82", fg="white").pack(pady=10)
        tk.Radiobutton(window, text="No, there are no other serves", variable=other_serves_var, value=0, font=("Arial", 12), bg="#305D82", fg="white").pack(pady=10)

        submit_button = tk.Button(
            window,
            text="Submit",
            command=lambda: handle_other_serves(other_serves_var.get(), window),
            font=("Arial", 12, "bold"), 
            bg="#84AED1", 
            fg="black"
        )
        
        submit_button.pack(pady=10)

        window.mainloop()

    # Function to handle the next step based on "Other Serves" selection
    def handle_other_serves(are_others, window):
        if are_others == 1:
            main_ip_address = get_ipconfig_ip()
            master_ip_main(main_ip_address)  # Call the master_ip_main function with the provided IP
            print("Master sever with other stations")
        elif are_others == 0:
            master_ip_main("127.0.0.1")
            print("No other serves, keep the setting.")  # Print a message if there are no other serves
        else:
            print("Please select an option.")  # Print an error message if no option is selected
        window.destroy()  # Close the current window
    

    master_serve_window()


# Call the function to start the program
if __name__ == "__main__":
    ip_config()
