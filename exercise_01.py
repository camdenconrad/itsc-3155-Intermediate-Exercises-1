def get_unique_list(my_list):
    locList = []

    for item in my_list:
        if locList.count(item) < 1:
            locList.append(item)

    return locList


def main():
    my_list = [1, 2, 3, 2, 1, 4]
    unique_list = get_unique_list(my_list)
    print(unique_list)


main()
