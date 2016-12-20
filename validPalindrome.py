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
        self.size = len(s)
        if(self.size == 0):
            return(True)
        self.oldString = s.lower()
        self.oldString = re.sub(r'[^a-zA-Z0-9]', '', self.oldString) #only alphanumerical characters
        self.newString = self.oldString[::-1] #reverse the string
        if(self.newString == self.oldString):
            return True
        return False

s = 'ab.a'
obj = Solution()
result = obj.isPalindrome(s)
print(result)