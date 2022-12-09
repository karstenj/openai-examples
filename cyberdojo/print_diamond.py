def solve_print_diamond(puzzle_input: str) -> str:
    result = ""
    for i in range(ord(puzzle_input) - ord('A') + 1):
        result += " " * (ord(puzzle_input) - ord('A') - i)
        result += chr(ord('A') + i)
        result += " " * (2 * i - 1)
        if i > 0:
            result += chr(ord('A') + i)
        result += "\n"
    for i in range(ord(puzzle_input) - ord('A') - 1, -1, -1):
        result += " " * (ord(puzzle_input) - ord('A') - i)
        result += chr(ord('A') + i)
        result += " " * (2 * i - 1)
        if i > 0:
            result += chr(ord('A') + i)
        result += "\n"
    return result