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

def find_files(blocks):
    # Store all the files in a dictionary that contains the file's ID, starting position, and length
    files = {}
    for i, block in enumerate(blocks):
        if block == '.':
            continue

        if block not in files:
            files[block] = {"id": block, "start": i, "length": 1}
        else:
            files[block]["length"] += 1

    return sorted(files.values(), key=lambda x: x["id"], reverse=True)

def find_free_space(blocks, start, length):
    """
    Finds the leftmost span of free space that can fit the given file.
    - Searches from the beginning of the disk to the given start position.
    """
    current_length = 0
    current_start = -1

    for i in range(start):
        if blocks[i] == '.':
            if current_start == -1:
                current_start = i
            current_length += 1

            if current_length == length:
                return current_start
        else:
            current_length = 0
            current_start = -1

    return -1

def move_file(blocks, file, new_start):
    """
    Moves a file to the new starting position.
    - Clears the original file position and sets the file blocks at the new position.
    """
    for i in range(file["start"], file["start"] + file["length"]):
        blocks[i] = '.'

    for i in range(file["length"]):
        blocks[new_start + i] = file["id"]
        
def compact_blocks(blocks):
    files = find_files(blocks)
    
    for file in files:
        free_space = find_free_space(blocks, file["start"], file["length"])

        if free_space != -1:
            move_file(blocks, file, free_space)
    return blocks

def calculate_checksum(compacted_blocks):
    return sum(idx * file_id for idx, file_id in enumerate(compacted_blocks) if file_id != '.')

def main(file_path):
    disk_map = parse_input(file_path)
    blocks = create_individual_blocks(disk_map)
    compacted_blocks = compact_blocks(blocks)
    print(calculate_checksum(compacted_blocks))

if __name__ == "__main__":
    main("2024/inputs/day9.txt")