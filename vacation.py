def hotel_cost(nights):
    return 40 * nights


def plane_cost(city):
    if city == "London":
        return 100
    elif city == "Paris":
        return 125
    elif city == "Tokyo":
        return 800
    elif city == "New York":
        return 750


def rental_car_cost(days):
    car_cost = 30 * days
    if days >= 7:
        car_cost -= 25
    elif days >= 3:
        car_cost -= 10
    return car_cost


def trip_cost(city, days, stuff):
    return rental_car_cost(days) + plane_cost(city) + hotel_cost(days) + stuff

cost_night=input("How many nights are you going to travel? ")

print("Total vacation cost:")
print(trip_cost("New York", 20, 600))
