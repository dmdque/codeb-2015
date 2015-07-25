from clientpy2 import *

TEAM_NAME = "Team_333"
TEAM_PW = "cs123"

def quick_run(commands):
    TEAM_NAME = "Team_333"
    TEAM_PW = "cs123"
    return ret_run(TEAM_NAME, TEAM_PW, commands)

class Order:
    price = None
    shares = None

    def __init__(self, price=None, shares=None):
        self.price = float(price)
        self.shares = int(shares)

    def s_print(self):
        print "{", self.price, self.shares, "}"

class Security:
    ticker = None
    shares = None
    dr = None

    def __init__(self, ticker=None, shares=None, dr=None):
        self.ticker = ticker
        self.shares = int(shares)
        self.dr = float(dr)

    def s_print(self):
        print "{", self.ticker, self.shares, self.dr, "}"

class SecurityMeta:
    ticker = None
    net_worth = None
    dr = None
    vol = None
    cash_diff = None

    def __init__(self, ticker=None, net_worth=None, dr=None, vol=None, cash_diff=None):
        self.ticker = ticker
        self.net_worth = float(net_worth)
        self.dr = float(dr)
        self.vol = float(vol)
        if cash_diff != None:
            self.cash_diff = float(cash_diff)

    def s_print(self):
        print "{", self.ticker, self.net_worth, self.dr, self.vol, "}"

def get_cash():
    return float(ret_run(TEAM_NAME, TEAM_PW, "MY_CASH")[0].split()[1])

# returns list of SecurityMeta
def get_securities():
    securities = []
    inputstr = ret_run(TEAM_NAME, TEAM_PW, "SECURITIES")[0].split()
    i = 1
    while i < len(inputstr):
        s = SecurityMeta(inputstr[i], inputstr[i+1], inputstr[i+2], inputstr[i+3])
        securities.append(s)
        i += 4
    return securities

# given a stock, return the best ask order
def find_highest_bid(ticker):
    bids, asks = get_ticker_orders(ticker)
    best_order = find_highest_order_price(bids)
    return best_order

# given a stock, return the best ask order
def find_lowest_ask(ticker):
    bids, asks = get_ticker_orders(ticker)
    best_order = find_lowest_order_price(asks)
    return best_order

# returns order with lowest price
def find_lowest_order_price(olist):
    prices = map(lambda e: e.price, olist)
    return olist[prices.index(min(prices))]

# returns order with highest price
def find_highest_order_price(olist):
    prices = map(lambda e: e.price, olist)
    return olist[prices.index(max(prices))]

# does this even work properly?
# rename to sell_best
def place_best_ask(ticker):
    print "place_best_ask"
    PRICE_DELTA = 0.01
    bids, asks = get_ticker_orders(ticker)
    best_order = find_highest_order_price(bids)
    best_order.s_print()

    best_price = best_order.price - PRICE_DELTA
    # TODO: compute best price
    my_securities = get_my_securities()
    sec = my_securities[map(lambda s: s.ticker, my_securities).index(ticker)]
    my_shares = sec.shares
    print "best_price", best_price
    print "my_shares", my_shares

    return place_ask(ticker, best_price, my_shares)

# places best bid for certain ticker
# tries to buy all of the shares of the lowest ask,
# or most possible (depending on cash)
def place_best_bid(ticker):
    PRICE_DELTA = 0.01
    bids, asks = get_ticker_orders(ticker)
    best_order = find_lowest_order_price(asks)

    best_price = best_order.price + PRICE_DELTA
    max_shares = best_order.shares

    cash = get_cash()
    possible_shares = int(float(cash) / best_price)
    shares = min(max_shares, possible_shares)
    print "best_price", best_price
    print "shares", shares
    # TODO: get num shares I have

    return place_bid(ticker, best_price, shares)

# simple wrapper for BID
def place_bid(ticker, price, shares):
    commands = " ".join(["BID", str(ticker), str(price), str(shares)])
    return quick_run(commands) # TODO: [0] or something

# currently tries to sell all shares
def place_ask(ticker, price, shares):
    print "ticker, price, shares", ticker, price, shares
    commands = " ".join(["ASK", str(ticker), str(price), str(shares)])
    return quick_run(commands)

def get_my_securities():
    securities = []
    inputstr = ret_run(TEAM_NAME, TEAM_PW, "MY_SECURITIES")[0].split()
    i = 1
    while i < len(inputstr):
        s = Security(inputstr[i], inputstr[i+1], inputstr[i+2])
        securities.append(s)
        i += 3
    return securities

# returns all orders for a given stock
# returns in two arrays: bids and asks
def get_ticker_orders(ticker):
    orders = quick_run("ORDERS " + ticker)[0].split()
    bids = []
    asks = []

    i = 1
    while i < len(orders):
        if orders[i] == "BID":
            o = Order(orders[i + 2], orders[i + 3])
            bids.append(o)
        elif orders[i] == "ASK":
            o = Order(orders[i + 2], orders[i + 3])
            asks.append(o)
        i+= 4
    return bids, asks

def get_highest_dr_sec(securities):
    drs = map(lambda e: e.dr, securities)
    return securities[drs.index(max(drs))]

# observe dividend and price to select best stock
def get_best_dividend_ticker():
    None

# returns list of all tickers
def get_tickers_list():
    securities = get_securities()
    return map(lambda e: e.ticker, securities)
