import random
from turtle import Turtle

# Constants for car properties and movement
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]  # List of car colors
STARTING_MOVE_DISTANCE = 5  # Initial speed of the cars
MOVE_INCREMENT = 10  # Speed increase when leveling up

class CarManager:

    def __init__(self):
        # Initialize the car manager
        self.all_cars = []  # List to store all car objects
        self.car_speed = STARTING_MOVE_DISTANCE  # Set the initial car speed

    def create_car(self):
        # Create a new car with a 1-in-6 chance on each call
        random_chance = random.randint(1, 6)  # Generate a random number between 1 and 6
        if random_chance == 1:  # Create a car only if the number is 1
            new_car = Turtle("square")  # Create a new car object
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch the car to look rectangular
            new_car.penup()  # Prevent the car from drawing lines
            new_car.color(random.choice(COLORS))  # Set a random color from the COLORS list
            random_y = random.randint(-250, 250)  # Generate a random y-coordinate for car placement
            new_car.goto(300, random_y)  # Position the car at the right edge of the screen
            self.all_cars.append(new_car)  # Add the car to the list of cars

    def move_car(self):
        # Move all cars on the screen
        for car in self.all_cars:
            car.backward(self.car_speed)  # Move each car to the left by the current car speed

    def level_up(self):
        # Increase the speed of the cars to make the game more challenging
        self.car_speed += MOVE_INCREMENT  # Increment the car speed by the MOVE_INCREMENT value
