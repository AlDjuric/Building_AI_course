"""
Suppose we also happen to know the gender of the lottery winner. Here are same OECD statistics as above broken down by gender:

Country	    Population	Male fishers	Female fishers	Fishers (total)
Denmark	    5,615,000	    1822	    69	             1891
Finland	    5,439,000	    2575	    77	             2652
Iceland	    324,000	        3400	    400	             3800
Norway	    5,080,000	    11,291	    320	            11,611
Sweden	    9,609,000	    1731	    26	             1757
TOTAL	    26,067,000  	20,819	    892	            21,711
Write a function that uses the above numbers and tries to guess the nationality of the winner when we know that the winner is a fisher and their gender (either female or male).

The argument of the function should be the gender of the winner ('female' or 'male'). The return value of the function should be a pair (country, probability) where country is the most likely nationality of the winner and probability is the probability of the country being the nationality of the winner.

Output Example
if the winner is male, my guess is he's from Finland; probability 08.56%
if the winner is female, my guess is she's from Norway; probability 23.98%
Tip: Your values might be different, but the formatting should be identical.
"""

countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
populations = [5615000, 5439000, 324000, 5080000, 9609000]
male_fishers = [1822, 2575, 3400, 11291, 1731]
female_fishers = [69, 77, 400, 320, 26]

def guess(winner_gender):
    if winner_gender == 'female':
        fishers = female_fishers
    else:
        fishers = male_fishers

    # Calculate the total number of male or female fishers
    total_fishers = sum(fishers)

    guess = None
    biggest = 0.0

    # Calculate the probability for each country
    for i in range(len(countries)):
        probability = fishers[i] / total_fishers
        if probability > biggest:
            biggest = probability
            guess = countries[i]

    return (guess, biggest * 100)

def main():
    country, fraction = guess("male")
    print("if the winner is male, my guess is he's from %s; probability %.2f%%" % (country, fraction))
    country, fraction = guess("female")
    print("if the winner is female, my guess is she's from %s; probability %.2f%%" % (country, fraction))

main()
