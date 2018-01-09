from shucks import Bullet, Player, Slime

key_states = [False for i in range(223)]

player = Player(PVector(200, 200), 40)

sm_factor = 3
b_list = []
s_list = [Slime(PVector(random(25, 750), random(25, 750)), 25, player.lo),
          Slime(PVector(random(25, 750), random(25, 750)), 25, player.lo),
          Slime(PVector(random(25, 750), random(25, 750)), 25, player.lo)]

score = 0
shot = False
slow_m = True
change = False

barrier_location = PVector(100, 250)
barrier_size = PVector(70, 50)

constant_fire = False

lives = 3

def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle).mult(-1)

def setup():
    size(750, 600)

def draw():
    background(209, 250, 255)
    fill(0)
    global score, change, b_done
    global speed, player_speed, bullets_speed, slimes_speed, constant_fire
    global regularscreen_clicked, fullscreen_clicked, screen, slimes, slimes_speed
    global lives, shot
    mouse = PVector(mouseX, mouseY)

    fill(0)
    textSize(32)
    text(lives, 100, 100)
 
    if change:
        for b in b_list:
            b.done = False

    rect(barrier_location.x, barrier_location.y, barrier_size.x, barrier_size.y, 10)
    
    fill(0)
    global sm_factor
    if key_states[65]:  # left a
        player.lo.x -= 3
        sm_factor = 13
        change = True
    elif key_states[68]:  # right d
        player.lo.x += 3
        sm_factor = 13
        change = True
    if key_states[87]:  # up w
        player.lo.y -= 3
        sm_factor = 13
        change = True
    elif key_states[83]:  # down s
        player.lo.y += 3
        sm_factor = 13
        change = True

    ellipse(player.lo.x, player.lo.y, player.si, player.si)

    # showing score
    textSize(24)
    text('Score: ' + str(score), width - 150, 50)

    # # constant fire
    # if constant_fire:
    #      for i in range(len(bullets)):
    #              ellipse(bullets[i].x, bullets[i].y, 5, 5)
    #              bullets[i].add(bullets_speed[i])
    #      bullets.append(PVector(player.x, player.y))
    #      bullets_speed.append(trajectory(mouse, player).mult(6))
    #      b_done.append(False)

    # slimes bounce off walls
    for s in s_list:
        if s.lo.x < 0 or s.lo.x > width:
            s.sp.x *= (-1)
            s.lo.add(s.sp)

        elif s.lo.y < 0 or s.lo.y > height:
            s.sp.y *= -1
            s.lo.add(s.sp)

    # makes slimes atrract to player
    for s in s_list:
        if dist(player.lo.x, player.lo.y, s.lo.x, s.lo.y) < 200:
            for s in s_list:
                s.sp = trajectory(player.lo, s.lo)
                s.sp.mult(-0.5)          
                s.lo.add(s.sp)
        
    for b in b_list:
        fill(155, 209, 229)
        ellipse(b.lo.x, b.lo.y, 5, 5)
        if slow_m and not b.done:
            b.sp.normalize()
            b.sp = b.sp.mult(sm_factor)
            b.done = True
        b.lo.add(b.sp)
              
    # if bullet hits player it disapears and lose a life
    for b in b_list:
        if not b.p:
            if dist(player.lo.x, player.lo.y, b.lo.x, b.lo.y) < (player.si / 2) + 2.5:
                b_list.remove(b)
                lives -= 1
                    
    for b in b_list:
        if b.lo.x < 0 \
        or b.lo.x > width or b.lo.y < 0 \
        or b.lo.y > height:
            b_list.remove(b)
            continue
        
        if b.lo.x > barrier_location.x and b.lo.x < barrier_location.x + barrier_size.x:
            if b.lo.y > barrier_location.y and b.lo.y < barrier_location.y + barrier_size.y:
                b_list.remove(b)
        else:
            if b.lo.x > barrier_location.x and b.lo.x < barrier_location.x + barrier_size.x:
                if b.lo.y > barrier_location.y and b.lo.y < barrier_location.y + barrier_size.y:
                    b_list.remove(b)

    if shot:
        b_list.append(Bullet(player.lo, mouse, True))
        shot = False
        
    for s in s_list:
        fill(21, 113, 69)
        s.lo.add(s.sp)
        ellipse(s.lo.x, s.lo.y, s.si, s.si)
        for b in b_list:
            if dist(b.lo.x, b.lo.y, s.lo.x, s.lo.y) < 25 and b.p:
                s.lo = PVector(random(25, 750), random(25, 550))
                score += 1
                
    if frameCount % 120 == 0:
        for s in s_list:
            b_list.append(Bullet(s.lo, player.lo, False))

                    
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
