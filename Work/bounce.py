# bounce.py
# Program that shows the height of ball as it is dropped from 100 m and bounces 10 times. Each time the ball bounces
# the height is reduced by 1/3 the previous height.


import matplotlib.pyplot as plt
height = 100
bounces = 0

plt.figure(figsize=(10, 8))
plt.xlim(0, 5)
while bounces < 10:
    bounces = bounces + 1
    height = height - 1/3 * height
    print(height)
    plt.scatter(2.5, height)
    plt.text(2.6, height, 'bounce {}'.format(bounces))

plt.show()
# Exercise 1.5
