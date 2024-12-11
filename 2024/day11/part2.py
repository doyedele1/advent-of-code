import math
from collections import Counter

def parse_input(file_path):
    with open(file_path, 'r') as file:
        return list(map(int, file.readline().strip().split()))

def split_number(num):
    n = num and int(math.log10(num) + 1)
    
    if n % 2 == 0:
        left = num // 10 ** (n // 2)
        right = num % 10 ** (n // 2)
    
    # num_str = str(num)
    # mid = len(num_str) // 2
    # left = int(num_str[:mid])
    # right = int(num_str[mid:])
    return left, right

def process_stone(stone, memo):
    if stone in memo:
        return memo[stone]

    if stone == 0:
        result = [1]
    elif len(str(stone)) % 2 == 0:
        result = list(split_number(stone))
    else:
        result = [stone * 2024]

    memo[stone] = result
    return result

def process_stones_count(stone_counts, memo):
    new_counts = Counter()
    for stone, count in stone_counts.items():
        processed_stones = process_stone(stone, memo)
        for new_stone in processed_stones:
            new_counts[new_stone] += count
    return new_counts

def count_stones_after_blinks(initial_stones, num_blinks):
    stone_counts = Counter(initial_stones)
    memo = {}

    for _ in range(num_blinks):
        stone_counts = process_stones_count(stone_counts, memo)

    return sum(stone_counts.values())

def main(file_path):
    initial_stones = parse_input(file_path)
    result = count_stones_after_blinks(initial_stones, 75)
    print(result)

if __name__ == "__main__":
    main("2024/inputs/day11.txt")