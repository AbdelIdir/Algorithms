#!/usr/bin/python

import argparse


def find_max_profit(prices):
    # keep track of the minimum price so far
    current_min_price_so_far = prices[0]
    # keep track of the maximum profit so far
    max_profit_so_far = prices[1] - current_min_price_so_far
    # while going though the array, we wanna make sure to constantly update the two.values
    for i in range(1, len(prices - 1)):
        if prices[i] > prices[i + 1]:
            current_min_price_so_far = prices[i+1]
            max_profit_so_far = prices[i+1]-prices[i]
    # once we have established which is the smallest and which is the biggest, we do the difference between the two
    return max_profit_so_far


if __name__ == '__main__':
        # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
