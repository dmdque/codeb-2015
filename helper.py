from clientpy2 import *

TEAM_NAME = "Team_333"
TEAM_PW = "cs123"

class Security:
    ticker = None
    net_worth = None
    dr = None
    vol = None
    

    def __init__(self, ticker=None, net_worth=None, dr=None, vol=None):
        self.ticker = ticker
        self.net_worth = float(net_worth)
        self.dr = float(dr)
        self.vol = float(vol)

    def s_print(self):
        print "{", self.ticker, self.net_worth, self.dr, self.vol, "}"

def get_cash():
    return float(ret_run(TEAM_NAME, TEAM_PW, "MY_CASH")[0].split()[1])

def get_securities():
    securities = []
    inputstr = ret_run(TEAM_NAME, TEAM_PW, "SECURITIES")[0].split()
    i = 1
    while i < len(inputstr):
        s = Security(inputstr[i], inputstr[i+1], inputstr[i+2], inputstr[i+3])
        securities.append(s)
        i += 4
    return securities        

def get_highest_dr_sec(securities):
    drs = map(lambda e: e.dr, securities)
    return securities[drs.index(max(drs))]



