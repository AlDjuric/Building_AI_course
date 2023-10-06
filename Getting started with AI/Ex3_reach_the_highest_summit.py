""" 
Let the elevation at each point on the mountain be stored in array h of size 100. 
The elevation at the leftmost point is thus stored in h[0] and the elevation at the rightmost point is stored in h[99].

The following program starts at a random position and keeps going to the right until Venla can no longer go up. 
However, perhaps the mountain is a bit rugged which means it's necessary to look a bit further ahead.

Edit the program so that Venla doesn't stop climbing as long as she can go up by moving up to five steps either left or right.
If there are multiple choices within five steps that go up, any one of them is good. 
To check how your climbing algorithm works in action, you can plot the results of your hill climbing using the Plot button. 
As a reminder, the summit will be marked with a blue triangle.

"""

#Solution

import math
import random

# Generate random mountains
w = [0.05, random.random() / 3, random.random() / 3]
h = [1.0 + math.sin(1 + x / 0.6) * w[0] + math.sin(-0.3 + x / 9.0) * w[1] + math.sin(-0.2 + x / 30.0) * w[2] for x in range(100)]

def climb(x, h):
    # Keep climbing until we've found a summit
    summit = False

    # Edit here
    while not summit:
        summit = True  # Stop unless there's a way up
        next_peak = x  # Initialize the next_peak variable to the current position

        # Check elevations within the next five steps to the right
        for i in range(1, 6):
            if x + i >= len(h):
                break
            if h[x + i] > h[next_peak]:
                next_peak = x + i

        # Check elevations within the next five steps to the left
        for i in range(1, 6):
            if x - i < 0:
                break
            if h[x - i] > h[next_peak]:
                next_peak = x - i

        if next_peak != x:
            x = next_peak  # Move to the next highest position
            summit = False  # Continue climbing

    return x

def main(h):
    # Start at a random place
    x0 = random.randint(1, 98)
    x = climb(x0, h)

    return x0, x

main(h)
