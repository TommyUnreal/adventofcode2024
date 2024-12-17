from aoc_utils.aoc_utils import current_folder, input_parser

def is_safe(i: list) -> bool:
    """Return True if numbers in list are either decreasing or increasing,
    and any two adjacent values differ by at least 1 and at most 3."""
    is_ordered = i == sorted(i) or i == sorted(i, reverse=True)
    if not is_ordered:
        return False

    adjacent_diff_valid = True
    for j in range(len(i) - 1):
        if not (1 <= abs(i[j] - i[j + 1]) <= 3):
            adjacent_diff_valid = False
            break

    return adjacent_diff_valid

def variant_is_safe(i: list) -> bool:
    """Return True if the original list or any variant by removing one element is safe."""
    if is_safe(i):
        return True

    for j in range(len(i)):
        modified_list = i.copy()
        modified_list.pop(j)
        if is_safe(modified_list):
            return True

    return False

input = input_parser(current_folder(__file__) / "input.txt")
safe_reports = [1 if variant_is_safe(i) else 0 for i in input]
result = sum(safe_reports)

print(result)

