#return method of recursive function

def recursive_function(i):
    if i == 100:
        return
    print('This is ', i, 'th recursive function calling ', i+1, 'th recursive function')
    recursive_function(i+1)
    print('Return ', i, 'th recursive function')

recursive_function(1)