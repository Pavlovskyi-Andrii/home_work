import random
num = random.randint(1, 100)
print(num)

x = 0
vvod = None
print(x)
while x <= 4:
    vvod = input("Вгадай число від 1 до 100 за 5 спроб : ")
    try:
        vvod = int(vvod)
        if num > vvod:
            x += 1
            
            print(f"менше ніж загадане число. спроб {x}")
            

        elif num < vvod:
            x += 1
            print(f"більше, ніж задумане число. спроб {x}")
            

        else:
            print("Вгадав !")
            
            break

    except ValueError:
        print("Помилка! Введіть ціле число.")
        continue
print(f"x = {x}, num = {num}, vvod = {vvod}")  # Отладочный вывод

if x == 5 and num != vvod:
    print(f"Ви програли! Загадане число було {num}")

     
