screen = 100
player = PVector(100, 100)
speeds = []
bullets = []
slimes = [PVector(random(25, 750), random(25, 550))]
def setup():
    size(int(screen * 7.5), int(screen * 6))
def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle)
def draw():
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
def keyPressed(q):
    global speed, mouse, player
    mouse = PVector(mouseX, mouseY)
    bullets.append(PVector(player.x, player.y))
    speeds.append(trajectory(mouse, player).mult(7))
