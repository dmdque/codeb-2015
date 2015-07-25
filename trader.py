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

    #securities = get_securities()
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
    if high_dividend:
        cash_diffs = map(lambda e: e.cash_diff, securities)
        index_highest = 0
        index_secondhighest = 0
        int i = 0
        while i < len(cash_diffs):
            if cash_diffs[i] < securities[index_highest].cash_diff:
                index_highest = i
            else if cash_diffs[i] < securities[index_secondhighest].cash_diff:
                index_secondhighest = i
        while True:
            place_best_bid(securities[index_highest].ticker)
            cash1 = get_cash()
            sleep(5)
            cash2 = get_cash()
            while (cash2 - cash1) > cash_diffs[index_secondhighest]:
                cash1 = get_cash()
                sleep(5)
                cash2 = get_cash()
            place_best_ask(securities[index_highest].ticker)
            place_best_bid(securities[index_secondhighest].ticker)
            cash1 = get_cash()
            sleep(5)
            cash2 = get_cash()
            while (cash2 - cash1) > cash_diffs[index_secondhighest]:
                cash1 = get_cash()
                sleep(5)
                cash2 = get_cash()
            place_best_ask(securities[index_secondhighest].ticker)

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
    bids, asks = get_ticker_orders("AAPL")
    num_shares = map(lambda e: e.shares, asks)
    order = asks[num_shares.index(max(num_shares))]
    price = order.price + PRICE_DELTA
    place_bid(ticker, price, 1)

def sell_one(ticker):
    PRICE_DELTA = 0.01
    # get price of order with highest number of shares
    # to guarantee quickness
    bids, asks = get_ticker_orders("AAPL")
    num_shares = map(lambda e: e.shares, bids)
    order = bids[num_shares.index(max(num_shares))]
    print map(lambda b: b.price, bids)
    print "sell max shares", max(num_shares), order.shares, order.price
    price = order.price - PRICE_DELTA
    place_ask(ticker, price, 1)

def measure_dividend_payout():
    # store securityMeta
    tickers = get_tickers_list()
    dividend_payouts = {}

    for ticker in tickers:
        buy_one(ticker)
        cash1 = get_cash()
        time.sleep(5)
        cash2 = get_cash()
        sell_one(ticker)

        dividend_payouts[ticker] = float(cash2 - cash1)
        print "dividend payout estimation", ticker, dividend_payouts[ticker]
    print dividend_payouts
    return dividend_payouts

main()
#measure_dividend_payout()
