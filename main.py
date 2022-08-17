destinations = ['Paris', 'Tokyo', 'Rome', 'Greece', "Los Angeles", 'Cancun', 'Las Vegas', 'Egypt', 'Puerto Rico', 'Brazil', 'Madagascar', "Alaska", "Miami", 'Amsterdam', 'Belgium', 'Iceland', 'London', 'Bora Bora']
restaurants = ['Coopers Hawk', 'Olive Garden', 'Red Lobster', "Hells Kitchen", 'Eggology', 'Savoury', 'Burnt Toast', 'The Fire Grille', 'Batter and Berries', 'Offshore Rooftop', 'Nutella Cafe']
transportation = ['Bus', 'Airplane', 'Train', 'Car', 'Boat', 'Bike', 'Helicopter', 'Ferry']
entertainment = ['Go Gambling', 'Go Shopping', 'Visit Historical Monument', 'Ask the Locals for what to do', 'Go to the club', 'Try new food']

import random

def greeting():
    greet_confirm = print("Hi, Welcome to the Day Trip Generator, where we help you make your perfect trip.Let's get started!")

def destination_set():
    random_destination = random.choice(destinations)
    finalized = False
    while finalized is False:
        user_agree = input(f'Now it is time to choose your destination, would you like to go to {random_destination}? y/n:')
        if user_agree == 'n':
            random_destination = random.choice(destinations)
            user_agree = input(f"Sorry you didn't like that choice, how about {random_destination} instead? y/n:")
        if user_agree == 'y':
            print(f"Okay! Your destination is set for {random_destination}")
            finalized = True
        elif user_agree != "y" and user_agree != "n":
            print("Sorry that is not a valid answer please try again")
    return random_destination

def restaurant_set():
    finalized = False
    while finalized is False:
        random_restaurant = random.choice(restaurants)
        user_agree = input(f'Now it is time to choose your restaurant, would you like to eat at {random_restaurant}? y/n:')
        while user_agree == 'n':
            random_restaurant =  random.choice(restaurants)
            user_agree = input(f"Sorry you didn't like that choice, how about {random_restaurant} instead? y/n:")
        if user_agree == "y":
            print (f'Okay! Your restaurant is set for {random_restaurant}')
            finalized = True
        elif user_agree != "y" and user_agree != "n":
            print("Sorry that is not a valid answer please try again")
    return random_restaurant

def transportation_set():
    finalized = False
    while finalized is False:
        random_transportation = random.choice(transportation)
        user_agree = input(f'Now it is time to choose your type of transportation, would you like to travel by {random_transportation}? y/n:')
        while user_agree == 'n':
            random_transportation = random.choice(transportation)
            user_agree = input(f"Sorry you didn't like that choice, how about {random_transportation} instead? y/n:")
        if user_agree =="y":
            print(f'Okay! Your transportation is set for {random_transportation}')
            finalized = True
        elif user_agree != "y" and user_agree != "n":
            print("Sorry that is not a valid answer please try again")
    return random_transportation

def entertainment_set():
    finalized = False
    while finalized is False:
        random_entertainment = random.choice(entertainment)
        user_agree = input(f'Now it is time to choose your form of entertainment, would you like to {random_entertainment}? y/n:')
        while user_agree == 'n':
            random_entertainment = random.choice(entertainment)
            user_agree = input(f"Sorry you didn't like that choice, how about {random_entertainment} instead? y/n:")
        if user_agree == 'y':
            print(f'Okay! Your entertainment is set for {random_entertainment}')
            finalized = True
        elif user_agree != "y" and user_agree != "n":
            print("Sorry that is not a valid answer please try again")
    return random_entertainment

def trip_confirmation_message():
   
        trip_confirm = input(f'''You are now ready to go on an amazing trip!
        Location: {set_destination}
        Restaurant: {set_restaurant}
        Transportation: {set_transportation}
        Entertainment: {set_entertainment}
        Would you like to confirm this trip? y/n:
        ''')
        
        return trip_confirm

def changing_options():
    trip_change= input('''We're sorry you didn't like your options, which part of your trip would you like to change?
        For Location Type 1:
        For Restaurant Type 2:
        For Transportation Type 3:
        For Entertainment Type 4:''')
    if trip_change == "1":
            global set_destination
            set_destination = destination_set()
            return set_destination

    if trip_change == "2":
            global set_restaurant
            set_restaurant = restaurant_set()
            return set_restaurant
        
    if trip_change=="3":
            global set_transportation
            set_transportation = transportation_set()
            return set_transportation

    if trip_change == "4":
            global set_entertainment
            set_entertainment= entertainment_set()
            return set_entertainment
           
def confirmed():
    print(f'''Thanks for using Day Trip Generator!
    Your trip is confirmed! You will be going to {set_destination}, and getting there by {set_transportation}.
    Once you are there you will dine at {set_restaurant} and {set_entertainment}''')

def run():
    confirmed_message = trip_confirmation_message()
    while confirmed_message =="n" :
        changing_options()
        confirmed_message = trip_confirmation_message()
    if confirmed_message == "y":
        confirmed()

greeting()
set_destination = destination_set()
set_restaurant = restaurant_set()
set_transportation = transportation_set()
set_entertainment = entertainment_set()
run()