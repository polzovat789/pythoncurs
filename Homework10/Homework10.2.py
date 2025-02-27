def solution(candle_number, make_new):
    total = 0
    leftovers = 0
    while candle_number > 0:
        total += candle_number
        leftovers += candle_number
        candle_number = leftovers // make_new
        leftovers = leftovers % make_new
    return total


assert solution(5, 2) == 9
assert solution(1, 2) == 1
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2
