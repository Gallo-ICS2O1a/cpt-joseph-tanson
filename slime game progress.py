# moving and shooting added together
# moving and shooting added together
# moving and shooting added together

screen = 100
speeds = []
bullets = []
slimes = [PVector(random(25, 750), random(25, 550))]

player = PVector(200, 200)
player_size = 100
player_speed = PVector(0, 0)

def setup():
    size(int(screen * 7.5), int(screen * 6))
    
def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle)

def draw():
    background(255)
    fill(0)
    noStroke()
    
    player.add(player_speed)
    ellipse(player.x, player.y, player_size, player_size)
    global speed
    background(255)
    
    mouse = PVector(mouseX, mouseY)
    ellipse(player.x, player.y, 50, 50)
    point(mouse.x, mouse.y)
    
    for i in range(len(bullets)):
        ellipse(bullets[i].x, bullets[i].y, 5, 5)
        bullets[i].add(speeds[i])
        if dist(bullets[i].x, bullets[i].y, slimes[0].x, slimes[0].y) < 25:
            slimes[0].x, slimes[0].y = random(25, 750), random(25, 500)
    ellipse(slimes[0].x, slimes[0].y, 25, 25)

def keyPressed():
    
    global w, a, s, d
    
    if key == 'w':
        player_speed.y -= 5
    if key == 'a':
        player_speed.x -= 5
    if key == 's':
        player_speed.y += 5
    if key == 'd':
        player_speed.x += 5
      
def mousePressed():
    global speed, mouse, player
    mouse = PVector(mouseX, mouseY)
    bullets.append(PVector(player.x, player.y))
    speeds.append(trajectory(mouse, player).mult(7))
        
def keyReleased():
    if key == 'w' or key == 's':
        player_speed.y = 0
    if key == 'a' or key == 'd':
        player_speed.x = 0

        
# button and attempt in slime movement, slow_mo
# button and attempt in slime movement, slow_mo
# button and attempt in slime movement, slow_mo

screen = 100
bullets_speed = []
bullets = []
slimes = [PVector(random(25, 750), random(25, 550))]
slimes_speed = PVector(1, 1)
score = 0

player = PVector(200, 200)
player_size = 100
player_speed = PVector(0, 0)

barrier = PVector(100, 100)
barrier_size = PVector(100, 500)

slow_mo = False

width = int(screen * 7.5)
height = int(screen * 6)

button_location = PVector((width / 2) - 50, (height / 2))
button_clicked = False
button_size = PVector(100, 50)

def setup():
    size(int(screen * 7.5), int(screen * 6))


def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle)

def draw():
    background(255)
    fill(0)
    global speed, score, player_speed, bullets_speed, slimes_speed
    
    if slow_mo:
        bullets_speed *= 2
        player_speed *= 2
        slimes_speed *= 2
        
    # slimes bouncing off walls
    if slimes[0].x > width or slimes[0].y < 0:
        slimes_speed.x *= -1
    elif slimes[0].y > width or slimes[0].y < 0:
        slimes_speed.y *= -1
    
    
    if not button_clicked:    
        fill(0)
        rect(button_location.x, button_location.y, button_size.x, button_size.y)
        
        fill(255)
        textSize(32)
        text('PLAY', button_location.x + 10, button_location.y + 30)

    fill(0)
    if button_clicked:
        player.add(player_speed)
        ellipse(player.x, player.y, player_size, player_size)
        
        mouse = PVector(mouseX, mouseY)
        ellipse(player.x, player.y, 50, 50)
        point(mouse.x, mouse.y)
        
        textSize(24)
        text('Score: ' + str(score), width - 100, 50)
        

        for i in range(len(bullets)):
        #   if bullets > barrier.y and :
            ellipse(bullets[i].x, bullets[i].y, 5, 5)
            bullets[i].add(bullets_speed[i])
            if dist(bullets[i].x, bullets[i].y, slimes[0].x, slimes[0].y) < 25:
                slimes[0].x, slimes[0].y = random(25, 750), random(25, 500)
                score += 1
        slimes[0].add(slimes_speed)
        ellipse(slimes[0].x, slimes[0].y, 25, 25)
   
def keyPressed():
    
    global w, a, s, d
    
    if key == 'w':
        player_speed.y -= 5
        slow_mo = True
        
    if key == 'a':
        player_speed.x -= 5
        slow_mo = True
        
    if key == 's':
        player_speed.y += 5
        slow_mo = True
        
    if key == 'd':
        player_speed.x += 5
        slow_mo = True
        
    if key == ' ':
        global speed, mouse, player
        mouse = PVector(mouseX, mouseY)
        bullets.append(PVector(player.x, player.y))
        bullets_speed.append(trajectory(mouse, player).mult(7))

def mousePressed():
    global speed, mouse, player, button_clicked
    
    mouse = PVector(mouseX, mouseY)
    bullets.append(PVector(player.x, player.y))
    bullets_speed.append(trajectory(mouse, player).mult(7))
     
    button_end = PVector(button_location.x + button_size.x, button_location.y + button_size.y)
    if mouseX in range(int(button_location.x), int(button_end.x)) and mouseY in range(int(button_location.y), int(button_end.y)):
        button_clicked = True
    
        
def keyReleased():
    if key == 'w' or key == 's':
        player_speed.y = 0
        slow_mo = False
        
    if key == 'a' or key == 'd':
        player_speed.x = 0
        slow_mo = False
    
