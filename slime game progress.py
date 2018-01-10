from shucks import Bullet, Player, Slime

key_states = [False for i in range(223)]

player = Player(PVector(200, 200), 40)

sm_factor = 3
b_list = []
s_list = [Slime(PVector(random(25, 750), random(25, 600)), player.lo),
          Slime(PVector(random(25, 750), random(25, 600)), player.lo),
          Slime(PVector(random(25, 750), random(25, 600)), player.lo)]

shot = False
slow_m = True
change = False

barrier1_location = PVector(200, -10)
barrier1_size = PVector(50, 400)

barrier2_location = PVector(500, 210)
barrier2_size = PVector(50, 400)

constant_fire = False
claim_rapid_rifle = False
rapid_rifle = False

score = 0
lives = 3
money = 0

weapons = 'Boring Blaster'

def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle).mult(-1)

def setup():
    size(750, 600)

def draw():
    background(209, 250, 255)
    global score, money, lives
    global change, b_done
    global constant_fire
    global shot, sm_factor
    global rapid_rifle, claim_rapid_rifle
    mouse = PVector(mouseX, mouseY)
    
    # # constant fire
    # if rapid_rifle:
    #     if constant_fire:
    #         for b in b_list:
    #                 ellipse(b.lo.x, b.lo.y, 5, 5)
    #                 b.lo.add(b.sp)
    #         global b
    #         b_list.append(PVector(player.lo.x, player.lo.y))
    #         b_list.append(trajectory(mouse, player.lo).mult(6))
    #         b_done.append(False)
    
    # makes the bullets faster
    if frameCount % 1000 == 0:
        #make the bullets faster and start the bullets slower
        pass
    
    # increases money
    if frameCount % 500 == 0:
        if money == 0:
            money += 2.0
        else:
            # do smthing that makes it so the more slimes you kill the faster the money increases
            money += (money * 1.25) // 1
    
    # makes the slimes shoot
    if frameCount % 120 == 0:
        for s in s_list:
            b_list.append(Bullet(s.lo, player.lo, False))

    fill(0)
    # Drawing barrier 1
    rect(barrier1_location.x, barrier1_location.y, barrier1_size.x, barrier1_size.y, 10)
    
    # Drawing barrier 2
    rect(barrier2_location.x, barrier2_location.y, barrier2_size.x, barrier2_size.y, 10)
    
    # Drawing player
    fill(0, 0, 80)
    ellipse(player.lo.x, player.lo.y, player.si, player.si)
    
    fill(100, 120, 200)
    textSize(18)
    # Showing weapons
    text('Weapons: ' + weapons, 20, 30)

    # Showing money
    text('Money: ' + str(money), 20, 50)

    # Showing score
    text('Score: ' + str(score), 20, 70)

    # Showing lives
    text('Lives: ' + str(lives), 20, 90)

    # Claiming the Rapid Rifle
    if money >= 150 or True:
        # Drawing claim button
        noFill()
        stroke(100, 120, 200)
        textSize(22)
        rect((width / 2) - 200, 50, 400, 80, 20)
        text('Click here to claim the Rapid Rifle', (width / 2) - 185, 95)
        stroke(50, 205, 50)
        claim_rapid_rifle = True



    # s_list for loop
    for s in s_list:
        # makes slimes atrract to player
        prev_lo = s.lo
        s.sp = trajectory(prev_lo, player.lo).mult(0.3)

        s.lo.add(s.sp)

        # Draws the slimes
        fill(21, 113, 69)
        ellipse(s.lo.x, s.lo.y, 25, 25)

        # Removes player bullets when hits slime and score increases
        for b in b_list:
            if dist(b.lo.x, b.lo.y, s.lo.x, s.lo.y) < 25 and b.p:
                s.lo = PVector(random(25, 750), random(25, 550))
                b_list.remove(b)
                score += 1
                
    # b_list for loop
    for b in b_list:
        # Draws the bullets
        fill(155, 209, 229)
        ellipse(b.lo.x, b.lo.y, 5, 5)

        # Adds the slow motion
        if slow_m and not b.done:
            b.sp.normalize()
            b.sp = b.sp.mult(sm_factor)
            b.done = True
        b.lo.add(b.sp)

        # if bullet hits player it disapears and lose a life   
        if not b.p and dist(player.lo.x, player.lo.y, b.lo.x, b.lo.y) < (player.si / 2) + 2.5:
            b_list.remove(b)
            lives -= 1

        # Removes bullets after they're off the screen
        if b.lo.x < 0 \
        or b.lo.x > width or b.lo.y < 0 \
        or b.lo.y > height:
            b_list.remove(b)
            continue

        # Removes bullets if they hit barrier 1
        if b.lo.x > barrier1_location.x and b.lo.x < barrier1_location.x + barrier1_size.x:
            if b.lo.y > barrier1_location.y and b.lo.y < barrier1_location.y + barrier1_size.y:
                b_list.remove(b)
                
        # Removes bullets if they hit barrier 2
        if b.lo.x > barrier2_location.x and b.lo.x < barrier2_location.x + barrier2_size.x:
            if b.lo.y > barrier2_location.y and b.lo.y < barrier2_location.y + barrier2_size.y:
                b_list.remove(b)
                

    # Adds bullet if shot
    if shot:
        b_list.append(Bullet(player.lo, mouse, True))
        shot = False
    
    if change:
        for b in b_list:
            b.done = False

    #Player movement
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

def keyPressed():
    global constant_fire, key_states

    if key == 'q':
         if constant_fire:
             constant_fire = False
         else:
             constant_fire = True

    key_states[keyCode] = True

def mousePressed():
    global shot, rapid_rifle, claim_rapid_rifle

    shot = True
    
    if claim_rapid_rifle:
        if mouseX > (width / 2) - 200 and mouseX < (width / 2) + 200:
            if mouseY > 50 and mouseY < 130:
                rapid_rifle = True


def keyReleased():
    global key_states, sm_factor, change
    key_states[keyCode] = False
    sm_factor = 3
    change = True
