class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)
    
class EngAlphabet(Alphabet):
    __letters_num = 26
    def __init__(self):
        super().__init__('En', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    def is_en_letter(self, letter):
        return letter.upper() in self.letters
    
    def letters_num(self):
        print(EngAlphabet.__letters_num)
        return EngAlphabet.__letters_num
    
    @staticmethod
    def example():
        return 'example text in English'



engish_alpha = EngAlphabet()
engish_alpha.print()
engish_alpha.letters_num()      
print("Приклад тексту англійською:", EngAlphabet.example())



user_input = input("Введите букву: ")  # Запрос буквы у пользователя
if engish_alpha.is_en_letter(user_input):
    print(f"Буква '{user_input}' є в англійському абетці.")
else:
    print(f"Буква '{user_input}' відсутня в англійському алфавіті.")
