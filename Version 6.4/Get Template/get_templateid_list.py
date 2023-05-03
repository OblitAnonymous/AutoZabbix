from pyzabbix import ZabbixAPI, ZabbixAPIException
import csv

## -- CREATE THE ZABBIX API OBJECT --- ##
zabbix_url = '<ZABBIX SERVER URL>'  
zabbix_user = '<ZABBIX USER>'  
zabbix_password = '<ZABBIX USER PASSWORD>' 
zapi = ZabbixAPI(zabbix_url)
zapi.login(zabbix_user, zabbix_password)

## --- FUNCTION: GET TEMPLATE --- ##
templates = zapi.template.get(output = ['name','templateid'])

## ==> PRINT CONNECTION CONFIRMATION
print('[+] Connected to Zabbix API Version %s' % zapi.api_version())

## --- MAIN --- ##
if __name__ == '__main__':
    with open('template_list.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Template Name', 'Template ID'])

        for template in templates:
            writer.writerow([template['name'], template['templateid']])

    print('[+] Successfully write template names and IDs to CSV file.')
