import tkinter as tk
from tkinter import simpledialog
from lxml import etree

def mysql_string():
    # File path to the configuration file
    file_path = r"C:\uServePro\Server\uServeService.exe.config"

    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user for the new MySQL connection string
    new_value = simpledialog.askstring("MySQL String", "Please Input the Multiple Station MySQL String:")

    # If the user entered a new value, proceed to replace it in the XML file
    if isinstance(new_value, str) and new_value.strip():  # Ensure the input is not empty or just whitespace
        # Parse the XML file
        parser = etree.XMLParser(remove_blank_text=True)  # Preserve formatting
        tree = etree.parse(file_path, parser)
        root_elem = tree.getroot()

        # Find and update the target node for MySQL connection string
        for add_element in root_elem.xpath("//add[@name='mysql']"):
            add_element.attrib['connectionString'] = new_value.strip()  # Update the connection string

        # Save the modified XML file
        tree.write(file_path, encoding="utf-8", xml_declaration=True, pretty_print=True)
        print("MySQL connection string has been updated.")  # Notify the user
    else:
        print("Invalid input")  # Error message for invalid input

'''
if __name__ == "__main__":
    mysql_string()
'''