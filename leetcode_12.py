class Solution:
    def intToRoman(self, num: int) -> str:
          # A list of tuples with integer values and their corresponding Roman numeral
        val = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
        ]

    # The result string
        roman_numeral = ''

    # Go through each value and numeral in the list
        for (i, numeral) in val:
        # While the number is greater than or equal to the value
            while num >= i:
            # Add the Roman numeral to the result
                roman_numeral += numeral
            # Subtract the value from the number
                num -= i

        return roman_numeral
