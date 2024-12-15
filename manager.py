# manager.py
from utils import Robot

class RobotManager:
    def __init__(self):
        self.robots = []

    def add_robot(self, robot):
        self.robots.append(robot)
        print(f"Robot {robot.name} added.")

    def remove_robot(self, robot_name):
        for robot in self.robots:
            if robot.name == robot_name:
                self.robots.remove(robot)
                print(f"Robot {robot_name} removed.")
                return
        print(f"Robot {robot_name} not found.")

    def get_robots_by_model(self, model):
        return [robot for robot in self.robots if robot.model == model]

    def display_robots(self):
        if not self.robots:
            print("No robots available.")
        else:
            print("List of Robots:")
            for robot in self.robots:
                print(f"Name: {robot.name}, Model: {robot.model}, Position: {robot.position}")

