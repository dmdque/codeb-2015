from clientpy2 import *
from helper import *

TEAM_NAME = "Team_333"
PASS = "cs123"

cash = 0
securities = []

def main():
    #cash = get_cash()
    #print cash

    #securities = get_securities()
    #get_highest_dr_sec(securities).s_print()
    print "bids and asks"
    bids, asks = get_ticker_orders("ATVI")
    print get_ticker_orders("ATVI")
    for e in bids:
        e.s_print()
    for e in asks:
        e.s_print()

    #print place_best_bid("ATVI")
    #print quick_run("MY_ORDERS")
    #print quick_run("MY_SECURITIES")

    #securities = get_my_securities()
    #for s in securities:
        #s.s_print()

    ##print place_best_bid("AAPL")
    #print place_best_ask("AAPL")

main()
