import csv
from random import choice


word_map = {}

if __name__ == "__main__":
    print('Create translation questions')
    total = 5
    count = 0
    with open('translation.csv', 'r') as f:
        file_reader = csv.reader(f, skipinitialspace=True)
        for row in file_reader:
            word_map[row[0]] = row[1]
    print(word_map)

    t = input('How many words should we test?')
    total = int(t)
    count = 0
    correct = 0
    for i in range(total):
        count = count + 1
        key_list = list(word_map.keys())
        key = choice(key_list)
        word = word_map.pop(key)
        print(f'{count}. {key}')
        answer = input('In English: ')

        if answer.strip().lower() == word.strip().lower():
            print('Correct!!')
            correct = correct + 1
        else:
            print('Wrong!!', word)

    print(f'Total {total} questions, you got {correct} correct - {correct/total*100.0}%. Congratulations!!')


