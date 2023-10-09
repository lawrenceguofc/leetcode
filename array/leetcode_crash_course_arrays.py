"""
https://leetcode.com/explore/interview/card/leetcodes-interview-crash-course-data-structures-and-algorithms/703/arraystrings/4501/
"""

# pattern 1: move two pointers toward the middle


"""
Example 1: Given a string s, return true if it is a palindrome, false otherwise.

A string is a palindrome if it reads the same forward as backward. That means, after reversing it, it is still the same string. For example: "abcdcba", or "racecar".

"""

def is_palindrome(s):
	left = 0
	right = len(s) - 1
	while left < right:
		if s[left] == s[right]:
				left += 1
				right -= 1
		else:
				return False
	return True

print(is_palindrome('raceecar'),is_palindrome('kdf'))

"""
Example 2: Given a sorted array of unique integers and a target integer, return true if there exists a pair of numbers that sum to target, false otherwise. This problem is similar to Two Sum. (In Two Sum, the input is not sorted).

For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.
"""

def sum_to_target(s, target):
	left = 0
	right = len(s) - 1
	while left < right:
		if s[left] + s[right] < target:
			left += 1
		elif s[left] + s[right] > target:
			right -= 1
		else:
			return True
	return False 

print(sum_to_target(s=[1, 2, 4, 6, 8, 9, 14, 15],target=13))
            
# pattern 2: move two pointers individually

"""
Example 3: Given two sorted integer arrays arr1 and arr2, return a new array that combines both of them and is also sorted.

"""
def combined_sorted(a1,a2):
	i = 0 
	j = 0
	arr = []
	while i < len(a1) and j < len(a2):
		if a1[i] <= a2[j]:
			arr.append(a1[i])
			i = i + 1
		else:
			arr.append(a2[j])
			j = j + 1
	if i < len(a1):
		arr.append(a1[i:])
	if j < len(a2):
		arr.append(a2[j:])
	return arr

print(combined_sorted(a1=[1,4,7,20],a2=[3,5,6]))

"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

"""
def reverseS(s):
	i = 0
	j = len(s) - 1
	while i < j:
		s[i],s[j]  = s[j],s[i]
		i += 1
		j -= 1
	return s

print(reverseS(["h","e","l","l","o"]))

"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""

def squared(nums):
	output = [0] * len(nums)
	left = 0
	right = len(nums) - 1
	for i in range(len(nums)-1,-1,-1):
		if abs(nums[left]) < abs(nums[right]):
			square  = nums[right]
			right = right - 1
		else:
			square = nums[left]
			left = left + 1
		output[i] = square*square

	return output

print(squared(nums=[-4,-1,0,3,10]))


# pattern 3: sliding window
"""
Pseudo code 
function fn(arr):
    left = 0
    for (int right = 0; right < arr.length; right++):
        Do some logic to "add" element at arr[right] to window

        while WINDOW_IS_INVALID:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer

"""


"""
Example 1: Given an array of positive integers nums and an integer k, find the length of the longest subarray whose sum is less than or equal to k. This is the problem we have been talking about above. We will now formally solve it.
it's useful to find
"""

def find_length(nums,k):
	left = curr = ans = 0
	for right in range(len(nums)):
		curr = curr + nums[right]
		while curr > k: 
			curr = curr - nums[left]
			left = left + 1
		ans = max(ans,right - left + 1)
	return ans

"""
Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111.

"""
# translate the problem into finding the longest string contains one 0
def flip_zero(s):
	# curr = count of 0s in the window
	left = curr = ans = 0 
	for right in range(len(s)):
		if s[right] == '0':
			curr = curr + 1 
		while curr > 1:
		    if s[left] == '0':
				curr = curr - 1
			left = left + 1
	    ans = max(ans,right - left  + 1)
	return ans 