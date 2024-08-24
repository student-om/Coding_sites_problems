
class Solution:
    def is_palindrome(self, n):
        p = str(n)
        a = p[::-1]
        return p == a

    def nearestPalindromic(self, n: str) -> str:
        n = int(n)
        if n > 0 and n < 10:
            return str(n - 1)

        temp_next = n + 1
        temp_prev = n - 1

        while True:
            if self.is_palindrome(temp_prev):
                return str(temp_prev)
            if self.is_palindrome(temp_next):
                return str(temp_next)
            
            temp_next += 1
            temp_prev -= 1
