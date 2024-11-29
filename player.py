from turtle import Turtle

# Constants for the player's starting position, movement, and finish line
STARTING_POSITION = (0, -280)  # Initial position of the player
MOVE_DISTANCE = 10  # Distance the player moves with each step
FINISH_LINE_Y = 280  # Y-coordinate of the finish line

class Player(Turtle):
    def __init__(self):
        # Initialize the player as a Turtle object
        super().__init__()  # Call the parent class (Turtle) constructor
        self.shape("turtle")  # Set the player's shape to a turtle
        self.penup()  # Lift the pen to prevent drawing lines while moving
        self.start()  # Place the player at the starting position
        self.setheading(90)  # Face the player upward (toward the finish line)

    def go_up(self):
        # Move the player upward by a fixed distance
        self.forward(MOVE_DISTANCE)

    def start(self):
        # Reset the player to the starting position
        self.goto(STARTING_POSITION)

    def finish(self):
        # Check if the player has crossed the finish line
        if self.ycor() > FINISH_LINE_Y:  # If the player's Y-coordinate is above the finish line
            return True  # Return True indicating the player finished
        else:
            return False  # Otherwise, return False
