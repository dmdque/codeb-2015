import clientpy2
import time
import sys

TEAM_NAME = "Team_333"
PASS = "cs123"

def run(commands):
    return clientpy2.ret_run(TEAM_NAME, PASS, commands)

def main():
    header = ["title", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility"]
    print ",".join(header)
    while True:
        s = run("SECURITIES")
        time.sleep(1)
        print ",".join(s[0].split())
        sys.stdout.flush()

        #s.pop(0) # title

        #res = []
        #for i in range(len(s)):
            #s.pop(0) # throw out ticker
            #entry = []
            #entry.append(s.pop(0))
            #entry.append(s.pop(0))
            #entry.append(s.pop(0))
            #res.append(entry)

main()
