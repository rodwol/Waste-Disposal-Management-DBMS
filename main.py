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

