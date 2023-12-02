import re
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

    for segment in split_line:
        seg_dict = {}
        sorted_seg_dict = {}

        for key in letter_numbers:
            indexes = [i.start() for i in re.finditer(key, segment)]

            for _ in indexes:
                seg_dict[_] = letter_numbers[key]

        for value in letter_numbers.values():
            indexes = [i.start() for i in re.finditer(value, segment)]

            for _ in indexes:
                seg_dict[_] = value

        sorted_seg_dict = dict(sorted(seg_dict.items()))

        for value in sorted_seg_dict.values():
            char_number += value

    if char_number not in '':
        calibration_values_raw.append(char_number)

for v in calibration_values_raw:
    if len(v) > 2:
        value = v[0] + v[-1]
    elif len(v) == 1:
        value = v[0] + v[0]
    else:
        value = v
    calibration_values.append(int(value))

print(sum(calibration_values))
