# This solution is a very slightly modification form https://github.com/LoicH/coding_challenges/blob/main/advent_of_code_2021/3.py


def binaryToDecimal(binary):

    return sum([int(bit) * 2 ** i for i, bit in enumerate(binary[::-1])])


def partition_numbers(numbers, pos):
    partition = {"0": [], "1": []}
    one_count = 0
    for bits in numbers:
        one_count += int(bits[pos])
        partition[bits[pos]].append(bits)
    if one_count >= len(numbers) / 2:
        return partition["1"], partition["0"]
    else:
        return partition["0"], partition["1"]


def part2(data):
    dominant, minority = partition_numbers(data, 0)
    pos = 1
    while len(dominant) > 1:
        dominant = partition_numbers(dominant, pos)[0]
        pos += 1
    oxygen = binaryToDecimal(dominant[0])
    pos = 1
    while len(minority) > 1:
        minority = partition_numbers(minority, pos)[1]
        pos += 1

    co2 = binaryToDecimal(minority[0])
    return oxygen * co2


with open("input.txt", "r") as fp:
    data = [line.rstrip() for line in fp.readlines()]


print(part2(data))
