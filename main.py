destinations = ['Paris', 'Tokyo', 'Rome', 'Greece', "Los Angeles", 'Cancun', 'Las Vegas', 'Egypt', 'Puerto Rico', 'Brazil', 'Madagascar', "Alaska"]
restaurants = ['Coopers Hawk', 'Olive Garden', 'Red Lobster', "Hells Kitchen", 'Eggology', 'Savoury', 'Burnt Toast', 'The Fire Grille']
transportation = ['Bus', 'Airplane', 'Train', 'Road Trip', 'Boat', 'Bike', 'Helicopter', 'Ferry']
entertainment = ['Go Gambling', 'Go Shopping', 'Visit Historical Monument', 'Ask the Locals for what to do', 'Go to the club', 'Try new food']

import random
def destination_set():
    random_destination = random.choices(destinations)
    user_agree = input(f'Hi, Welcome to the Day Trip Generator, where we help you make your perfect trip. We have chosen {random_destination} for your destination. Would you like to keep this Destination? y/n:')
    while user_agree == 'n':
        random_destination = random.choices(destinations)
        user_agree = input(f'Sorry you didnt like that choice, how about {random_destination} instead? y/n:')
    if user_agree == 'y':
        print(f"Okay! Your destination is set for {random_destination}")


destination_set()