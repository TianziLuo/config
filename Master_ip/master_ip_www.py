import os
import json

def master_ip_www(ip):
    www_path = r"C:\uServePro\Server\www\assets\config.json"

    # Read the JSON file as plain text to preserve comments and format
    with open(www_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # Load the JSON data from the file (ignore comments and extra whitespace)
    content = ''.join(lines)
    data = json.loads(content)

        # Update the IP values
    data['SERVER_URL'] = ip
    data['WS_URL'] = f"{ip}:10180"  # Dynamically build WS_URL
    data['SERVER_IMG'] = ip

    # Write the updated data back to the file, preserving formatting
    with open(www_path, 'w', encoding='utf-8') as file:
        file.write(''.join(lines).replace(content, json.dumps(data, indent=4)))

'''
if __name__ == "__main__":
    ip = "127.0.0.1"
    master_ip_www(ip)
'''