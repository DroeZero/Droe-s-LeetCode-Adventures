class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_x = str(x)
        i = len(new_x) -1
        result = ""
        while i >= 0:
            result += new_x[i]
            i -= 1
        if "-" in result:
            return False
        elif int(result) == x:
            return True
        else:
            return False



        