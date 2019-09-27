import argparse
import get_data as gd
import data_viz as dv


def main():
    parser = argparse.ArgumentParser(
            description='Program that allows one to create a boxplot, ' +
                        'histogram, or combo of the two of a set of data.',
            prog='viz')

    parser.add_argument('--out_file_name',
                        type=str,
                        help='The output file name.',
                        required=True)

    parser.add_argument('--col_num',
                        type=int,
                        help='The input column.',
                        required=True)

    parser.add_argument('--plot_type',
                        type=str,
                        help='Choices are boxplot, histogram, or combo.',
                        required=True)

    args = parser.parse_args()

    out_file_name = args.out_file_name
    col_num = args.col_num
    plot_type = args.plot_type

    data = gd.read_stdin_col(col_num)

    if plot_type == "boxplot":
        dv.boxplot(data, out_file_name)
    if plot_type == "histogram":
        dv.histogram(data, out_file_name)
    if plot_type == "combo":
        dv.combo(data, out_file_name)


if __name__ == '__main__':
    main()
