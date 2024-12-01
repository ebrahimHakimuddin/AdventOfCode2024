def part_one():
    with open("day1.input") as f:
        data = f.read().strip().split()
    left, right = [], []
    for i in range(len(data)):
        if i % 2 != 0:
            left.append(int(data[i]))
        else:
            right.append(int(data[i]))
    left.sort()
    right.sort()
    dist = 0
    for i in range(min(len(left), len(right))):
        dist += abs(left[i] - right[i])
    print(dist)


def part_two():
    with open("day1.input") as f:
        data = f.read().strip().split()
    left, right = [], []
    for i in range(len(data)):
        if i % 2 != 0:
            left.append(int(data[i]))
        else:
            right.append(int(data[i]))
    left.sort()
    right.sort()
    similarity = 0
    for i in range(min(len(left), len(right))):
        similarity += left[i] * right.count(left[i])
    print(similarity)


def main():
    part_one()
    part_two()


if __name__ == "__main__":
    main()
