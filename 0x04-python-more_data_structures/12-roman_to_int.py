#!/usr/bin/python3
def roman_to_int(roman_string):
    mapping = {"I": 1, "IV": 4, "V": 5,
            "IX": 9, "X": 10, "XL": 40,
            "L": 50, "XC": 90, "C": 100,
            "CD": 400, "D": 500, "CM": 900, "M": 1000
            }
    ans = 0
    
    if not roman_string:
        return

    for idx, ele in enumerate(roman_string):
        if mapping.get(ele, -1) == -1:
            return 0

        if idx < len(roman_string) - 1 and (mapping.get(roman_string[idx]) < mapping.get(roman_string[idx + 1])):
            ans -= mapping.get(roman_string[idx])

        else:
            ans += mapping.get(roman_string[idx])
    return ans
