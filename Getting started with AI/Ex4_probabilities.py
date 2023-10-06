""" 
Write a program that prints "I love" followed by one word: the additional word should be 'dogs' with 80% probability, 'cats' with 10% probability, and 'bats' with 10% probability.

Here's an example output:

I love bats
"""

#Solution

import random

def main():
    words = ['dogs', 'cats', 'bats']
    probabilities = [0.8, 0.1, 0.1]

    favorite = random.choices(words, probabilities)[0]
    print("I love " + favorite)

main()
