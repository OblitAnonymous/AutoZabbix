from pyzabbix import ZabbixAPI
import csv

## -- CREATE THE ZABBIX API OBJECT --- ##
zabbix_url = '<Zabbix-Server-URL>'  
zabbix_user = '<Zabbix-User-Username'  
zabbix_password = 'zabbix-User-Password' 
zapi = ZabbixAPI(zabbix_url)
zapi.login(zabbix_user, zabbix_password)

## --- FUNCTION: CREATE HOSTS --- ##
## -- HOST PARAMETERS
interface_port = '10050'
interface_type = 1
inventory_mode = 1  # 0 for disabled, 1 for manual, 2 for automatic
group_id = '22'
template_id = 10564

def create_host():
    ## --- API CALL TO CREATE THE HOST WITH ASSOCIATED VALUES --- ##
    host = zapi.host.create(
        ## ==> DEFINE THE HOST NAME
        host=host_name,
    
        ## ==> DEFINE INTERFACES, TYPES AND PORTS
        interfaces=[
            {
                'type': interface_type,
                'main': 1,
                'useip': 1,
                'ip': interface_ip,
                'dns': '',
                'port': interface_port,
            }
        ],
        ## ==> DEFINE GROUP
        groups=[
            {
                'groupid': group_id
            }
        ],
        ## ==> DEFINE TEMPLATES
        templates=[
            {
                'templateid': template_id
            }
        ],
        ## ==> DEFINE INVENTORY
        inventory_mode=inventory_mode,
        inventory={
                'location': 'South Africa',
                'location_lat': gps_lat,
                'location_long': gps_long,
                'contact':'<Contact Person Details>'
            }
    )

    print('[+] Host ' , host_name, ' created with ID:', host['hostids'])

## ==> PRINT CONNECTION CONFIRMATION
print('[+] Connected to Zabbix API Version %s' % zapi.api_version())


## --- DEFINE THE CSV --- ##
with open('Add Host/test.csv', 'r') as hosts_file:
    ## --- READ FROM CSV FILE --- ##
    csv_reader = csv.reader(hosts_file, delimiter=';')

    print('[+] File Name:', hosts_file.name)


    for row in csv_reader:
        host_name, interface_ip, gps_long, gps_lat = row

        ## --- FUNCTION CALL: CREATE HOSTS WITHIN CSV FILE --- ##
        create_host()        

    

