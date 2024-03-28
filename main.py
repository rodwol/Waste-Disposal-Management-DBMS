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

