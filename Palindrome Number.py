class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=""
        for i in range(len(str(x))):
            y = y + str(x)[len(str(x))-1-i]

        if str(x) == y:
            palindrome = True
        else:
            palindrome = False

        return palindrome 
