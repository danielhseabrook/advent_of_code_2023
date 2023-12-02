import re
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
letter_numbers = {
    "one" : "1",
    "two" : "2",
    "three": "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9"
}
with open ("puzzle_input.txt", "r") as file:
    data = file.readlines()

calibration_values_raw = []
calibration_values = []

for line in data:
    char_number = ""
    split_line = re.findall('(\d+|[A-Za-z]+)', line)
    # print(split_line)

    for segment in split_line:
        for key in letter_numbers:
            if key in segment:
                char_number += str(letter_numbers.get(key))
        for number in segment:
            if number in letter_numbers.values():
                char_number += number

    with open ("calibration_values_raw.txt", "a") as file:
        file.write(f'{char_number}\n')
    calibration_values_raw.append(char_number)

    # for char in line:
        # if segmentiter in numbers:
        # char_number += str(char)

for v in calibration_values_raw:
    if len(v) > 2:
        value = v[0] + v[-1]
    elif len(v) == 1:
        value = v[0] + v[0]
    else:
        value = v
    calibration_values.append(int(value))

    with open ("result_test.txt", "a") as file:
        file.write(f'{value}\n')

print(sum(calibration_values))
