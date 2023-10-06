"""In this exercise you need to list all the possible routes that start from Panama and visit each of the other ports exactly once.

The template code below contains an incomplete permutations function which takes as input a specified route and a list of port names absent from that route. 
Modify the function so that it prints out all the possible orderings of the ports that always begin with Panama (PAN).

The mathematical term for such orderings is a permutation. Note that your program should work for an input portnames list of any length. 
The order in which the permutations are printed doesn't matter.

As the output the function should print each permutation on its own row, as one string, with the port names separated by spaces. 
For this, you can use the join function as follows: print(' '.join([portnames[i] for i in route])).

Output Example:
PAN AMS CAS NYC HEL

...

PAN CAS AMS NYC HEL

Tip: Your values might be different, but the formatting should be identical.

TEMPLATE CODE BELOW:
________________________________________
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # Write your recursive code here
    
    # Print the port names in route when the recursion terminates
    print(' '.join([portnames[i] for i in route]))


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))

________________________________________
"""

#Solution   
portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

def permutations(route, ports):
    if len(ports) == 0:
        # If there are no more ports to visit, print the route
        print(' '.join([portnames[i] for i in route]))
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

# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(portnames))))