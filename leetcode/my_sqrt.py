def mySqrt(x: int) -> int:
    start = 1
    end = x
    result = 0
    while start <= end:
        mid = (end - start) // 2 + start
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    return result


print(mySqrt(4))
print(mySqrt(8))
