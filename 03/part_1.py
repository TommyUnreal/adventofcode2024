from aoc_utils.aoc_utils import current_folder, input_parser, extract_ints
import re

def find_mul_matches(s: str):
    """Return a list of matches in the format 'mul(x, y)' from the input."""
    pattern = r"mul\(\d+,\d+\)"
    return re.findall(pattern, s)

def execute_mul(s: str) -> int:
    """Finds all mul(x, y) in the string, performs the multiplication, and returns their sum."""
    matches = find_mul_matches(s)
    total_sum = 0

    for match in matches:
        x, y = tuple(extract_ints(match))
        total_sum += x * y

    return total_sum

input = input_parser(current_folder(__file__) / "input.txt")
uncorrupted_muls = [execute_mul(str(s)) for s in input]
print(uncorrupted_muls)
result = sum(uncorrupted_muls)

print(result)

