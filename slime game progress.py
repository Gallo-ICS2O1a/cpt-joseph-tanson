from shucks import Bullet, Player, Slime

key_states = [False for i in range(223)]

player = Player(PVector(375, 300), 40)

sm_factor = 3
b_list = []

key_states = [False for i in range(223)]

player = Player(PVector(375, 300), 40)

sm_factor = 3
b_list = []
s_list = [Slime(PVector(random(25, 750), random(25, 600)), player.lo),
          Slime(PVector(random(25, 750), random(25, 600)), player.lo),
          Slime(PVector(random(25, 750), random(25, 600)), player.lo)]

shot = False
slow_m = True
change = True

bar1_loc = PVector(200, -10)
bar1_size = PVector(50, 400)

bar2_loc = PVector(500, 210)
bar2_size = PVector(50, 400)

health_loc = PVector(100, 200)
health_size = 60
health_pack = True

claim_rapid_rifle = False
rapid_rifle = False
rrclaimed = False

score = 0
health = 80
money = 0
ammo = 0

weapons = ['Boring Blaster']
weap_show = ''

res_loc = PVector(175, 50)
res_si = PVector(400, 100)

no_spawn1x = [i for i in range(int(bar1_loc.x), int(bar1_loc.x + bar1_size.x))]
no_spawn1y = [i for i in range(int(bar1_loc.y), int(bar1_loc.y + bar1_size.y))]

no_spawn2x = [i for i in range(int(bar2_loc.x), int(bar2_loc.x + bar2_size.x))]
no_spawn2y = [i for i in range(int(bar2_loc.y), int(bar2_loc.y + bar2_size.y))]

play_loc = PVector(100, 150)
play_si = PVector(550, 150)

menu = True

auto_fire = False
af_freq = 600
claim_af = False

shoot_freq = 200

play_fill = 255

bs_fac = 1


def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle).mult(-1)



def in_barrier(v):
    if (
        (int(v.x) in no_spawn1x) and (int(v.y) in no_spawn1y) or
        (int(v.x) in no_spawn2x) and (int(v.y) in no_spawn2y)
    ):
        return True
    else:
        return False


def setup():
    size(750, 600)


