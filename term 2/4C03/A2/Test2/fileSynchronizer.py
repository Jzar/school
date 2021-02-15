#!/usr/bin/python3
#==============================================================================
#description     :This is a skeleton code for programming assignment 
#usage           :python Skeleton.py trackerIP trackerPort
#python_version  :3.5
#Authors         :Yongyong Wei, Rong Zheng
#==============================================================================

import socket, sys, threading, json,time,os,ssl
import os.path
import os
import glob
import json
import optparse
from math import floor

def validate_ip(s):
    """
    Validate the IP address of the correct format
    Arguments: 
    s -- dot decimal IP address in string
    Returns:
    True if valid; False otherwise
    """
    a = s.split('.')
    if len(a) != 4:
        return False
    for x in a:
        if not x.isdigit():
            return False
        i = int(x)
        if i < 0 or i > 255:
            return False
    return True

def validate_port(x):
    """Validate the port number is in range [0,2^16 -1 ]
    Arguments:
    x -- port number
    Returns:
    True if valid; False, otherwise
    """
    if not x.isdigit():
        return False
    i = int(x)
    if i < 0 or i > 65535:
            return False
    return True

def get_file_info():
    """ Get file info in the local directory (subdirectories are ignored) 
    Return: a JSON array of {'name':file,'mtime':mtime}
    i.e, [{'name':file,'mtime':mtime},{'name':file,'mtime':mtime},...]
    Hint: a. you can ignore subfolders, *.so, *.py, *.dll
          b. use os.path.getmtime to get mtime, and round down to integer
    """
    def dir_scan():
        """[summary]
        scans dir (assumed path to be ".", i.e. uses the path the script is invoked in)

        return: List of dicts containing file name, and mtime (last modified time in UNIX time)
        """
        files =  [
            {
                'name': entry.name,
                'mtime': floor(os.path.getmtime(entry.path))
            }
            for entry in os.scandir(".") if entry.is_file() #used os.scandir as it is does not recurse through child directories, per specifications
        ]
        return(files)

    return dir_scan()

def check_port_available(check_port):
    """Check if a port is available
    Arguments:
    check_port -- port number
    Returns:
    True if valid; False otherwise
    """
    if str(check_port) in os.popen("netstat -na").read():
        return False
    return True
	
def get_next_available_port(initial_port):
    """Get the next available port by searching from initial_port to 2^16 - 1
       Hint: You can call the check_port_avaliable() function
             Return the port if found an available port
             Otherwise consider next port number
    Arguments:
    initial_port -- the first port to check

    Return:
    port found to be available; False if no port is available.
    """
    for port in range(initial_port,(2**16-1)): 
        if check_port_available(port): 
            yield(port) # make it a generator to save memory



class FileSynchronizer(threading.Thread):
    def __init__(self, trackerhost,trackerport,port, host='0.0.0.0'):

        threading.Thread.__init__(self)
        #Port for serving file requests
        self.port = port
        self.host = host

        #Tracker IP/hostname and port
        self.trackerhost = trackerhost
        self.trackerport = trackerport

        self.BUFFER_SIZE = 8192

        #Create a TCP socket to communicate with the tracker
        self.client = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
        self.client.settimeout(180)

    
        #Store the message to be sent to the tracker. 
        #Initialize to the Init message that contains port number and file info.
        #Refer to Table 1 in Instructions.pdf for the format of the Init message
        #You can use json.dumps to conver a python dictionary to a json string

        self.msg = json.dumps({
            'port': self.port,
            'files': get_file_info()
        })

        #Create a TCP socket to serve file requests from peers.
        self.server = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

        try:
            self.server.bind((self.host, self.port))
        except socket.error:
            print(('Bind failed %s' % (socket.error)))
            sys.exit()
        self.server.listen(10)

    # Not currently used. Ensure sockets are closed on disconnect
    def exit(self):
        self.server.close()


    #Handle file request from a peer(i.e., send the file content to peers)
    def process_message(self, conn,addr):
        '''
        Arguments:
        self -- self object
        conn -- socket object for an accepted connection from a peer
        addr -- address bound to the socket of the accepted connection
        '''

        with conn:
            while True:
                name = conn.recv(self.BUFFER_SIZE)
                if not name: break
            with open("name",'rb') as file:
                for line in file:
                    conn.sendall(line)

    def run(self):
        self.client.connect((self.trackerhost,self.trackerport))
        t = threading.Timer(2, self.sync)
        t.start()
        print(('Waiting for connections on port %s' % (self.port)))
        while True:
            conn, addr = self.server.accept()
            threading.Thread(target=self.process_message, args=(conn,addr)).start()

    #Send Init or KeepAlive message to tracker, handle directory response message
    #and  request files from peers
    def sync(self):
        print(('connect to:'+self.trackerhost,self.trackerport))
        #Step 1. send Init msg to tracker (Note init msg only sent once)
        #Note: self.msg is initialized with the Init message (refer to __init__)
        #      then later self.msg contains the Keep-alive message
        #
        self.server.connect((self.trackerhost,self.trackerport))
        self.server.send(self.msg)

        #Step 2. now receive a directory response message from tracker

        drm = self.client.recv(self.BUFFER_SIZE)
        drm = drm.decode('utf-8')

            
        #YOUR CODE
        print('received from tracker:',drm)

        #Step 3. parse the directory response message. If it contains new or
        #more up-to-date files, request the files from the respective peers.
        #NOTE: compare the modified time of the files in the message and
        #that of local files of the same name.
        #Hint: a. use json.loads to parse the message from the tracker
        #      b. read all local files, use os.path.getmtime to get the mtime 
        #         (also note round down to int)
        #      c. for new or more up-to-date file, you need to create a socket, 
        #         connect to the peer that contains that file, send the file name, and 
        #         receive the file content from that peer
        #      d. finally, write the file content to disk with the file name, use os.utime
        #         to set the mtime
        #YOUR CODE

        #Step 4. construct and send the KeepAlive message
        #Note KeepAlive msg is sent multiple times, the format can be found in Table 1
        #use json.dumps to convert python dict to json string.
        self.msg = json.dumps({
            'port': self.trackerport
        })

        #Step 5. start timer
        t = threading.Timer(5, self.sync)
        t.start()

if __name__ == '__main__':
    #parse command line arguments
    parser = optparse.OptionParser(usage="%prog ServerIP ServerPort")
    options, args = parser.parse_args()
    if len(args) < 1:
        parser.error("No ServerIP and ServerPort")
    elif len(args) < 2:
        parser.error("No  ServerIP or ServerPort")
    else:
        if validate_ip(args[0]) and validate_port(args[1]):
            tracker_ip = args[0]
            tracker_port = int(args[1])

        else:
            parser.error("Invalid ServerIP or ServerPort")
    #get free port
    synchronizer_port = next(get_next_available_port(8000))
    synchronizer_thread = FileSynchronizer(tracker_ip,tracker_port,synchronizer_port)
    synchronizer_thread.start()