from turtle import Turtle

# Constant for the font style used in the scoreboard
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        # Initialize the scoreboard
        super().__init__()  # Call the parent class (Turtle) constructor
        self.level = 1  # Start the game at level 1
        self.hideturtle()  # Hide the turtle shape (used only for writing text)
        self.penup()  # Lift the pen to avoid drawing lines while moving
        self.goto(-290, 260)  # Position the scoreboard at the top-left corner of the screen
        self.update_scoreboard()  # Display the initial level

    def update_scoreboard(self):
        # Update the scoreboard display with the current level
        self.clear()  # Clear the previous level text
        self.write(f"Level {self.level}", align="left", font=FONT)  # Write the current level

    def increase(self):
        # Increment the level and update the scoreboard
        self.level += 1  # Increase the level by 1
        self.update_scoreboard()  # Refresh the scoreboard to display the new level

    def game_over(self):
        # Display "GAME OVER" message at the center of the screen
        self.goto(0, 0)  # Move to the center of the screen
        self.write(f"GAME OVER", align="center", font=FONT)  # Write the game-over text
