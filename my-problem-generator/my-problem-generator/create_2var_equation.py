from random import seed
from random import randint
from datetime import datetime

# seed random generator
seed(datetime.now())


def print_equation(co_x, co_y, result, revert=False):
    if revert:
        # put Y first
        if co_x < 0:
            eq_str = f'{co_y}Y - {-co_x}X = {result}'
        else:
            eq_str = f'{co_y}Y + {co_x}X = {result}'
    else:
        if co_y < 0:
            eq_str = f'{co_x}X - {-co_y}Y = {result}'
        else:
            eq_str = f'{co_x}X + {co_y}Y = {result}'

    # make it as conventional equation format
    eq_str = eq_str.replace(' 1X', ' X').replace(' 1Y', ' Y').replace('-1X', '-X').replace('-1Y', '-Y')
    return eq_str


def generate_equation(start_range, end_range, result_file):
    x = randint(start_range, end_range)
    y = randint(start_range, end_range)
    co1_x = randint(start_range, end_range)
    co1_y = randint(start_range, end_range)
    co2_x = randint(start_range, end_range)
    co2_y = randint(start_range, end_range)

    # if one of coefficient is 0, skip this equation
    if co1_x * co1_y * co2_x * co2_y == 0:
        return False

    eq1 = print_equation(co1_x, co1_y, co1_x * x + co1_y * y, False)
    eq2 = print_equation(co2_x, co2_y, co2_x * x + co2_y * y, True)
    print(eq1)
    print(eq2)
    print(f'X={x}, Y={y}', file=result_file)
    print(eq1, file=result_file)
    print(eq2, file=result_file)

    return True


if __name__ == "__main__":
    print('Create 2-Variable equations')
    total = 5
    count = 0
    with open('result.txt', 'w') as f:
        while count < total:
            if generate_equation(-10, 10, f):
                print('========================')
                print('========================', file=f)
                count = count + 1


