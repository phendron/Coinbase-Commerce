#!/bin/python3
import hashlib
import hmac
import sys
import http.server
import http.client
import random
import socketserver
import threading
import time
from urllib.parse import urlparse
import json
from testChargeApi import CC as Coinbase
from testChargeApi import CCsim as CoinbaseWebhook

PORT = 8002


class handler(http.server.BaseHTTPRequestHandler):

    def __init__(self, host="localhost", port=443, relay_type="TRANSACTION", api_key=None, shared_secret=None):
        self.relay_type = relay_type
        self.webhook_host = host
        self.webhook_port = port
        self.webhook_url = self.webhook_host+":"+str(self.webhook_port)
        self.cc_api_key = api_key
        self.cc_webhook_shared_secret = shared_secret

        # super().__init__() must be called at the end
        # because it's immediately calling handle method
        #super().__init__(request, client_address, server)

    def __call__(self, *args, **kwargs):
        """Handle a request."""
        super().__init__(*args, **kwargs)

    def do_GET(self):

        #self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        #data = json.loads(self.data_string)
        path = self.path.split("/")
        if path[1] == "charges":
            Cb = Coinbase()
            Cb.apiKey(self.cc_api_key)
            if len(path) > 2:
                Cb.getCharge(path[2])
            else:
                Cb.all()

            if (Cb.hasError()):
                self.wfile.write(bytes("Error:", "utf8"))
                self.wfile.write(bytes(Cb.getErrorMsg(), "utf8"))
            else:
                data = Cb.getResponse()
                data_len = len(data)
                self.wfile.write(bytes("length: "+str(data_len), "utf8"))
                self.wfile.write(bytes(Cb.getResponse(), "utf8"))

    def do_POST(self):

        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        data = json.loads(self.data_string)

        if self.path == "/charges":
            Cb = Coinbase()
            Cb.apiKey(self.cc_api_key)
            if "local_price" in data:
                if "amount" in data["local_price"] and "currency" in data["local_price"]:
                    Cb.local_price(data["local_price"]["amount"], data["local_price"]["currency"])
            if "pricing_type" in data:
                Cb.priceType(data["pricing_type"])
            Cb.create()
            if(Cb.hasError()):
                self.wfile.write(bytes(Cb.getErrorMsg(), "utf8"))
            else:
                response = Cb.getResponse()
                self.wfile.write(bytes(response, "utf8"))
                self.relay(json.loads(response))
        else:

            Cb = Coinbase()
            Cb.apiKey(self.cc_api_key)
            path = self.path.split("/")

            if path[1] == "charges" and path[3] == "cancel":
                Cb.cancel(path[2])

                if (Cb.hasError()):
                    self.wfile.write(Cb.getErrorMsg())
                else:
                    data = Cb.getResponse()
                    self.wfile.write(bytes(data, "utf8"))
                    self.relay(json.loads(data))

    def relay(self, data=None):

        if self.relay_type == "TRANSACTION":
            callback = self.transaction
        elif self.relay_type == "NEW":
            callback = self.new
        elif self.relay_type == "SIGNED":
            callback = self.signed
        elif self.relay_type == "PENDING":
            callback = self.pending
        elif self.relay_type == "COMPLETE":
            callback = self.complete
        elif self.relay_type == "FAILED":
            callback = self.failed
        else:
            callback = self.transaction
            self.relay_type = "TRANSACTION"

        sthread = threading.Thread(target = callback, args=(data,))
        sthread.start()

    def randomSecond(self):
        return random.randint(0, 60)

    def new(self, data):
        CbW = CoinbaseWebhook()
        CbW.getMockPacket()
        CbW.eventData(data['data'])
        CbW.createCharge(False)
        self.webhook(1, CbW.getEvent())

    def signed(self, data):
        CbW = CoinbaseWebhook()
        CbW.getMockPacket()
        CbW.eventData(data['data'])
        CbW.signedCharge()
        self.webhook(1, CbW.getEvent())

    def pending(self, data):
        CbW = CoinbaseWebhook()
        CbW.getMockPacket()
        CbW.eventData(data['data'])
        CbW.pendingCharge()
        self.webhook(1, CbW.getEvent())

    def complete(self, data):
        CbW = CoinbaseWebhook()
        CbW.getMockPacket()
        CbW.eventData(data['data'])
        CbW.confirmedCharge()
        self.webhook(1, CbW.getEvent())

    def failed(self, data):
        CbW = CoinbaseWebhook()
        CbW.getMockPacket()
        CbW.eventData(data['data'])
        CbW.failedCharge()
        self.webhook(1, CbW.getEvent())

    def transaction(self, data):
        self.new(data)
        self.signed(data)
        self.pending(data)
        self.complete(data)

    def webhook(self, delay=1, data={}):
        time.sleep(delay)

        self.conn = http.client.HTTPConnection(self.webhook_url)
        self.headers = {"Connection": "Keep-Alive"}
        data_response = json.dumps(data)

        x_cc_webhook_signature = hmac.new(bytes(self.cc_webhook_shared_secret , 'latin-1'), msg = bytes(data_response , 'latin-1'), digestmod = hashlib.sha256).hexdigest()
        self.headers['X-CC-WEBHOOK-SIGNATURE'] = x_cc_webhook_signature
        print("sending data relay:("+self.relay_type+")")
        self.conn.request("POST", "/", data_response, self.headers)
        res = self.conn.getresponse()


def compileArgs():

    args = {"host": "localhost", "port": 8002, "protocol":"http", "webhook_host":"localhost", "webhook_port":9001, "transaction":"transaction", "api_key":"e72a4f87-f039-4aa6-ae3d-05b3487b0fcb", "webhook_shared_secret":"e72a4f87-f039-4aa6-ae3d-05b3487b0fcb"}

    for i in range(0, len(sys.argv)):
        arg = sys.argv[i]
        arg_kv = arg.split("=")
        if len(arg_kv) > 1:
            key = arg_kv[0]
            value = arg_kv[1]
            if key in args:
                args[key] = value

    return args

cli_args = compileArgs()
server_handler = handler(cli_args['webhook_host'], cli_args['webhook_port'], cli_args['transaction'], cli_args['api_key'], cli_args['webhook_shared_secret'])
with socketserver.TCPServer((cli_args['host'], cli_args['port']), server_handler) as httpd:
    print("serving on port", cli_args['host']+":"+str(cli_args['port']))
    print("webhook url: ", cli_args['webhook_host']+":"+str(cli_args['webhook_port']))
    httpd.serve_forever()