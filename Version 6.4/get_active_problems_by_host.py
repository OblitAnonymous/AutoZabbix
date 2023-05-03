from pyzabbix import ZabbixAPI, ZabbixAPIException
from datetime import datetime

zabbix_server = "<ZABBIX SERVER URL>"
zabbix_user = "ZABBIX USER"
zabbix_password = "ZABBIX USER PASSWORD"

zapi = ZabbixAPI(zabbix_server)
zapi.login(user=zabbix_user, password=zabbix_password)

def get_host(hostname):
    host = zapi.host.get(filter= {
                                'host': hostname  
                                    }, output='extend')

    if not host:
        print(f'[-]Not Found!')
        return
    else:
        get_host_host_id = host[0]['hostid']
        print(f'[+]Host was found with the name {hostname}')
        print(f'[+]hostid: {get_host_host_id}')
    
    return(get_host_host_id)

def get_problem(host_id):
    # Get the active problems for the host
    problems = zapi.problem.get(filter={"hostid": host_id, 
                                        "value": 1}, 
                                        selectAcknowledges="extend",
                                        output=["eventid", "severity", "name", "clock" ],
                                        sortfield="eventid",
                                        sortorder = 'DESC',
                                        limit=1)

    # Print the details of each problem
    for problem in problems:
        event_id = problem['eventid']
        severity = problem['severity']
        name = problem['name']
        

        print(f"[+] Event ID: {event_id}, Severity: {severity}, Name: {name}")

## ==> PRINT CONNECTION CONFIRMATION
print('[+] Connected to Zabbix API Version %s' % zapi.api_version())    

if __name__ == '__main__':
    host_input = input('[!] Host Name to Searchg for:')

    hostid = get_host(host_input)
    problemid = get_problem(hostid)

    print(hostid)
    print(problemid)
