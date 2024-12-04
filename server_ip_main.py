from Other_ip.server_ip_services import server_ip_services
from Other_ip.server_ip_www import server_ip_www

def server_ip_main(main_ip_address):
    server_ip_services(main_ip_address)
    server_ip_www(main_ip_address)

'''
if __name__ == "__main__":
    ip = "127.0.0.1"
    server_ip_main(ip)
''' 