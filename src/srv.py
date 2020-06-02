import os
import socketserver
from http.server import SimpleHTTPRequestHandler as MyHandler

PORT = os.getenv("PORT", 8000)
print(f"PORT = {PORT}")

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("it works")
    httpd.serve_forever()

