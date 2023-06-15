'''
try python function closure and function decorator
'''
def function2():
    print('Calling function2')

def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power

def mean():
    sample = []
    def inner_mean(number):
        sample.append(number)
        return sum(sample) / len(sample)
    return inner_mean


if __name__ == '__main__':
    raise_power2 = generate_power(2)
    print(raise_power2(3))
    raise_power3 = generate_power(3)
    print(raise_power3(3))
    raise_power4 = generate_power(4)
    print(raise_power4(3))

    sample_mean = mean()
    print(sample_mean(100))
    print(sample_mean(105))
    print(sample_mean(101))
    print(sample_mean(98))

