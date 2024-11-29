import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Configure the screen size to 600x600
screen.tracer(0)  # Turn off the automatic screen updates for smoother animation

# Initialize game objects
player = Player()  # Create the player object
car_manager = CarManager()  # Create the car manager for handling car objects
scoreboard = Scoreboard()  # Create the scoreboard for tracking and displaying the score

# Set up keyboard controls
screen.listen()  # Enable the screen to listen for keyboard events
screen.onkey(player.go_up, "Up")  # Move the player up when the "Up" arrow key is pressed

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Pause for a short duration to control game speed
    screen.update()  # Refresh the screen

    car_manager.create_car()  # Generate a new car at intervals
    car_manager.move_car()  # Move all the cars on the screen

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If any car is too close to the player
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display the "Game Over" message

    # Detect successful crossing
    if player.finish():  # Check if the player has reached the finish line
        player.start()  # Reset the player's position to the start
        car_manager.level_up()  # Increase car speed to make the game harder
        scoreboard.increase()  # Update and display the new score

# Exit the game when the screen is clicked
screen.exitonclick()
