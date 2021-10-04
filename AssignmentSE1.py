

def find_divisible_in_1000_nums(num1, num2, list):
    for x in range(1000):
        if x % num1 == 0 or x % num2 == 0:
            if x == 0:
                continue
            list.append(x)

    for i in num_list:
        if i < 999:
            print('{}'.format(i) + " +", end=" " )
        else:
            continue
    return (print('{}'.format(i) + " = " + str(sum(list))))

print("The numbers are: ", end=" ")
num_list = []
find_divisible_in_1000_nums(3, 5, num_list)
