import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=",", new_line="\n") -> list[dict]:
    with open(filename) as file_csv:  # TODO реализовать конвертер из csv в json
        columns = file_csv.readline().strip(new_line).split(delimiter)
        list_ = []
        for index, line in enumerate(file_csv):
            line_in_list = line.strip(new_line).split(delimiter)
            list_.extend([{f'{columns[i]}': n for i, n in enumerate(line_in_list)}])
    return list_


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
