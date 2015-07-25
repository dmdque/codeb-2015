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
            print ",".join(quick_run("ORDERS " + ticker).split())
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

def track_my_securities():
    tickers = get_tickers_list()
    print tickers
    # buy one of each stock
    for ticker in tickers:
        price = find_lowest_ask(ticker).price
        place_bid(ticker, price, 1)
        print "bought", ticker, price, 1
    for i in range(5 * 60):
        print ",".join(quick_run("MY_SECURITIES").split())
        sys.stdout.flush()
        time.sleep(1)

#main()
track_my_securities()
