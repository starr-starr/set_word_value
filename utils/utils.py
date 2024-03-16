import json


def process_file_path(path):
    if not path.endswith("\\"):
        path += "\\"
    return path


def load_json():
    with open("config/config.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
