#!/usr/bin/env/python3

"""
Given a roman numeral, convert it to an integer.
"""


class Solution:

    def _lkp(self):
        """ conversion dictionary """
        kvs = [('M', 1000), ('D', 500), ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)]
        self.dct = {key: val for key, val in kvs}

    def _get_next(self: object, numerals: str):
        """ recursive roman numeral parse """

        # base case
        current = numerals[0]
        if len(numerals) == 1:
            return self.dct[current]
        
        # recursive case
        nextone = numerals[1]
        if self.dct[nextone] > self.dct[current]:
            value = -self.dct[current]
        else:
            value = self.dct[current]
        return value + self._get_next(numerals[1:])

    def roman_to_int(self, numerals: str) -> int:
        """ convert valid roman numeral to an integer """
        self._lkp()
        return self._get_next(numerals)


sol = Solution()

assert sol.roman_to_int('I') == 1
assert sol.roman_to_int('IV') == 4
assert sol.roman_to_int('MCMXLVIII') == 1948
