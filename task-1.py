import random

'''
class LotoCard - генерирует карточки Игроку и Компу и возвращет их ввиде словарей
Словарь содержит {Имя_Игрока: числа_карточки_ввиде_списка, Имя_Компьютера: числа_карточки_ввиде_списка}
class LotoGame:
 - получает словарь
 - генерирует число бочонка
 - запрашивает у пользователя y/n (есть проверка и возможность исправить, если
 пользователь ввел символ отлычный от [y, Y, n, N])
 - вычеркивает числа
 - выводит числа карточки после зачеркивания
   (print_script - функция преобразования списка в строки ввиде таблицы)
- проверяет кто победил
'''

class LotoCard: # просходит генерация карточек
    def __init__(self, player):
        self.player = player

    def card_generat(self):
        numbers = list(range(1, 90))
        random.shuffle(numbers)
        total_list = numbers[:15]
        line = 0
        final_card = []
        while line < 3:
            card_line = total_list[line * 5:line * 5 + 5]
            card_line.sort()
            line += 1
            # втсавляем 4 пробела в строку карточки:
            i = 1
            while i < 5:
                pos = random.randint(0, 4 + i)
                card_line.insert(pos, " ")
                i += 1
            final_card = final_card + card_line
        final_card_dict = {'name': self.player, 'card': final_card}
        return final_card_dict


class LotoGame:
    def __init__(self, human_player_dict, computer_player_dict):
        self.human_player = human_player_dict['card']
        self.computer_player = computer_player_dict['card']
        self.human_name = human_player_dict['name']
        self.computer_name = computer_player_dict['name']

    def start(self):

        # функция, выводящая карточку список ввиде таблицы
        def print_script(player):
            card_print = ''
            i = 0
            while i < 3:
                card_print = card_print + ' '.join(map(str, player[i * 9:i * 9 + 9])) + "\n"
                i += 1
            return card_print

        # создаем 90 номеров (боченков) и перемешиваем их, а потом берем подряд
        gen_list = [el for el in range(1, 91)]
        random.shuffle(gen_list)
        user_count = 0
        comp_count = 0
        i = 1
        while i <= 90:
            rand_number = gen_list[i-1]
            print(f'{i}-й бочонок номер {rand_number}. Осалось {90 - i}\n')
            print(f'Ваша карточка:\n {print_script(self.human_player)}')
            print(f'Карточка компьютера:\n {print_script(self.computer_player)}')

            # проверка корректности ввода y/n
            try_ways = ['y', 'Y', 'n', 'N']
            while True:
                try:
                    try_guess = input('Есть ли у Вас такое число? (y/n)')
                    try_1 = try_ways.index(try_guess)
                except ValueError:
                    print('Вы опечатались, нужно ввести y/n!')
                else:
                    break

            # проверка есть ли совпадения
            try:
                pos_number = self.human_player.index(rand_number)
            except ValueError:
                if try_guess == 'y' or try_guess == 'Y':
                    print('у Вас нет такого числа, Вы проиграли')
                    exit()
                print('все верно, у Вас нет такого числа')
            else:
                if try_guess == 'n' or try_guess == 'N':
                    print('Ошибка, у Вас есть такое число, Вы проиграли')
                    exit()
                self.human_player[pos_number] = '-'
                user_count += 1
                print(f'Есть совпадение, зачеркнуто {user_count}-ое число \nУ вас осталось {15 - user_count} чисел')
            try:
                pos_number = self.computer_player.index(rand_number)
            except ValueError:
                print('у компьютера нет совпадений')
            else:
                self.computer_player[pos_number] = '-'
                comp_count += 1
                print(f'У компа совпадение, зачеркнуто {comp_count}-ое число\nУ компа осталось {15 - comp_count} чисел')
            i += 1

            # проверяем количество зачеркнутых чисел, появился ли победитель
            if user_count == 15 and comp_count == 15:
                print('Ничья')
                exit()
            elif user_count == 15:
                print(f'{self.human_name} победил')
                exit()
            elif comp_count == 15:
                print(f'{self.computer_name} победил')
                exit()


human_player = LotoCard('Петя')
computer_player = LotoCard('Компьютер')

game = LotoGame(human_player.card_generat(), computer_player.card_generat())
game.start()
