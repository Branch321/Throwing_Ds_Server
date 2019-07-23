# A simple FTP server to host character sheets for
# Throwin_Ds: RPG Assistant -  https://github.com/Branch321/Throwing_Ds
# So simple there is no need for comments

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


authorizer = DummyAuthorizer()
authorizer.add_anonymous("characters/")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()