def draw():
    global rrclaimed, rapid_rifle, claim_rapid_rifle
    global bar1_loc, bar1_size, bar2_loc, bar2_size
    global health_pack, health_loc, health_size
    global score, money, health, ammo
    global change, b_done
    global shoot_freq
    global weap_show
    global play_fill
    global sm_factor
    global claim_af
    global bs_fac
    global shot
    background(209, 250, 255)
    mouse = PVector(mouseX, mouseY)

    if menu:
        # Play button
        noStroke()
        textSize(72)
        if frameCount % 60 == 0:
            play_fill = 255
        if frameCount % 80 == 0:
            play_fill = 247
        fill(play_fill)
        rect(play_loc.x, play_loc.y, play_si.x, play_si.y, 20)
        fill(155, 209, 229)
        text('PLAY SHUCKS', 140, 250)

        # Showing controls
        fill(255)
        rect(337.5, 450, 75, 75, 20)
        rect(337.5, 375, 75, 75, 20)
        rect(262.5, 450, 75, 75, 20)
        rect(412.5, 450, 75, 75, 20)

        fill(155, 209, 229)
        textSize(65)
        text('W', 347, 442)
        text('S', 357, 510)
        text('A', 277, 510)
        text('D', 426, 510)

        textSize(32)
        text('Use Mouse to Aim and Fire', 180, 570)

    elif health > 0:

        if health > 100 : health = 100

        # constant fire
        if rapid_rifle and frameCount % 5 == 0 and ammo > 0:
            b_list.append(Bullet(player.lo, mouse, True))
            ammo -= 1

        # Auto firing
        if auto_fire and frameCount % af_freq == 0:
            for s in s_list:
                b_list.append(Bullet(player.lo, s.lo, True))

        # increases money
        if frameCount % 300 == 0 : money += 15

        # makes the slimes shoot
        if frameCount % shoot_freq == 0:
            for s in s_list:
                b_list.append(Bullet(s.lo, player.lo, False))

        # Spawning health packs
        if frameCount % 1800 == 0:
            health_loc = PVector(random(30, 720), random(30, 570))
            while in_barrier(health_loc):
                health_loc = PVector(random(30, 720), random(30, 570))
            health_pack = True

        if frameCount % 2400 == 0:
            health_pack = False

        # increase freq slimes shoot and speed of bullets
        if frameCount % 1200 == 0:
            shoot_freq = int(shoot_freq * 0.95)
            for b in b_list:
                if not b.p:
                    bs_fac *= 1.05

        stroke(0)
        fill(255)
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

        # Drawing player
        stroke(100, 120, 200)
        fill(0, 0, 80)
        ellipse(player.lo.x, player.lo.y, player.si, player.si)

        fill(100, 120, 200)
        textSize(18)
        # Showing weapons
        for weapon in weapons:
            if weapon not in weap_show : weap_show += weapon + ' / '
        text('Weapons: ' + weap_show, 20, 30)

        # Showing auto shooting level
        if auto_fire:
            af_level = str((af_freq / 60) * -1 + 10)
            if af_level == '9':
                af_level = 'max.'
            text('Auto Shoot lv: ' + af_level, 550, 30)

        # Showing money
        text('Money: $' + str(money), 20, 50)

        # Showing score
        text('Score: ' + str(score), 20, 70)

        # Showing health
        text('Health: ' + str(health), 20, 90)

        # Showing ammo
        if rrclaimed and ammo != 0 : text('RR Ammo: ' + str(ammo), 20, 110)

        # Claiming the Rapid Rifle
        if money >= 150 and ammo == 0:
            # Drawing claim button
            noFill()
            stroke(100, 120, 200)
            textSize(22)
            rect(450, 50, 130, 100, 20)
            text('Rapid Rifle', 460, 80)
            text('$150', 460, 110)
            text('(press "Q")', 460, 140)
            claim_rapid_rifle = True

        # Buying auto fires
        if money >= 100 and af_freq > 60:
            noFill()
            stroke(100, 120, 200)
            textSize(22)
            rect(600, 50, 130, 100, 20)
            text('Auto Shoot', 610, 80)
            text('$100', 610, 120)
            claim_af = True

        # Collecting health packs
        h_p_dist = dist(player.lo.x, player.lo.y, health_loc.x, health_loc.y)
        if h_p_dist < (player.si / 2) + (health_size / 2) and health_pack:
            health_pack = False
            health += 20

        # s_list for loop
        for s in s_list:

            # makes slimes atrract to player
            s.sp = trajectory(s.lo, player.lo).mult(0.2)  # Adds the slow mo
            if slow_m and not s.done:
                s.sp.normalize()
                s.sp = s.sp.mult(sm_factor).mult(0.1)
                s.done = True
            if in_barrier(PVector(s.lo.x + s.sp.x, s.lo.y + s.sp.y)):
                s.sp = PVector(s.sp.x * 0.22, s.sp.y * 0.22)
            s.lo.add(s.sp)

            # Draws the slimes
            fill(21, 113, 69)
            ellipse(s.lo.x, s.lo.y, 25, 25)

            # Removes player bullets when hits slime and score increases
            for b in b_list:
                if dist(b.lo.x, b.lo.y, s.lo.x, s.lo.y) < 15 and b.p:
                    s.lo = PVector(random(25, 750), random(25, 550))
                    while in_barrier(s.lo):
                        s.lo = PVector(random(25, 750), random(25, 550))
                    b_list.remove(b)
                    score += 1

        # b_list for loop
        for b in b_list:

            # Draws the bullets
            if b.p:
                fill(0)
            elif not b.p:
                fill(241, 219, 75)
            ellipse(b.lo.x, b.lo.y, 5, 5)

            # Adds the slow motion
            if slow_m and not b.done:
                b.sp.normalize()
                b.sp = b.sp.mult(sm_factor)
                b.done = True

            # Adds the bullet speed to the locaiton
            b.sp.mult(bs_fac)
            b.lo.add(b.sp.mult(0.5))

            # if bullet hits player it disapears and lose a life
            if (
                not b.p and
                dist(player.lo.x, player.lo.y, b.lo.x, b.lo.y) <
                (player.si / 2) + 2.5
            ):
                b_list.remove(b)
                health -= 10

            # Removes bullets after they're off the screen
            if (
                b.lo.x < 0 or
                b.lo.x > width or b.lo.y < 0 or
                b.lo.y > height
            ):
                b_list.remove(b)
                continue

            # Removes bullets if they hit barrier 1
            if (
                b.lo.x > bar1_loc.x and b.lo.x < bar1_loc.x + bar1_size.x and
                b.lo.y > bar1_loc.y and b.lo.y < bar1_loc.y + bar1_size.y
            ):
                    b_list.remove(b)

            # Removes bullets if they hit barrier 2
            if (
                b.lo.x > bar2_loc.x and b.lo.x < bar2_loc.x + bar2_size.x and
                b.lo.y > bar2_loc.y and b.lo.y < bar2_loc.y + bar2_size.y
            ):
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

        # Player movement
        if key_states[65]:  # left a
            if not in_barrier(PVector(player.lo.x - 3 - 18, player.lo.y)):
                player.lo.x -= 3
                sm_factor = 13
                change = True
        elif key_states[68]:  # right d
            if not in_barrier(PVector(player.lo.x + 3 + 18, player.lo.y)):
                player.lo.x += 3
                sm_factor = 13
                change = True
        if key_states[87]:  # up w
            if not in_barrier(PVector(player.lo.x, player.lo.y - 3 - 18)):
                player.lo.y -= 3
                sm_factor = 13
                change = True
        elif key_states[83]:  # down s
            if not in_barrier(PVector(player.lo.x, player.lo.y + 3 + 18)):
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
        text('Restart', (
         ((res_loc.x + res_si.x) / 2) - 50),
         res_loc.y + res_si.y - 20
         )

        # Showing scores
        textSize(72)
        text('GAME OVER', 200, 300)
        textSize(32)
        text('Score: ' + str(score), 200, 350)
        text('Money: ' + str(money), 200, 390)
        text('Health: ' + str(health), 200, 430)


