"""
Give a list of strings, find the mapping from 1–26 for each string that maximize the value for each string. 
Do not distinguish between capital letter and lower case, other characters do not count.
"""
from collections import defaultdict
import string
class Solution:
    def __init__(self):
        self.data = None
    def max_value(self,str_list):
        d = defaultdict(int)   
        str_list_lower = [str.lower() for str in str_list]
        for str in str_list_lower:
            if str in d:
                d[str] += 1
            else:
                d[str] = 1
        d_sorted = {k:v for k,v in sorted(d.items(),key=lambda item: item[1],reverse=True)}
        result_d = {}
        i = 26
        for key,value in d_sorted.items():
            if i == 0:
                break
            else:
                result_d[key] = i
                i = i - 1
        return result_d

def main():
    s = Solution()
    l = "Square is a mobile payment company focused on credit card processing and merchant solutions. The company was founded in 2009 by Jack Dorsey — who is also Twitter’s co-founder and CEO — and Jim McKelvey, and aims to make commerce easy. Over the years, square has developed both software and hardware products, as well as business solutions to enable commerce. Square’s annual net revenue reached the 3.3 billion U.S. dollars mark in 2018, up from over 200 million U.S. dollars in 2012. Square internally has hardware, software, cash app, caviar, capital, risk and security as different teams working on technology. Data Science weaves through all these teams in different capacity. Square does billions of transactions every month and hence, each team has a huge amount of data which they can employ to generate interesting insights. Data Scientists from different domains and within fintech can find interesting work at Square."
    l = l.split()
    # print(l)
    ### remove punctuation
    exclude = set(string.punctuation)
    l = [s for s in l if s not in exclude]
    mapping = s.max_value(l)
    max_value = 0
    print(mapping)
    for key,value in mapping.items():
        max_value += value
    print('the max value from the list is {}'.format(max_value))


if __name__ == "__main__":
    main()
        
 


