from aoc_utils.aoc_utils import current_folder, input_parser

input = input_parser(current_folder(__file__) / "input.txt")
left_list = [i[0] for i in input]
right_list = [i[1] for i in input]
result = sum(n * right_list.count(n) for n in left_list)

print(result)