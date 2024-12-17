from pathlib import Path

def current_folder(file) -> Path:
    """Return

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
    Tries to parse a string value as an integer. Falls back to the original string if parsing fails.

    Args:
        value (str): The value to parse.

    Returns:
        int | str: Parsed integer or the original string.
    """
    try:
        return int(value)
    except ValueError:
        return str(value)