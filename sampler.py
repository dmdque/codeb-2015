import clientpy2
import time
import sys
from helper import *

TEAM_NAME = "Team_333"
PASS = "cs123"

def main():
    header = ["title", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility", "ticker", "shares", "dividend ratio", "volatility"]
    print ",".join(header)
    s = quick_run("SECURITIES")
    print ",".join(s[0].split())
    sys.stdout.flush()
    securities = get_securities()
    tickers = map(lambda e: e.ticker, securities)
    for i in range(50):
        print "time", time.time()
        for ticker in tickers:
            print ",".join(quick_run("ORDERS " + ticker)[0].split())
            sys.stdout.flush()
        time.sleep(20)

        #s.pop(0) # title

        #res = []
        #for i in range(len(s)):
            #s.pop(0) # throw out ticker
            #entry = []
            #entry.append(s.pop(0))
            #entry.append(s.pop(0))
            #entry.append(s.pop(0))
            #res.append(entry)

    print "done"
main()
