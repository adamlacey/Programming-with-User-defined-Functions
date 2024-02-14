print("Welcome to the holiday cost calculator! Please answer the following \
questions:\n")

# Function to ask the user which city they are going to. This will get \
# the user input for each chosen city below.

def city_flight():
    print("Which city will you be flying to?\n")
    print("1. Tokyo")
    print("2. Paris")
    print("3. Rome")
    print("4. Singapore")
    print("5. Amsterdam\n")
    
    while True:
        choice = input("Please enter a number of your choice: ")
        if choice in ["1", "2", "3", "4", "5"]:
            
# Asking the user to enter a valid number for city choices below.

            if choice == "1":
                return "Tokyo"
            elif choice == "2":
                return "Paris"
            elif choice == "3":
                return "Rome"
            elif choice == "4":
                return "Singapore"
            elif choice == "5":
                return "Amsterdam"
            else:
                print("Invalid choice. Please enter the correct number.")
        #return city_flight
   
flight_choice = city_flight()
print("You will be flying to:", flight_choice, "\n") # Users choice \ 
# determines holiday location which is printed.

# Function below requires user to input how many nights they \
# will be staying for.

def num_nights():
    while True:
        try:
            nights = int(input("How many nights will you be staying at a hotel \
for?: "))
            if nights > 0: # If user input is below 0, an error is displayed.
                return nights
            else:
                print("Please enter a positive number of nights.")
        except ValueError:
            print("Invalid choice. Please enter a valid number of nights.")

# Users choice determines how many nights they will be staying for.
# Statement printed below.

holiday_nights = num_nights()
print("You will be staying at the hotel for", holiday_nights, "nights.\n")

# Function below requires user to input how many days \
# they will be hiring a car for.

def rental_days():
    while True:
        try:
            days = int(input("How many days will you be hiring a car for?: "))
            if days > 0:
                return days
            else: # If user input is below 0, an error is displayed.
                print("Please enter a positive number of days.")
        except ValueError:
            print("Invalid choice. Please enter a valid number of days.")

# Users choice determines how many days they will need a car for.
# Statement printed below.

car_hire = rental_days()
print("You will be hiring a car for", car_hire, "days.\n")


def hotel_cost(num_nights, price_per_night): 
    total_cost = num_nights * price_per_night
    return total_cost # Calculating the total cost based on the users \
# number of nights * the price per night.

price_per_night = 300
hotel_total_cost = hotel_cost(holiday_nights, price_per_night)
print("The total cost of the stay at your hotel is: £" + str(hotel_total_cost) \
+ "\n") # Displays users total hotel cost for their holiday duration.

# Flight costs based upon location selected by user.

def plane_cost(city_flight): 
    if city_flight == "Tokyo":
        return 1200
    elif city_flight == "Paris":
        return 500
    elif city_flight == "Rome":
        return 750
    elif city_flight == "Singapore":
        return 1000
    elif city_flight == "Amsterdam":
        return 600
    else:
        return None

flight_cost = plane_cost(flight_choice)

if flight_cost is not None:
    print("The cost of your flight to", flight_choice, "is: £" + str(flight_cost) \
+ "\n") # Displays users cost of flight to selected location.
else:
    print("Invalid city choice.")


def car_rental(rental_days):
    daily_rental_cost = 20
    total_cost = rental_days * daily_rental_cost
    return total_cost # Users total car rental cost is calculated based \
# upon how many days they need a car for and the daily cost.

car_rental_total_cost = car_rental(car_hire)
print("The total cost for your car rental is: £" + str(car_rental_total_cost) \
+ "\n") # Displays users total cost of rental car.


def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_cost = hotel_cost + plane_cost + car_rental
    return total_cost # Calculation to find total holiday cost.

total_cost = holiday_cost(hotel_total_cost, flight_cost, car_rental_total_cost)
print("Your total holiday cost is: £" + str(total_cost))

# Statement above is printed to show users total holiday cost.