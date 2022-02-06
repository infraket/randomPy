import random

pb = [str(num) for num in range(1, 101)]
pb_aft = [str(num) for num in range(1, 101)]


def display_board(pb):
    for i in range(100):
        print(pb[i], end='\t')
        if (i + 1) % 10 == 0:
            print('\n')


def player_input():
    player_first = ''
    while player_first not in ('X', '0'):
        player_first = input('Выбрать - Х или 0?:').upper()
        if player_first == 'X':
            comp_second = 'O'
        else:
            comp_second = 'X'
    return player_first, comp_second


def is_num(pos, mark, pb):
    if pb[pos] in ('X', '0'):
        return True


def place_marker(pos, mark, pb_aft, pb):
    pb_aft.remove(pb[pos])
    pb[pos] = mark


def two_line(pos, mark, pb):
    count = 1
    step = 0
    for i in range(9 - pos // 10):
        if (pos + step + 1) % 10 != 0 and (
                pos + step) // 10 != 9:
            step += 11
            if pb[pos + step] == mark:
                count += 1
            else:
                break
        else:
            break
    step = 0
    for i in range(pos // 10):
        if (pos + step + 1) % 10 != 1 and (
                pos + step) // 10 != 0:
            step -= 11
            if pb[pos + step] == mark:
                count += 1
            else:
                break
        else:
            break
    if count >= 5:
        return True
    count = 1
    step = 0
    for i in range(9 - pos // 10):
        if (pos + step + 1) % 10 != 1 and (
                pos + step) // 10 != 9:
            step += 9
            if pb[pos + step] == mark:
                count += 1
            else:
                break
        else:
            break
    step = 0
    for i in range(pos // 10):
        if (pos + step + 1) % 10 != 0 and (
                pos + step) // 10 != 0:
            step -= 9
            if pb[pos + step] == mark:
                count += 1
            else:
                break
        else:
            break
    if count >= 5:
        return True


def gorizontal_line(pos, mark, pb):
    count = 1
    step = 1
    while True:
        if (pos + 1) % 10 != 0:
            for i in range(9 - pos % 10):
                if pb[pos + step] == mark:
                    count += 1
                    step += 1
                else:
                    break
        step = -1
        if (pos + 1) % 10 != 1:
            for i in range(pos % 10):
                if pb[pos + step] == mark:
                    count += 1
                    step -= 1
                else:
                    break
        break
    if count >= 5:
        return True


def vertical_line(pos, mark, pb):
    count = 1
    step = 10
    while True:
        if pos // 10 != 9:
            for i in range(9 - pos // 10):
                if pb[pos + step] == mark:
                    count += 1
                    step += 10
                else:
                    break
        step = -10
        if pos // 10 != 0:
            for i in range(pos // 10):
                if pb[pos + step] == mark:
                    count += 1
                    step -= 10
                else:
                    break
        break
    if count >= 5:
        return True


def check_game_finish(pos, mark, pb):
    if gorizontal_line(pos, mark, pb) or vertical_line(pos, mark, pb) or two_line(
            pos, mark, pb):
        return True


def computer_check(comp_second, pb_aft, pb):
    pb_aft_c = pb_aft.copy()
    for i in range(len(pb_aft)):
        pos = int(random.choice(pb_aft_c)) - 1
        pb_aft_c.remove(pb[pos])
        tmp = pb[pos]
        place_marker(pos, comp_second, pb_aft, pb)
        if check_game_finish(pos, comp_second, pb) and i != len(pb_aft):
            pb_aft.append(tmp)
            pb[pos] = tmp
            continue
        elif not check_game_finish(pos, comp_second, pb):
            return True
        else:
            return False


def replay():
    decision = ""
    while decision not in ('да', 'нет'):
        decision = input(
            'Сыграть еще раз? Напишите "да" или "нет": '
        ).lower()

    return decision == 'да'


def new_game():
    pb = [str(num) for num in range(1, 101)]
    pb_aft = [str(num) for num in range(1, 101)]
    player_first, comp_second = player_input()

    return pb, pb_aft, player_first, comp_second


player_first, comp_second = player_input()


def game_xo(player_first, comp_second, pb, pb_aft):
    display_board(pb)
    print('\n\n')
    while True:
        if len(pb_aft) > 0:
            try:  # Ход игрока
                pos = int(input('Выберите свободную ячейку: ')) - 1
                print()
                assert pos in range(100)
                if is_num(pos, player_first, pb):
                    print('Ячейка занята')
                    continue
                place_marker(pos, player_first, pb_aft, pb)
                if check_game_finish(pos, player_first, pb):
                    display_board(pb)
                    print('Вы проиграли')
                    if replay():
                        pb, pb_aft, player_first, comp_second = new_game()
                        display_board(pb)
                        print('\n\n')
                        continue
                    else:
                        return
            except ValueError:
                print('Введите число: ')
                continue
            except AssertionError:
                print('Вы должны ввести число в диапазоне от 1 до 100: ')
                continue

            if computer_check(comp_second, pb_aft, pb):
                display_board(pb)
                continue
            else:
                display_board(pb)
                print('Компьютер проиграл')
                if replay():
                    pb, pb_aft, player_first, comp_second = new_game()
                    display_board(pb)
                    print('\n\n')
                    continue
                else:
                    return
            display_board(pb)
        else:
            print('Ничья')
            if replay():
                pb, pb_aft, player_first, comp_second = new_game()
                display_board(pb)
                print('\n\n')
                continue
            else:
                return


if __name__ == '__main__':
    game_xo(player_first, comp_second, pb, pb_aft)
