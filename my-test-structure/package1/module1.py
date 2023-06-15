'''
try python inner / nested / enclosing function feature
'''
def function1():
    print('Calling function1')

def sort_by_last_letter(strings):
    # local function
    def last_letter(s):
        return s[-1]
    
    print(last_letter)
    return sorted(strings, key=last_letter)

# return local functions
def enclosing():
    x = 'closed over'
    def localfunc():
        print('local func:', x)
    return localfunc

message = 'global'

def enclosing2():
    message = 'enclosing'

    def local():
        message = 'local'
    
    print('enclosing message:', message)
    local()
    print('enclosing message:', message)

if __name__ == '__main__':
    l = 'hello from a local function'.split()
    print(sort_by_last_letter(l))   # each time create a new local func object
    print(sort_by_last_letter(l))
    print(sort_by_last_letter(l))
    lf = enclosing()
    lf()
    print(lf.__closure__)

    print('global message:', message)
    enclosing2()
    print('global message:', message)
