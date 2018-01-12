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

bar1_loc = PVector(200, -10)
bar1_size = PVector(50, 400)

bar2_loc = PVector(500, 210)
bar2_size = PVector(50, 400)

health_loc = PVector(200, 200)
health_size = 60
health_pack = True

constant_fire = False
claim_rapid_rifle = False
rapid_rifle = False

score = 0
health = 80
money = 0

weapons = ['Boring Blaster']
weap_show = ''

res_loc = PVector(175, 50) 
res_si = PVector(400, 100)

# no_spawn1 = PVector([i for i in range(int(bar1_loc.x), int(bar1_loc.x + bar1_size.x))], 
#                     [i for i in range(int(bar1_loc.y), int(bar1_loc.y + bar1_size.y))])

# no_spawn1 = PVector([i for i in range(int(bar2_loc.x), int(bar2_loc.x + bar2_size.x))],
#                     [i for i in range(int(bar2_loc.y), int(bar2_loc.y + bar2_size.y))])

no_spawn1x = [i for i in range(int(bar1_loc.x - health_size / 2), int(bar1_loc.x + bar1_size.x + health_size / 2))]
no_spawn1y = [i for i in range(int(bar1_loc.y - health_size / 2), int(bar1_loc.y + bar1_size.y + health_size / 2))]

no_spawn2x = [i for i in range(int(bar2_loc.x - health_size / 2), int(bar2_loc.x + bar2_size.x + health_size / 2))]
no_spawn2y = [i for i in range(int(bar2_loc.y - health_size / 2), int(bar2_loc.y + bar2_size.y + health_size / 2))]

def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle).mult(-1)

def midpoint(x1, y1, x2, y2, x3, y3):
    mid = PVector((x1 + x2 + x3) / 3, (y1 + y2 + y3) / 3)
    return mid

def in_barrier(v):
    if (int(v.x) in no_spawn1x) and (int(v.y) in no_spawn1y) \
    or (int(v.x) in no_spawn2x) and (int(v.y) in no_spawn2y):
        return True
    else:
        return False

def setup():
    size(750, 600)

