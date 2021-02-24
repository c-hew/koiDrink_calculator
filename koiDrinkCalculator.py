''' Earn 3 Leaves with every $1 spent with your KOIThélicious card, and
earn 1.5 Leaves with every $0.6-$0.9 spent. Leaves will be calculated
based on the total spending amount in a single receipt. (E.g. $15.60
spent, 15 x 3 + 1.5 = 46.5 Leaves rewarded) 
Source:
https://www.koithe.sg/FAQsMemPortalRevised_Oct2019.pdf

'''
import math
class Rewards(object):
    def __init__(self, name):
        self.name = name
        
    def redeem(self, leaves_count):
        ''' Method '''
        pass


def earnLeavesOnSpend(amt_spent):
    amt_spent_floor = math.floor(amt_spent)
    print(amt_spent_floor)
    other_amt = 0

    if 0.6 <= float(round(amt_spent-amt_spent_floor, 2)) <= 0.9:
        other_amt = 1.5

    output = str(amt_spent_floor*3 + other_amt) + " leaves"
    return output


print(earnLeavesOnSpend(4.6))
