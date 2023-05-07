#print(f'NameError - {type(NameError)} - {issubclass(NameError, BaseException)}')
#print(f'ImportError - {type(ImportError)} - {issubclass(ImportError, BaseException)}')
#print('hi')
#try:
   # print('start')
   # print(10/0)
   # print('no error')
#except (ZeroDivisionError, NameError):
   # print('we have an error')
#print('code after capsule')



def cheker(var_1):
    if type(var_1)!=str:
        raise TypeError(f'Пробачте, Собачка не одобряє клас {type(var_1)},'f'Собачці потрібен клас str')
    else:
        return var_1
first_var=10
cheker(first_var)