# created functional settings button and semi-functional full and regular screen button
# created functional settings button and semi-functional full and regular screen button
# created functional settings button and semi-functional full and regular screen button

screen = 100
bullets_speed = []
bullets = []
slimes = [PVector(random(25, 750), random(25, 550))]
slimes_speed = PVector(1, 1)
score = 0

player = PVector(200, 200)
player_size = 100
player_speed = PVector(0, 0)

barrier = PVector(100, 100)
barrier_size = PVector(100, 500)

slow_mo = False

width = int(screen * 7.5)
height = int(screen * 6)

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
    
    
    
    
    # play button
    if not play_clicked and not settings_clicked:    
        fill(0)
        rect(play_location.x, play_location.y, play_size.x, play_size.y)
        
        fill(255)
        textSize(32)
        text('PLAY', play_location.x + 10, play_location.y + 30)

    # if button clicked start game
    fill(0)
    if play_clicked and not settings_clicked:
        player.add(player_speed)
        ellipse(player.x, player.y, player_size, player_size)
        
        mouse = PVector(mouseX, mouseY)
        ellipse(player.x, player.y, 50, 50)
        point(mouse.x, mouse.y)
        
        # showing score
        textSize(24)
        text('Score: ' + str(score), width - 150, 50)
        
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
            if dist(bullets[i].x, bullets[i].y, slimes[0].x, slimes[0].y) < 25:
                slimes[0].x, slimes[0].y = random(25, 750), random(25, 500)
                score += 1
        slimes[0].add(slimes_speed)
        ellipse(slimes[0].x, slimes[0].y, 25, 25)
   
   
   
    # settings for changing screen size
    if not settings_clicked and not play_clicked:
        fill(0)
        rect(settings_location.x, settings_location.y, settings_size.x, settings_size.y)
        
        fill(255)
        textSize(24)
        text('Settings', settings_location.x + 5, settings_location.y + 30)

    if settings_clicked and not play_clicked:
        # making full screen and mimimized screen buttons
        fill(0)
        rect(fullscreen_location.x, fullscreen_location.y, fullscreen_size.x, fullscreen_size.y)
        
        rect(regularscreen_location.x, regularscreen_location.y, regularscreen_size.x, regularscreen_size.y)
        
        fill(0)
        textSize(16)
        text('Double click the setting',  fullscreen_location.x - 20, fullscreen_location.y - 30)
        
        fill(255)
        text('Full screen', fullscreen_location.x + 5, fullscreen_location.y + 20)
        text('Regular', regularscreen_location.x + 5, regularscreen_location.y + 20)
        
    # if the fullscreen/regularscreen buttons are pressed change screen size
    if settings_clicked and regularscreen_clicked:
        screen = 50
        regularscreen_clicked = False
    
    if settings_clicked and fullscreen_clicked:
        screen = 100
        fullscreen_clicked = False


def keyPressed():
    
    if key == 'w':
        player_speed.y -= 5
        slow_mo = True
        
    if key == 'a':
        player_speed.x -= 5
        slow_mo = True
        
    if key == 's':
        player_speed.y += 5
        slow_mo = True
        
    if key == 'd':
        player_speed.x += 5
        slow_mo = True
        
    if key == ' ':
        global speed, mouse, player
        mouse = PVector(mouseX, mouseY)
        bullets.append(PVector(player.x, player.y))
        bullets_speed.append(trajectory(mouse, player).mult(7))

def mousePressed():
    global speed, mouse, player, play_clicked, settings_clicked
    
    mouse = PVector(mouseX, mouseY)
    bullets.append(PVector(player.x, player.y))
    bullets_speed.append(trajectory(mouse, player).mult(7))
     
    # play button 
    if not settings_clicked:
        button_end = PVector(play_location.x + play_size.x, play_location.y + play_size.y)
        if mouseX in range(int(play_location.x), int(button_end.x)):
            if mouseY in range(int(play_location.y), int(button_end.y)):
                play_clicked = True
    
    # settings button
    settings_end = PVector(settings_location.x + settings_size.x, settings_location.y + settings_size.y)
    if mouseX in range(int(settings_location.x), int(settings_end.x)):
        if mouseY in range(int(settings_location.y), int(settings_end.y)):
            settings_clicked = True
    
    # fullscreen button
    if settings_clicked:
        fullscreen_end = PVector(fullscreen_location.x + fullscreen_size.x, fullscreen_location.y + fullscreen_size.y)
        if mouseX in range(int(fullscreen_location.x), int(fullscreen_end.x)):
            if mouseY in range(int(fullscreen_location.y), int(fullscreen_end.y)):
                fullscreen_clicked = True
    
    #regularscreen button
    if settings_clicked:
        regularscreen_end = PVector(regularscreen_location.x + regularscreen_size.x, regularscreen_location.y + regularscreen_size.y)
        if mouseX in range(int(regularscreen_location.x), int(regularscreen_end.x)):
            if mouseY in range(int(regularscreen_location.y), int(regularscreen_end.y)):
                regularscreen_clicked = True
                
    global regularscreen_clicked, fullscreen_clicked
    print('regular', regularscreen_clicked, settings_clicked)
    print('full', fullscreen_clicked, settings_clicked)
    print(screen)
    
def keyReleased():
    if key == 'w' or key == 's':
        player_speed.y = 0
        slow_mo = False
        
    if key == 'a' or key == 'd':
        player_speed.x = 0
        slow_mo = False
        
        
        
        
        
