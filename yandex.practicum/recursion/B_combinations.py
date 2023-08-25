keyboard = {"1": "", "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl", "6": "mno",
            "7": "pqrs", "8": "tuv", "9": "wxyz",
            "0": ""
            }


def generate_letters_sequence(sequence: str):
    prefix = []

    def generate_letters_permutations(elements: str, combination: list = None):
        combination = combination or []
        if len(elements) == 0:
            prefix.append("".join(combination))
        else:
            for letter in keyboard[elements[0]]:
                combination.append(letter)
                generate_letters_permutations(elements[1:], combination)
                combination.pop()

    generate_letters_permutations(sequence)
    return prefix


if __name__ == "__main__":
    numbers = input()
    sequence = ""
    for i in numbers:
        for j in keyboard[i]:
            sequence += j
    print(*generate_letters_sequence(numbers))
