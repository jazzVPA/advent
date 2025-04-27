MAX_CUBES = {
    'blue': 14,
    'green': 13,
    'red': 12,
}

def get_game_id_and_color_sets(line: str) -> tuple[int, list[dict[str, int]]]:
    game_id_section, color_sets_section = line.split(':')
    game_id = int(game_id_section.split()[1])
    color_sets = color_sets_section.strip().split(";")

    revealed_colors_sets = []
    for color_set in color_sets:
        color_cubes = color_set.strip().split(",")
        color_cubes_dict = {}
        for color_cube in color_cubes:
            count, color = color_cube.split()
            color_cubes_dict[color] = int(count) # {'blue': 3}
        revealed_colors_sets.append(color_cubes_dict) # [{'blue': 3, 'red': 4}, {'red': 1, 'green': 2, 'blue': 6}, {'green': 2}])
    return game_id, revealed_colors_sets

def check_game_possible(revealed_colors_sets: list[dict[str, int]], max_cubes: dict[str, int]) -> bool:
    for cube_set in revealed_colors_sets:
        for color, count in cube_set.items():
            if count > max_cubes.get(color, 0):
                return False
    return True

def read_file_find_total(filepath: str) -> int:

    total = 0
    try:
        with open(filepath, 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                game_id, revealed_colors_sets = get_game_id_and_color_sets(line)
                if check_game_possible(revealed_colors_sets, MAX_CUBES):
                    total += game_id
        return total

    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return 0

    except Exception as e:
        print(f"Error processing file '{filepath}': {e}")
        return 0


if __name__ == '__main__':
    result = read_file_find_total("2023_d02_input.txt")
    print("Sum of the IDs of those games is", result)