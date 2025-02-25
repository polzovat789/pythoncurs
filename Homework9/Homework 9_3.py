def solution(number):
    if not isinstance(number, int) or number < 0:
        return False

    digits = [int(d) for d in str(number)]
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] = digits[i] - 9

    return sum(digits) % 10 == 0


assert not solution(4561261212345464)
assert solution(4561261212345467)
