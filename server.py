import os
import http.server
import socketserver
import sys
from http import HTTPStatus


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        msg = 'Hello! you requested %s' % (self.path)
        self.wfile.write(msg.encode())


#open('logfile.txt', 'w').writelines('')        
        
port = int(os.getenv('PORT', 80))
print('Listening on port %s' % (port))
httpd = socketserver.TCPServer(('', port), Handler)

buffer = 1
sys.stderr = open('logfile.txt', 'a', buffer)

httpd.serve_forever()
