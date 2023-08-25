def generate_bracers_sequence(left: int, right: int = -1, prefix=None) -> None:
    if right == -1:
        right = left
    prefix = prefix or []
    if left > right:
        return
    if left == 0 and right == 0:
        print(*prefix, sep="")
        return
    if left > 0:
        prefix.append("(")
        generate_bracers_sequence(left - 1, right, prefix)
        prefix.pop()
    if right > 0:
        prefix.append(")")
        generate_bracers_sequence(left, right - 1, prefix)
        prefix.pop()


if __name__ == "__main__":
    amount = int(input())
    generate_bracers_sequence(amount)
