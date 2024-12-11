import math

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

def process_stone(stone):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        return list(split_number(stone))
    else:
        return [stone * 2024]

def process_stones(stones):
    new_stones = []
    for stone in stones:
        new_stones.extend(process_stone(stone))
    return new_stones

def count_stones_after_blinks(initial_stones, num_blinks):
    stones = initial_stones
    for _ in range(num_blinks):
        stones = process_stones(stones)
    return len(stones)

def main(file_path):
    initial_stones = parse_input(file_path)
    result = count_stones_after_blinks(initial_stones, 25)
    print(result)

if __name__ == "__main__":
    main("2024/inputs/day11.txt")