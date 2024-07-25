import easygui
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Easy GUI ##
msg = "Enter velocity, angle, and mass"
title = "Input for projectile simulation"
fieldNames = ["Velocity", "Angle", "Mass"]
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

## Matplotlib Plot ##
sns.set()
fig, ax = plt.subplots()
g = 9.81  # value of gravity
v = float(fieldValues[0])  # initial velocity
theta = float(fieldValues[1]) * np.pi / 180.0  # initial angle of launch in radians
m = float(fieldValues[2])  # mass of the projectile

# Adjust initial velocity based on mass
# Assuming a simple inverse relationship for demonstration
#we know that p = mv 
# p = movementum , v = velocity and m = mass 
V_adj = v * (1 / (1 + m / 10.0))

vx = V_adj * np.cos(theta)
vy = V_adj * np.sin(theta)
x, y = 0, 0

# Calculate time of flight, horizontal range, and maximum height
time_of_flight = (2 * V_adj * np.sin(theta)) / g
horizontal_range = (V_adj ** 2 * np.sin(2 * theta)) / g
maximum_height = (V_adj ** 2 * (np.sin(theta)) ** 2) / (2 * g)

print(f"Time of flight: {time_of_flight} seconds")
print(f"Horizontal range: {horizontal_range} meters")
print(f"Maximum height: {maximum_height} meters")

# Arrays to store the full trajectory
t = np.linspace(0, time_of_flight, num=500)  # Time array for the full trajectory
x_data = vx * t
y_data = vy * t - 0.5 * g * t ** 2

x_data = np.array(x_data)
y_data = np.array(y_data)

# Set up plot limits dynamically based on the trajectory
x_max = np.max(x_data) * 1.1
y_max = np.max(y_data) * 1.1
ax.set_xlim(0, x_max)
ax.set_ylim(0, y_max)

# Plot the trajectory
ax.plot(x_data, y_data, 'r-', lw=2)  # Red line to show trajectory

# Add labels and title
ax.set_xlabel('X Distance (m)')
ax.set_ylabel('Y Distance (m)')
ax.set_title('Projectile Motion')

# Show calculated values on the plot
plt.figtext(0.15, 0.8, f'Time of flight: {time_of_flight:.2f} s', fontsize=10, color='blue')
plt.figtext(0.15, 0.75, f'Horizontal range: {horizontal_range:.2f} m', fontsize=10, color='blue')
plt.figtext(0.15, 0.7, f'Maximum height: {maximum_height:.2f} m', fontsize=10, color='blue')

# Show plot
plt.show()
