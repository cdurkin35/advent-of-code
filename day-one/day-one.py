def find_all_substring(string, substring):
    indicies = []
    index = string.find(substring)
    while index != -1:
        indicies.append(index)
        index = string.find(substring, index + 1)
    return indicies


def main():
    word_to_int = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
    }
    input_file = open("input.txt", "r")
    lines = input_file.readlines()
    input_file.close()
    sum = 0
    for line in lines:
        indicies = []
        digits = []
        for key, value in word_to_int.items():
            temp_indicies = find_all_substring(line, key)
            for index in temp_indicies:
                digits.append(value)
                indicies.append(index)
        first_digit = digits[indicies.index(min(indicies))]
        second_digit = digits[indicies.index(max(indicies))]
        sum += first_digit * 10 + second_digit

    print(sum)


if __name__ == "__main__":
    main()
