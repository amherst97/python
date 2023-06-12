import csv
import sys


def process(filename):
    print(filename)
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print('insert into employee values({}, "{}", "{}", {});'.format(
                row['emp_id'], row['emp_name'], row['dept_name'], row['salary']))


if __name__ == '__main__':
    process(sys.argv[1])
