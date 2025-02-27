def solution(n, f_number):
    return (f_number + n // 2) % n


assert solution(10, 6) == 1
assert solution(10, 2) == 7
assert solution(10, 4) == 9
