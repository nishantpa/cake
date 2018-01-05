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
	# Address an edge case where there's only 1 entry
	if len(raw) < 2:
    		raise ValueError('Getting a profit requires at least 2 prices')
	
	# Edge case of cosistently decreasing stock price.
		# This is a neat way to check if the list is reverse sorted or, in this
		#  case, forever decreasing (descending order)
	if all(earlier >= later for earlier, later in zip(raw, raw[1:])):
		answer = "The stock price decreased all day. Profit not possible."
		return answer

	# Find index of stock at lowest price in the day
	lowestTradeIndex = min( xrange(len(raw)), key = raw.__getitem__ )

	# The high trade must occur AFTER lowest.
	highTradeIndex = raw.index(max(raw[raw.index(min(raw)):])) 

	# Return answer
	cake = raw[highTradeIndex] - raw[lowestTradeIndex]
	return cake

case1 = [10, 7, 11, 8, 5, 9]
case2 = [6, 5, 4, 3, 2, 1, 0]
answer = stock_prices_yesterday(case2)
print answer

'''
I want cake
'''
