import tkinter as tk
from tkinter import simpledialog
from master_ip_main import master_ip_main
from server_ip_main import server_ip_main

# Function to create the main window for "Master Serve" selection
def master_serve_window():
    # Create the main Tkinter root window
    root = tk.Tk()
    root.title("Master Serve")  # Set the window title

    # Set the size of the window
    root.geometry("300x200")

    # Add a label to prompt the user
    label = tk.Label(root, text="Are you the master serve?")
    label.pack(pady=10)

    # Create an integer variable to store the state of the radio buttons
    master_serve_var = tk.IntVar(value=-1)  # Default value is -1 (no selection)

    # Create radio buttons for "Yes" and "No" options
    tk.Radiobutton(root, text="Yes, I am the master serve", variable=master_serve_var, value=1).pack(pady=10)
    tk.Radiobutton(root, text="No, I am not the master serve", variable=master_serve_var, value=0).pack(pady=10)

    # Create a "Next" button to proceed to the next step
    submit_button = tk.Button(
        root,
        text="Next",
        command=lambda: handle_master_serve(master_serve_var.get(), root)
    )
    submit_button.pack(pady=10)

    # Start the Tkinter main event loop
    root.mainloop()

# Function to handle the next step based on "Master Serve" selection
def handle_master_serve(is_master, root):
    if is_master == 1:
        # If the user is the master serve, proceed to the next window
        root.destroy()  # Close the current window
        other_serves_window()
    elif is_master == 0:
        # If the user is not the master serve, prompt for the main server's IP address
        main_ip_address = simpledialog.askstring("Input", "Please enter the main server IP address:")
        if main_ip_address:
            server_ip_main(main_ip_address)  # Call the server_ip_main function with the provided IP
        root.destroy()
    else:
        print("Please select an option.")  # Print an error message if no option is selected

# Function to create a window asking about additional serves
def other_serves_window():
    # Create a new window
    window = tk.Tk()
    window.title("Other Serves")  # Set the window title

    # Set the size of the window
    window.geometry("300x200")

    # Add a label to prompt the user
    label = tk.Label(window, text="Are there any other serves?")
    label.pack(pady=10)

    # Create an integer variable to store the state of the radio buttons
    other_serves_var = tk.IntVar(value=-1)  # Default value is -1 (no selection)

    # Create radio buttons for "Yes" and "No" options
    tk.Radiobutton(window, text="Yes, there are other serves", variable=other_serves_var, value=1).pack(pady=10)
    tk.Radiobutton(window, text="No, there are no other serves", variable=other_serves_var, value=0).pack(pady=10)

    # Create a "Submit" button to proceed
    submit_button = tk.Button(
        window,
        text="Submit",
        command=lambda: handle_other_serves(other_serves_var.get(), window)
    )
    submit_button.pack(pady=10)

    # Start the Tkinter main event loop for this window
    window.mainloop()

# Function to handle the next step based on "Other Serves" selection
def handle_other_serves(are_others, window):
    if are_others == 1:
        # If there are other serves, prompt for the main server's IP address
        main_ip_address = simpledialog.askstring("Input", "Please enter the main server IP address:")
        if main_ip_address:
            master_ip_main(main_ip_address)  # Call the master_ip_main function with the provided IP
    elif are_others == 0:
        master_ip_main("127.0.0.1")
        print("No other serves.")  # Print a message if there are no other serves
    else:
        print("Please select an option.")  # Print an error message if no option is selected
    window.destroy()  # Close the current window

# Entry point of the script
if __name__ == "__main__":
    master_serve_window()
