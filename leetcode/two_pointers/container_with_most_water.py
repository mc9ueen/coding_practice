# https://leetcode.com/problems/container-with-most-water/
def max_area(height: list) -> int:
    begin: int = 0
    end: int = len(height) - 1
    max_square = -1

    while begin < end:
        lowest_height = min(height[begin], height[end])
        length = end - begin
        max_square = max(max_square, lowest_height * length)

        if height[begin] < height[end]:
            begin += 1
        else:
            end -= 1

    return max_square
