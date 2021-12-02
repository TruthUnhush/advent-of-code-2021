with open("input.txt", "r") as f:
    content = f.readlines()

    h_position = 0
    depth = 0

    for move in content:
        move = move.rstrip()
        order, n = move.split()
        n = int(n)

        if order == "forward":
            h_position += n
        elif order == "up":
            depth -= n
        elif order == "down":
            depth += n

    print(h_position, depth)
