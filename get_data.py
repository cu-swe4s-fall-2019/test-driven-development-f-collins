import sys

def read_stdin_col(col_num):
    if col_num == None:
        return None

    data = []
    for line in sys.stdin.readlines():
        try:
            data.append(float(line.rstrip().split(' ')[col_num]))
        except IndexError:
            print("Attempt to access column that does not exist, quitting.")
            sys.exit(1)

    return data
