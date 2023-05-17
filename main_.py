#assert 2+2==5, 'ستيهتشسخيتسشهت'

#"""
#>>> 1+1
#3
#"""

#if __name__=="__main__":
#    import doctest
#    doctest.testmod()

def adder(*args, **kwargs):
    result = 0
    for _ in args:
        result +=_
    for _ in kwargs.values():
        result +=_
    return result