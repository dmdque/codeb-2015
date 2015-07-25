from clientpy2 import *
from helper import *

TEAM_NAME = "Team_333"
PASS = "cs123"

cash = 0
securities = []

def main():
    cash = get_cash()
    print cash

    securities = get_securities()
    get_highest_dr_sec(securities).s_print()

main()
