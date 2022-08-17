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
        if trip_confirm == "n":
            trip_change= input('''We're sorry you didn't like your options, which part of your trip would you like to change?
            For Location Type 1:
            For Restaurant Type 2:
            For Transportation Type 3:
            For Entertainment Type 4:''')
            if trip_change == "1":
                set_destination = destination_set()
            if trip_change == "2":
                set_restaurant = restaurant_set()
            if trip_change=="3":
                set_transportation = transportation_set()
            if trip_change == "4":
                set_entertainment= entertainment_set()
            