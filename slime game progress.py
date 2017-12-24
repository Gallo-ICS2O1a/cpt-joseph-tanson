key_states = [False for i in range(223)]

screen = 100
width = int(screen * 7.5)
height = int(screen * 6)

sm_factor = 3
b_done = []
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
slow_m = True
change = False

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
    global score, change, b_done
    global speed, player_speed, bullets_speed, slimes_speed, constant_fire
    global regularscreen_clicked, fullscreen_clicked, screen, slimes, slimes_speed
    mouse = PVector(mouseX, mouseY)
    
    if change:
        b_done = [False for b in b_done]
    


    rect(barrier_location.x, barrier_location.y, barrier_size.x, barrier_size.y, 10)
    
    fill(0)
    global sm_factor
    if key_states[65]:  # left a
        player.x -= 3
        sm_factor = 6
        change = True
    elif key_states[68]:  # right d
        player.x += 3
        sm_factor = 6
        change = True
    if key_states[87]:  # up w
        player.y -= 3
        sm_factor = 6
        change = True
    elif key_states[83]:  # down s
        player.y += 3
        sm_factor = 6
        change = True

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
         b_done.append(False)

# if slow_mo:
#     bullets_speed *= 2
#     player_speed *= 2

    # slimes bounce off walls
    


    # makes slimes atrract to player
    for s in range(len(slimes)):
        if dist(player.x, player.y, slimes[s].x, slimes[s].y) < 50:
            print('sss')
            for x in range(len(slimes)):
                slimes_speed[x] = trajectory(slimes[x], player)
                slimes[x].add(slimes_speed[x].mult(-1))
        
    for i in range(len(bullets)):
    #   if bullets > barrier.y and :
        fill(155, 209, 229)
        ellipse(bullets[i].x, bullets[i].y, 5, 5)
        if slow_m and not b_done[i]:
            bullets_speed[i].normalize()
            bullets_speed[i] = bullets_speed[i].mult(sm_factor)
            b_done[i] = True
        bullets[i].add(bullets_speed[i])
                
    for i in range(len(bullets)):
        if i >= len(bullets):
            break
            
        if bullets[i].x < 0 or bullets[i].x > width or bullets[i].y < 0 or bullets[i].y > height:
            bullets.remove(bullets[i])
            bullets_speed.remove(bullets_speed[i])
            b_done.remove(b_done[i])
            continue
        
        if bullets[i].x > barrier_location.x and bullets[i].x < barrier_location.x + barrier_size.x:
            if bullets[i].y > barrier_location.y and bullets[i].y < barrier_location.y + barrier_size.y:
                bullets.remove(bullets[i])
                bullets_speed.remove(bullets_speed[i])
                b_done.remove(b_done[i])
        else:
            if bullets[i].x > barrier_location.x and bullets[i].x < barrier_location.x + barrier_size.x:
                if bullets[i].y > barrier_location.y and bullets[i].y < barrier_location.y + barrier_size.y:
                    bullets.remove(bullets[i])
                    bullets_speed.remove(bullets_speed[i])
                    b_done.remove(b_done[i])
        
    
    global shot
    if shot:
        bullets.append(PVector(player.x, player.y))
        bullets_speed.append(trajectory(mouse, player).mult(7))
        b_done.append(False)
        shot = False
        
    for i in range(len(slimes)):
        fill(21, 113, 69)
        slimes[i].add(slimes_speed[i])
        ellipse(slimes[i].x, slimes[i].y, 25, 25)
        for x in range(len(bullets)):
            if dist(bullets[x].x, bullets[x].y, slimes[i].x, slimes[i].y) < 25:
                slimes[i] = PVector(random(25, 750), random(25, 550))
                score += 1

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
    global key_states, sm_factor, change
    key_states[keyCode] = False
    sm_factor = 3
    change = True

          
          
# EXTRA CODE **STILL NEEDS TO BE COMBINED**

key_states = [False for i in range(223)]

screen = 100
width = int(screen * 7.5)
height = int(screen * 6)

sm_factor = 3
b_done = []
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
slow_m = True
change = False

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
    global score, change, b_done
    global speed, player_speed, bullets_speed, slimes_speed, constant_fire
    global regularscreen_clicked, fullscreen_clicked, screen, slimes, slimes_speed
    mouse = PVector(mouseX, mouseY)
    
    if change:
        b_done = [False for b in b_done]
    


    rect(barrier_location.x, barrier_location.y, barrier_size.x, barrier_size.y, 10)
    
    fill(0)
    global sm_factor
    if key_states[65]:  # left a
        player.x -= 3
        sm_factor = 6
        change = True
    elif key_states[68]:  # right d
        player.x += 3
        sm_factor = 6
        change = True
    if key_states[87]:  # up w
        player.y -= 3
        sm_factor = 6
        change = True
    elif key_states[83]:  # down s
        player.y += 3
        sm_factor = 6
        change = True

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
         b_done.append(False)

# if slow_mo:
#     bullets_speed *= 2
#     player_speed *= 2

    # slimes bounce off walls
    


    # makes slimes atrract to player
    for s in range(len(slimes)):
        if dist(player.x, player.y, slimes[s].x, slimes[s].y) < 50:
            print('sss')
            for x in range(len(slimes)):
                slimes_speed[x] = trajectory(slimes[x], player)
                slimes[x].add(slimes_speed[x].mult(-1))
        
    for i in range(len(bullets)):
    #   if bullets > barrier.y and :
        fill(155, 209, 229)
        ellipse(bullets[i].x, bullets[i].y, 5, 5)
        if slow_m and not b_done[i]:
            bullets_speed[i].normalize()
            bullets_speed[i] = bullets_speed[i].mult(sm_factor)
            b_done[i] = True
        bullets[i].add(bullets_speed[i])
                
    for i in range(len(bullets)):
        if i >= len(bullets):
            break
            
        if bullets[i].x < 0 or bullets[i].x > width or bullets[i].y < 0 or bullets[i].y > height:
            bullets.remove(bullets[i])
            bullets_speed.remove(bullets_speed[i])
            b_done.remove(b_done[i])
            continue
        
        if bullets[i].x > barrier_location.x and bullets[i].x < barrier_location.x + barrier_size.x:
            if bullets[i].y > barrier_location.y and bullets[i].y < barrier_location.y + barrier_size.y:
                bullets.remove(bullets[i])
                bullets_speed.remove(bullets_speed[i])
                b_done.remove(b_done[i])
        else:
            if bullets[i].x > barrier_location.x and bullets[i].x < barrier_location.x + barrier_size.x:
                if bullets[i].y > barrier_location.y and bullets[i].y < barrier_location.y + barrier_size.y:
                    bullets.remove(bullets[i])
                    bullets_speed.remove(bullets_speed[i])
                    b_done.remove(b_done[i])
        
    
    global shot
    if shot:
        bullets.append(PVector(player.x, player.y))
        bullets_speed.append(trajectory(mouse, player).mult(7))
        b_done.append(False)
        shot = False
        
    for i in range(len(slimes)):
        fill(21, 113, 69)
        slimes[i].add(slimes_speed[i])
        ellipse(slimes[i].x, slimes[i].y, 25, 25)
        for x in range(len(bullets)):
            if dist(bullets[x].x, bullets[x].y, slimes[i].x, slimes[i].y) < 25:
                slimes[i] = PVector(random(25, 750), random(25, 550))
                score += 1

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
    global key_states, sm_factor, change
    key_states[keyCode] = False
    sm_factor = 3
    change = True
