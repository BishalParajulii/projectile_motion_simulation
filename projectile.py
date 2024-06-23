import easygui
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

## Easy GUI ##
msg = "Enter velocity & angle"
title = "Input for projectile simulation"
fieldNames = ["Velocity", "Angle"]
fieldValues = []  # we start with blanks for the values
fieldValues = easygui.multenterbox(msg, title, fieldNames)
print(fieldValues)

while 1:
    if fieldValues is None: break
    errmsg = ""
    for i in range(len(fieldNames)):
        if fieldValues[i].strip() == "":
            errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break  # no problems found
    fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
print("Reply was:", fieldValues)

## Matplotlib Animation ##
sns.set()
fig, ax = plt.subplots()
g = 9.81  # value of gravity
v = float(fieldValues[0])  # initial velocity
theta = float(fieldValues[1]) * np.pi / 180.0  # initial angle of launch in radians
vx = v * np.cos(theta)
vy = v * np.sin(theta)
x, y = 0, 0

# Arrays to store the full trajectory
x_data = []
y_data = []

while vy > 0.1:  # Continue bouncing until vertical velocity is very small
    t = np.linspace(0, 2 * vy / g, num=100)  # Time array for one bounce
    x_bounce = x + vx * t
    y_bounce = y + vy * t - 0.5 * g * t ** 2

    x_data.extend(x_bounce)
    y_data.extend(y_bounce)

    x, y = x_bounce[-1], 0  # Ball lands on the ground
    vy = -vy * 0.7  # 30% energy loss on each bounce
    vx *= 0.7

x_data = np.array(x_data)
y_data = np.array(y_data)

# Set up plot limits dynamically based on the trajectory
x_max = np.max(x_data) * 1.1
y_max = np.max(y_data) * 1.1
ax.set_xlim(0, x_max)
ax.set_ylim(0, y_max)

# Plot initial point and the ball
point, = ax.plot([x_data[0]], [y_data[0]], 'bo')
line, = ax.plot([], [], 'r-', lw=2)  # Red line to show trajectory

# Function to update the animation
def animate(num):
    point.set_data([x_data[num]], [y_data[num]])
    if y_data[num] > 0:  # Only draw the trajectory when the ball is above the x-axis
        line.set_data(x_data[:num+1], y_data[:num+1])
    else:
        line.set_data([], [])
    return point, line

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(x_data), interval=50, blit=True)

# Add labels and title
ax.set_xlabel('X Distance (m)')
ax.set_ylabel('Y Distance (m)')
ax.set_title('Projectile Motion with Bounces')

# Show plot
plt.show()
