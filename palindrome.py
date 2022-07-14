from audioop import reverse
from math import fabs
import sys

class Solution:
    # Write code below to complete prompt
    def isPalindrome(self, s):
        
        # TODO: Write code below to return a bool with the solution to the prompt
        b = False
        if s[::-1] == s:
            b = True
        if(b and len(s) > 6):
            return True
        else:
            return False
        pass

def main():
    tc1 = Solution()
    inpyt = input()
    # Write code below to complete prompt
    print(tc1.isPalindrome(inpyt))

if __name__ == "__main__":
    main()