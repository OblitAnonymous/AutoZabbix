# 1. Project Description:

### Motivation for this Project:

The main motivation for this project derives from the fact that after setting up an initial zabbix server, it is then extremely time consuming to create, edit and manage hosts as laid out in the normal user interface.

By using the built-in Zabbix API, and some smart python coding, this extremely time consuming task of adding hudereds or even thousands of hosts becomes a function and a tool that will execute perfectly every time within minutes.

### Why I decided to use the API:

I decided to use the API for zabbix after creating multiple zabbix servers, and then manually adding thousands of hosts by hand for each of these servers, which became a time consuming task, and interrupted my other work and workflows.

### Why use these tools?
These tools are easy to use and understand, and are written in Python, which is an extremely simple programming language.

Paired with these tools and the provided Zabbix API documentation, you can use them as templates to edit and or create your own scripts to run.


# 3. Installation:
### Python Installation:
* You should install the __pyzabbix__ library.
```
pip install pyzabbix
```

### Zabbix Server Configuration:
To stay in line with a secure zabbix server configuration, you should consider doing the following:

* Create a Zabbix User account, which has access to the API.
* Use this Zabbix user's credentials within the scripts in order to execute them.
* Remove the user account from the server after you are done with the scripts.

# 4. How to use the project:
* Change the __ZABBIX SERVER URL__ within the code to your own Zabbix Server URL.
* Change the __ZABBIX ZERVER USER__ & __ZABBIX USER PASSWORD__ to the username and password you created earlier for the Zabbix API user.

# 5. Credits
```
Zabbix API Documentation
Zabbix API Automation with the various Zabbix versions
```
