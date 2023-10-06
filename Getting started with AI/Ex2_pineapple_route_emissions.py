""" 
Building on the previous solution, modify the code so that it finds the route with minimum carbon emissions and prints it out. 
Again, the program should work for any number of ports. 
You can assume that the distances between the ports are given in an array of the appropriate size so that the distance between ports i and j is found in D[i][j].

Output Example
PAN AMS CAS NYC HEL 240.1 kg


"""

#Solution
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

# https://sea-distances.org/
# nautical miles converted to km
D = [
    [0, 8943, 8019, 3652, 10545],
    [8943, 0, 2619, 6317, 2078],
    [8019, 2619, 0, 5836, 4939],
    [3652, 6317, 5836, 0, 7825],
    [10545, 2078, 4939, 7825, 0]
]

# https://timeforchange.org/co2-emissions-shipping-goods
# assume 20g per km per metric ton (of pineapples)
co2 = 0.020

# Initialize variables to track the smallest emissions and the best route
smallest = 1000000
bestroute = [0, 0, 0, 0, 0]

def calculate_emissions(route):
    emissions = 0
    for i in range(len(route) - 1):
        from_port = route[i]
        to_port = route[i + 1]
        emissions += D[from_port][to_port] * co2
    return emissions

def permutations(route, ports):
    global smallest, bestroute

    if len(ports) == 0:
        # If there are no more ports to visit, calculate emissions
        emissions = calculate_emissions(route)
        
        # Check if this route has the smallest emissions
        if emissions < smallest:
            smallest = emissions
            bestroute = route.copy()
    else:
        for port in ports:
            # Copy the route and ports list to avoid modifying the original
            new_route = route.copy()
            new_ports = ports.copy()

            # Add the current port to the route and remove it from the list of ports to visit
            new_route.append(port)
            new_ports.remove(port)

            # Recursively call permutations with the updated route and ports
            permutations(new_route, new_ports)

def main():
    # Do not edit any (global) variables using this function, as it will mess up the testing

    # This will start the recursion
    permutations([0], list(range(1, len(portnames))))

    # Print the best route and its emissions
    print(' '.join([portnames[i] for i in bestroute]) + " %.1f kg" % smallest)

main()
