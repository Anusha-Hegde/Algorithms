'''
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        res = 0
        odd = False
        for i in s:
            if i not in dic: dic[i] = 0
            dic[i] += 1
        for i in dic:
            #check if one lone character is present
            if dic[i] % 2: odd = True
            #add all even number of characters 
            res  += int(dic[i] / 2) * 2
        if odd: res += 1
        return res