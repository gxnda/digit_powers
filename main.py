"""
Other than the numbers 1 to 9 are there any numbers that can be written as a sum of integer powers of its digits?
"""

from itertools import product


def is_sum_of_digit_powers(n: int) -> tuple[bool, list[int]]:
    digits = [int(d) for d in str(n)]
    powers = range(1, len(str(n)) + 1)
    combinations = product(powers, repeat=len(digits))

    for power_combo in combinations:
        digit_powers = [d ** p for d, p in zip(digits, power_combo)]
        if n == sum(digit_powers):
            return True, digit_powers

    return False, []


if __name__ == '__main__':
    num = 10

    running = True
    while running:
        is_sum = is_sum_of_digit_powers(num)
        if is_sum[0]:
            print(num, is_sum[1])

        num += 1
