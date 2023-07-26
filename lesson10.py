# with open('text.txt','r')as filel,open ('text2.txt','r') as filel
# text1=file1.read()
# text2=file2.read()

# with open('merge.txt','w') as merge:
# merge.write(text1+'\n'+text2)


# words=input('Enter Words: ')


# with open('merge.txt','w') as merge:
#  merge.write(''.join(words))



# def my_decorator(func):
#     def wrapper():
#         print('До вызова функции')

#         func()

#         print('После вызова функции')

    # return wrapper


# @my_decorator
# def hello():
#     print('Привет,это между вызовами')

# hello()

# Пример декоратора с аргументами

# def in_num(n):
#     def decoration(func):
#         def wrapper(*args,**kwargs):
#             for _ in range(n):
#                result = func(*args, **kwargs)
#             return result
#         return wrapper
#     return decoration
    

# @in_num(5)
# def hello(name):
#         print('hello',name)

# hello('Tilek') 


# @classmethod
# @property
# @staticmethod

# def decoration(func):
#     def wrapper(x,y):
#         if not isinstance(x,int):
#             print('x, Не соответствует,должно быть число')
#         else:
#              print('Праивльно ')
#         if not isinstance(y,str):
#               print('y,Не соответствует,должна быть строка')
#         else:
#              print("Правильно2")
#         return func (x,y)
#     return wrapper
# @decoration
# def example(x,y):
#      pass
# example(5,'hello')
# example('hello','hello2')



