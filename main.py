# A simple FTP server to host character sheets for
# Throwin_Ds: RPG Assistant -  https://github.com/Branch321/Throwing_Ds
# So simple there is no need for comments
# Need to have a frozen version of main from Throwing D's stored in a zip file named "current_version.zip"

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


authorizer = DummyAuthorizer()
# The msg_login variable needs to be updated with the version number
authorizer.add_anonymous(".", msg_login="1.0")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("127.0.0.1", 1026), handler)
server.serve_forever()

