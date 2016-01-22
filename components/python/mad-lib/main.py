# Jeffrey Davidson
# January 22, 2016
# MadLib

# Your name provided by input
your_name = raw_input("Enter your name: ")

# The amount of days you want to be gone on vacation.
your_vacation_days = raw_input("How many days do you want to go on a vacation to Disney World? ")

# Decision on whether to go to multiple parks on the same day.
park_hopper = raw_input("Would you like to be able to go to more than one park in a day? Answer must be either Yes or No: ")

# Decision whether or not to go to Sea World during the vacation.
sea_world = raw_input("Do you want to go to Sea World on your vacation? Answer must be either Yes or No: ")

# Estimated price of a single one day ticket to Sea World.
price_sea_world = int(50)

# Estimated price of a park hopper add on to a Disney package.
price_park_hopper = int(80)

# Amount of days desired for vacation by you.
your_vacation_days = int(your_vacation_days)

# The amount of days I want to be gone on vacation.
my_vacation_days = int(12)

# Time to find out who wants a longer vacation. The higher number of days is the number of days used.
if your_vacation_days >= my_vacation_days:
    total_days = your_vacation_days
else:
    total_days = my_vacation_days

# Total price of 1 day per per in a Disney Park
price_per_day = int(80)

# Array of 4 theme parks inside of Walt Disney World
disney_parks = ["Magic Kingdom", "Animal Kingdom", "Hollywood Studios", "Epcot"]

# Dictionary of assigned park icons that belong to their parks.
disney_parks_icons = dict()
disney_parks_icons = {disney_parks[0]:"Cinderella's Castle", disney_parks[1]:"Tree Of Life", disney_parks[2]:"unknown", disney_parks[3]:"Epcot Ball"}

# Calculates how much money it will be to go on our vacation
def calculateVacationCost(total_days, price):
    total_price = int(total_days) * price

    # Using answers provided to calculate possible additional cost.
    if (park_hopper == "Yes" and sea_world == "Yes"):
        additional_money = price_park_hopper + price_sea_world
    elif (park_hopper == "Yes" and sea_world == "No"):
        additional_money = price_park_hopper
    elif (sea_world == "Yes" and park_hopper == "No"):
        additional_money = price_sea_world
    elif (park_hopper == "No" and sea_world == "No"):
        additional_money = 0
    else:
        pass

    vacation_cost = int(total_price) + int(additional_money)

    return vacation_cost

# Amount returned for cost of vacation
vacation_cost = calculateVacationCost(total_days, price_per_day)

# Total amount of cost for vacation of both of us going.
grand_total_vacation_cost = vacation_cost + vacation_cost

# Start of our vacation.
print "Today we are planning our next vacation together to Walt Disney World in Orlando, Florida. We have decided to be gone for " + str(total_days) + " days. What a vacation we will have. We will be gong to "

# Listing out the parks inside of Walt Disney World.
for park in range(0, len(disney_parks)):
    if park==(len(disney_parks)-1):
        print "and " + disney_parks[park] + '.',
    else:
        print disney_parks[park] + ',',


