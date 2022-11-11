from rich import print, console

def add(x,y):
    '''
    Adds two numbers together
    >>> add(2,3)
    5
    
    >>> add(0, 0)
    0

    >>> add(1, 0)
    1

    >>> add(-1, 10)
    9
    
    '''


    return x + y


if __name__ == '__main__':
    import doctest
    (doctest.testmod(verbose=True))