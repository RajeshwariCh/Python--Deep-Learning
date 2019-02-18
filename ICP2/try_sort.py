data_list = ["1", "4", "0", "6", "9"]
new_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)
print(str(new_list)[1:-1])

