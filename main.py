#!/usr/bin/python3

#Models
class Truck:
    def __init__(self, license_plate, type):
        self.license_plate = license_plate
        self.type = type
        self.driver = None
        self.route = None

    def assign_driver(self, driver):
        self.driver = driver

    def assign_route(self, route):
        self.route = route

class Driver:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.truck = None

    def assign_truck(self, truck):
        self.truck = truck

class Route:
    def __init__(self, area):
        self.area = area
        self.truck = None

    def assign_truck(self, truck):
        self.truck = truck

class WasteManagementSystem:
    def __init__(self):
        self.trucks = []
        self.drivers = []
        self.routes = []

def menu():
    print("\nWaste Disposal Management System")
    print("1. Add a Truck")
    print("2. Add a Driver")
    print("3. Add a Route")
    print("4. Assign a Driver to a Truck")
    print("5. Assign a Route to a Truck")
    print("6. View Trucks")
    print("7. View Drivers")
    print("8. View Routes")
    print("9. Update Truck Information")
    print("10. Update Driver Information")
    print("11. Delete Truck")
    print("12. Delete Driver")
    print("13. Delete Route")
    print("14. Generate report on the list of routes assigned to each truck")
    print("15. Exit")

# Continuing from the existing WasteManagementSystem class... (menu 5 to 7)
    def assign_route_to_truck(self, license_plate, area):
        truck = next((truck for truck in self.trucks if truck.license_plate == license_plate), None)
        route = next((route for route in self.routes if route.area == area), None)
        if truck and route:
            truck.route = route
            print(f"Route '{area}' has been assigned to truck '{license_plate}'.")
        else:
            print("Error: Truck or route not found.")

    def view_trucks(self):
        print("Trucks in the system:")
        for truck in self.trucks:
            driver_name = truck.driver.name if truck.driver else "No driver assigned"
            route_area = truck.route.area if truck.route else "No route assigned"
            print(f"License Plate: {truck.license_plate}, Type: {truck.type}, Driver: {driver_name}, Route: {route_area}")

    def view_drivers(self):
        print("Drivers in the system:")
        for driver in self.drivers:
            truck_license = driver.truck.license_plate if driver.truck else "No truck assigned"
            print(f"Name: {driver.name}, Phone Number: {driver.phone_number}, Truck: {truck_license}")

