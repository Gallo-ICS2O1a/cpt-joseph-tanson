screen = 100
ball = PVector(100, 100)
speeds = []
bullets = []
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
    ellipse(ball.x, ball.y, 50, 50)
    point(mouse.x, mouse.y)
    for i in range(len(bullets)):
        ellipse(bullets[i].x, bullets[i].y, 5, 5)
        bullets[i].add(speeds[i])
def mousePressed():
    global speed, mouse, ball
    mouse = PVector(mouseX, mouseY)
    bullets.append(PVector(ball.x, ball.y))
    speeds.append(trajectory(mouse, ball).mult(7))
