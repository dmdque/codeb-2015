from clientpy2 import *
from helper import *
import time
import signal
import numpy as np
import random

NUM_INPUTS = 9
SUCCESS_THRESHOLD = 50
LEARN_RATE = 5

def heavyside(z):
    if z < 0:
        return 0
    else:
        return 1

def get_avg_asks(ticker):
    bids, asks = get_ticker_orders(ticker)
    ask_prices = map(lambda e: e.price, asks)
    return np.average(ask_prices)

def get_avg_bids(ticker):
    bids, asks = get_ticker_orders(ticker)
    bid_prices = map(lambda e: e.price, bids)
    return np.average(bid_prices)

def get_ticker_inputs(ticker):
    tickers = get_tickers_list()
    ticker_index = tickers.index(ticker)

    securities = get_my_securities()
    meta_securities = get_securities()

    # TODO: need to add number of shares I own
    shares = securities[ticker_index].shares
    dr_current = securities[ticker_index].dr
    nw = meta_securities[ticker_index].net_worth
    dr_max = meta_securities[ticker_index].dr
    vol = meta_securities[ticker_index].vol
    cash = get_cash()
    bid = get_avg_bids(ticker)
    ask = get_avg_asks(ticker)
    bias = 1

    return shares, dr_current, nw, dr_max, vol, cash, bid, ask, bias

def initialize_neurons(tickers):
    global ticker_networks
    ticker_networks = []

    for ticker in tickers:
        neuron_weights = np.random.rand(NUM_INPUTS)
        shift = np.zeros(NUM_INPUTS)
        shift.fill(-0.5)
        neuron_weights += shift
        neuron_weights *= 0.00001

        ticker_networks.append(neuron_weights)
    return ticker_networks


def main():
    connect()
    train()
    disconnect()

def train():
    is_stop_critereon = False
    tickers = get_tickers_list()
    ticker_networks = initialize_neurons(tickers)

    last_ticker_z_values, last_ticker_a_values = None, None
    last_ticker_i, last_decision, = None, None
    i = 0
    while not is_stop_critereon:
        # TODO: replace cash with net worth
        cash1 = get_cash()
        ticker_z_values, ticker_a_values, ticker_inputs = forward(ticker_networks)

        #z_max = max(ticker_z_values)
        #z_min = min(ticker_z_values)
        #ticker_i = None
        #if abs(z_max) - abs(z_min) > 0:
            #ticker_i = ticker_z_values.index(z_max)
        #else:
            #ticker_i = ticker_z_values.index(z_min)
        ticker_i = int(random.random() * NUM_INPUTS)

        decision = ticker_a_values[ticker_i]
        act_ticker = tickers[ticker_i]
        inputs = ticker_inputs[ticker_i]
        print "choosing", decision, "of ticker:", act_ticker

        if decision == 1:
            time.sleep(3)
        cash2 = get_cash()
        # divide funds evenly as a budget for each stock
        if decision == 1:
            place_best_bid(act_ticker)
        else:
            # sell all act_ticker
            for ticker in tickers:
                if random.random() > 0.7:
                    place_best_ask(ticker)

        if last_ticker_z_values and last_ticker_a_values:
            #z_max = max(last_ticker_z_values)
            #z_min = min(last_ticker_z_values)
            #ticker_i = None
            #if abs(z_max) - abs(z_min) > 0:
                #ticker_i = last_ticker_z_values.index(z_max)
            #else:
                #ticker_i = last_ticker_z_values.index(z_min)

            decision = last_ticker_a_values[last_ticker_i]
            inputs = last_ticker_inputs[last_ticker_i]

            y = None
            print "cash delta:", cash2 - cash1
            if cash2 - cash1 > SUCCESS_THRESHOLD:
                y = 0
            else:
                y = 1
            if decision != y:
                print "punish"
                ticker_networks[ticker_i] += (y - decision) * inputs * 0.01
            else:
                #ticker_networks[ticker_i] *= 0.7
                print "reward"

        last_ticker_z_values = ticker_z_values
        last_ticker_a_values = ticker_a_values
        last_ticker_inputs = ticker_inputs
        last_ticker_i = ticker_i
        i += 1
        print "i:", i
        if i > 100:
            is_stop_critereon = True
            print ticker_networks


def forward(ticker_networks):
    tickers = get_tickers_list()
    ticker_z_values = []
    ticker_a_values = []
    for i, ticker in enumerate(tickers):
        inputs = np.array(get_ticker_inputs(ticker))
        neuron_weights = ticker_networks[i]
        z = np.dot(inputs, neuron_weights)
        #print "Z", z
        a = heavyside(z)

        ticker_z_values.append(z)
        ticker_a_values.append(a)

    return ticker_z_values, ticker_a_values, inputs


# causes disconnect on SIGINT
def exit_gracefully(signum, frame):
    # restore the original signal handler as otherwise evil things will happen
    # in raw_input when CTRL+C is pressed, and our signal handler is not re-entrant
    signal.signal(signal.SIGINT, original_sigint)

    try:
        if raw_input("\nReally quit? (y/n)> ").lower().startswith('y'):
            global ticker_networks
            disconnect()
            tnl = list(ticker_networks)
            print map(lambda e: list(e), tnl)
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
    main()
