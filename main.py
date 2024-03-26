#!/usr/bin/python3
class Truck:
    def __init__(self, license_plate, type):
        self.license_plate = license_plate
        self.type = type
        self.driver = None
        self.route = None

class Driver:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.truck = None

class Route:
    def __init__(self, area):
        self.area = area

class WasteManagementSystem:
    def __init__(self):
        self.trucks = []
        self.drivers = []
        self.routes = []

    def add_truck(self, license_plate, type):
        truck = Truck(license_plate, type)
        self.trucks.append(truck)

    def add_driver(self, name, phone_number):
        driver = Driver(name, phone_number)
        self.drivers.append(driver)

    def assign_driver_to_truck(self, truck_index, driver_index):
        self.trucks[truck_index].driver = self.drivers[driver_index]

    def add_route(self, area):
        route = Route(area)
        self.routes.append(route)

    def assign_route_to_truck(self, truck_index, route_index):
        self.trucks[truck_index].route = self.routes[route_index]

    def view_trucks(self):
        for index, truck in enumerate(self.trucks):
            print("Truck {}: License Plate: {}, Type: {}, Assigned Driver: {}, Assigned Route: {}".format(index + 1, truck.license_plate, truck.type, truck.driver.name if truck.driver else 'Not Assigned', truck.route.area if truck.route else 'Not Assigned'))
    def view_drivers(self):
        for index, driver in enumerate(self.drivers):
            print("Driver {}: Name: {}, Phone Number: {}, Assigned Truck: {}".format(index + 1, driver.name, driver.phone_number, driver.truck.license_plate if driver.truck else 'Not Assigned'))
    def view_routes(self):
        for index, route in enumerate(self.routes):
            print("Route {}: Area: {}".format(index + 1, route.area))
    def update_truck_information(self, truck_index, driver_index=None, route_index=None):
        if driver_index is not None:
            self.trucks[truck_index].driver = self.drivers[driver_index]
        if route_index is not None:
            self.trucks[truck_index].route = self.routes[route_index]

    def update_driver_information(self, driver_index, phone_number):
        self.drivers[driver_index].phone_number = phone_number

    def delete_truck(self, truck_index):
        del self.trucks[truck_index]

    def delete_driver(self, driver_index):
        del self.drivers[driver_index]

    def delete_route(self, route_index):
        del self.routes[route_index]

    def generate_reports(self):
        for truck in self.trucks:
            print("Truck: {}, Routes: {}".format(truck.license_plate, [route.area for route in self.routes if route == truck.route]))
def main():
    system = WasteManagementSystem()

    while True:
        print("\nWaste Management System Menu:")
        print("1. Add Truck")
        print("2. Add Driver")
        print("3. Assign Driver to Truck")
        print("4. Add Route")
        print("5. Assign Route to Truck")
        print("6. View Trucks")
        print("7. View Drivers")
        print("8. View Routes")
        print("9. Update Truck Information")
        print("10. Update Driver Information")
        print("11. Delete Truck")
        print("12. Delete Driver")
        print("13. Delete Route")
        print("14. Generate Reports")
        print("15. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            license_plate = input("Enter truck's license plate number: ")
            type = input("Enter truck's type (e.g., recycling, garbage): ")
            system.add_truck(license_plate, type)
        elif choice == 2:
            name = input("Enter driver's name: ")
            phone_number = input("Enter driver's phone number: ")
            system.add_driver(name, phone_number)
        elif choice == 3:
            truck_index = int(input("Enter truck index: ")) - 1
            driver_index = int(input("Enter driver index: ")) - 1
            system.assign_driver_to_truck(truck_index, driver_index)
        elif choice == 4:
            area = input("Enter route's area: ")
            system.add_route(area)
        elif choice == 5:
            truck_index = int(input("Enter truck index: ")) - 1
            route_index = int(input("Enter route index: ")) - 1
            system.assign_route_to_truck(truck_index, route_index)
        elif choice == 6:
            system.view_trucks()
        elif choice == 7:
            system.view_drivers()
        elif choice == 8:
            system.view_routes()
        elif choice == 9:
            truck_index = int(input("Enter truck index: ")) - 1
            driver_index = int(input("Enter driver index: ")) - 1
            route_index = int(input("Enter route index: ")) - 1
            system.update_truck_information(truck_index, driver_index, route_index)
        elif choice == 10:
            driver_index = int(input("Enter driver index: ")) - 1
            phone_number = input("Enter new phone number: ")
            system.update_driver_information(driver_index, phone_number)
        elif choice == 11:
            truck_index = int(input("Enter truck index: ")) - 1
            system.delete_truck(truck_index)
        elif choice == 12:
            driver_index = int(input("Enter driver index: ")) - 1
            system.delete_driver(driver_index)
        elif choice == 13:
            route_index = int(input("Enter route index: ")) - 1
            system.delete_route(route_index)
        elif choice == 14:
            system.generate_reports()
        elif choice == 15:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 15.")

if __name__ == "__main__":
    main()
