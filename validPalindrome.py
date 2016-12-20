# This class is used to determine if a string is a palindrome, 
# considering only alphanumeric characters and ignoring cases 
# https://leetcode.com/problems/valid-palindrome/

import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        size = len(s)
        if(size == 0):
            return(True)
        oldString = s.lower()
        oldString = re.sub(r'[^a-zA-Z0-9]', '', oldString) #only alphanumerical characters
        newString = oldString[::-1] #reverse the string
        if(newString == oldString):
            return True
        return False

s = 'ab.a'
obj = Solution()
result = obj.isPalindrome(s)
print(result)