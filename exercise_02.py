def get_combined_dict(my_dict_1, my_dict_2):
    locDict = {}
    for k, v in my_dict_1.items():
        if k in my_dict_2:
            locDict[k] = my_dict_1[k] + my_dict_2[k]

    return locDict


def main():
    my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
    my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
    combined_dict = get_combined_dict(my_dict_1, my_dict_2)
    print(combined_dict)
    return


main()
