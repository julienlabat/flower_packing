from export import mousePressed

# parameters
accent = ["ffe045","dd2a3b","7621d9","2D27E3","0de0a8"]
colors = [accent[int(random(len(accent)))]] + ["ffffff","222222","AAAAAA"]
w = 1080
h = 1080
margin_h = 270
margin_v = 170
max_instances = 2000
min_radius = 5
max_radius = 50
precision = 10 # the smaller the more filled (also takes more time)
# outer frame
framing = True
frame_size = 35
##
b = int(random(len(colors)))
bg = "#" + colors.pop(b)
col = "#" + colors[int(random(len(colors)))]
flowers = []


def setup():
    size(w,h)
    background(bg)
    noLoop()    
    noFill()
    flowers_packing(margin_h, margin_v, w-margin_h, h-margin_v)
        
        
def draw():
    # main drawing with random choices of shapes 
    d = random(1)
    
    # 1/4 chance of drawing flowers
    if d < 0.25 :
        for f in flowers:
            f.flower()
        # 1/2 chance of adding stars
        if random(1) < 0.5 :
            for f in flowers:
                f.star()
        # 1/2 chance of adding polygons
        if random(1) < 0.5 :
            for f in flowers:
                f.polygon()
    # 1/4 chance of drawing polygons
    elif d < 0.5 :
        for f in flowers:
            f.polygon()
        # 1/2 chance of adding stars
        if random(1) < 0.5 :
            for f in flowers:
                f.star()
    # 1/4 chance of drawing stars
    elif d < 0.75 :
        for f in flowers:
            f.star()
    # 1/4 of each instance having its own shape
    else :
        for f in flowers:
            f.random_shape()
            
    # drawing the outer frame
    frame(frame_size, 255)
    
    
def flowers_packing(x,y,w,h):
    # safety variables
    max_iterations = (w*h)//precision    
    stop = 0
    # create Flower list with collision check
    while len(flowers) < max_instances:
        f = Flower(x,y,w,h,col)
        flowers.append(f)
        if len(flowers) > 0:
            for i in range(len(flowers[:-1])):
                # if last created collide with existing, pop and repeat
                if flowers[i].intersects(flowers[-1]):
                    flowers.pop()
                    break
        stop += 1
        # safety break if too much iterations and list not full
        if stop > max_iterations:
            break
        

class Circle(object):
    
    def __init__(self,x,y,w,h):
        self.radius = random(min_radius, max_radius)
        self.x = random(self.radius+x, w-self.radius)
        self.y = random(self.radius+y, h-self.radius)
        
        
    def intersects(self, c):
        ''' checks if this Circle intersects with a given circle
            c : Circle instance '''
        return dist(self.x, self.y, c.x, c.y) < self.radius + c.radius
    
    
    def show(self):
        circle(self.x, self.y, self.radius*2)
        
        
class Flower(Circle):
    
    def __init__(self,x,y,w,h,col):
        Circle.__init__(self,x,y,w,h)
        self.petals = int(random(5+self.radius/10, self.radius/5))
        self.angle = TAU/self.petals
        self.col = col
        stroke(self.col)
        self.rotation = random(PI)
        
        
    def flower(self):
        r = random(self.radius/3,self.radius/1.5)
        i = 0
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.rotation)
        while i < TAU:                
            circle(cos(i)*r,sin(i)*r,self.radius*2-r*2-2)            
            i += self.angle
        popMatrix()
        
    
    def polygon(self):
        r = self.radius
        i = 0
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.rotation)
        beginShape()
        while i < TAU:        
            vertex(cos(i)*r,sin(i)*r)
            i += self.angle
        vertex(cos(0)*r,sin(0)*r)
        endShape()
        popMatrix()
        
    
    def star(self):
        r = self.radius-1
        i = 0
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.rotation)
        while i < TAU:        
            line(0,0,cos(i)*r,sin(i)*r)
            i += self.angle
        popMatrix()
        
    
    def random_shape(self):
        ''' Returns a random shape method from Flower class '''
        d = random(3)
        if d < 1:
            return self.flower()
        elif d < 2:
            return self.polygon()
        else:
            return self.star()
        
        
def frame(frame_size, col):
    ''' Draws 4 rectangles to create an outer frame on the canvas.
        frame_size : int thickness of canvas in pixels
        col : color of the frame '''
    if framing:    
        fill(col)
        noStroke()
        rect(0,0,width,frame_size)
        rect(0,height-frame_size,width,frame_size)
        rect(0,0,frame_size,height)
        rect(width-frame_size,0,frame_size,height)
        
