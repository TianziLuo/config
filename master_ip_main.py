from Master_ip.master_ip_app import master_ip_app
from Master_ip.master_ip_services import master_ip_services
from Master_ip.master_ip_www import master_ip_www

def master_ip_main(ip):
    master_ip_services(ip)
    master_ip_www(ip)
    master_ip_app(ip)

'''
if __name__ == "__main__":
    master_ip_main()
'''
