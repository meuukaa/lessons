# def hello (a,b): Позиционные аргументы
#     c = a + b
#     # print("hello world")
    
#     return c


# def hello (a=2,b=4): Именованные аргументы
#     c = a + b
#     # print("hello world")
    
#     return c  
# print(hello())
# *args , **kwargs

# #def hello(*args):
# resul = 0
# for i in args:
# resul+= i

# return resul
    
#  print (hello(1,2,3,4) )


# def hello (**kwargs):переменная которая принимет в себя неограниченое колличество именованных аргументов

#     for key ,value in kwargs.items():
#         print(value**)
# a = 'не хелло'

# def hello ():
#     a = "hello"
#     return a
# def ne_hello(*args):
#     return args


# print(hello())
# print(ne_hello(a))

# анонимнаая функция без названия
# num = lambda x,y : x+y
# print(num(1,3))
# num = lambda n : n % 2 == 0
# print(num(4))
# функция рекурсия (вызов из самой себя)

def fak (u):
    if u == 0:
        return 1
    else:
         return u *factorial(u - 1)* u
    print(fak(5))