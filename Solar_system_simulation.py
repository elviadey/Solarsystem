from vpython import *

scene = canvas() 

#defining the value of G
G=6.673e-11

# Acceleration of object a due to object b because of their gravitational interaction
def acc(a, b):
    rel_pos = b.pos - a.pos
    return G*b.mass * norm(rel_pos)/rel_pos.mag2

# Accelaration of a due to all the objects b intracting with it
def totalacc (a, objlist):
    sum_acc = vector (0,0,0)
    for b in objlist:
        if (a!=b):
            sum_acc = sum_acc + acc(a, b)
    return sum_acc

#Solar system on a computer

#Defining constants 
G=6.673e-11
myPi = 3.141592
AU = 149.6e9       #mean earth sun orbital distance

#Initial conditions
sun_mass = 2e30
earth_mass = 6e24
mars_mass = 6.39e24
jupiter_mass= 1.9e27
saturn_mass= 5.6e26
uranus_mass= 8.6e25
neptune_mass = 1e26

# average velocity = 2*Pi*R/T
earth_vel = 2* myPi * AU/(365.25 *24 *60*60)
mars_vel = 2* myPi * 1.52*AU/(687 *24 *60 * 60)
jupiter_vel = 2* myPi * 5.2*AU/(11.86*365.25*24*60*60)
saturn_vel = 2* myPi * 9.55*AU/(29.4*365.25 *24. *60.*60)
uranus_vel = 2* myPi * 19.8*AU/(84 *365.25 *24. *60.*60)
neptune_vel = 2* myPi * 30*AU/(165 *365.25 *24. *60.*60)

#setting for animations
scene.background = color.black
scene.autoscale = 0
scene.range = 30*AU

#objects making up our solar system
sun = sphere(pos= vector(0,0,0), velocity = vector(0,0,0),
             mass=sun_mass, radius = 0.4*AU, color =color.yellow)
earth = sphere(pos= vector(AU, 0, 0), velocity = vector(0,earth_vel,0),
               mass=earth_mass, radius=0.15*AU, color =color.blue)
mars = sphere(pos= vector(1.52*AU,0,0), velocity = vector(0,mars_vel,0),
             mass=mars_mass, radius = 0.2*AU, color =color.red)
jupiter = sphere(pos=vector(5.2*AU,0,0),velocity=vector(0,jupiter_vel,0),
             mass=jupiter_mass, radius=0.3*AU, color=color.orange)
saturn = sphere(pos=vector(9.55*AU,0,0),velocity=vector(0,saturn_vel,0),
             mass=saturn_mass, radius=0.25*AU, color=color.yellow)
uranus = sphere(pos=vector(19.8*AU,0,0),velocity=vector(0,uranus_vel,0),
             mass=uranus_mass, radius=0.2*AU, color=color.cyan)
neptune = sphere(pos=vector(30*AU,0,0),velocity=vector(0,neptune_vel,0),
             mass=neptune_mass, radius=0.2*AU, color=color.white)
#note the radius of sun,and other planets are NOT
# their true radius, these are the radius of the spherical object
#that will be draw on the computer screen

#Create a list of objects making up our solar system 
#and add attributes for their accelaration and orbits

bodies = [sun, earth, mars, jupiter, saturn, uranus, neptune]

for b in bodies:
    b.acc = vector(0,0,0)
    b.track=curve (color = b.color)

# set total momentum of system to zero (centre of mass frame) 
sum=vector(0,0,0)
for b in bodies:
    if (b!=sun):
        sum=sum+b.mass*b.velocity

sun.velocity=-sum/sun.mass

# dt corresponds to 3000 mins here
dt= 30.*60.*100

#Initialize leap-frog by finding the velocites at t=dt/2

for b in bodies:
    b.velocity = b.velocity + totalacc(b, bodies)*dt/2.0

#start leap-frog
while True:
    rate(50)  #not more than 100 time steps in a second
    for b in bodies:
        #update the positions
        b.pos = b.pos + b.velocity*dt
        b.track.append(pos=b.pos)

        #update the velocities
        b.velocity = b.velocity + totalacc(b, bodies)*dt

    scene.center = vector(0,0,0) #view centered on the origin of CM coord system
