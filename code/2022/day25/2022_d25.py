from dec_to_SNAFU_conversion import convert_dec_to_SANFU


def convert_full_file_to_SNAFU(filepath: str):

    data_list = []

    try:
        with open(filepath, mode='r') as file:
            for line in file:
                number = int(line)
                SNAFU = convert_dec_to_SANFU(number)
                data_list.append([number, SNAFU])
        return data_list
    except FileNotFoundError:
        print(f"File {filepath} not found")


if __name__ == '__main__':
    data = convert_full_file_to_SNAFU('2022_d25_input.txt')

    # Print headers
    print(f"{'decimal':<10} {'SNAFU':<10}")

    # Print each row
    for a, b in data:
        print(f"{a:<10} {b:<10}")

    #print(convert_full_file_to_SNAFU('input.txt'))

