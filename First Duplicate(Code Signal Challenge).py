def solution(a):
    unique = set()
    for num in a:
        if num in unique:
            return num
        unique.add(num)
    return -1

