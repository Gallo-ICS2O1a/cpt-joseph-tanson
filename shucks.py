def trajectory(v1, v2):
    difference = PVector.sub(v1, v2)
    angle = difference.heading()
    return PVector.fromAngle(angle).mult(-1)

class Bullet:
    def __init__(self, v1, v2):
        self.location = PVector(v1.x, v1.y)
        self.speed = trajectory(v1, v2).mult(7)
        self.done = False
