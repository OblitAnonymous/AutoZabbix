from pyzabbix import ZabbixAPI, ZabbixAPIException

## -- CREATE THE ZABBIX API OBJECT --- ##
zabbix_url = '<ZABBIX SERVER URL>'  
zabbix_user = '<zABBIX USER>'  
zabbix_password = '<ZABBIX USER PASSWORD>' 
zapi = ZabbixAPI(zabbix_url)
zapi.login(zabbix_user, zabbix_password)

## ==> PRINT CONNECTION CONFIRMATION
print('[+] Connected to Zabbix API Version %s' % zapi.api_version())  

hostgroups = zapi.hostgroup.get(output=['name', 'groupid'])

# Print the list of host groups with their IDs
for hg in hostgroups:
    print("[+] Host Group: {0}, ID: {1}".format(hg['name'], hg['groupid']))
