def main():
    inc: int = 0
    for i in range(5):
        while True:
            try:
                inc += int(input(f'Enter int #{i + 1}: '))
                break
            except ValueError:
                pass

    print(f'Sum: {inc}')
    return


main()
