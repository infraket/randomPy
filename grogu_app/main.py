import random
import pgzrun
from pgzero.actor import Actor

score = 0
game_over = False
game_win = False

TITLE = "GroguApp"
WIDTH = 600
HEIGHT = 500

grogu = Actor("grogu2.png")
grogu.x = 120
grogu.y = 420

ball = Actor("ball.png")
ball.x = 30
ball.y = 300

ball_x_speed = -1
ball_y_speed = -1

bars_list = []


def update():
    global ball_x_speed, ball_y_speed, score, game_win
    music.play('preview-3.ogg')
    if score == 18:
        sounds.win.play()
        game_win = True
    if keyboard.left:
        grogu.x = grogu.x - 5
    if keyboard.right:
        grogu.x = grogu.x + 5
    if keyboard.rctrl:
        music.stop()

    if grogu.x < 88:
        grogu.x = 88
    if grogu.x > 512:
        grogu.x = 512

    update_ball()
    for bar in bars_list:
        if ball.colliderect(bar):
            sounds.jump.play()
            bars_list.remove(bar)
            ball_y_speed *= -1
            score += 1

    if grogu.colliderect(ball):
        ball_y_speed *= -1
        sounds.up.play()
        rand = random.randint(0, 1)
        if rand:
            ball_x_speed *= -1


def draw():
    screen.blit("back.jpg", (0, 0))
    if game_over:
        screen.draw.text("GAME OVER", (230, 200), color="red")
        screen.draw.text('Final Score: ' + str(score), (180, 300), color="black")


    else:
        if game_win:
            screen.draw.text("WIN WIN WIN", (230, 200), color="red")
        else:
            grogu.draw()
            ball.draw()
            screen.draw.text('Score: ' + str(score), (15, 10), color="black")
            for bar in bars_list:
                bar.draw()


def place_bars(x, y, image):
    bar_x = x
    bar_y = y
    for i in range(6):
        bar = Actor(image)
        bar.x = bar_x
        bar.y = bar_y
        bar_x += 70
        bars_list.append(bar)


def update_ball():
    global ball_x_speed, ball_y_speed, game_over
    ball.x -= ball_x_speed
    ball.y -= ball_y_speed
    if ball.y >= HEIGHT:
        sounds.losing.play()
        game_over = True
    if (ball.x >= WIDTH) or (ball.x <= 0):
        ball_x_speed *= -1
    if (ball.y >= HEIGHT) or (ball.y <= 0):
        ball_y_speed *= -1


coloured_box_list = ["frog5.png", "frog12.png", "frog5.png"]
x = 120
y = 100
for coloured_box in coloured_box_list:
    place_bars(x, y, coloured_box)
    y += 50
pgzrun.go()
