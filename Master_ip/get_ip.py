import subprocess
import re

def get_ipconfig_ip():
    try:
        result = subprocess.run(['ipconfig'], stdout=subprocess.PIPE, text=True)
        # Extract IPv4 addresses using a regular expression
        ip_addresses = re.findall(r"IPv4 Address[^\:]*: (\d+\.\d+\.\d+\.\d+)", result.stdout)
        # Return the first IPv4 address found, or a default message if none are found
        return ip_addresses[0] if ip_addresses else "No IPv4 address found"
    except Exception as e:
        return f"Error: {e}"

'''
if __name__ == "__main__":
    ip_address = get_ipconfig_ip()
    print(f"IP Address from ipconfig: {ip_address}")
'''