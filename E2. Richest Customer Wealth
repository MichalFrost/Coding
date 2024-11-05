from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        MaxValue = 0
        for i in range(len(accounts)):
            SumValue = sum(accounts[i])
            MaxValue = max(MaxValue, SumValue)
        return MaxValue

def test_solution(accounts: List[List[int]], expected_output: int):
    solution = Solution()
    result = solution.maximumWealth(accounts)

    if result == expected_output:
        print(f"Wynik testu jest poprawny dla Accounts = {accounts}. Wynik: {result}")
    else:
        print(f"Wynik testu nie jest poprawny dla Accounts = {accounts}. Wynik: {result}, oczekiwano: {expected_output}")

# Przykłady testów
test_solution([[1,2,3],[3,2,1]], 6) 
test_solution([[1,5],[7,3],[3,5]], 10)
test_solution([[2,8,7],[7,1,3],[1,9,5]], 17)
