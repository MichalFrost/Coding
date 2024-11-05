class Solution:
    def romanToInt(self, s: str) -> int:
        dict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum=0

        for i in range(len(s)):
            a = dict[str(s[i])]
            if (i == len(s)-1):
                b = 0
            else:
                b = dict[str(s[i+1])]

            if a < b:
                sum-= a
            else:
                sum += a
        return sum;
