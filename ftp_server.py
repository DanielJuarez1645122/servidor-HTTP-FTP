from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user(
    "user",
    "1234",
    r"C:\Users\Daniel Juarez\Documents\Universidad Daniel\2026\primer\Ingenieria De Software II\Servidor-ParcialRedesIII",
    perm="elradfmw"
)

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("0.0.0.0", 2121), handler)
print("FTP corriendo en puerto 2121")
server.serve_forever()