#!/bin/python

import os
import sys
import math
import string
import json
from urllib import request, parse
import random

class requestTest:

    def __init__(self):
        self.proto = "http"
        self.addr = "127.0.0.1"
        self.port = "8002"
        self.route = "charges"

        self.url = self.proto+"://"+self.addr+":"+self.port+"/"+self.route


    def create(self):
        print("start::create()")
        data = {
                  "local_price": {
                    "amount": "4.70",
                    "currency": "gbp"
                  },
                  "pricing_type": "fixed_price"
                }

        data = json.dumps(data)

        data = str(data)

        data = data.encode('utf-8')

        print(self.url)
        r = request.Request(self.url, data=data)

        rsp = request.urlopen(r)

        data_str = rsp.read()

        if len(data_str) == 0:
            print("no response or something")
            return
        data_rsp = json.loads(data_str)
        data = data_rsp["data"]

        print("ID: "+data['id'])
        print("Created: "+data['created_at'])
        print("Expires: "+data['expires_at'])
        print("Organization: "+data['organization_name'])
        print("Price: "+data['pricing']['local']['amount']+" "+data['pricing']['local']['currency'])
        print("Go to, to pay: "+data['hosted_url'])

        print(data)

    def all(self, output=False):
        print("start::all()")
        r = request.Request(self.url)
        rsp = request.urlopen(r)
        data_rsp = json.loads(rsp.read())

        if output:
            for n in range(0, len(data_rsp['data'])):
                charge = data_rsp['data'][n]
                self.printCharge(charge)
                print("_________________________________________________________")
        else:
            return data_rsp

    def getCharge(self, chargeID=None, output=False):
        r = request.Request(self.url+"/"+chargeID)
        rsp = request.urlopen(r)
        data_rsp = json.loads(rsp.read())

        if output:
            print(data_rsp)
        else:
            return data_rsp

    def randomCharge(self, charges=None):

        if "data" in charges:
            charges_count = len(charges['data'])
            charge = charges['data'][random.randint(0, charges_count)]
            self.printCharge(charge)
            print("------------------/r/n")

    def printCharge(self, charge):

        data = charge
        print("ID: " + data['id'])
        print("Created: " + data['created_at'])
        print("Expires: " + data['expires_at'])
        print("Organization: " + data['organization_name'])
        print("Price: " + data['pricing']['local']['amount'] + " " + data['pricing']['local']['currency'])
        print("--> Go to, to pay: " + data['hosted_url'])
        if "timeline" in charge:
            for i in range(0, len(charge['timeline'])):
                timeline = charge['timeline'][i]
                print(" - Status: " + timeline['status'])
                print(" -  - Event-At: " + timeline['time'])

    def cancel(self, chargeID=None, output=False):
        print("start::cancel()")
        canceled = False
        if self.isCanceled(chargeID)==False:
            r = request.Request(self.url + "/"+chargeID+"/cancel")
            rsp = request.urlopen(r, str(json.dumps({})).encode('utf-8'))
            data_rsp = json.loads(rsp.read())

            if "error" in data_rsp:
                if output:
                    print("Error: ["+data_rsp['error']['type']+"] "+data_rsp['error']['message'])
                return data_rsp
            elif self.isCanceled(None, data_rsp['data']):
                canceled = True
                if output:
                    print(data_rsp)
            return canceled

    def isCanceled(self, chargeID=None, charge=None):
        canceled = False
        if charge is None:
            charge = self.getCharge(chargeID)
        if "timeline" in charge:
            for i in range(0, len(charge['timeline'])):
                timeline = charge['timeline'][i]
                if timeline['status'] == "CANCELED":
                    canceled = True
                    break
        return canceled

    def testAll(self):
        self.create()
        #self.all()
        #self.cancel("c360f3c2-7683-4d8d-8eac-3bbcf69ea9a3")


rT = requestTest()
rT.testAll()

