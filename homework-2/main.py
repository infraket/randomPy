import pygame as pg
import random

white = (255, 255, 255)

pg.init()


def draw_grid(scr):
    for i in range(50, 500, 50):
        pg.draw.line(scr, (0, 0, 0), (i, 0), (i, 500), 2)
    for i in range(50, 500, 50):
        pg.draw.line(scr, (0, 0, 0), (0, i), (500, i), 2)


def draw_tic_tac_toe(scr, items):
    for i in range(10):
        for j in range(10):
            if items[i][j] == "o":
                pg.draw.circle(scr, (30, 144, 255), (j * 50 + 25, i * 50 + 25), 20)
            elif items[i][j] == "x":
                pg.draw.line(scr, (0, 0, 255), (j * 50 + 5, i * 50 + 5), (j * 50 + 45, i * 50 + 45), 3)
                pg.draw.line(scr, (0, 0, 255), (j * 50 + 45, i * 50 + 5), (j * 50 + 5, i * 50 + 45), 3)


def get_win_check(fd, symbol):
    flag_win = False
    # for line in fd:
    #     if line.count(symbol) == 5:
    #         flag_win = True
    for i in range(10):
        if fd[i][0] == fd[i][1] == fd[i][2] == fd[i][3] == fd[i][4] \
                == symbol:


            flag_win = True


        if fd[i][1] == fd[i][2] == fd[i][3] == fd[i][4] == fd[i][5] \
                == symbol:
            flag_win = True
        if fd[i][2] == fd[i][3] == fd[i][4] == fd[i][5] == fd[i][6] \
                == symbol:
            flag_win = True
        if fd[i][3] == fd[i][4] == fd[i][5] == fd[i][6] == fd[i][7] \
                == symbol:
            flag_win = True
        if fd[i][4] == fd[i][5] == fd[i][6] == fd[i][7] == fd[i][8] \
                == symbol:
            flag_win = True
        if fd[i][5] == fd[i][6] == fd[i][7] == fd[i][8] == fd[i][9] \
                == symbol:
            flag_win = True

    for i in range(10):
        if fd[0][i] == fd[1][i] == fd[2][i] == fd[3][i] == fd[4][i] \
                == symbol:
            flag_win = True
        if fd[1][i] == fd[2][i] == fd[3][i] == fd[4][i] == fd[5][i] \
                == symbol:
            flag_win = True
        if fd[2][i] == fd[3][i] == fd[4][i] == fd[5][i] == fd[6][i] \
                == symbol:
            flag_win = True
        if fd[3][i] == fd[4][i] == fd[5][i] == fd[6][i] == fd[7][i] \
                == symbol:
            flag_win = True
        if fd[4][i] == fd[5][i] == fd[6][i] == fd[7][i] == fd[8][i] \
                == symbol:
            flag_win = True
        if fd[5][i] == fd[6][i] == fd[7][i] == fd[8][i] == fd[9][i] \
                == symbol:
            flag_win = True

    for i in range(6):
        if fd[i][0] == fd[1][1] == fd[2][2] == fd[3][3] == fd[4][4] \
                == symbol or fd[i][-1] == fd[1][-2] == fd[2][-3] == fd[3][-4] == fd[4][-5] == symbol or fd[i][1] == \
                fd[1][2] == fd[2][3] == fd[3][4] == fd[4][5] == symbol:
            flag_win = True
        if fd[i][1] == fd[2][2] == fd[3][3] == fd[4][4] == fd[5][5] \
                == symbol or fd[0][-2] == fd[i][-3] == fd[2][-4] == fd[3][-5] == fd[4][-6] == symbol or fd[0][2] == \
                fd[i][3] == fd[2][4] == fd[3][5] == fd[4][6] == symbol:
            flag_win = True
        if fd[i][2] == fd[3][3] == fd[4][4] == fd[5][5] == fd[6][6] \
                == symbol or fd[0][-3] == fd[1][-4] == fd[i][-5] == fd[3][-6] == fd[4][-7] == symbol or fd[0][3] == \
                fd[1][4] == fd[i][5] == fd[3][6] == fd[4][7] == symbol:
            flag_win = True
        if fd[i][3] == fd[4][4] == fd[5][5] == fd[6][6] == fd[7][7] \
                == symbol or fd[0][-4] == fd[1][-5] == fd[2][-6] == fd[i][-7] == fd[4][-8] == symbol or fd[0][4] == \
                fd[1][5] == fd[2][6] == fd[i][7] == fd[4][8] == symbol:
            flag_win = True
        if fd[i][4] == fd[5][5] == fd[6][6] == fd[7][7] == fd[8][8] \
                == symbol or fd[0][-5] == fd[1][-6] == fd[2][-7] == fd[3][-8] == fd[i][-9] == symbol or fd[0][5] == \
                fd[1][6] == fd[2][7] == fd[3][8] == fd[i][9] == symbol:
            flag_win = True
        if fd[i][5] == fd[6][6] == fd[7][7] == fd[8][8] == fd[9][9] \
                == symbol or fd[0][-6] == fd[1][-7] == fd[2][-8] == fd[3][-9] == fd[4][0] == symbol or fd[4][i] == \
                fd[i][6] == fd[6][7] == fd[7][8] == fd[8][9] == symbol:
            flag_win = True

    if fd[1][0] == fd[2][1] == fd[3][2] == fd[4][3] == fd[5][4] \
            == symbol or fd[1][2] == fd[2][3] == fd[3][4] == fd[4][5] == fd[5][6] == symbol or fd[1][3] == fd[2][4] == \
            fd[3][5] == fd[4][6] == fd[5][7] == symbol \
            or fd[1][4] == fd[2][5] == fd[3][6] == fd[4][7] == fd[5][8] == symbol \
            or fd[1][5] == fd[2][6] == fd[3][7] == fd[4][8] == fd[5][9] \
            == symbol or fd[1][-1] == fd[2][-2] == fd[3][-3] == fd[4][-4] == fd[5][-5] == symbol or \
            fd[1][-2] == fd[2][-3] == fd[3][-4] == fd[4][-5] == fd[5][-6] == symbol or \
            fd[1][-3] == fd[2][-4] == fd[3][-5] == fd[4][-6] == fd[5][-7] == symbol or \
            fd[1][-4] == fd[2][-5] == fd[3][-6] == fd[4][-7] == fd[5][-8] == symbol or \
            fd[1][-5] == fd[2][-6] == fd[3][-7] == fd[4][-8] == fd[5][-9] == symbol or \
            fd[1][-6] == fd[2][-7] == fd[3][-8] == fd[4][-9] == fd[5][-0] == symbol:
        flag_win = True
    if fd[2][0] == fd[3][1] == fd[4][2] == fd[5][3] == fd[6][4] == symbol or \
            fd[2][1] == fd[3][2] == fd[4][3] == fd[5][4] == fd[6][5] == symbol or \
            fd[2][2] == fd[3][3] == fd[4][4] == fd[5][5] == fd[6][6] == symbol or \
            fd[2][3] == fd[3][4] == fd[4][5] == fd[5][6] == fd[6][7] == symbol or \
            fd[2][4] == fd[3][5] == fd[4][6] == fd[5][7] == fd[6][8] \
            == symbol or fd[2][5] == fd[3][6] == fd[4][7] == fd[5][8] == fd[6][9] == symbol or \
            fd[2][-1] == fd[3][-2] == fd[4][-3] == fd[5][-4] == fd[6][-5] == symbol or \
            fd[2][-2] == fd[3][-3] == fd[4][-4] == fd[5][-5] == fd[6][-6] == symbol or \
            fd[2][-3] == fd[3][-4] == fd[4][-5] == fd[5][-6] == fd[6][-7] == symbol or \
            fd[2][-4] == fd[3][-5] == fd[4][-6] == fd[5][-7] == fd[6][-8] == symbol or \
            fd[2][-5] == fd[3][-6] == fd[4][-7] == fd[5][-8] == fd[6][-9] == symbol or \
            fd[2][-6] == fd[3][-7] == fd[4][-8] == fd[5][-9] == fd[6][0] == symbol:
        flag_win = True
    if fd[3][0] == fd[4][1] == fd[5][2] == fd[6][3] == fd[7][4] \
            == symbol or fd[3][1] == fd[4][2] == fd[5][3] == fd[6][4] == fd[7][5] == symbol or fd[3][2] == fd[4][3] == \
            fd[5][4] == fd[6][5] == fd[7][6] == symbol \
            or fd[3][3] == fd[4][5] == fd[5][6] == fd[6][7] == fd[7][8] == symbol \
            or fd[3][4] == fd[4][5] == fd[5][6] == fd[6][7] == fd[7][8] \
            == symbol or fd[3][5] == fd[4][6] == fd[5][7] == fd[6][8] == fd[7][9] == symbol or \
            fd[3][-1] == fd[4][-2] == fd[5][-3] == fd[6][-4] == fd[7][-5] == symbol or \
            fd[3][-2] == fd[4][-3] == fd[5][-4] == fd[6][-5] == fd[7][-6] == symbol or \
            fd[3][-3] == fd[4][-4] == fd[5][-5] == fd[6][-6] == fd[7][-7] == symbol or \
            fd[3][-4] == fd[4][-5] == fd[5][-6] == fd[6][-7] == fd[7][-8] == symbol or \
            fd[3][-5] == fd[4][-6] == fd[5][-7] == fd[6][-8] == fd[7][-9] == symbol or \
            fd[3][-6] == fd[4][-7] == fd[5][-8] == fd[6][-9] == fd[7][0] == symbol:
        flag_win = True
    if fd[4][0] == fd[5][1] == fd[6][2] == fd[7][3] == fd[8][4] \
            == symbol or fd[4][1] == fd[5][2] == fd[6][3] == fd[7][4] == fd[8][5] == symbol or fd[4][2] == fd[5][3] == \
            fd[6][4] == fd[7][5] == fd[8][6] == symbol \
            or fd[4][3] == fd[5][5] == fd[6][6] == fd[7][7] == fd[8][8] == symbol \
            or fd[4][4] == fd[5][5] == fd[6][6] == fd[7][7] == fd[8][8] \
            == symbol or fd[4][5] == fd[5][6] == fd[6][7] == fd[7][8] == fd[8][9] == symbol or \
            fd[4][-1] == fd[5][-2] == fd[6][-3] == fd[7][-4] == fd[8][-5] == symbol or \
            fd[4][-2] == fd[5][-3] == fd[6][-4] == fd[7][-5] == fd[8][-6] == symbol or \
            fd[4][-3] == fd[5][-4] == fd[6][-5] == fd[7][-6] == fd[8][-7] == symbol or \
            fd[4][-4] == fd[5][-5] == fd[6][-6] == fd[7][-7] == fd[8][-8] == symbol or \
            fd[4][-5] == fd[5][-6] == fd[6][-7] == fd[7][-8] == fd[8][-9] == symbol or \
            fd[4][-6] == fd[5][-7] == fd[6][-8] == fd[7][-9] == fd[8][0] == symbol:
        flag_win = True
    if fd[5][0] == fd[6][1] == fd[7][2] == fd[8][3] == fd[9][4] \
            == symbol or fd[5][1] == fd[6][2] == fd[7][3] == fd[8][4] == fd[9][5] == symbol or fd[5][2] == fd[6][3] == \
            fd[7][4] == fd[8][5] == fd[9][6] == symbol \
            or fd[5][3] == fd[6][5] == fd[7][6] == fd[8][7] == fd[9][8] == symbol \
            or fd[5][4] == fd[6][5] == fd[7][6] == fd[8][7] == fd[9][8] \
            == symbol or fd[5][5] == fd[6][6] == fd[7][7] == fd[8][8] == fd[9][9] == symbol or \
            fd[5][-1] == fd[6][-2] == fd[7][-3] == fd[8][-4] == fd[9][-5] == symbol or \
            fd[5][-2] == fd[6][-3] == fd[7][-4] == fd[8][-5] == fd[9][-6] == symbol or \
            fd[5][-3] == fd[6][-4] == fd[7][-5] == fd[8][-6] == fd[9][-7] == symbol or \
            fd[5][-4] == fd[6][-5] == fd[7][-6] == fd[8][-7] == fd[9][-8] == symbol or \
            fd[5][-5] == fd[6][-6] == fd[7][-7] == fd[8][-8] == fd[9][-9] == symbol or \
            fd[5][-6] == fd[6][-7] == fd[7][-8] == fd[8][-9] == fd[9][0] == symbol:
        flag_win = True

    return flag_win


