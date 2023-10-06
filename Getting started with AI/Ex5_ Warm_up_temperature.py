""" 
Suppose the current solution has score S_old = 150 and you try a small modification to create a new solution with score S_new = 140. 
In the greedy solution, this new solution wouldn't be accepted because it would mean a decrease in the score. In simulated annealing, 
the new solution is accepted with a certain probability as explained above.

Modify the accept_prob function so that it returns the probability of accepting the new state using simulated annealing.
The program should take the two score values (the current and the new) and the temperature value as arguments.
"""

#Solution
import math, random

def accept_prob(S_old, S_new, T):
    # Modify the acceptance probability to select S_new if it's greater than S_old
    if S_new >= S_old:
        return 1.0
    else:
        return math.exp((S_new - S_old) / T)  # Accept with probability e^((S_new - S_old) / T)

# Example usage:
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)

# Test the accept function
accept(150, 140, 1.0)  # Example: S_old = 150, S_new = 140, T = 1.0
