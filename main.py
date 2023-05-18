# For implementing the HTTP Web servers
import http.server

# provides access to the BSD socket interface
import socket

# a framework for network servers
import socketserver

# to display a web-based documents to users
import webbrowser

# to generate qrcode
import pyqrcode
from pyqrcode import QRCode

# convert into png format
import png

# to access operating system control
import os

# assigning the appropriate port value
PORT = 8010
# gives the name of the computer user
os.getlogin()

# changing the directory to access the files desktop with the help of os module
home_dir = os.path.expanduser("~")
desktop_dir = os.path.join(home_dir, "Documents")
os.chdir(desktop_dir)

# creating a http request
Handler = http.server.SimpleHTTPRequestHandler
#returns, host name of the system under which python interpreter is executed
hostname = socket.gethostname()

# finding the IP address of the PC
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
IP = "http://" + s.getsockname()[0] + ":" + str(PORT)
link = IP

# convert IP into a qrcode
url = pyqrcode.create(link)
url.svg("myqr.svg", scale=8)
webbrowser.open('myqr.svg')


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    print("Type this in your Browser", IP)
    print("or Use the ORCode")
    httpd.serve_forever()