screen_size = (500, 500)

window = pg.display.set_mode(screen_size)

screen = pg.Surface(screen_size)

programIcon = pg.image.load('icon.png')
pg.display.set_icon(programIcon)

pg.display.set_caption("Reverse Tic-Tac-Toe")

screen.fill(white)

field = [["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", "", "", ""], ]

mainloop = True
game_over = False

while mainloop:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            mainloop = False

        if event.type == pg.MOUSEBUTTONDOWN and not game_over:
            pos = pg.mouse.get_pos()
            if field[pos[1] // 50][pos[0] // 50] == "":
                field[pos[1] // 50][pos[0] // 50] = "x"
                x, y = random.randint(0, 9), random.randint(0, 9)
                while field[x][y] != "":
                    for line in field:
                        if line.count('o') % 2 == 0 and line.count('o') >= 4:
                            x *= 2
                            y *= 2

                    x, y = random.randint(0, 9), random.randint(0, 9)
                field[x][y] = "o"

            player_win = get_win_check(field, "x")
            ai_win = get_win_check(field, "o")
            if player_win or ai_win:
                game_over = True
                if player_win:
                    pg.display.set_caption("You lose")
                else:
                    pg.display.set_caption("AI lose")

            draw_tic_tac_toe(screen, field)

    draw_grid(screen)
    window.blit(screen, (0, 0))
    pg.display.update()
