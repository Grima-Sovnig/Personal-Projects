##This is an external part of the program. This file will control the network server that the rest of the program will reach out to.
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
hostName = "localhost"
serverport 8080