import csv
from timeit import default_timer
from typing import Callable


def logging_func(func: Callable):
    def inner(*args, **kwargs):
        start_time = default_timer()
        res = func(*args, **kwargs)
        diff_time = round(default_timer() - start_time, 3)
        print(f"func '{func.__name__}', running time - {diff_time:.3f} sec")
        return res

    return inner

@logging_func
def add_id_in_csv_file(filename):
    with open(filename, "r", encoding="utf-8") as infile:
        csv_dct = csv.DictReader(infile)
        output_lst = []
        for indx, row in enumerate(csv_dct):
            row.update({"id": indx + 1})
            output_lst.append(row)
    with open("index_" + filename, "w", encoding="utf-8") as outfile:
        fieldnames = list(output_lst[0].keys())
        fieldnames = [fieldnames[-1]] + fieldnames[:-1]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_lst)


def main():
    add_id_in_csv_file("users.csv")
    add_id_in_csv_file("likes.csv")


if __name__ == '__main__':
    main()
