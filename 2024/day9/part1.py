def parse_input(file_path):
    with open(file_path, 'r') as file:
        return list(map(int, file.read().strip()))

def create_individual_blocks(disk_map):
    blocks = []
    file_id = 0

    for i, length in enumerate(disk_map):
        if i % 2 == 0:
            blocks.extend([file_id] * length)
            file_id += 1
        else:
            blocks.extend(['.'] * length)

    return blocks

def compact_blocks(blocks):
    while True:
        first_free_space = blocks.index('.') if '.' in blocks else -1
        # No free spaces remain
        if first_free_space == -1:
            break

        last_file_pos = len(blocks) - 1
        while last_file_pos >= 0 and blocks[last_file_pos] == '.':
            last_file_pos -= 1

        # All file blocks are already compacted
        if last_file_pos <= first_free_space:
            break

        # Move the last file block to the first gap
        blocks[first_free_space], blocks[last_file_pos] = blocks[last_file_pos], '.'

    return blocks

def calculate_checksum(compacted_blocks):
    res = 0
    for idx, file_id in enumerate(compacted_blocks):
        if file_id != '.':
            res += idx * file_id
    return res
    # return sum(idx * file_id for idx, file_id in enumerate(compacted_blocks) if file_id != '.')

def main(file_path):
    disk_map = parse_input(file_path)
    blocks = create_individual_blocks(disk_map)
    compacted_blocks = compact_blocks(blocks)
    print(calculate_checksum(compacted_blocks))

if __name__ == "__main__":
    main("2024/inputs/day9.txt")