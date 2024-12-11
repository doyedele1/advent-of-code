def parse_input(file_path):
    return [list(map(int, line.strip())) for line in open(file_path)]

def find_trailheads(grid):
    trailheads = []

    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == 0:
                trailheads.append((r, c))
    return trailheads

def is_valid_move(grid, r, c, curr_height):
    m, n = len(grid), len(grid[0])
    return 0 <= r < m and 0 <= c < n and grid[r][c] == curr_height + 1

def dfs(grid, trailhead):
    stack = [trailhead]
    visited = set()
    reachable_nines = 0

    while stack:
        r, c = stack.pop()

        visited.add((r, c))

        if grid[r][c] == 9:
            reachable_nines += 1
        
        if is_valid_move(grid, r - 1, c, grid[r][c]):
            stack.append((r - 1, c))
        if is_valid_move(grid, r + 1, c, grid[r][c]):
            stack.append((r + 1, c))
        if is_valid_move(grid, r, c - 1, grid[r][c]):
            stack.append((r, c - 1))
        if is_valid_move(grid, r, c + 1, grid[r][c]):
            stack.append((r, c + 1))
    return reachable_nines

def main(file_path):
    grid = parse_input(file_path)
    trailheads = find_trailheads(grid)
    
    count = 0
    for trailhead in trailheads:
        count += dfs(grid, trailhead)
    print(count)

if __name__ == "__main__":
    main("2024/inputs/day10.txt")