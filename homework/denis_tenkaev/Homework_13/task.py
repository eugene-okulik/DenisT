import os
import datetime as dt

my_base_path = os.path.dirname(__file__)
base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
datafile_path = os.path.join(base_path, "eugene_okulik", "hw_13", "data.txt")


def read_task():
    with open(datafile_path, encoding="utf-8") as task_file:
        for string in task_file:
            yield string.split()


for line in read_task():
    if line[0] == "1.":
        data1 = dt.datetime.strptime(
            f"{line[1]} {line[2]}", "%Y-%m-%d %H:%M:%S.%f"
        )
        data1 = data1 + dt.timedelta(days=7)
        print(data1)

    elif line[0] == "2.":
        data2 = dt.datetime.strptime(
            f"{line[1]} {line[2]}", "%Y-%m-%d %H:%M:%S.%f"
        )
        print(data2.strftime("%A"))

    elif line[0] == "3.":
        data3 = dt.datetime.strptime(
            f"{line[1]} {line[2]}", "%Y-%m-%d %H:%M:%S.%f"
        )
        data3 = dt.datetime.now() - data3
        print(data3.days)
