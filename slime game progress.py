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
    
    
# diff code
# diff code
rectangle = PVector(100, 100)
clicked = False

def setup():
    size(400, 400)
    
def mouseClicked():
    global clicked
    
    if clicked:
        clicked = False
    if not clicked:    
        clicked = True
    
def draw():

    if clicked:
        if mouseX > rectangle.x and mouseX < rectangle.x + 100 and mouseY > rectangle.y and mouseY < rectangle.y + 100:
            background(0)
    
    elif not clicked:
        background(255)
        

    fill(0)
    rect(rectangle.x, rectangle.y, 100, 100)
    fill(255)
    textSize(16)
    text('play', rectangle.x + 40, rectangle.y + 50)
    
    # diff code
    # diff code
player = PVector(200, 200)
player_size = 100
player_speed = PVector(0, 0)



def setup():
    size(400, 400)
    
def draw():
    background(255)
    fill(0)
    noStroke()
    
    player.add(player_speed)
    ellipse(player.x, player.y, player_size, player_size)
    

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
        
def keyReleased():
    if key == 'w' or key == 's':
        player_speed.y = 0
    if key == 'a' or key == 'd':
        player_speed.x = 0
        
        
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


    
    




    
 
 

    
        
        
        
        
    
    