def draw():
    background(209, 250, 255)
    global score, money, health
    global change, b_done
    global constant_fire
    global shot, sm_factor
    global rapid_rifle, claim_rapid_rifle
    global health_pack, health_loc, health_size, health
    global circle
    global weap_show
    mouse = PVector(mouseX, mouseY)
    
    if health > 0: 
        if health > 100:
            health = 100
    
        # constant fire
        # if rapid_rifle or True:
        #     if constant_fire:
        #         for b in b_list:
        #             ellipse(b.lo.x, b.lo.y, 5, 5)
        #         b.lo.add(b.sp)
        #         b_list.append(PVector(player.lo.x, player.lo.y))
        #         b_list.append(Bullet)
        #         b_list.append(player.lo)
        #         b_list.append(mouse)
        #         b_list.append(False)
                
        # add a auto shoot for every 10 seconds
        
        
        
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

        if frameCount % 1800 == 0:
            health_loc = PVector(random(30, 720), random(30, 570))
            while in_barrier(health_loc):
                health_loc = PVector(random(30, 720), random(30, 570))
            health_pack = True
            
        if frameCount % 2400 == 0:
            health_pack = False
    
        noFill()
        # Drawing bar 1
        rect(bar1_loc.x, bar1_loc.y, bar1_size.x, bar1_size.y, 10)
        
        # Drawing bar 2
        rect(bar2_loc.x, bar2_loc.y, bar2_size.x, bar2_size.y, 10)
        
        # Drawing health pack
        if health_pack:
            fill(255)
            noStroke()
            ellipse(health_loc.x, health_loc.y, health_size, health_size)
            fill(128, 0, 0)
            rect(health_loc.x - 5, health_loc.y - 20, 10, 40)
            rect(health_loc.x - 20, health_loc.y - 5, 40, 10)
            
        stroke(100, 120, 200)
        # Drawing player
        fill(0, 0, 80)
        ellipse(player.lo.x, player.lo.y, player.si, player.si)
        
        fill(100, 120, 200)
        textSize(18)
        # Showing weapons
        for weapon in weapons:
            if weapon not in weap_show:
                weap_show += weapon + ' '
        text('Weapons: ' + weap_show, 20, 30)
    
        # Showing money
        text('Money: ' + str(money), 20, 50)
    
        # Showing score
        text('Score: ' + str(score), 20, 70)
    
        # Showing health
        text('Health: ' + str(health), 20, 90)
    
        # Claiming the Rapid Rifle
        if money >= 150:
            # Drawing claim button
            noFill()
            stroke(100, 120, 200)
            textSize(22)
            rect((width / 2) - 200, 50, 400, 80, 20)
            text('Click here to claim the Rapid Rifle', (width / 2) - 185, 95)
            stroke(50, 205, 50)
            claim_rapid_rifle = True
    
        # Collecting health packs
        h_p_dist = dist(player.lo.x, player.lo.y, health_loc.x, health_loc.y)
        if h_p_dist < (player.si / 2) + (health_size / 2) and health_pack:
            health_pack = False
            health += 20
    
        # s_list for loop
        for s in s_list:
            # makes slimes atrract to player
            s.sp = trajectory(s.lo, player.lo).mult(0.2)# Adds the slow motion
            if slow_m and not s.done:
                s.sp.normalize()
                s.sp = s.sp.mult(sm_factor).mult(0.1)
                s.done = True
            s.lo.add(s.sp)
    
            # if s.lo.x in no_spawn1x:
            #     if s.lo.x < (bar_loc.x + bar_si.x) / 2:
            #         s.lo.x = bar_loc.x
    
            # Draws the slimes
            fill(21, 113, 69)
            ellipse(s.lo.x, s.lo.y, 25, 25)
    
            # Removes player bullets when hits slime and score increases
            for b in b_list:
                if dist(b.lo.x, b.lo.y, s.lo.x, s.lo.y) < 25 and b.p:
                    s.lo = PVector(random(25, 750), random(25, 550))
                    while in_barrier(s.lo):
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
                health -= 10
    
            # Removes bullets after they're off the screen
            if b.lo.x < 0 \
            or b.lo.x > width or b.lo.y < 0 \
            or b.lo.y > height:
                b_list.remove(b)
                continue
    
            # Removes bullets if they hit barrier 1
            if b.lo.x > bar1_loc.x and b.lo.x < bar1_loc.x + bar1_size.x:
                if b.lo.y > bar1_loc.y and b.lo.y < bar1_loc.y + bar1_size.y:
                    b_list.remove(b)
                    
            # Removes bullets if they hit barrier 2
            if b.lo.x > bar2_loc.x and b.lo.x < bar2_loc.x + bar2_size.x:
                if b.lo.y > bar2_loc.y and b.lo.y < bar2_loc.y + bar2_size.y:
                    b_list.remove(b)
                    
    
        # Adds bullet if shot
        if shot:
            b_list.append(Bullet(player.lo, mouse, True))
            shot = False
        
        if change:
            for b in b_list:
                b.done = False
            for s in s_list:
                s.done = False
    
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
            
    else:
        if health < 0:
            health = 0
            
        # Drawing restart button
        fill(255)
        rect(res_loc.x, res_loc.y, res_si.x, res_si.y, 20)
        fill(155, 209, 229)
        textSize(72)
        text('Restart', (((res_loc.x + res_si.x) / 2) - 50), res_loc.y + res_si.y - 20)
        
        # Showing scores    
        textSize(72)
        text('GAME OVER', 200, 300)
        textSize(32)
        text('Score: ' + str(score), 200, 350)
        text('Money: ' + str(money), 200, 390)
        text('Health: ' + str(health), 200, 430)

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
    global health, money, score
    shot = True
    
    if claim_rapid_rifle:
        if mouseX > (width / 2) - 200 and mouseX < (width / 2) + 200:
            if mouseY > 50 and mouseY < 130:
                rapid_rifle = True
                
                
    if health <= 0:
        if mouseX > res_loc.x and mouseX < res_loc.x + res_si.x \
        and mouseY > res_loc.y and mouseY < res_loc.y + res_si.y:
            health = 100
            money = 0
            score = 0
            b_list = []
            s_list = [Slime(PVector(random(25, 750), random(25, 600)), player.lo),
                      Slime(PVector(random(25, 750), random(25, 600)), player.lo),
                      Slime(PVector(random(25, 750), random(25, 600)), player.lo)]
            

def keyReleased():
    global key_states, sm_factor, change
    key_states[keyCode] = False
    sm_factor = 3
    change = True
