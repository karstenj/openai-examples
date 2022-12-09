def solve_anagrams(puzzle_input: str) -> set[str]:
    result = set()
    if len(puzzle_input) == 1:
        result.add(puzzle_input)
    else:
        for i, c in enumerate(puzzle_input):
            for anagram in solve_anagrams(puzzle_input[:i] + puzzle_input[i+1:]):
                result.add(c + anagram)
    return result