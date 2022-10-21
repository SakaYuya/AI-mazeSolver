from timeit import repeat
from turtle import circle
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def drawRoute(fig, route):
    # ims is a list of lists, each row is a list of artists to draw in the
    # current frame; here we are just animating one artist, the image, in
    # each frame 
    ims = []
    x = []
    y = []
    # Draw search path
    for i in range(len(route[0])-2):
        for j in range(i+1):
            x.append(route[0][j+1][1])
            y.append(-route[0][j+1][0])
        im = plt.scatter(x, y,
                        marker='h',color='silver')
        ims.append([im])


    #Draw result
    x1 = []
    y1 = []
    for i in range(len(route[1])-2):
        for j in range(i+1):
            x1.append(route[1][j+1][1])
            y1.append(-route[1][j+1][0])
        im = plt.scatter(x1, y1,
                        marker='o',color='red')
        ims.append([im])
    ani = animation.ArtistAnimation(fig, ims, interval=100, repeat=False, blit=True)

    ani.save('dynamic_images.gif')

    plt.show()
