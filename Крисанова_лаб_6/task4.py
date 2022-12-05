import json
INPUT_FILE = "input.csv"
def csv_to_list_dict(filename) -> list[dict]:
    with open(filename, "r") as f:
        headers = f.readline().split(",")
        headers[-1] = headers[-1].replace("\n", "")
        json_file = []
        for line in f:
            line = line.replace("\n", "")
            line1 = line.split(",")
            json_file.append(dict(zip(headers, line1)))
        if not isinstance(json_file, list):
            raise TypeError(f"У переменной json_file должен быть тип list, не {type(json_file)}")
    return json_file      # TODO реализовать конвертер из csv в json
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
