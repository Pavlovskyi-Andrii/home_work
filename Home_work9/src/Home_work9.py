import random


def number_guessing_game():
    x = 5
    num = random.randint(1, 100)
    

    while x > 0:
        
        vvod = input("Вгадай число від 1 до 100 за 5 спроб : ")
        print(num)
        try:
            vvod = int(vvod)
            if num > vvod:
                x -= 1
                print(f"Менше ніж загадане число. Залишилось спроб: {x}")
            

            elif num < vvod:
                x -= 1
                print(f"Більше, ніж задумане число. Залишилось спроб: {x}")
            

            else:
                print("Вітаємо! Ви вгадали правильне число")          
                return

        except ValueError:
            print("Помилка! Введіть ціле число!")
            continue


    if x == 0 and num != vvod:
        print(f"Ви програли! Загадане число було {num}")

     
number_guessing_game()