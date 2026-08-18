class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {
                        "I": 1,
                        "V" :5,
                        "X": 10,
                        "L": 50,
                        "C" : 100,
                        "D" : 500,
                        "M" : 1000,
                    }
        kek = list(s)
        count = 0
        number = 0
        skip = False
        for i in kek:
                if skip:
                    skip = False
                    count += 2
                    continue
                new_i = i.upper()
                if (count + 1 < len(kek) and new_i == "I" and kek[count + 1].upper() == "V"):
                    number += 4
                    skip = True
                    continue
                elif  (count + 1 < len(kek) and new_i == "I" and kek[count + 1].upper() == "X"):
                    number += 9
                    skip = True
                    continue
                elif  (count + 1 < len(kek) and new_i == "X" and kek[count + 1].upper() == "L"):
                            number += 40
                            skip = True
                            continue
                elif  (count + 1 < len(kek) and new_i == "X" and kek[count + 1].upper() == "C"):
                            number += 90
                            skip = True
                            continue
                elif  (count + 1 < len(kek) and new_i == "C" and kek[count + 1].upper() == "D"):
                            number += 400
                            skip = True
                            continue
                elif  (count + 1 < len(kek) and new_i == "C" and kek[count + 1].upper() == "M"):
                            number += 900
                            skip = True
                            continue
                number += numerals[new_i]
                count += 1
        return number


                        