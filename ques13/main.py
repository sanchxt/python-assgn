def main():
    with open('idk.txt', 'rb') as file:
        initial_pos = file.tell()
        print(f'Initial cursor position: {initial_pos}')

        file.seek(3)
        print(f'5 characters from position 4: {file.read(5).decode("utf-8")}')

        file.seek(10, 1)
        print(f'Current cursor position: {file.tell()}')

        print(f'Next 10 characters: {file.read(10).decode("utf-8")}')


if __name__ == '__main__':
    main()
