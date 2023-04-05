import threading
import multiprocessing

from utilitas import add_id_in_csv_file, logging_func


@logging_func
def consistent_running(args):
    for arg in args:
        add_id_in_csv_file(arg)


@logging_func
def threading_running(args):
    for arg in args:
        thread = threading.Thread(target=add_id_in_csv_file, args=(arg,))
        thread.start()
    thread.join()


@logging_func
def multiprocessing_running(args):
    for arg in args:
        process = multiprocessing.Process(target=add_id_in_csv_file, args=(arg,))
        process.start()
    process.join()


def main():
    args = ("users.csv", "likes.csv", "posts.csv", "comments.csv")
    consistent_running(args)
    print()
    threading_running(args)
    print()
    multiprocessing_running(args)


if __name__ == "__main__":
    main()
