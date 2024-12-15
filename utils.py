# utils.py

class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.position = 0  # Robot starts at position 0
    
    def move(self, distance):
        self.position += distance
        print(f"{self.name} moved {distance} units. New position: {self.position}")
    
    def speak(self, message):
        print(f"{self.name} says: {message}")


def reset_robot_position(robot):
    """
    Reset the robot's position to 0.
    """
    robot.position = 0
    print(f"{robot.name}'s position has been reset to {robot.position}.")

def check_robot_status(robot):
    """
    Check and return the robot's current status.
    """
    return f"Robot {robot.name} (Model: {robot.model}) is currently at position {robot.position}."

def find_robot_by_name(name, robots):
    """
    Find and return a robot by its name from a list of robots.
    """
    for robot in robots:
        if robot.name == name:
            return robot
    return None
