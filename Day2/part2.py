with open("input.txt", "r") as f:
    content = f.readlines()

    h_position = 0
    depth = 0
    aim = 0

    for move in content:
        move = move.rstrip()
        order, n = move.split()
        n = int(n)

        if order == "forward":
            h_position += n
            depth += n * aim
        elif order == "up":
            aim -= n
        elif order == "down":
            aim += n

    print(h_position, depth)
