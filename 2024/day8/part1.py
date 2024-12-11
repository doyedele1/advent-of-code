from collections import defaultdict
from itertools import combinations

def process_input_and_save_antennas_locations(file_path):
    with open(file_path, "r") as file:
        grid = [line.strip() for line in file]

    antennas_with_their_locations = defaultdict(set)
    
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell != '.':
                antennas_with_their_locations[cell].add((r, c))
    
    return grid, antennas_with_their_locations

def find_pair_antinodes(grid, pair):
    (r1, c1), (r2, c2) = pair
    diff_r, diff_c = r2 - r1, c2 - c1
    m, n = len(grid), len(grid[0])

    antinodes = {
        (r1 - diff_r, c1 - diff_c),
        (r2 + diff_r, c2 + diff_c)
    }
    
    valid_antinodes = set()
    for r, c in antinodes:
        if 0 <= r < m and 0 <= c < n:
            valid_antinodes.add((r,c))
    return valid_antinodes

def find_all_antinodes(grid, antennas_locations):
    all_antinodes = set()
    
    for antenna, locations in antennas_locations.items():
        for pair in combinations(locations, 2):
            all_antinodes.update(find_pair_antinodes(grid, pair))
    
    return all_antinodes

def main(file_path):
    grid, antennas_locations = process_input_and_save_antennas_locations(file_path)
    antinodes = find_all_antinodes(grid, antennas_locations)
    
    print(len(antinodes))

if __name__ == "__main__":
    main("2024/inputs/day8.txt")