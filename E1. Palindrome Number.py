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

def test_solution(x: int, expected_output: bool):
    solution = Solution()
    result = solution.isPalindrome(x)

    if result == expected_output:
        print(f"Wynik testu jest poprawny dla x = {x}. Wynik: {result}")
    else:
        print(f"Wynik testu nie jest poprawny się dla x = {x} . Wynik: {result}, oczekiwano: {expected_output}")

# Przykłady testów
test_solution(121, True)    # Palindrom, powinno wypisać, że test przeszedł poprawnie
test_solution(-121, False)  # Liczba ujemna, nie jest palindromem
test_solution(123, False)   # Nie-palindrom
test_solution(0, True)      # Palindrom (0 jest palindromem)
