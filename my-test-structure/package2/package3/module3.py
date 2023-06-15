'''
Try out python arbitrary position and keyword arguments
'''
def function3():
    print('Calling function3')

def hypervolume(*args):
    print(args)
    print(type(args))
    v = 1
    for n in args:
        v *= n
    print(v)

def hyper2(arg, *args):
    print(arg, args)

# test arbitary keyword arguments
def tag(name, **kwargs):
    print(name)
    print(kwargs)
    print(type(kwargs))

def color(red, green, blue, **kwargs):
    print('r=', red)
    print('g=', green)
    print('b=', blue)
    print(kwargs)



if __name__ == '__main__':
    hypervolume(1, 2, 3, 5)
    hypervolume()
    hyper2(1, 2, 3, 5)
    # hyper2() ## throw missing argument error
    # test arbitary keyword arguments
    tag('img', src='monet.img', alt='Sunrise by Claude Monet', border=1)
    k = {'red':21, 'green':58, 'blue': 79, 'alpha':100}
    color(**k)
    color(**k, beta=35)