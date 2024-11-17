class employees():
    def __init__(self):
        print('making employee...')
    def __del__(self):
        print('employee is deleted.')

def x():
    print('creating object')
    obj = employees()
    print('function has ended.')
    return obj

print('calling x')
obj = x()
print('program x')
