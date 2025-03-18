from numpy import random, hypot, round, sqrt, asarray, linspace
sqrt3 = sqrt(3)
sqrt5 = sqrt(5)
# W_0=3
def wind_mouse(start_x, start_y, dest_x, dest_y, G_0=9, W_0=9, M_0=15, D_0=30, move_mouse=lambda x,y: None):
    '''
    WindMouse algorithm. Calls the move_mouse kwarg with each new step.
    Released under the terms of the GPLv3 license.
    G_0 - magnitude of the gravitational fornce
    W_0 - magnitude of the wind force fluctuations
    M_0 - maximum step size (velocity clip threshold)
    D_0 - distance where wind behavior changes from random to damped
    '''
    current_x,current_y = start_x,start_y
    v_x = v_y = W_x = W_y = 0
    while (dist:=hypot(dest_x-start_x,dest_y-start_y)) >= 1:
        W_mag = min(W_0, dist)
        if dist >= D_0:
            W_x = W_x/sqrt3 + (2*random.random()-1)*W_mag/sqrt5
            W_y = W_y/sqrt3 + (2*random.random()-1)*W_mag/sqrt5
        else:
            W_x /= sqrt3
            W_y /= sqrt3
            if M_0 < 3:
                M_0 = random.random()*3 + 3
            else:
                M_0 /= sqrt5
        v_x += W_x + G_0*(dest_x-start_x)/dist
        v_y += W_y + G_0*(dest_y-start_y)/dist
        v_mag = hypot(v_x, v_y)
        if v_mag > M_0:
            v_clip = M_0/2 + random.random()*M_0/2
            v_x = (v_x/v_mag) * v_clip
            v_y = (v_y/v_mag) * v_clip
        start_x += v_x
        start_y += v_y
        move_x = int(round(start_x))
        move_y = int(round(start_y))
        if current_x != move_x or current_y != move_y:
            #This should wait for the mouse polling interval
            move_mouse(current_x:=move_x,current_y:=move_y)
    return current_x,current_y

# import matplotlib.pyplot as plt

# points = []
# wind_mouse(0, 0, 500, 1000, move_mouse=lambda x,y: points.append([x,y]))
# points = np.asarray(points)
# for i in range(len(points)):
#     win32api.SetCursorPos((points[i][0], points[i][1]))
#     time.sleep(0.001)

# import matplotlib.pyplot as plt

# fig = plt.figure(figsize=[13,13])
# plt.axis('off')
# for y in linspace(-200,200,25):
#     points = []
#     wind_mouse(0,y,500,y,move_mouse=lambda x,y: points.append([x,y]))
#     points = asarray(points)
#     plt.plot(*points.T)
# plt.xlim(-50,550)
# plt.ylim(-250,250)
# plt.show()

