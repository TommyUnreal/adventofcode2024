from pathlib import Path
import re

def current_folder(file) -> Path:
    """Return the path to the parent folder.

    Args:
        file (str): The path to the running py file.

    Returns:
        os.Path: Path to the parent folder.
    """
    return Path(file).parent


def input_parser(file_path: Path) -> list:
    """
    Parse a text file into a list of lists, separating each line by whitespace
    and attempting to guess the type of each value (int or str).

    Args:
        file_path (Path): The path to the input text file.

    Returns:
        list[list]: A list of lists containing parsed values with guessed types.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    parsed_data = []

    with file_path.open('r', encoding='utf-8') as file:
        for line in file:
            elements = line.strip().split()
            parsed_line = [try_parse(item) for item in elements]
            parsed_data.append(parsed_line)

    return parsed_data


def try_parse(value):
    """
    Try to parse a string value as an integer. Fall back to the string type if parsing fail.

    Args:
        value (str): The value to parse.

    Returns:
        int | str: Parsed integer or the original string.
    """
    try:
        return int(value)
    except ValueError:
        return str(value)


def extract_ints(s: str) -> list:
    """Extract  integers from a string."""
    return [int(match) for match in re.findall(r'\d+', s)]