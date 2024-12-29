#!/bin/python3
import hashlib
import hmac
import http.server
import socketserver
from urllib.parse import urlparse
import json
from testChargeApi import CC as Coinbase

PORT = 9001


class handler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):

        self.webhook_signature = self.headers['X-CC-WEBHOOK-SIGNATURE']
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        data = json.loads(self.data_string)
        x_cc_webhook_signature = hmac.new(bytes(self.cc_webhook_shared_secret , 'latin-1'), msg = bytes(data , 'latin-1'), digestmod = hashlib.sha256).hexdigest()
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        print("Content-Length: "+str(int(self.headers['Content-Length'])))
        print(data, True)



with socketserver.TCPServer(("", PORT), handler) as httpd:
    print("serving on port", PORT)
    httpd.serve_forever()