#!/bin/python3

import http.client
import json
from xmlrpc.client import DateTime
from datetime import datetime


class CC:

    def __init__(self):
        self.api_url = "api.commerce.coinbase.com"
        self.error = {"error": False, "msg": None}
        self.data = None
        self.conn = None
        self.payload = {
          "local_price": {
            "amount": "0.00",
            "currency": "gbp"
          },
          "pricing_type": "fixed_price"
        }
        self.headers = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          'X-CC-Api-Key': '46b59134-616f-46d0-8189-4d34c0f902ef',
          'X-CC-Version': '2018-03-22'
        }

    def raiseError(self, msg=None):
        self.error["error"] = True
        self.error["msg"] = msg

    def resetError(self):
        self.error["error"] = False
        self.error["msg"] = None

    def hasError(self):
        return self.error["error"]

    def getErrorMsg(self):
        if self.hasError():
            return self.error["msg"]
        else:
            return "No Error"

    def apiKey(self, apiKey=""):
        self.headers["X-CC-APi-Key"] = apiKey

    def priceType(self, type):
        if type != "fixed_price" and type != "no_price":
            type = "fixed_price"

        self.payload["pricing_type"] = type

    def local_price(self, amount="0.00", currency="gbp"):
        self.payload["local_price"]["amount"] = amount
        self.payload["local_price"]["currency"] = currency

    def create(self):
        try:
            self.conn = http.client.HTTPSConnection("api.commerce.coinbase.com")
            self.conn.request("POST", "/charges", json.dumps(self.payload), self.headers)
            res = self.conn.getresponse()
            self.data = res.read()
        except Exception as e:
            self.raiseError(str(e))

    def all(self):
        try:
            self.conn = http.client.HTTPSConnection(self.api_url)
            self.conn.request("GET", "/charges", None, self.headers)
            res = self.conn.getresponse()
            self.data = res.read()
        except Exception as e:
            self.raiseError(str(e))

    def getCharge(self, chargeID=None):
        try:
            self.conn = http.client.HTTPSConnection(self.api_url)
            self.conn.request("GET", "/charges/"+chargeID, None, self.headers)
            res = self.conn.getresponse()
            self.data = res.read()
        except Exception as e:
            self.raiseError(str(e))

    def cancel(self, chargeID=None):
        try:
            self.conn = http.client.HTTPSConnection("api.commerce.coinbase.com")
            self.conn.request("POST", "/charges/"+chargeID+"/cancel", None, self.headers)
            res = self.conn.getresponse()
            self.data = res.read()
        except Exception as e:
            self.raiseError(str(e))

    def getResponse(self):
        return self.data.decode('utf-8')

    def printResponse(self):
        print(self.data.decode("utf-8"))

