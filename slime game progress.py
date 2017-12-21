key_states = [False for i in range(223)]

screen = 100
width = int(screen * 7.5)
height = int(screen * 6)

bullets_speed = []
bullets = []
slimes = [PVector(random(25, 750), random(25, 550)), 
          PVector(random(25, 750), random(25, 550)), 
          PVector(random(25, 750), random(25, 550))]

slimes_speed = [PVector(random(-0.5, 0.5), random(-0.5, 0.5)),
                PVector(random(-0.5, 0.5), random(-0.5, 0.5)),
                PVector(random(-0.5, 0.5), random(-0.5, 0.5))]

score = 0
shot = False

player = PVector(200, 200)
player_size = 40
player_speed = PVector(0, 0)

barrier_location = PVector(100, 250)
barrier_size = PVector(700, 50)

constant_fire = False

def setup():
    size(width, height)


def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle)

def draw():
    background(209, 250, 255)
    fill(0)
    global score
    global speed, player_speed, bullets_speed, slimes_speed, constant_fire
    global regularscreen_clicked, fullscreen_clicked, screen, slimes, slimes_speed
    mouse = PVector(mouseX, mouseY)
    


    rect(barrier_location.x, barrier_location.y, barrier_size.x, barrier_size.y, 10)
    
    fill(0)
    
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
    if constant_fire:
         for i in range(len(bullets)):
                 ellipse(bullets[i].x, bullets[i].y, 5, 5)
                 bullets[i].add(bullets_speed[i])
         bullets.append(PVector(player.x, player.y))
         bullets_speed.append(trajectory(mouse, player).mult(6))

# if slow_mo:
#     bullets_speed *= 2
#     player_speed *= 2

    # slimes bounce off walls
    for s in range(len(slimes)):
        if slimes[s].x < 0 or slimes[s].x > width:
            print('x')
            slimes_speed[s].x *= (-1)
            slimes[s].add(slimes_speed[s])

        elif slimes[s].y < 0 or slimes[s].y > height:
            print('y')
            slimes_speed[s].y *= -1
            slimes[s].add(slimes_speed[s])


    # makes slimes atrract to player
    for s in range(len(slimes)):
        if dist(player.x, player.y, slimes[s].x, slimes[s].y) < 200:
            for x in range(len(slimes)):
                slimes_speed[s] = (trajectory(slimes[s], player))
                slimes_speed[s].mult(0.1)
                slimes[s].add(slimes_speed[s].mult(-1))
        
    # if shot adds a bullet to the game
    global shot
    if shot:
        bullets.append(PVector(player.x, player.y))
        bullets_speed.append(trajectory(mouse, player).mult(7))
        shot = False
        
    for i in range(len(bullets)):
        
        #   if bullets > barrier.y and :
            fill(155, 209, 229)
            ellipse(bullets[i].x, bullets[i].y, 5, 5)
            bullets[i].add(bullets_speed[i])
            for x in range(len(slimes)):
                
                if dist(bullets[i].x, bullets[i].y, slimes[x].x, slimes[x].y) < 25:
                    
                    slimes[x] = PVector(random(25, 750), random(25, 550))
                    score += 1
    for i in range(len(bullets)):
        if i >= len(bullets):
            break
            
        if bullets[i].x < 0 or bullets[i].x > width or bullets[i].y < 0 or bullets[i].y > height:
            bullets.remove(bullets[i])
            bullets_speed.remove(bullets_speed[i])
            continue
        
        if bullets[i].x > barrier_location.x and bullets[i].x < barrier_location.x + barrier_size.x:
            if bullets[i].y > barrier_location.y and bullets[i].y < barrier_location.y + barrier_size.y:
                bullets.remove(bullets[i])
                bullets_speed.remove(bullets_speed[i])
                
        else:
            if bullets[i].x > barrier_location.x and bullets[i].x < barrier_location.x + barrier_size.x:
                if bullets[i].y > barrier_location.y and bullets[i].y < barrier_location.y + barrier_size.y:
                    bullets.remove(bullets[i])
                    bullets_speed.remove(bullets_speed[i])
            
        
    

        
    for i in range(len(slimes)):
        fill(21, 113, 69)
        slimes[i].add(slimes_speed[i])
        ellipse(slimes[i].x, slimes[i].y, 25, 25)

def keyPressed():
    global constant_fire

    if key == 'q':
         if constant_fire:
             constant_fire = False
         else:
             constant_fire = True
    global key_states
    key_states[keyCode] = True

def mousePressed():
    global speed, mouse, player, play_clicked, settings_clicked, shot

    shot = True

def keyReleased():
    global key_states
    key_states[keyCode] = False
