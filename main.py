from math import sqrt


def is_perfect_square(num):
    low, high = 1, num
    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        if square == num:
            return True
        elif square < num:
            low = mid + 1
        else:
            high = mid - 1
    return False


# print(is_perfect_square(16))

max_num = 4000*4000

for x in range(25, max_num, 25):
    x = x * x
    if not is_perfect_square(x):
        continue
    for a in range(1, x):
        if not is_perfect_square(x-a):
            continue
        if not is_perfect_square(x+a):
            continue
        for b in range(1, a):
            if x-a-b <= 0:
                continue
            if not is_perfect_square(x-b):
                continue
            if not is_perfect_square(x+b):
                continue
            print(sqrt(x), sqrt(x-a), sqrt(x+a),  sqrt(x-b), sqrt(x+b))

            if not is_perfect_square(x+a+b):
                continue
            if not is_perfect_square(x+a-b):
                continue
            if not is_perfect_square(x-a+b):
                continue
            if not is_perfect_square(x-a-b):
                continue
            
            print("YAY", sqrt(x), sqrt(x-a), sqrt(x+a),  sqrt(x-b), sqrt(x+b))

