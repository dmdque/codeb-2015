import socket
import sys

def connect():
    global sock
    global sfile
    TEAM_NAME = "Team_333"
    TEAM_PW = "cs123"
    user, password = TEAM_NAME, TEAM_PW

    HOST, PORT = "codebb.cloudapp.net", 17429

    data=user + " " + password + "\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
    finally:
        print "connected"

def disconnect():
    global sock
    global sfile
    data = "\nCLOSE_CONNECTION\n"
    try:
        sock.sendall(data)
        sock.close()
    finally:
        print "disconnected"

# modification which returns instead of printing to stdout
def ret_run(*commands):
    global sock
    global sfile
    return_line = None

    data="\n".join(commands) + "\n"

    try:
        sock.sendall(data)
        sfile = sock.makefile()
        return_line = sfile.readline().strip()
    finally:
        None

    return return_line

def run(user, password, *commands):
    HOST, PORT = "codebb.cloudapp.net", 17429

    data=user + " " + password + "\n" + "\n".join(commands) + "\nCLOSE_CONNECTION\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
    finally:
        sock.close()

def subscribe(user, password):
    HOST, PORT = "codebb.cloudapp.net", 17429
    
    data=user + " " + password + "\nSUBSCRIBE\n"

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((HOST, PORT))
        sock.sendall(data)
        sfile = sock.makefile()
        rline = sfile.readline()
        while rline:
            print(rline.strip())
            rline = sfile.readline()
    finally:
        sock.close()
