destinations = ['Paris', 'Tokyo', 'Rome', 'Greece', "Los Angeles", 'Cancun', 'Las Vegas', 'Egypt', 'Puerto Rico', 'Brazil', 'Madagascar', "Alaska", "Miami", 'Amsterdam', 'Belgium', 'Iceland', 'London', 'Bora Bora']
restaurants = ['Coopers Hawk', 'Olive Garden', 'Red Lobster', "Hells Kitchen", 'Eggology', 'Savoury', 'Burnt Toast', 'The Fire Grille', 'Batter and Berries', 'Offshore Rooftop', 'Nutella Cafe']
transportation = ['Bus', 'Airplane', 'Train', 'Car', 'Boat', 'Bike', 'Helicopter', 'Ferry']
entertainment = ['Go Gambling', 'Go Shopping', 'Visit Historical Monument', 'Ask the Locals for what to do', 'Go to the club', 'Try new food']

import random

def greeting():
    greet_confirm = print("Hi, Welcome to the Day Trip Generator, where we help you make your perfect trip.Let's get started!")
greeting()
def destination_set():
    random_destination = random.choice(destinations)
    user_agree = input(f'Now it is time to choose your destination, would you like to go to {random_destination}? y/n:')
    while user_agree == 'n':
        random_destination = random.choice(destinations)
        user_agree = input(f"Sorry you didn't like that choice, how about {random_destination} instead? y/n:")
    if user_agree == 'y':
        print(f"Okay! Your destination is set for {random_destination}")
    return random_destination
set_destination = destination_set()

def restaurant_set():
    random_restaurant = random.choice(restaurants)
    user_agree = input(f'Now it is time to choose your restaurant, would you like to eat at {random_restaurant}? y/n:')
    while user_agree == 'n':
        random_restaurant =  random.choice(restaurants)
        user_agree = input(f"Sorry you didn't like that choice, how about {random_restaurant} instead? y/n:")
    if user_agree == "y":
        print (f'Okay! Your restaurant is set for {random_restaurant}')
    return random_restaurant

set_restaurant = restaurant_set()

def transportation_set():
    random_transportation = random.choice(transportation)
    user_agree = input(f'Now it is time to choose your type of transportation, would you like to travel by {random_transportation}? y/n:')
    while user_agree == 'n':
        random_transportation = random.choice(transportation)
        user_agree = input(f"Sorry you didn't like that choice, how about {random_transportation} instead? y/n:")
    if user_agree =="y":
        print(f'Okay! Your transportation is set for {random_transportation}')
    return random_transportation

set_transportation = transportation_set()

def entertainment_set():
    random_entertainment = random.choice(entertainment)
    user_agree = input(f'Now it is time to choose your form of entertainment, would you like to {random_entertainment}? y/n:')
    while user_agree == 'n':
        random_entertainment = random.choice(entertainment)
        user_agree = input(f"Sorry you didn't like that choice, how about {random_entertainment} instead? y/n:")
    if user_agree == 'y':
        print(f'Okay! Your entertainment is set for {random_entertainment}')
    return random_entertainment

set_entertainment = entertainment_set()

def trip_confirmation():
    confirm_start= False
    while confirm_start == False:
        trip_confirm = input(f'''You are now ready to go on an amazing trip!
        Location: {set_destination}
        Restaurant: {set_restaurant}
        Transportation: {set_transportation}
        Entertainment: {set_entertainment}
        Would you like to confirm this trip? y/n:
        ''')
        if trip_confirm == "y":
            print(f'''Thanks for using Day Trip Generator!
        Your trip is confirmed! You will be going to {set_destination}, and getting there by {set_transportation}.
        Once you are there you will dine at {set_restaurant} and {set_entertainment}''')
            return trip_confirm
        if trip_confirm == "n":
            changing_options()
            
def changing_options():
    trip_change= input('''We're sorry you didn't like your options, which part of your trip would you like to change?
        For Location Type 1:
        For Restaurant Type 2:
        For Transportation Type 3:
        For Entertainment Type 4:''')
    if trip_change == "1":
            set_destination = destination_set()
            return set_destination

    if trip_change == "2":
            set_restaurant = restaurant_set()
            return set_restaurant
        
    if trip_change=="3":
            set_transportation = transportation_set()
            return set_transportation

    if trip_change == "4":
            set_entertainment= entertainment_set()
            return set_entertainment

            
trip_confirmation()

# def run():
#     greeting()
#     destination_set()
#     restaurant_set()
#     transportation_set()
#     entertainment_set()
#     trip_confirmation()
# run()