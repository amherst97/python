## calculate how many unique 4-digit numbers, using each following number only once
## 0 1 2 3 4
## Expected counts: 4 x 4 x 3 X 2
from collections import Counter


def contain_others(array):
    if '5' in array:
        return True
    if '6' in array:
        return True
    if '7' in array:
        return True
    if '8' in array:
        return True
    if '9' in array:
        return True
    return False


def has_duplicate(array):
    counter = Counter(array)
    for value in counter.values():
        if value > 1:
            return True

    return False


def main():
    smallest = 1000
    biggest = 9999
    result = 0

    for i in range(smallest, biggest+1):
        array = list(str(i))
        if contain_others(array) or has_duplicate(array):
            # print("exclude", "".join(array))
            pass
        else:
            print("include ", "".join(array))
            result = result + 1

    print("The total number is ", result)


if __name__ == '__main__':
    main()

