import tkinter as tk
from tkinter import simpledialog
from lxml import etree

def store_info():
    # File path to the configuration file
    file_path = r"C:\uServePro\Server\uServeService.exe.config"

    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Prompt the user for a new value through an input dialog
    new_value = simpledialog.askstring("Store Info", "Please Input the Store Info String:")

    # If the user has entered a new value, proceed with replacing
    if isinstance(new_value, str) and new_value.strip():
        # Parse the XML file
        parser = etree.XMLParser(remove_blank_text=True)  # Keep the formatting intact
        tree = etree.parse(file_path, parser)
        root = tree.getroot()

        # Locate the element where the 'store' key is present and update its value
        for add_element in root.xpath("//add[@key='store']"):
            add_element.attrib['value'] = new_value  # Replace with the new value provided by the user

        # Save the modified XML back to the file
        tree.write(file_path, encoding="utf-8", xml_declaration=True, pretty_print=True)
        print("Store info has been updated.")  # Notify the user that the update is complete
    else:
        print("Invalid input")  # Error message for invalid input

'''
if __name__ == "__main__":
    store_info()
'''
