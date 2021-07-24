import json
import socket
import requests
from threading import Thread
from http.server import BaseHTTPRequestHandler, HTTPServer


class MockServerRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        #status code
        self.send_response(requests.codes.ok)

        #response header
        self.send_header('Content-Type', 'application/json;')
        self.end_headers()

        #content
        response_content = json.dumps(
            {
                "message": "this is from a mock server" 
            }
        )

        self.wfile.write(response_content.encode('utf-8'))
    
    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        #status code
        self.send_response(requests.codes.ok)

        #response header
        self.send_header('Content-Type', 'application/json;')
        self.end_headers()

        self.wfile.write(
            json.dumps({"message": "OK"}).encode("utf-8")
        )


def start_mock_server(port=8080):
    mock_server = HTTPServer(('localhost', port), MockServerRequestHandler)
    mock_server_thread = Thread(target=mock_server.serve_forever)
    mock_server_thread.setDaemon(True)
    mock_server_thread.start()
