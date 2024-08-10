class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Checks "x" to see if it is negative
        if x < 0:
            return False
        #Converts int to string
        str_x = str(x)
        #Compares if the number is the same in reverse
        return str_x == str_x[::-1]
