from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8080

handler = SimpleHTTPRequestHandler

with HTTPServer(("", PORT), handler) as server:
    print("Servidor corriendo en puerto", PORT)
    server.serve_forever()