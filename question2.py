
class Taxi:

    def calculate_fare(self, distance):
        return 5000 + (2000 * distance)


# Bus class
class Bus:

    def calculate_fare(self, distance):
        return 1000 * distance


# Motorcycle class
class Motorcycle:

    def calculate_fare(self, distance):
        return 2000 + (1500 * distance)

 # transport objects
taxi = Taxi()
bus = Bus()
motorcycle = Motorcycle()

transports = [taxi, bus, motorcycle]

# Distance
distance = 10

print("TRANSPORT BOOKING SYSTEM")

for transport in transports:
    fare = transport.calculate_fare(distance)
    print("Fare for 10 km:", "UGX", fare)