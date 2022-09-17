import json

from constants import USER_DATA_FILE


def get_file_data():
    with open("user_data.json") as file_cursor:
        file_data = json.load(file_cursor)
        return file_data


def write_to_file(file_data):
    with open("user_data.json", "w") as file_cursor:
        json.dump(file_data, file_cursor)

