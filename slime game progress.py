# created functional settings button and semi-functional full and regular screen button
# created functional settings button and semi-functional full and regular screen button
# created functional settings button and semi-functional full and regular
# screen button


# constant_fire = False

key_states = [False for i in range(223)]

screen = 100
width = int(screen * 7.5)
height = int(screen * 6)

i = 0
bullets_speed = []
bullets = []
slimes = [PVector(random(25, 750), random(25, 550)), 
          PVector(random(25, 750), random(25, 550)), 
          PVector(random(25, 750), random(25, 550))]
slimes_speed = PVector(1, 1)
score = 0
shot = False

player = PVector(200, 200)
player_size = 40
player_speed = PVector(0, 0)

barrier = PVector(100, 100)
barrier_size = PVector(100, 500)

slow_mo = False

play_location = PVector((width / 2) - 150, (height / 2) - 50)
play_clicked = False
play_size = PVector(100, 50)

settings_location = PVector((width / 2) - 150, (height / 2) + 50)
settings_clicked = False
settings_size = PVector(100, 50)

fullscreen_location = PVector((width / 2) + 50, (height / 2) - 50)
fullscreen_clicked = False
fullscreen_size = PVector(100, 50)

regularscreen_location = PVector((width / 2) + 50, (height / 2) + 50)
regularscreen_clicked = False
regularscreen_size = PVector(100, 50)


def setup():
    size(width, height)


def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle)


def draw():
    background(255)
    fill(0)
    global score
    global speed, player_speed, bullets_speed, slimes_speed
    global regularscreen_clicked, fullscreen_clicked, screen
    mouse = PVector(mouseX, mouseY)

    # play button
    # if not play_clicked and not settings_clicked:
    #     fill(0)
    #     rect(play_location.x, play_location.y, play_size.x, play_size.y)

    #     fill(255)
    #     textSize(32)
    #     text('PLAY', play_location.x + 10, play_location.y + 30)

    # if button clicked start game
    fill(0)
    # if play_clicked and not settings_clicked:
    if key_states[65]:  # left a
        player.x -= 3
    elif key_states[68]:  # right d
        player.x += 3

    if key_states[87]:  # up w
        player.y -= 3
    elif key_states[83]:  # down s
        player.y += 3

    ellipse(player.x, player.y, player_size, player_size)

    point(mouse.x, mouse.y)

    # showing score
    textSize(24)
    text('Score: ' + str(score), width - 150, 50)

        # constant fire
        # if constant_fire:
        #     for i in range(len(bullets)):
        #             ellipse(bullets[i].x, bullets[i].y, 5, 5)
        #             bullets[i].add(bullets_speed[i])
        #     bullets.append(PVector(player.x, player.y))
        #     bullets_speed.append(trajectory(mouse, player).mult(6))

    # if slow_mo:
    #     bullets_speed *= 2
    #     player_speed *= 2
    #     slimes_speed *= 2

    # slimes bouncing off walls
    # if slimes[0].x > width or slimes[0].y < 0:
    #     slimes_speed.x *= -1
    # elif slimes[0].y > width or slimes[0].y < 0:
    #     slimes_speed.y *= -1

    for i in range(len(bullets)):
        #   if bullets > barrier.y and :
            ellipse(bullets[i].x, bullets[i].y, 5, 5)
            bullets[i].add(bullets_speed[i])
            for x in range(len(slimes)):
                if dist(bullets[i].x, bullets[i].y, slimes[x].x, slimes[x].y) < 25:
                    slimes[x] = PVector(random(25, 750), random(25, 550))
                    score += 1
    i = 0
    while True:
        if i >= len(bullets) - 1:
            break
        if bullets[i].x < 0 or bullets[i].x > 600 or bullets[i].y > 600 or bullets[i].y < 0:
            bullets.remove(bullets[i])
            bullets_speed.remove(bullets_speed[i])
            i = 0
        i += 1
    
    global shot
    if shot:
        bullets.append(PVector(player.x, player.y))
        bullets_speed.append(trajectory(mouse, player).mult(7))
        shot = False
    for s in slimes:
        ellipse(s.x, s.y, 25, 25)

    # settings for changing screen size
    # if not settings_clicked and not play_clicked:
    #     fill(0)
    #     rect(settings_location.x, settings_location.y, settings_size.x, settings_size.y)

    #     fill(255)
    #     textSize(24)
    #     text('Settings', settings_location.x + 5, settings_location.y + 30)

    # if settings_clicked and not play_clicked:
    # making full screen and mimimized screen buttons
    #     fill(0)
    #     rect(fullscreen_location.x, fullscreen_location.y, fullscreen_size.x, fullscreen_size.y)

    #     rect(regularscreen_location.x, regularscreen_location.y, regularscreen_size.x, regularscreen_size.y)

    #     fill(0)
    #     textSize(16)
    #     text('Double click the setting',  fullscreen_location.x - 20, fullscreen_location.y - 30)

    #     fill(255)
    #     text('Full screen', fullscreen_location.x + 5, fullscreen_location.y + 20)
    #     text('Regular', regularscreen_location.x + 5, regularscreen_location.y + 20)

    # if the fullscreen/regularscreen buttons are pressed change screen size
    # if settings_clicked and regularscreen_clicked:
    #     screen = 50
    #     regularscreen_clicked = False

    # if settings_clicked and fullscreen_clicked:
    #     screen = 100
    #     fullscreen_clicked = False


