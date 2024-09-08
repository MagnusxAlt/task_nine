#!/usr/bin/env python3

import http.server
import socketserver
import os

# Define the port to listen on
PORT = 8000

# Define the directory to serve files from
DIRECTORY = "."

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Serve files from the specified directory
        path = super().translate_path(path)
        return os.path.join(DIRECTORY, path)

def run(server_class=http.server.HTTPServer, handler_class=CustomHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {PORT}...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
