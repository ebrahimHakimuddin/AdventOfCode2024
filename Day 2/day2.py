def part_one():
    with open("day2.input") as f:
        data = f.readlines()

    safe_count = 0

    for line in data:
        numbers = list(map(int, line.strip().split()))
        if not numbers:
            continue

        is_safe = True
        prev_diff = 0

        for i in range(len(numbers) - 1):
            diff = numbers[i] - numbers[i + 1]

            if numbers[i] == numbers[i + 1]:
                is_safe = False
                break

            if (prev_diff >= 0 and diff >= 0) or (prev_diff <= 0 and diff <= 0):
                if 1 <= abs(diff) <= 3:
                    prev_diff = diff
                else:
                    is_safe = False
                    break
            else:
                is_safe = False
                break

        if is_safe:
            safe_count += 1

    print("Part One:", safe_count)


def part_two():
    with open("day2.input") as f:
        data = f.readlines()

    safe_count = 0

    for line in data:
        numbers = list(map(int, line.strip().split()))
        if not numbers:
            continue

        is_safe = True
        prev_diff = 0
        fail_count = 0

        for i in range(len(numbers) - 1):
            diff = numbers[i] - numbers[i + 1]

            if numbers[i] == numbers[i + 1]:
                fail_count += 1
                if fail_count > 1:
                    is_safe = False
                    break
                continue

            if (prev_diff >= 0 and diff >= 0) or (prev_diff <= 0 and diff <= 0):
                if 1 <= abs(diff) <= 3:
                    prev_diff = diff
                else:
                    fail_count += 1
                    if fail_count > 1:
                        is_safe = False
                        break
            else:
                fail_count += 1
                if fail_count > 1:
                    is_safe = False
                    break

        if is_safe:
            safe_count += 1

    print("Part Two:", safe_count)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