def keyPressed():
    global rapid_rifle, key_states

    if rrclaimed and key == 'q':
        if rapid_rifle:
            rapid_rifle = False
        else:
            rapid_rifle = True

    key_states[keyCode] = True


def mousePressed():
    global rapid_rifle, claim_rapid_rifle, rrclaimed
    global claim_af, af_freq, auto_fire
    global health, money, score, ammo
    global weap_show, weapons
    global b_list, s_list
    global play_fill
    global sm_factor
    global bs_fac
    global menu
    global shot
    shot = True

    if claim_rapid_rifle:
        if (
            mouseX > 450 and mouseX < 580 and
            mouseY > 50 and mouseY < 150
        ):
            claim_rapid_rifle = False
            rrclaimed = True
            ammo = 300
            money -= 150
            weapons.append('Rapid Rifle')

    if claim_af:
        if (
            mouseX > 600 and mouseX < 730 and
            mouseY > 50 and mouseY < 150
        ):
            claim_af = False
            money -= 100
            auto_fire = True
            if af_freq > 60:
                af_freq -= 60
            weapons.append('Auto-Shoot')

    if health <= 0:
        if (
            mouseX > res_loc.x and mouseX < res_loc.x + res_si.x and
            mouseY > res_loc.y and mouseY < res_loc.y + res_si.y
        ):
            health = 80
            money = 0
            score = 0

            auto_fire = False
            af_freq = 600
            claim_af = False

            claim_rapid_rifle = False
            rapid_rifle = False
            rrclaimed = False

            weapons = ['Boring Blaster']
            weap_show = ''
            b_list = []
            s_list = [
                Slime(PVector(random(25, 750), random(25, 600)), player.lo),
                Slime(PVector(random(25, 750), random(25, 600)), player.lo),
                Slime(PVector(random(25, 750), random(25, 600)), player.lo)
                ]

            menu = True
            shoot_freq = 200
            play_fill = 255
            bs_fac = 1
            sm_factor = 3

    if menu:
        if (
            mouseX in range(int(play_loc.x), int(play_loc.x + play_si.x)) and
            mouseY in range(int(play_loc.y), int(play_loc.y + play_si.y))
        ):
            menu = False


def keyReleased():
    global key_states, sm_factor, change
    key_states[keyCode] = False
    sm_factor = 3
    change = True
