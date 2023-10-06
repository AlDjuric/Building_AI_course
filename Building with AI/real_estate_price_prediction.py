# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200 , -50, 5000, 100]

def predict(X, c):
    # Initialize an empty list to store the predicted prices
    predicted_prices = []
    
    # Loop over the cabins and calculate the predicted price for each one
    for cabin in X:
        price = 0
        for i in range(len(c)):
            price += cabin[i] * c[i]  # Multiply each feature by its corresponding coefficient
        predicted_prices.append(price)
    
    # Print the predicted prices for all cabins
    for price in predicted_prices:
        print(price)

predict(X, c)
