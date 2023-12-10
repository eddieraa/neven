import http.server
import socketserver

port = 80
address = ("", port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = socketserver.TCPServer(address, handler)

print(f"Serveur démarré sur le PORT {port}")

httpd.serve_forever()