
def calculate_total_distance(filepath: str)-> int:

    left_numbers = []
    right_numbers = []

    try:
        with open (filepath, 'r') as file:
            for line in file:
                file_contents = line.strip().split()
                if len(file_contents) >= 2:
                    left_numbers.append(int(file_contents[0]))
                    right_numbers.append(int(file_contents[1]))

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return 0

    except ValueError:
         print(f"Error: Non-integer value found in file '{filepath}'.")
         return 0

    left_sorted = sorted(left_numbers)
    right_sorted = sorted(right_numbers)

    total_distance = sum(abs(l-r) for l,r in zip(left_sorted, right_sorted))
    return total_distance


if __name__ == "__main__":
    print("Total distance:",calculate_total_distance('input.txt'))
