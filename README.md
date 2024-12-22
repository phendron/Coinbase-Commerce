# Coinbase Commerce API TestSuite

**Description**
This test suite is designed to fake the Charge API service webhook responses from Coinbase.

## Getting Started

```
main.py host=localhost port=8001 protocol=http webhook_host=localhost webhook_port=9001 transaction=TRANSACTION
```
The above command outlines the default arguments and parameters for the **main.py** script it is the same as
executing the script without any arguments.

### Main Server
**These arguments act as replacement for the api.commerce.coinbase.com url**

* **host** - The webserver host address

* **port** - The webserver host port

* **protocol** - The webserver host protocol

### Webhook 

* **webhook_host** - Specifies the address that webhooks are received [you domain]/[webhook pathway]
* **webhook_port** - Specifies the port that webhooks are received [you domain]:[webhook port]/[webhook_pathway]


### Transaction
The following options are all valid for the ```transaction``` argument
* **TRANSACTION** - Simulates a full successfull charge event (NEW, SIGNED, PENDING, COMPLETE)
* **NEW** - Simulates a new successfull charge creation event
* **SIGNED** - SImulates a successfull charge signing event
* **PENDING** - Simulates a successfull charge pending event
* **COMPLETE** - Simulates a sucessfull chare complete event

```
server.py
```
The above scripts is the default server that acts as an endpoint defined for webhook calls this script is designed to be exe-cute-ied
along with the main.py scrripts default webhook parameters

```
requestTest.py
```
The above file performs a variety of test api calls this script can be modified to best fit your individual needs.

