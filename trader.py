from clientpy2 import *
from helper import *
import time

TEAM_NAME = "Team_333"
PASS = "cs123"

cash = 0
security_metas = []

def main():
    #cash = get_cash()
    #print cash

    security_metas = get_securities()
    measure_dividend_payout(security_metas)
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
        cash_diffs = map(lambda e: e.cash_diff, security_metas)
        index_highest = 0
        index_secondhighest = 0
        i = 0
        while i < len(cash_diffs):
            print cash_diffs[i], " ", security_metas[index_highest].cash_diff, " ", security_metas[index_secondhighest].cash_diff
            if cash_diffs[i] > security_metas[index_highest].cash_diff:
                index_highest = i
            elif cash_diffs[i] > security_metas[index_secondhighest].cash_diff:
                index_secondhighest = i
            i += 1
        print "highest: ", index_highest, " "
        security_metas[index_highest].s_print()
        print "second highest", index_secondhighest, " "
        security_metas[index_secondhighest].s_print()
        while True:
            print "buying highest"
            place_best_bid(security_metas[index_highest].ticker)
            cash1 = get_cash()
            time.sleep(5)
            cash2 = get_cash()
            while (cash2 - cash1) > cash_diffs[index_secondhighest]:
                cash1 = get_cash()
                time.sleep(5)
                cash2 = get_cash()
            print "selling highest"
            place_best_ask(security_metas[index_highest].ticker)
            print "buying second highest"
            place_best_bid(security_metas[index_secondhighest].ticker)
            cash1 = get_cash()
            time.sleep(5)
            cash2 = get_cash()
            while (cash2 - cash1) > cash_diffs[index_secondhighest]:
                print "cash2 - cash1", (cash2 - cash1), "second highest: ", cash_diffs[index_secondhighest]
                cash1 = get_cash()
                time.sleep(5)
                cash2 = get_cash()
            print "selling second highest"
            place_best_ask(security_metas[index_secondhighest].ticker)

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
