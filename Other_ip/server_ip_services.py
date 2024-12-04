from lxml import etree

def server_ip_services(main_ip_address):

    service_file_path = r"C:\uServePro\Server\uServeService.exe.config"
    # 如果用户输入了新的值，进行替换
    if main_ip_address:
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(service_file_path, parser)
        root = tree.getroot()

        # Find and update the server_address and client_address values
        for add_element in root.xpath("//add[@key='server_address']"):
            add_element.attrib['value'] = main_ip_address  # Replace with the new IP

        for add_element in root.xpath("//add[@key='master']"):
            add_element.attrib['value'] = "false" 

        # Save the modified XML file back with the updated values
        tree.write(service_file_path, encoding="utf-8", xml_declaration=True, pretty_print=True)


'''
if __name__ == "__main__":
    ip = "127.0.0.3"
    server_ip_services(ip)
'''