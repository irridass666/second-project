# products = int(input('Введите число покупок: '))
# res = []

# while products > 0:
#     prod = input('Введите продукт: ')
#     res.append(prod)
#     products -= 1

# print("Все ваши покупки - ", res)

# class Person:
#     def __init__(self, name, age , skill):
#         self.name = name  
#         self.age = age
#         self.skill = skill 
#     def hello(self):
#         print('hello, im', self.name)
#     def show_skill(self):
#         print("im very good at", self.skill)


# chel1 = Person("Maksim", 12, "programming")
# print(chel1.name)
# print(chel1.age)
# print(chel1.skill)


# Lowstr = 'samira'
# uppstr = Lowstr.upper()
# print(uppstr)


# uppstr = 'SAMIRA'
# lowstr = uppstr.lower()
# print(lowstr)

# text = "Hello, my name is Samira, im 15 years old"
# x = text.split(',')
# print(x)


# myArr = ['hello', 'world', '!']

# myStr = ' '.join(myArr)

# print(myStr)

# print(myStr[0])
# print(myStr[-3])
# print(myStr[0:4])
# print(myStr[0:6:2])




# print("Добро пожаловать в магазин!")

# users = {
#     "samira": "admin",
#     "sveta": "manager"

# }

# games = ["saya no uta", "doki doki", "yttd"]
# phones = ["xiaomi", "iphone", "samsung"]

# def login():
#     while True:
#         user_login = input("Напишите ваш логин: ")
#         password = input("Напишите ваш пароль: ")

#         if user_login in users and users[user_login] == password:
#             print("Вы успешно зашли!")
#             choice = int(input("Напишите 1 чтобы посмотреть список игр,Напишите 2 для телефонов"))

#             if(choice == 1):

#                 print(games)
#             elif(choice == 2):
#                 print(phones)
#             else:
#                 print("Неправильно!")

#             break
#         else:
#             print("Неправильный пароль или логин!")

# login()



# print ("Добро пожаловать в антикино!")

# users = {
#     "samira": "666",
#     "sveta": "777"
# }

# serials = ["skins", "the end of the fucking world"]
# films = ["im Kristina", "miavi"]

# def login():
#     while True:
#         us_login = input("Напишите логин аккаунта: ")
#         password = input("Напишите пароль аккаунта: ")

#         if us_login in users and users[us_login] == password:
#              print("Вы успешно зашли!")
#              choice = int(input("Напишите 1 чтобы посмотреть список сериалов,Напишите 2 для списка фильмов"))

#              if(choice == 1):
#                  print(serials)
#              elif(choice == 2):
#                  print(films)
#              else:
#                  print("Выберете еще раз.")

#             break
    


# import time 
# print('im going to bed')
# time.sleep(5)
# print('i woke up)


# users = {}
# def registration():
#         while True:
#             name = input('Введите имя: ')
#             password = input("Введите пароль: ")

#             if len(name) < 5 or len(password) < 5 :
#                   print("Имя и\или пароль должен содержать не менее 5ти символов!")
#                   continue 
#             else:
#                   users[name] = password
#                   print("Вы успешно зарегистрированы!")
#                   break
# registration()


# sum = lambda x,y : x + y
# x = sum(1,21)
# print(x) 


# import random

# def game():
#     number_to_guess = random.randint(1,100)
#     tries = 0
#     while tries < 7:
#         guess = int(input("Введите число от 1 до 100: "))
#         tries += 1
#         if guess == number_to_guess:
#             print("Поздравляем! Вы угадали число за {tries} попыток!")
#             return
#         elif guess < number_to_guess:
#             print("Загаданное число больше")
#         else:
#             print("Загаданное число меньше")
#     print(f"Вы не угадали число. Загаданное число было: {number_to_guess}")

# game()


# 1. переменная это простыми словами коробка в которую кладут типы данных . Переменную используют для хранения элементов.
# 2. я знаю цикл for и while
# 3. числа,строки,массивы,
# 4. 
# 5.
# 6. в блоке условий elif может быть любое кол-во
# 7. f строка позволяет увидеть в консоли что лежит в переменной,
# 8. прописать while True 
# 9. чтобы добавить элемент в массив,нужно использовать метод append 
# 10. обратиться к словарю,указать в кв.скобках указать новый элемент
# 11. метод split разделяет строку,метод join соединяет 
# 12. с помощью команды del 
# 13. 
# 14. 
# 15.
# 16.
# 17. 







# myList = [2, 4, 6, 9, 10, 32]
# myListStr = ['hii', 'haaiii', 'hello']

# print(myListStr)
# myListStr.sort()
# print(myListStr) 


# myList = [2, 4, 6, 9, 10, 32]
# myListStr = ['hii', 'haaiii', 'hello']

# print(sorted(myListStr))



# def buble_sort(numbers):
#     is_sorted = False
#     while not is_sorted:
#         is_sorted = True
#         for i in range(len(numbers) - 1):
#             if numbers[i] > numbers[i + 1]:
#                 numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
#                 is_sorted = False

#     return numbers

# my_Arr = [1, 4, 3, 5, 6, 7, 8, 9, 3, 4, 5, 10]
# my_Arr = [124324, 4450955590, 913034904903, 82928903890, 32940923]

# print(buble_sort(my_Arr))

# def binary_search(numbers, target):
#     left = 0
#     right = len(numbers) - 1

#     while left <= right:
#         middle = (left + right) // 2
#         corrent_element = numbers[middle]

#         if corrent_element == target:
#             return middle
#         elif corrent_element < target:
#             left = middle + 1
#         else: 
#             right = middle - 1

#     return -1

# myArr = [49490, 4, 4904, 5, 9094, 8, 2, 4, 3, 293, 399403]
# target_number = 5
# index = binary_search(myArr, target_number)

# if index == -1:
#     print(f"число {target_number} не найдено в списке")
# else:
#     print(f"число {target_number} находится в индексе {index}")



# myArr = [1, 4, 5, 7, 11, 12, 15, 17]

# for i in range(len(myArr) - 1):
#     print(myArr[i]), (myArr[i + 1])



# x1 = 100
# x2 = 200

# x1, x2 = x2, x1 
# print(f"{x1} и {x2}")


# def myFun(a, b):
#     return a // b 

# # print(myFun(10, 2))

# isAuth = False 

# while not isAuth:
#     print('hello')
#     break

from tkinter import * 

def finish():
    root.destroy()
    print('приложение закрыто')

root = Tk()
root.title("приложение")
root.geometry("700x500")
root.minsize(200,200)
# root.maxsize(900,700)
root.protocol("WM_DELETE_WINDOW", finish)
# root.attributes("-fullscreen", True)
# root.attributes("-alpha", 0.1)

icon = PhotoImage(file="icon.png")
root.iconphoto(False, icon)

label = Label(text='hello stupids')
label.pack()

# bth = Button(text='leave')
# bth.pack()

# clicks = 0

# def click_button():
#     global clicks 
#     clicks += 1
#     btn["text"] = f"Clicks {clicks}"

# btn = Button(text='Click me', command=click_button)
# btn.pack()


def click_button1():
    root.attributes("-fullscreen", True)
    btn["state"] = ["disabled"]
    btn["state"] = ["normal"]

def click_button2():
    root.attributes("-fullscreen", False)
    btn2["state"] = ["disabled"]
    btn["state"] = ["normal"]
    

btn = Button(text='full screen', command=click_button1, state=["normal"])
btn.pack() 

btn2 = Button(text='normal', command=click_button2, state=["disabled"])
btn2.pack() 

root.mainloop()


