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

def track_orders():
    connect()
    times_bids = []
    times_asks = []
    for i in range(3 * 60)
        bids, asks = get_ticker_orders(ticker)
        times_bids.append(map(lambda e: [e.price, e.shares], bids))
        times_asks.append(map(lambda e: [e.price, e.shares], asks))
        time.sleep(1)
    disconnect()
    for bs in times_bids:
        print

#main()
#track_my_securities()

# causes disconnect on SIGINT
def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
            disconnect()
            sys.exit(1)

    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)

    # restore the exit gracefully handler here    
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store the original SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
    track_orders()
