class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1:

            # Cycle detected, not a happy number
            if n in seen:
                return False  
            seen.add(n)

            new_n = 0

            while n > 0:
                # Take the last digit from the 'n' number
                digit = n % 10

                # Counts the new sum of number's digits
                new_n += digit**2
                
                # Take out the last digit from the 'n' number
                n //= 10

            n = new_n

        return True