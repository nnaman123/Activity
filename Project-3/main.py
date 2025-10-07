def hotel_cost(nights):
    return nights * 140

def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return "City not found"

def rental_car_cost(days):
    cost = days * 40
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost

def trip_cost(city, days, spending_money):
    return hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print("cost of car rental", rental_car_cost(5))
print("cost of hotel", hotel_cost(5))
print("cost of plane ride", plane_ride_cost("Los Angeles"))
print("total trip cost", trip_cost("Los Angeles", 5, 600))
print("trip cost", trip_cost("Tampa", 3, 300))