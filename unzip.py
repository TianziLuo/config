import os
import shutil
import rarfile

def unzip():
    # Specify the path to unrar and rar executables
    rarfile.UNRAR_TOOL = r"C:\Program Files\WinRAR\unrar.exe"
    rarfile.RAR_TOOL = r"C:\Program Files\WinRAR\rar.exe"

    # Set folder paths
    downloads_path = os.path.expanduser("~/Downloads")
    desktop_path = os.path.expanduser("~/Desktop")
    final_folder_name = "uServePro"  # Final folder name
    d_drive_target = r"C:\uServePro"  # Target path on D drive

    # Find .rar files starting with "uServePro"
    files = [f for f in os.listdir(downloads_path) if f.startswith("uServePro") and f.endswith(".rar")]

    if not files:
        print("No .rar file starting with 'uServePro' was found!")
    else:
        print(f"File found: {files[0]}")

        try:
            # Full path to the .rar file
            rar_file = os.path.join(downloads_path, files[0])
            
            # Temporary extraction directory
            temp_extract_dir = os.path.join(desktop_path, "temp_extracted")
            if not os.path.exists(temp_extract_dir):
                os.makedirs(temp_extract_dir)
            
            # Extract the .rar file
            with rarfile.RarFile(rar_file, 'r') as rar_ref:
                rar_ref.extractall(temp_extract_dir)
            
            # Handle extracted content
            extracted_items = os.listdir(temp_extract_dir)
            if len(extracted_items) == 1 and os.path.isdir(os.path.join(temp_extract_dir, extracted_items[0])):
                # If a single folder exists, rename it directly
                extracted_folder = os.path.join(temp_extract_dir, extracted_items[0])
            else:
                # If multiple items exist, treat temp_extract_dir as the folder
                extracted_folder = temp_extract_dir

            # Final target folder on Desktop
            final_path = os.path.join(desktop_path, final_folder_name)
            
            # Remove existing folder with the same name, if it exists
            if os.path.exists(final_path):
                shutil.rmtree(final_path)
            
            # Rename or move extracted folder to the final name
            shutil.move(extracted_folder, final_path)
            
            # Cleanup temporary directory if it was not renamed
            if os.path.exists(temp_extract_dir):
                os.rmdir(temp_extract_dir)

            # Handle the D drive target
            if os.path.exists(d_drive_target):
                shutil.rmtree(d_drive_target)  # Remove the old folder if it exists
                print(f"Old folder on D drive has been deleted: {d_drive_target}")
            
            # Copy to D drive
            shutil.copytree(final_path, d_drive_target)
            print(f"Files have been successfully copied to D drive: {d_drive_target}")
            
            # Delete the renamed folder on Desktop
            shutil.rmtree(final_path)
            print(f"The folder on the Desktop has been deleted: {final_path}")
            
        except rarfile.BadRarFile:
            print("Unable to read the .rar file. Please check if the file is corrupted or the path is correct!")
        except Exception as e:
            print(f"An error occurred during extraction or copying: {e}")


"""
if __name__ == "__main__":
    unzip()
"""