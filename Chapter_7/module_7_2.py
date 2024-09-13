from typing import List, Dict, Tuple

from typing import List, Dict, Tuple


def write_lines(file, lines: List[str]) -> Dict[Tuple[int, int], str]:
    positions: Dict[Tuple[int, int], str] = {}

    for line_number, line in enumerate(lines, start=1):
        byte_position = file.tell()
        file.write(line + '\n')
        positions[(line_number, byte_position)] = line

    return positions


def custom_write(file_name: str, strings: List[str]) -> Dict[Tuple[int, int], str]:
    with open(file_name, 'w', encoding='utf-8') as file:
        return write_lines(file, strings)


def main():
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]
    result = custom_write('test.txt', info)
    for elem in result.items():
        print(elem)


if __name__ == '__main__':
    main()
