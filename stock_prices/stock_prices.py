#!/usr/bin/python

import argparse

def find_max_profit(prices):
  buy = sell = 0
  profit = -1
  change = True

  for i in range(0, len(prices)-1):
    sell = prices[i+1]
    
    if change:
      buy = prices[i]
    
    if sell < buy:
      change = True
      continue
    
    else:
      p = sell - buy
      if p > profit:
        profit = p
      change = False
    return sell
  #   if p < p + 1:
  #      buy = p
  #      sell = p + 1
  #      profit = buy - sell
  #   elif p < buy:
  #     buy = p
  #     sell = p + 1
  #   elif p > sell:
  #     sell = p
  # return profit

    


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))

  