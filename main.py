import dataclasses
import machine
from machine import Pin

@dataclasses.dataclass
class Doors:
    main_door: Pin = Pin(0, Pin.IN)
    garage_door: Pin = Pin(0, Pin.IN)

@dataclasses.dataclass
class Lights:
    light_1: Pin = Pin(0, Pin.IN)
    light_2: Pin = Pin(0, Pin.IN)
    light_3: Pin = Pin(0, Pin.IN)
    light_4: Pin = Pin(0, Pin.IN)

@dataclasses.dataclass
class Utils:
    alarm: Pin = Pin(0, Pin.IN)
    piezo: Pin = Pin(0, Pin.IN)
    car: Pin = Pin(0, Pin.IN)
    electric_meter: Pin = Pin(0, Pin.IN)

@dataclasses.dataclass
class Pins:
    utils = Utils()
    lights = Lights()
    doors = Doors()

class Program:
    def __init__(self):
        self.pins = Pins()

    def open_garage(self):
        self.pins.doors.garage_door.high()

    def close_garage(self):
        self.pins.doors.garage_door.low()

    def open_door(self):
        self.pins.doors.garage_door.high()

    def close_door(self):
        self.pins.doors.garage_door.high()
