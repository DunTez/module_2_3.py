my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
counter = 0
while counter < len(my_list):
    number = my_list[counter]
    counter = counter + 1
    if number == 0:
        continue
    elif number < 0:
        break
    elif counter == len(my_list):
        print(number)
    else:
        print(number)