class CCsim:

    def __init__(self):
        self.mock = {
            "attempt_number": 1,
            "event": {
            "api_version": "2018-03-22",
            "created_at": "2023-08-30T19:29:20Z",
            "data": {
            "id": "2aee9dd1-67b8-43ef-8dfe-977959850f27",
            "code": "XA6G6ZFR",
            "pricing": {
            "local": {
              "amount": "1.00",
              "currency": "USD"
            },
            "settlement": {
              "amount": "1",
              "currency": "USDC"
            }
            },
            "metadata": {
            "name": "Bobby Axlerod",
            "email": "bobby@axecapital.com"
            },
            "timeline": [
            {
              "time": "2023-08-30T18:55:51Z",
              "status": "NEW"
            },
            {
              "time": "2023-08-30T19:24:27Z",
              "status": "SIGNED"
            },
            {
              "time": "2023-08-30T19:24:45Z",
              "status": "PENDING"
            },
            {
              "time": "2023-08-30T19:29:20Z",
              "status": "COMPLETED"
            }
            ],
            "redirects": {
            "cancel_url": "",
            "success_url": "",
            "will_redirect_after_success": False
            },
            "web3_data": {
            "failure_events": [],
            "success_events": [
              {
                "sender": "0xb6d00d83158fee6695c72ff9c5e915478a479224",
                "tx_hsh": "0xc0a731f82af615d7a5f6ba691ba07e083d5403d812adaa8659ed5892c9d3320d",
                "finalized": False,
                "recipient": "0x293a08a589f44a6188d65e92fbcd2a27e93d49e3",
                "timestamp": "2023-08-30T19:24:37Z",
                "network_fee_paid": "17215600576946625",
                "input_token_amount": "1000000",
                "input_token_address": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
              },
              {
                "sender": "0xb6d00d83158fee6695c72ff9c5e915478a479224",
                "tx_hsh": "0xc0a731f82af615d7a5f6ba691ba07e083d5403d812adaa8659ed5892c9d3320d",
                "finalized": True,
                "recipient": "0x293a08a589f44a6188d65e92fbcd2a27e93d49e3",
                "timestamp": "2023-08-30T19:24:37Z",
                "network_fee_paid": "17215600576946625",
                "input_token_amount": "1000000",
                "input_token_address": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
              }
            ],
            "transfer_intent": {
              "metadata": {
                "sender": "0xB6d00D83158feE6695C72ff9c5E915478A479224",
                "chain_id": 137,
                "contract_address": "0xeF0D482Daa16fa86776Bc582Aff3dFce8d9b8396"
              },
              "call_data": {
                "id": "0x58e8e1e895274125a3dcc7e398daa6c0",
                "prefix": "0x4b3220496e666f726d6174696f6e616c204d6573736167653a20333220",
                "deadline": "2023-09-01T18:55:51Z",
                "operator": "0x8fccc78dae0a8f93b0fe6799de888d4c57e273db",
                "recipient": "0x293a08a589f44a6188d65e92fbcd2a27e93d49e3",
                "signature": "0xc9b4b26d20ef9e953d145214a335e61495e9d4a559329885952a1b98c72611601e4deb30556b457bdcc1c66ce93976bed9b261447ce7eb770fce70f5216b3a481b",
                "fee_amount": "10000",
                "recipient_amount": "990000",
                "recipient_currency": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
                "refund_destination": "0xB6d00D83158feE6695C72ff9c5E915478A479225"
              }
            },
            "contract_addresses": {
              "1": "0x71b3ba7607abd0cd35eb398c2a38313f10aa3fdb",
              "137": "0xeF0D482Daa16fa86776Bc582Aff3dFce8d9b8396"
            }
            },
            "created_at": "2023-08-30T18:55:51Z",
            "expires_at": "2023-09-01T18:55:51Z",
            "hosted_url": "https://commerce.coinbase.com/pay/2aee9dd1-67b8-43ef-8dfe-977959850f27",
            "brand_color": "#000000",
            "charge_kind": "WEB3",
            "confirmed_at": "2023-08-30T19:29:20Z",
            "pricing_type": "fixed_price",
            "support_email": "",
            "brand_logo_url": "https://res.cloudinary.com/commerce/image/upload/v1653516296/dlwoolpero6qgsffxmpz.jpg",
            "organization_name": "Fine Art"
            },
            "id": "053b96aa-868f-4d8f-8ac6-6b96644da340",
            "resource": "event",
            "type": "charge:confirmed"
            },
            "id": "5306c113-7ece-4b8b-9452-49abf442bbe4",
            "scheduled_for": "2023-08-30T19:29:20Z"
        }
        self.packet = None
        self.payment = {
            'status': ['NEW','SIGNED','PENDING','COMPLETE','FAILED'],
            "contract_addresses": {
                "1": "0x71b3ba7607abd0cd35eb398c2a38313f10aa3fdb",
                "137": "0xeF0D482Daa16fa86776Bc582Aff3dFce8d9b8396"
            }

        }


    def getMockPacket(self, ret = False):
        self.packet = self.mock
        if ret:
            return self.packet

    def addMetadata(self, key="", value=""):
        if key not in self.packet['event']['metadata']:
            self.packet['event']['metadata'][key] = value

    def id(self, id=""):
        self.packet['event']['data']['id'] = id

    def code(self, code=""):
        self.packet['event']['data']['code'] = code

    def createdAt(self, created_at=None):
        self.packet['event']['data']['created_at'] = created_at

    def expiresAt(self, expires_at=None):
        self.packet['event']['data']['expires_at'] = expires_at;

    def hosted_url(self, hosted_url=None):
        self.packet['event']['data']['hosted_url'] = hosted_url

    def organization_name(self, organization_name="None"):
        self.packet['event']['data']['organization_name'] = organization_name

    def priceLocal(self, amount="0.00", currency="gbp"):
        self.packet['event']['data']['pricing']['local']['amount'] = amount
        self.packet['event']['data']['pricing']['local']['currency'] = currency

    def priceSettlement(self, amount="0.00", currency="gbp"):
        self.packet['event']['data']['pricing']['settlement']['amount'] = amount
        self.packet['event']['data']['pricing']['settlement']['currency'] = currency

    def pricingtType(self, pricing_type="fixed_price"):
        self.packet['event']['data']['pricing_type'] = pricing_type

    def createCharge(self, Timeline=True):
        self.packet['event']['type'] = "charge:created"
        if Timeline:
            now = datetime.now()
            self.addTimeline("NEW", now.strftime("%m/%d/%YTZ%H:%M:%S"))

    def signedCharge(self):
        self.packet['event']['type'] = 'charge:signed'
        now = datetime.now()
        self.addTimeline("SIGNED", now.strftime("%m/%d/%YTZ%H:%M:%S"))

    def pendingCharge(self):
        self.packet["event"]["type"] = "charge:pending"
        now = datetime.now()
        self.addTimeline("PENDING", now.strftime("%m/%d/%YTZ%H:%M:%S"))

    def confirmedCharge(self):
        self.packet['event']['type'] = "charge:confirmed"
        now = datetime.now()
        self.addTimeline("COMPLETE", now.strftime("%m/%d/%YTZ%H:%M:%S"))

    def failedCharge(self):
        self.packet['event']['type'] = "charge:failed"
        now = datetime.now()
        self.addTimeline("FAILED", now.strftime("%m/%d/%YTZ%H:%M:%S"))

    def replaceMetadata(self, metadata):
        self.packet['event']['data']['metadata'] = metadata

    def replaceTimeline(self, timeline={}):
        self.packet['event']['data']['timeline'] = timeline

    def addTimeline(self, status="NEW", timestamp=None):

        if status not in self.payment['status']:
            status = "NEW"

        if timestamp is None:
            timestamp = datetime.now()

        self.packet['event']['data']['timeline'].append({'status': status, 'time': timestamp})

    def removeTimeline(self, index=0):
        removed = False
        timeline_count = len(self.packet['event']['timeline'])

        if index >= 0 and index < timeline_count:
            del self.packet['event']['data']['timeline'][index]
            removed = True
        return removed

    def sender(self, address=None):
        updated = False
        if address:
            self.packet['event']['data']['web3_data']['transfer_intent']['metadata']['sender'] = address
            updated = True
        return updated

    def senderWithChain(self, address=None, chain=137):
        updated = False
        chain = str(chain)
        if address and str(chain) in self.payment['contract_addresses']:
            self.packet['event']['data']['web3_data']['transfer_intent']['metadata']['sender'] = address
            self.packet['event']['data']['web3_data']['transfer_intent']['metadata']['chain_id'] = chain
            self.packet['event']['data']['web3_data']['transfer_intent']['metadata']['contract_address'] = self.payment['contract_address'][chain]
            updated = True
        return updated

    def replaceEventSuccess(self, success):
        self.packet['event']['data']['web3_data']['success_events'] = success

    def addEventSuccess(self, event=None):

        if event is None:
            event = {
                "sender": "0xb6d00d83158fee6695c72ff9c5e915478a479224",
                "tx_hsh": "0xc0a731f82af615d7a5f6ba691ba07e083d5403d812adaa8659ed5892c9d3320d",
                "finalized": False,
                "recipient": "0x293a08a589f44a6188d65e92fbcd2a27e93d49e3",
                "timestamp": DateTime(),
                "network_fee_paid": "17215600576946625",
                "input_token_amount": "1000000",
                "input_token_address": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
              },

        self.packet['event']['data']['web3_data']['success_events'].append(event)

    def replaceEventFailure(self, failure={}):
        self.packet['event']['data']['web3_data']['failure_events'] = failure

    def addEventFailure(self, event=None):
        if event is None:
            event = {
                "sender": "0xb6d00d83158fee6695c72ff9c5e915478a479224",
                "tx_hsh": "0xc0a731f82af615d7a5f6ba691ba07e083d5403d812adaa8659ed5892c9d3320d",
                "finalized": False,
                "recipient": "0x293a08a589f44a6188d65e92fbcd2a27e93d49e3",
                "timestamp": DateTime(),
                "network_fee_paid": "17215600576946625",
                "input_token_amount": "1000000",
                "input_token_address": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
              },

        self.packet['event']['data']['web3_data']['failure_events'].append(event)

    def replaceTransferIntent(self, transferIntent={}):
        self.packet['event']['data']['web3_data']['transfer_intent'] = transferIntent

    def createTransferIntentMetadata(self):
        metadata = {
                        "sender": "0xB6d00D83158feE6695C72ff9c5E915478A479224",
                        "chain_id": 137,
                        "contract_address": "0xeF0D482Daa16fa86776Bc582Aff3dFce8d9b8396"
                      }
        self.packet['event']['data']['web3_data']['transfer_intent']['metadata'] = metadata

    def createTransferIntentCallData(self):
        call_data = {
                        "id": "0x58e8e1e895274125a3dcc7e398daa6c0",
                        "prefix": "0x4b3220496e666f726d6174696f6e616c204d6573736167653a20333220",
                        "deadline": "2023-09-01T18:55:51Z",
                        "operator": "0x8fccc78dae0a8f93b0fe6799de888d4c57e273db",
                        "recipient": "0x293a08a589f44a6188d65e92fbcd2a27e93d49e3",
                        "signature": "0xc9b4b26d20ef9e953d145214a335e61495e9d4a559329885952a1b98c72611601e4deb30556b457bdcc1c66ce93976bed9b261447ce7eb770fce70f5216b3a481b",
                        "fee_amount": "10000",
                        "recipient_amount": "990000",
                        "recipient_currency": "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
                        "refund_destination": "0xB6d00D83158feE6695C72ff9c5E915478A479225"
                      }
        self.packet['event']['data']['web3_data']['transfer_intent']['call_data'] = call_data

    def eventData(self, data={}, ret=False):

        if 'created_at' in data:
            self.createdAt(data['created_at'])

        if 'expires_at' in data:
            self.expiresAt(data['expires_at'])

        if 'hosted_url' in data:
            self.hosted_url(data['hosted_url'])

        if 'organization_name' in data:
            self.organization_name(data['organization_name'])

        if 'id' in data:
            self.id(data['id'])

        if 'code' in data:
            self.code(data['code'])

        if 'pricing' in data:
            if 'local' in data['pricing']:
                if 'amount' in data['pricing']['local'] and 'currency' in data['pricing']['local']:
                    self.priceLocal(data['pricing']['local']['amount'], data['pricing']['local']['currency'])

        if 'pricing' in data:
            if 'settlement' in data['pricing']:
                if 'amount' in data['pricing']['settlement'] and 'currency' in data['pricing']['settlement']:
                    self.priceSettlement(data['pricing']['settlement']['amount'], data['pricing']['settlement']['currency'])

        if 'price_type' in data:
            self.pricingType(data['price_type'])

        if 'metadata' in data:
            self.replaceMetadata(data['metadata'])

        if 'timeline' in data:
            self.replaceTimeline(data['timeline'])

        if ret:
            return self.packet['event']['data']

    def getEvent(self):
        return self.packet

