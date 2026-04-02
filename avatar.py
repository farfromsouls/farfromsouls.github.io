import matplotlib.pyplot as plt

def fcheck(x, y):
    if x**2 + y**2 < 270:
        if y**2<x**2:
            return x*7
        else:
            return y*7

    return (x**2 + y**2)**0.4

scale = 500
rx = [i/10 for i in range(-1*scale, scale)]
ry = [i/10 for i in range(scale, -1*scale, -1)]

array_2d = [[fcheck(round(x), round(y)) for x in rx] for y in ry]

plt.imshow(array_2d, cmap='bone')
plt.show()
plt.imsave('avatar.png', array_2d, cmap='bone')