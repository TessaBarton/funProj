#
# hw11pr1.py
#

import math
from visual import *
from random import choice
from hw11pr2 import *   # for the Alien class

def main():
    """ This is the main function. It
        (1) creates the objects to show
        (2) runs an event loop allowing the user
            to move the objects and view around
    """
    # our hero!
    alien = Alien( (5,0,5) )
    alien.body.color = color.green
    RADIUS = alien.body.radius

    # another alien...
    friend = Alien( (10,0,10) )
    friend.body.color = color.green
    friend.vel = vector(0,0,0)  # zero velocity to start

    # other objects in the scene: beach and ocean
    beach = box(pos = (0,-1,0),
                length = 40, width = 40, height = 0.1,
                color = color.yellow)

    ocean = cylinder( pos = (10,-1,-10), axis=(0,.1,0),
                      color = color.blue, radius = 2 )
    black_hole = ellipsoid( pos = (1,0,1),
                       length = 5,
                       width = 3,
                       height = 1,
                       color = color.black)
    cloud_of_heaven1 = ellipsoid( pos = (2,5,-3),
                                  length = 5,
                                  width = 3,
                                  height = 2.5,
                                  color = color.white)
    cloud_of_heaven2 = ellipsoid( pos = (2,7,-3),
                                  length = 3,
                                  width = 2,
                                  height = 3,
                                  color = color.white)
    cloud_of_heaven3 = ellipsoid( pos = (2.5,5,-4),
                                  length = 2,
                                  width = 4,
                                  height = 1,
                                  color = color.white)
                                  

    RATE = 100          # maximum update rate (in hertz)
    dt = 1.0/RATE       # time per loop
    scene.autoscale = False    # helpful for viewing

    SB_List = []
    for i in range(3):
        x_pos = choice(range(5))
        z_pos = choice(range(5))
        sb = sphere(pos=(x_pos,10,z_pos))
        SB_List += [sb]

    # the main simulation loop
    while True:

        rate(RATE)  # this many times per second, at most

        # update the friend's position, based on velocity
        friend.f.pos += dt*friend.vel

        # Snowballs
        for sb in SB_List:
            sb.pos += 0.02 * vector(0,-1,0)
            
        # if friend is too far away from the origin, reset it
        if mag(friend.f.pos) > 30: friend.f.pos = vector(0,0,0)

        # check for collisions: alien - friend
        if alien.check_for_collision( friend.f, r=2 ) == True:
            friend.body.color = color.red
    
        # check for collisions: alien - ocean
        if alien.check_for_collision( ocean, r=3 ) == True:
            alien.body.color = color.blue
            ocean.color = color.cyan
        else:
            alien.body.color = color.green
            ocean.color = color.blue
            
        if friend.f.pos.x > 20:
            friend.vel.x *= -1
        if friend.f.pos.x < -20:
            friend.vel.x *= -1
        if friend.f.pos.z > 20:
            friend.vel.z *= -1
        if friend.f.pos.z < -20:
            friend.vel.z *= -1

        ## gameplay goal is to tag your friend!

        if alien.check_for_collision(friend.f, r=2):
            print 'You Win!!!!'
            break

        #another interaction, penalty for falling in the black hole

        if alien.check_for_collision(black_hole, r=2):
            alien.body.color = color.red
            alien.f.x = 2
            alien.f.y = 7
            alien.f.z = -3
        



        #
        # handle mouse and keyboard events
        #
        if scene.mouse.clicked != 0: # is there a mouse click?
            print "mouse click!"
            event = scene.mouse.getclick() # remove event
            scene.mouse.events = 0   # then reset mouse events
            
        if scene.kb.keys:            # is there a keyevent?
            s = scene.kb.getkey()    # get keypress
            #print "keypress is", s
            if s == "p": 
                print alien

            # start/stop moving the friend around...
            if s == "M":
                if mag(friend.vel) > 0.1:
                    friend.vel = vector(0,0,0)
                else:
                    friend.vel = 3*vector(choice([-1,1]),0,
                                    choice([-1,1]))

            # move the alien around
            if s == "i":
                alien.f.pos += vector(0,0,1)
            if s == "k":
                alien.f.pos += vector(0,0,-1)
            if s == "j":
                alien.f.pos += vector(-1,0,0)
            if s == "l":
                alien.f.pos += vector(1,0,0)

            # move the center of the viewing window
            if s == "w":
                scene.center += vector(0,0,1)
            if s == "s":
                scene.center += vector(0,0,-1)
            if s == "W":
                scene.center += vector(0,-1,0)
            if s == "S":
                scene.center += vector(0,1,0)
            if s == "a":
                scene.center += vector(-1,0,0)
            if s == "d":
                scene.center += vector(1,0,0)




if __name__ == "__main__":
    main()





