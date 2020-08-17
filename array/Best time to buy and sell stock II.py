#!/usr/bin/env python
class Solution:
    def maxProfit(self, prices):
        ## [7,1,5,3,6,4]
        ## [1,2,3,4,5]
        max_profit = 0
        peak = prices[0]
        valley = prices[0]
        i = 0
        while i < len(prices) - 1:
            if prices[i+1] < prices[i]:
                i = i + 1
                valley = prices[i]
            else:
                i = i + 1
                peak = prices[i]
                max_profit += peak-valley
                # set the new floor for next profit seeking
                valley = peak
        return max_profit

def main():
    prices = [10,14,5,8,1,12,9]
    profit_calculator = Solution()
    print(profit_calculator.maxProfit(prices))

if __name__ == "__main__":
    main()