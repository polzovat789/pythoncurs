def solution(sequence):
    count = 0
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            count += 1
            if count > 1:
                return False
            if i > 1 and sequence[i] <= sequence[i - 2]:
                sequence[i] = sequence[i - 1]
    return True


assert solution([1, 2, 3])
assert not solution([1, 2, 1, 2])
assert not solution([1, 3, 2, 1])
assert not solution([1, 2, 3, 4, 5, 3, 5, 6])
assert not solution([40, 50, 60, 10, 20, 30])
