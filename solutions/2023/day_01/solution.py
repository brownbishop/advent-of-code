# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    # @answer(1234)
    def part_1(self) -> int:
        sum = 0
        for line in self.input:
            digits = list(filter(str.isdigit, line))
            calibration_value = int(digits[0]) * 10 + int(digits[-1])
            sum += calibration_value
        return sum


    # @answer(1234)
    def part_2(self) -> int:
        sum = 0
        for line in self.input:
            digits = line_to_digits(line)
            calibration_value = int(digits[0]) * 10 + int(digits[-1])
            sum += calibration_value
        return sum

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

value = {
     "one": 1,
     "two": 2,
     "three": 3,
     "four": 4,
     "five": 5,
     "six": 6,
     "seven": 7,
     "eight": 8,
     "nine": 9,
     "1": 1,
     "2": 2,
     "3": 3,
     "4": 4,
     "5": 5,
     "6": 6,
     "7": 7,
     "8": 8,
     "9": 9,
}

def line_to_digits(line: str) -> list[int]:
    digits = []
    for i in range(len(line)):
        for key in value:
            if line[i:].find(key) == 0:
                digits.append(value[key])
                break
    return digits
