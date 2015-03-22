cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#100
print "There are", cars, "cars available."
#30
print "There are only", drivers, "drivers available."
#70
print "There will be", cars_not_driven, "empty cars today."
#120
print "We can transport", carpool_capacity, "people today."
#90
print "We have", passengers, "to carpool today."
#3
print "We need to put about", average_passengers_per_car, "in the car."
