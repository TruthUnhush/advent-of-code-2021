def binaryToDecimal(binary):

    binary = int(binary)
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1

    return decimal


with open("input.txt", "r") as f:
    content = f.readlines()

    my_binaries = {f"b{i}": 0 for i in range(1, 13)}

    for b_number in content:

        for i, element in enumerate(my_binaries):

            if b_number[i] == "1":
                my_binaries[element] += 1

    gamma_rate = ""
    epsilon_rate = ""

    for value in my_binaries.values():

        if value > 500:
            gamma_rate = gamma_rate + "1"
            epsilon_rate = epsilon_rate + "0"
        else:
            gamma_rate = gamma_rate + "0"
            epsilon_rate = epsilon_rate + "1"

    print(binaryToDecimal(gamma_rate) * binaryToDecimal(epsilon_rate))
