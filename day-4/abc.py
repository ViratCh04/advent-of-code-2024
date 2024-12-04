def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    item = 'XMAS'
    total = 0
    
    # Horizontal check
    for line in grid:
        for i in range(len(line) - len(item) + 1):
            if item == line[i:i+len(item)]:
                total += 1
            if item == line[i:i+len(item)][::-1]:
                total += 1
                
    # Vertical check
    for col in range(cols):
        vert_str = ''.join(grid[row][col] for row in range(rows))
        for i in range(len(vert_str) - len(item) + 1):
            if item == vert_str[i:i+len(item)]:
                total += 1
            if item == vert_str[i:i+len(item)][::-1]:
                total += 1
                
    # Diagonal checks
    for row in range(rows - len(item) + 1):
        for col in range(cols - len(item) + 1):
            # Forward diagonal
            diag_str = ''.join(grid[row+i][col+i] for i in range(len(item)))
            if item == diag_str:
                total += 1
            # Backward diagonal
            if col >= len(item) - 1:
                diag_str = ''.join(grid[row+i][col-i] for i in range(len(item)))
                if item == diag_str:
                    total += 1
    
    return total

grid = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

print(f"Total XMAS occurrences: {count_xmas(grid)}")