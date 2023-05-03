# What this script does:

The provided script uses the Pyzabbix Python library to automate the process of creating new hosts on a Zabbix monitoring server. It reads the host information from a CSV file, which should contain columns as specified with the headers. 

The script creates new hosts on the Zabbix server based on the information provided in each row of the CSV file.

# Brief Overview of how the script works:

* 1.) The script begins by creating a connection to the Zabbix API using the credentials provided (URL, Username and Password).
* 2.) It then defines a function called "create_host" that takes no arguments and creates a new host on the Zabbix server using the information provided in the CSV file.
* 3.) The "create_host" function uses the PyZabbix API to make a call to the Zabbix server's API to create a new host with the specified values.
* 4.) The script then reads the CSV fiel line by line and extracts the values for each columns in the row.
* 5.) For each row in teh CSV file, the script calls the "create_host" function with the values extracted from the CSV file.
* 6.) Finally, the script prints a confirmation message indicating that it has successfully connected to the Zabbix API.

## Notes about the script:

* The script assuemes that the CSV file is located in a folder called "Add Host" in the same directory as the script.
> If the CSV file is located elsewhere, the file path in the __"with open"__ statement will need to be updated.

* The script assumes that the values in the __"Site Name"__ column of the CSV file will be used as the name of the new host.
> If the CSV file contains a different column that should be used as the host name, the script will need to be modified accordingly.

* The script also assumes that the Zabbix server is already set up with the necessary templates and groups to create new hosts.
> If these are not already set up, the script will need to be modified to add them.
