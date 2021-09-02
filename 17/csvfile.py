"""
130. Working with CSV Files in Python
"""
from csv import reader, writer

if __name__ == "__main__":
    with open("../tmp/example.csv", encoding="utf-8") as data:
        csv_data = reader(data)
        data_lines = list(csv_data)
    json_data = []
    for line in data_lines[1:]:
        data = {}
        for num, key in enumerate(data_lines[0]):
            data[key] = line[num]
        data["fullname"] = f"{line[1]} {line[2]}"
        json_data.append(data)
    print(json_data)
    with open(
        "../tmp/to_save_file.csv", mode="w", newline="", encoding="utf-8"
    ) as file_to_output:
        csv_writer = writer(file_to_output, delimiter=",")
        csv_writer.writerow(["a", "b", "c"])
        csv_writer.writerows([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
