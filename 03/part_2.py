from aoc_utils.aoc_utils import current_folder, input_parser, extract_ints
import re

def part_2(string):
    pattern = r"do\(\)|don't\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)"
    regex_expr = re.compile(pattern)

    result = 0
    enabled = True

    for match in re.finditer(regex_expr, string):
        if match.group(0) == "do()":
            enabled = True
            continue
        if match.group(0) == "don't()":
            enabled = False
            continue
        if enabled:
            numbers = [int(_) for _ in match.group(0)[4:-1].split(",")]
            result += numbers[0] * numbers[1]

    return result

def find_mul_matches(s: str):
    """Return a list of matches in the format 'mul(x, y)' from the input."""
    pattern = r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)"
    return re.findall(pattern, s)

def execute_mul(s: str) -> int:
    """Finds all mul(x, y) in the string, performs the multiplication, and returns their sum."""
    matches = find_mul_matches(s)
    total_sum = 0
    enabled = True

    for match in matches:
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
        else:
            if enabled:
                x, y = tuple(extract_ints(match))
                total_sum += x * y

    return total_sum

input = input_parser(current_folder(__file__) / "input.txt")
uncorrupted_muls = "".join([(str(s)) for s in input])
result = execute_mul(uncorrupted_muls)

print(result)

