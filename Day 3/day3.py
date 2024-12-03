import re


def part_one():
    pattern = r"mul\((\d+),(\d+)\)"
    with open("day3.input") as f:
        text = f.read()

    matches = re.findall(pattern, text)
    sum = 0
    for num in matches:
        sum += mul(num)
    print("Part One:", sum)


def part_two():
    pattern = r"mul\((\d+),(\d+)\)"
    with open("day3.input") as f:
        data = f.read().split("do()")
    mult = []
    for text in data:
        new = text.split("don't()")
        mult.append(new[0])
    matches = re.findall(pattern, "".join(mult))
    sum = 0
    for match in matches:
        sum += mul(match)
    print("Part Two:", sum)


def mul(mult):
    x, y = mult
    return int(x) * int(y)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
