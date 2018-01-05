# << Swami Shreeji >>
# 4 Jan 2018

# Apple Stocks - A function that returns the best profit one could make from
#  one purchase and one sale of one stock from a point in time.

# One caveat is that there's no "shorting." You MUST buy before you sell
	
	# stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
	#
	# get_max_profit(stock_prices_yesterday)
	# # returns 6 (buying for $5 and selling for $11)

import sys

def stock_prices_yesterday(raw = []):
	# Find index of stock at lowest price in the day
	lowestTradeIndex = min( xrange(len(raw)), key = raw.__getitem__ )

	# The high trade must occur AFTER lowest.
	highTradeIndex = raw.index(max(raw[raw.index(min(raw)):])) 

	# Return answer
	cake = raw[highTradeIndex] - raw[lowestTradeIndex]
	return cake

case1 = [10, 7, 11, 8, 5, 9]
case2 = [6, 5, 4, 3, 2, 1, 0]
answer = stock_prices_yesterday(case1)
print answer