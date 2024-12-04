import configparser

def master_ip_app(ip):
    app_path = r"C:\uServePro\App\config.ini"
    """
    Updates the IP addresses in a .ini file while preserving comments and formatting.

    Parameters:
    - ip (str): The new IP address to set.
    - app_path (str): The path to the .ini file.
    """
    with open(app_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        # Update specific lines containing the IP addresses
        if "URL_MAIN" in line:
            updated_lines.append(f"URL_MAIN=http://{ip}:8888/index.html\n")
        elif "URL_SECONDARY" in line:
            updated_lines.append(f"URL_SECONDARY=http://{ip}:8888/dual\n")
        elif line.strip().startswith("IP="):  # For SERVER and LOCAL sections
            updated_lines.append(f"IP={ip}\n")
        else:
            # Keep the line as is
            updated_lines.append(line)

    # Write back to the file
    with open(app_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

'''
if __name__ == "__main__":
    ip = "127.0.0.1"
    master_ip_app(ip)
'''

