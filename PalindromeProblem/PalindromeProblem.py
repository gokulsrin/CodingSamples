class Solution:
    def isPalindrome(self, x: int) -> bool:
        # typecast the int into string so that I can check the text at each index
        y = str(x)
        palindrome = True
        i = 0
        j = len(y) - 1
        # the loop proceeds if the paldindome is true -- or the letters at the i and j index are the same-- and i and j are within the range of the string
        while palindrome and i < len(y) and j >= 0:
            palindrome = y[i] == y[j]
            i += 1
            j -= 1
        
        return palindrome