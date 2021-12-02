with open("input.txt", "r") as f:
    content = f.readlines()

    current_depth = (
        int(content[0].strip()) + int(content[1].strip()) + int(content[2].strip())
    )
    depth_increases = 0

    for measure in content[1:-2]:
        pass

    a = [1, 2, 3, 4, 5]
    for i in range(1, len(content[:-2])):
        measure = 0

        for j in range(i, i + 3):
            measure += int(content[j].strip())

        if current_depth < measure:
            depth_increases += 1

        current_depth = measure

    print(depth_increases)
