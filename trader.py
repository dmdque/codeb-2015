from clientpy2 import *
from helper import *
import time

TEAM_NAME = "Team_333"
PASS = "cs123"

cash = 0
securities = []

def main():
    #cash = get_cash()
    #print cash

    security_metas = get_securities()
    measure_dividend_payout(security_metas)
    print map(lambda s: (s.ticker, s.cash_diff), security_metas) # for demo purposes
    #get_highest_dr_sec(securities).s_print()
    #print "bids and asks"
    #bids, asks = get_ticker_orders("AAPL")
    #print get_ticker_orders("AAPL")
    #print "bid"
    #for e in bids:
    #    e.s_print()
    #print "ask"
    #for e in asks:
    #    e.s_print()

    # STEP 1

    # STEP 2

    # STEP 3

    # STEP 4

    #print place_best_bid("ATVI")
    #print quick_run("MY_ORDERS")
    #print quick_run("MY_SECURITIES")

    #securities = get_my_securities()
    #for s in securities:
        #s.s_print()

    #print place_best_bid("AAPL")
    #print place_best_ask("AAPL")

# buys for speed, at the cost of cash
def buy_one(ticker):
    PRICE_DELTA = 0.01
    # get price of order with highest number of shares
    # to guarantee quickness
    bids, asks = get_ticker_orders(ticker)
    num_shares = map(lambda e: e.shares, asks)
    order = asks[num_shares.index(max(num_shares))]
    price = order.price + PRICE_DELTA
    place_bid(ticker, price, 1)

# sells at price given by order with most shares
def sell_one(ticker):
    PRICE_DELTA = 0.01
    # get price of order with highest number of shares
    # to guarantee quickness
    bids, asks = get_ticker_orders(ticker)
    num_shares = map(lambda e: e.shares, bids)
    order = bids[num_shares.index(max(num_shares))]
    price = order.price - PRICE_DELTA
    place_ask(ticker, price, 1)

# adds cash diff info to security meta
def measure_dividend_payout(security_metas):
    # store securityMeta
    tickers = get_tickers_list()

    for i, ticker in enumerate(tickers):
        buy_one(ticker)
        cash1 = get_cash()
        time.sleep(5)
        cash2 = get_cash()
        sell_one(ticker)

        security_metas[i].cash_diff = float(cash2 - cash1)
        print "dividend payout estimation", ticker, security_metas[i].cash_diff

main()
