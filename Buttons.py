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

    # play button
    # if not play_clicked and not settings_clicked:
    #     fill(0)
    #     rect(play_location.x, play_location.y, play_size.x, play_size.y)

    #     fill(255)
    #     textSize(32)
    #     text('PLAY', play_location.x + 10, play_location.y + 30)

    # if button clicked start game
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
