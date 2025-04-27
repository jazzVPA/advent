import re

def extract_calibration_values(filepath: str)-> int:
    calibration_values = []
    total = 0
    try:
        with open(filepath, "r") as file:
            for line in file:
                digits = re.findall(r"\d+", line)
                if digits:
                    value= int(digits[0] + digits[-1])
                    calibration_values.append(value)
                    total += value
        print(f"Calibration values: {calibration_values}")
        print(f"sum of all the calibration values: {total}")
        return total

    except FileNotFoundError:
        print(f"File {filepath} not found")

    except PermissionError:
        print(f"File {filepath} not readable")

    except Exception as e:
        print(f"Error: {e}")
    return 0

if __name__ == "__main__":
    file_path = '2023_d01_input.txt'
    extract_calibration_values(file_path)
