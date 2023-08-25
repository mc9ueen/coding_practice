def find_max_perimiter_of_triangle(sections: list, size: int):
    perimiter = 0
    sections = sorted(sections, reverse=True)
    for length in range(size - 2):
        c, a, b = sections[length], sections[length + 1], sections[length + 2]
        sum_of_abc = a + b + c
        if c < a + b:
            perimiter = sum_of_abc if sum_of_abc > perimiter else perimiter
    return perimiter


if __name__ == "__main__":
    amount_of_sections = int(input())
    sections = [int(i) for i in input().split()]
    print(find_max_perimiter_of_triangle(sections, amount_of_sections))