def keyPressed():
    # global constant_fire

    # if key == 'q':
    #     if constant_fire:
    #         constant_fire = False
    #     else:
    #         constant_fire = True
    global key_states
    key_states[keyCode] = True

    # if key == ' ':
        # global speed, mouse, player
        # mouse = PVector(mouseX, mouseY)
        # bullets.append(PVector(player.x + 30, player.y + 30))
        # bullets.append(PVector(player.x + 15, player.y + 15))
        # bullets.append(PVector(player.x, player.y))
        # bullets.append(PVector(player.x - 15, player.y - 15))
        # bullets.append(PVector(player.x - 30, player.y - 30))

        # bullets_speed.append(trajectory(mouse, player).mult(6))
        # bullets_speed.append(trajectory(mouse, player).mult(6))
        # bullets_speed.append(trajectory(mouse, player).mult(7))
        # bullets_speed.append(trajectory(mouse, player).mult(6))
        # bullets_speed.append(trajectory(mouse, player).mult(6))

def mousePressed():
    global speed, mouse, player, play_clicked, settings_clicked, shot

    shot = True

    # if play_clicked:
    # mouse = PVector(mouseX, mouseY)
    # bullets.append(PVector(player.x, player.y))
    # bullets_speed.append(trajectory(mouse, player).mult(7))

    # play button
    # if not settings_clicked:
    #     button_end = PVector(play_location.x + play_size.x, play_location.y + play_size.y)
    #     if mouseX in range(int(play_location.x), int(button_end.x)):
    #         if mouseY in range(int(play_location.y), int(button_end.y)):
    #             play_clicked = True

    # settings button
    # settings_end = PVector(settings_location.x + settings_size.x, settings_location.y + settings_size.y)
    # if mouseX in range(int(settings_location.x), int(settings_end.x)):
    #     if mouseY in range(int(settings_location.y), int(settings_end.y)):
    #         settings_clicked = True

    # fullscreen button
    # if settings_clicked:
    #     fullscreen_end = PVector(fullscreen_location.x + fullscreen_size.x, fullscreen_location.y + fullscreen_size.y)
    #     if mouseX in range(int(fullscreen_location.x), int(fullscreen_end.x)):
    #         if mouseY in range(int(fullscreen_location.y), int(fullscreen_end.y)):
    #             fullscreen_clicked = True

    # regularscreen button
    # if settings_clicked:
    #     regularscreen_end = PVector(regularscreen_location.x + regularscreen_size.x, regularscreen_location.y + regularscreen_size.y)
    #     if mouseX in range(int(regularscreen_location.x), int(regularscreen_end.x)):
    #         if mouseY in range(int(regularscreen_location.y), int(regularscreen_end.y)):
    #             regularscreen_clicked = True

    # global regularscreen_clicked, fullscreen_clicked
    # print('regular', regularscreen_clicked, settings_clicked)
    # print('full', fullscreen_clicked, settings_clicked)
    # print(screen)

def keyReleased():
    global key_states
    key_states[keyCode] = False
