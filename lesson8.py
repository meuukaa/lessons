
# работа с файлами 

# file=open(имя файла,режим доступа к файлу)

# 'r'- read()за чтение файла
# 'w' - write ()запись с удалением уже существующих данных
# a- append() запись без удаления данных в файле в новой строке
# 'x' создание файла если его не существует
# rb-wb -- чтение и запись в данном виде



# file = open('text.txt','w')
# text = file.write('Hello world')

# print(text)
# file.close()


# file = open('text.txt','a')
# text = file.write('\t hello')

# print(text)
# file.close()

open('textst.txt','+a') 
# text = file.write('lyalyalya') as file:

# with open('text.txt','+x') as file:
# text =file.write('lyalyalya;')


with open ('image.jpg','rb') as file:
    data = file.read()
    print(data)

    
    



