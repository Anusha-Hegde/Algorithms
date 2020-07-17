'''
Given an input string, reverse the string word by word.

Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "a good   example"
Output: "example good a"

'''


class Solution:
    def reverseWords(self, s: str) -> str:
        st = s.strip().split(' ')
        i = 0
        num = len(st)
        #check for empty spaces
        while i < num:
            if len(st[i]) == 0: 
                st.pop(i)
                num -= 1
            else: i += 1
        st.reverse()
        return ' '.join(st)