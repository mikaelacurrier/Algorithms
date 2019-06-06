#!/usr/bin/python

import argparse
import math

def find_max_profit(prices):
  max_profit = -math.inf

  for idx, price in enumerate(prices):
    future = prices[idx+1:]
    if future:
      max_price = max(future)
      current = max_price - price

      if current > max_profit:
        max_profit = current

  return max_profit
    


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

  