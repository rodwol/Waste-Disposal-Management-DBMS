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

#Helper functions for the menu (1-4)
def add_truck():
    plate_number = input("Enter truck's license plate number: ")
    truck_type = input("Enter truck's type (e.g., recycling, garbage): ")
    return Truck(plate_number, truck_type)

def add_driver():
    name = input("Enter driver's name: ")
    phone_number = input("Enter driver's phone number: ")
    return Driver(name, phone_number)

def add_route():
    area = input("Enter route's area: ")
    return Route(area)

def assign_driver_to_truck(truck, driver):
    truck.assign_driver(driver)
    driver.assign_truck(truck)


# functions for menu 5 to 7!

# Global lists to store trucks, drivers, and routes
trucks = []
drivers = []
routes = []

def assign_route_to_truck():
    plate_number = input("Enter truck's license plate number for route assignment: ")
    area = input("Enter route's area for the truck: ")
    
    # Search the truck and route if they are available in the system
    truck = next((truck for truck in trucks if truck.license_plate == plate_number), None)
    route = next((route for route in routes if route.area == area), None)

    if truck is not None and route is not None:
        truck.assign_route(route)
        route.assign_truck(truck)
        print("Route assigned successfully.")
    else:
        print("Truck or Route not found.")

def view_trucks():
    if not trucks:
        print("No trucks registered.")
        return
    for truck in trucks:
        print(f"License Plate: {truck.license_plate}, Type: {truck.type}, Driver: {(truck.driver.name if truck.driver else 'None')}, Route: {(truck.route.area if truck.route else 'None')}")

def view_drivers():
    if not drivers:
        print("No drivers registered.")
        return
    for driver in drivers:
        print(f"Name: {driver.name}, Phone Number: {driver.phone_number}, Truck: {(driver.truck.license_plate if driver.truck else 'None')}")


# functions for menu options 8-10
def view_routes(routes):
    print("Routes in the system:")
    for route in routes:
        truck_license = route.truck.license_plate if route.truck else "No route assigned"
        print("Area: {}, Truck: {}".format(route.area, truck_license))

def update_truck_information(trucks):
    license_plate = input("Enter truck's license plate number: ")
    truck = next((truck for truck in trucks if truck.license_plate == license_plate), None)
    if truck:
        new_driver_name = input("Enter new driver's name: ")
        new_route_area = input("Enter new route's area: ")

        # Check if the truck has a driver assigned
        if truck.driver:
            truck.driver.name = new_driver_name
        else:
            print("Error: No driver assigned to the truck.")

        # Check if the truck has a route assigned
        if truck.route:
            truck.route.area = new_route_area
        else:
            print("Error: No route assigned to the truck.")

        print("Truck information updated successfully!")
    else:
        print("Error: Truck not found.")

def update_driver_information(drivers):
    name = input("Enter driver's name: ")
    driver = next((driver for driver in drivers if driver.name == name), None)
    if driver:
        new_phone_number = input("Enter new phone number: ")
        driver.phone_number = new_phone_number
        print("Driver information updated successfully!")
    else:
        print("Error: Driver not found.")

#functions for menu options 11-13
def delete_truck(trucks):
    license_plate = input("Enter truck's license plate number to delete: ")
    for truck in trucks:
        if truck.license_plate == license_plate:
            trucks.remove(truck)
            print("Truck deleted successfully!")
            return
    print("Error: Truck not found.")

def delete_driver(drivers):
    name = input("Enter driver's name to delete: ")
    for driver in drivers:
        if driver.name == name:
            drivers.remove(driver)
            print("Driver deleted successfully!")
            return
    print("Error: Driver not found.")

def delete_route(routes):
    area = input("Enter route's area to delete: ")
    for route in routes:
        if route.area == area:
            routes.remove(route)
            print("Route deleted successfully!")
            return
    print("Error: Route not found.")

#Menu Options
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

trucks = []
drivers = []
routes = []

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        truck = add_truck()
        trucks.append(truck)
        print("Truck added successfully!")

    elif choice == '2':
        driver = add_driver()
        drivers.append(driver)
        print("Driver added successfully!")

    elif choice == '3':
        route = add_route()
        routes.append(route)
        print("Route added successfully!")

    elif choice == '4':
        if trucks and drivers:
            print("Available Trucks:")
            for i, truck in enumerate(trucks):
                print(f"{i+1}. License Plate: {truck.license_plate}, Type: {truck.type}")
            truck_index = int(input("Enter the index of the truck: ")) - 1
            print("Available Drivers:")
            for i, driver in enumerate(drivers):
                print(f"{i+1}. Name: {driver.name}, Phone Number: {driver.phone_number}")
            driver_index = int(input("Enter the index of the driver: ")) - 1
            assign_driver_to_truck(trucks[truck_index], drivers[driver_index])
            print("Driver assigned to truck successfully!")
        else:
            print("Please add trucks and drivers first.")

    elif choice == '5':
        assign_route_to_truck()
    
    elif choice == '6':
        view_trucks()

    elif choice == '7':
        view_drivers()

    elif choice == '8':
        view_routes(routes)

    elif choice == '9':
        update_truck_information(trucks)

    elif choice == '10':
        update_driver_information(drivers)
 
    elif choice == '11':
        delete_truck(trucks)

    elif choice == '12':
        delete_driver(drivers)

    elif choice == '13':
        delete_route(routes)
   
    elif choice == '15':
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
