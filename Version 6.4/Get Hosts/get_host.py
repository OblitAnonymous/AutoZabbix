## --- MODULE IMPORTS --- ##
from pyzabbix import ZabbixAPI, ZabbixAPIException

## --- DEFINING THE SERVER CREDENTIALS --- ##
zabbix_server = '<Zabbix Server URL>'
zabbix_user = '<User Username>'
zabbix_password = '<User Password'

zapi = ZabbixAPI(zabbix_server)
zapi.login(user=zabbix_user, password=zabbix_password)  

## --- FUNCTION: SEARCH FOR THE SPECEFIED HOSTNAME --- ##
def get_host(hostname):
    host = zapi.host.get(filter={
                                'host': hostname
                                 },
                                 output='extend')
    ## --- ERROR HANDLING: CHECKING IF THE HOST EXISTS OR NOT --- ##
    if not host:
        print(f'[-] No host was found with the name {hostname}')
    else:
        print(f'[+] Host was found with the name {hostname}' +  host[0]['hostid']) #==> Print host and host ID

print('[+] Connected to Zabbix API Version %s' % zapi.api_version())


host_name = input('[!] Host Name to Searchg for:') #==>DEFINE THE HOST TO SEARCH FOR

## --- FUNCTION CALL: FIND THE SPECIFIED HOST --- ##
get_host(host_name)
