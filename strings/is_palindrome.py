class Solution:
    def isPalindrome(self,s):
        s_filtered = list(filter(lambda x:x.isalnum(),s))
        s_cleaned = [i.lower() for i in s_filtered]
        reversed_s = [a for a in reversed(s_cleaned)]
        if s_cleaned == reversed_s:
            return True
        else:
            return False

def main():
    input = "A man, a plan, a canal: Panama"
    s = Solution()
    print(s.isPalindrome(input))

if __name__ == "__main__":
    main()