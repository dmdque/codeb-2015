from clientpy2 import *
from helper import *
import time

TEAM_NAME = "Team_333"
PASS = "cs123"

cash = 0
security_metas = []

def test_two_max():
    # security_metas = [SecurityMeta(1, 1, 1, 1, 6), SecurityMeta(1, 1, 1, 1, 7), SecurityMeta(1, 1, 1, 1, 8)]
    security_metas = [SecurityMeta(1, 1, 1, 1, 11), SecurityMeta(1, 1, 1, 1, 7), SecurityMeta(1, 1, 1, 1, 8)]
    print map(lambda e: e.cash_diff, security_metas)
    maxes = two_max(security_metas)
    print map(lambda e: e.cash_diff, maxes)


def two_max(sec_metas):
    cash_diffs = map(lambda s: s.cash_diff, sec_metas)
    max1 = max(cash_diffs)
    cash_diffs2 = cash_diffs[:]
    cash_diffs2.remove(max1)
    max2 = max(cash_diffs2)
    
    return sec_metas[cash_diffs.index(max1)], sec_metas[cash_diffs.index(max2)]
    
def main():
    #cash = get_cash()
    #print cash

    security_metas = get_securities()
    measure_dividend_payout(security_metas)
    for s in security_metas:
        s.s_print()
    print map(lambda s: (s.ticker, s.cash_diff), security_metas) # for demo purposes
    #get_highest_dr_sec(security_metas).s_print()
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
    n = len(security_metas)
    asum = 0
    high_dividend = False
    for ii in range(0,n-1):
        bids, asks = get_ticker_orders(security_metas[ii].ticker)
        asksPrice = map(lambda e: e.price, asks)
        bidsPrice = map(lambda e: e.price, bids)
        ask_price = asks[asksPrice.index(max(asksPrice))].price + 0.03
        bid_price = bids[bidsPrice.index(min(bidsPrice))].price
        theprice = (bid_price + ask_price)/2.0 - ask_price - 0.05
        if security_metas[ii].cash_diff < theprice:
            asum = asum + 1
    if asum > (float(n)/2.0):
        print "high dividend"
        high_dividend = True

    print high_dividend    
    high_dividend = True

    # STEP 3
    if high_dividend:
        first,second=two_max(security_metas)
        print "highest: "
        first.s_print()
        print "second highest"
        second.s_print()
        while True:
            print "buying highest"
            place_best_bid(first.ticker)
            cash1 = get_cash()
            time.sleep(5)
            cash2 = get_cash()
            while (cash2 - cash1) > second.cash_diff:
                cash1 = get_cash()
                time.sleep(5)
                cash2 = get_cash()
            print "selling highest"
            place_best_ask(first.ticker)
            print "buying second highest"
            place_best_bid(first.ticker)
            cash1 = get_cash()
            time.sleep(5)
            cash2 = get_cash()
            while (cash2 - cash1) > second.cash_diff:
                print "cash2 - cash1", (cash2 - cash1), "second highest: ", second.cash_diff
                cash1 = get_cash()
                time.sleep(5)
                cash2 = get_cash()
            print "selling second highest"
            place_best_ask(second.ticker)

    # STEP 4

    #print place_best_bid("ATVI")
    #print quick_run("MY_ORDERS")
    #print quick_run("MY_SECURITIES")

    #security_metas = get_my_securities()
    #for s in security_metas:
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
