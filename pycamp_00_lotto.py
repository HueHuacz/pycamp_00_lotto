""" Skrypt symulujący losowania lotto """

from sys import exit as sysexit
from random import sample


SINGLE_DRAW_COST = 3
DRAWS_IN_YEAR = 52 * 3


def make_user_list():
    """ Tworzy listę z wartościami podanymi przez użytkownika """
    user_input = input("Podaj 6 liczb z zakresu od 1 do 49 (rozdzielonych spacjami): ")
    user_input_list = user_input.split()
    return user_input_list


def make_user_set(num_list):
    """ Tworzy set i sprawdza czy podane wartości spełaniją założenia """
    num_set = set()
    for num in num_list:
        try:
            num_set.add(int(num))
        except ValueError:
            sysexit(f'Wartość: "{num}" nie jest wymaganą liczbą!\n')
    if len(num_set) != 6:
        sysexit(f'Podano niewłaściwą ilość liczb! Podano {len(num_set)}, a oczekiwano 6\n')
    for num in num_set:
        if num > 49 or num < 1:
            sysexit(f'Wartość: "{num}" nie zajduje się w przedziale od 1 do 49!\n')
    return num_set


def one_draw():
    """ Pojedyńcze losowanie 6 liczb z zakresu od 1 do 49 """
    return set(sample(range(1, 50), 6))


def play_until_win(numbers_set, draw_algoritm):
    """ Pętla dziłająca do momentu wylosowania liczb z numbers_set. Zwraca ilość losowań i
    ilość trafionych piątek, czwarótek i trójek """
    draw_set = set()
    index = index_5 = index_4 = index_3 = 0

    while numbers_set != draw_set:
        draw_set = draw_algoritm()
        # if len(numbers_set.intersection(draw_set)) == 5:
        #     index_5 += 1
        # elif len(numbers_set.intersection(draw_set)) == 4:
        #     index_4 += 1
        # elif len(numbers_set.intersection(draw_set)) == 3:
        #     index_3 += 1
        len_common_part = len(numbers_set.intersection(draw_set))
        match len_common_part:
            case 5:
                index_5 += 1
            case 4:
                index_4 += 1
            case 3:
                index_3 += 1
        index += 1

    return index, index_5, index_4, index_3


if __name__ == '__main__':

    print('\n\t--- LOTTO ---\n')
    user_age = int(input("Podaj swój wiek: "))

    user_list = make_user_list()
    user_set = make_user_set(user_list)
    print(f'\nTwoje liczby to: {user_set}')
    print('W kasecie maszyny losującej znajduje się 49 liczb. Komora maszyny losującej jest pusta.')
    print('Następuje zwolnienie blokady... i rozpoczynamy losowanie sześciu liczb...')

    draw_index, hit_5, hit_4, hit_3 = play_until_win(user_set, one_draw)

    PRICE = SINGLE_DRAW_COST * draw_index
    YEARS = draw_index / DRAWS_IN_YEAR
    user_future_age = user_age + int(YEARS)

    print('\n\tWYGRANA!!!\n')
    print(f'W losowaniu nr. {draw_index:,} padły Twoje liczby: {user_set}.')
    print(f'Całkowity koszt zakładów wyniósł {PRICE:,} złotych. W dniu wygranej będziesz miał {user_future_age:,} lat.')
    print(f'W tych losowaniach trafiłeś {hit_5:,} razy piątkę, {hit_4:,} razy czwórkę i {hit_3:,} razy trójkę.')
    print('')
