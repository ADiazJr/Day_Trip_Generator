destinations = ['Paris', 'Tokyo', 'Rome', 'Greece', "Los Angeles", 'Cancun', 'Las Vegas', 'Egypt', 'Puerto Rico', 'Brazil', 'Madagascar', "Alaska", "Miami", 'Amsterdam', 'Belgium', 'Iceland', 'London', 'Bora Bora']
restaurants = ['Coopers Hawk', 'Olive Garden', 'Red Lobster', "Hells Kitchen", 'Eggology', 'Savoury', 'Burnt Toast', 'The Fire Grille', 'Batter and Berries', 'Offshore Rooftop', 'Nutella Cafe']
transportation = ['Bus', 'Airplane', 'Train', 'Road Trip', 'Boat', 'Bike', 'Helicopter', 'Ferry']
entertainment = ['Go Gambling', 'Go Shopping', 'Visit Historical Monument', 'Ask the Locals for what to do', 'Go to the club', 'Try new food']

import random
def destination_set():
    random_destination = random.choices(destinations)
    user_agree = input(f'Hi, Welcome to the Day Trip Generator, where we help you make your perfect trip. We have chosen {random_destination} for your destination. Would you like to keep this Destination? y/n:')
    while user_agree == 'n':
        random_destination = random.choices(destinations)
        user_agree = input(f"Sorry you didn't like that choice, how about {random_destination} instead? y/n:")
    if user_agree == 'y':
        print(f"Okay! Your destination is set for {random_destination}")

destination_set()

def restaurant_set():
    random_restaurant = random.choices(restaurants)
    user_agree = input(f'Now it is time to choose your restaurant, would you like to eat at {random_restaurant}? y/n:')
    while user_agree == 'n':
        random_restaurant =  random.choices(restaurants)
        user_agree = input(f"Sorry you didn't like that choice, how about {random_restaurant} instead? y/n:")
    if user_agree == "y":
        print (f'Okay! Your restaurant is set for {random_restaurant}')

restaurant_set()

def transportation_set():
    random_transportation = random.choices(transportation)
    user_agree = input(f'Now it is time to choose your type of transportation, would you like to travel by {random_transportation}? y/n:')
    while user_agree == 'n':
        random_transportation = random.choices(transportation)
        user_agree = input(f"Sorry you didn't like that choice, how about {random_transportation} instead? y/n:")
    if user_agree =="y":
        print(f'Okay! Your transportation is set for {random_transportation}')

transportation_set()

def entertainment_set():
    random_entertainment = random.choices(entertainment)
    user_agree = input(f'Now it is time to choose your form of entertainment, would you like to {entertainment}? y/n:')
    while user_agree == 'n':
        random_entertainment = random.choices(entertainment)
        user_agree = input(f"Sorry you didn't like that choice, how about {random_entertainment} instead? y/n:")
    if user_agree == 'y':
        print(f'Okay! Your entertainment is set for {random_entertainment}')

entertainment_set()