with open("input.txt", "r") as f:
    content = f.readlines()

    current_depth = int(content[0].strip())
    depth_increases = 0

    for measure in content[1:]:
        measure = int(measure.strip())

        if current_depth < measure:
            depth_increases += 1

        current_depth = measure

    print(depth_increases)
