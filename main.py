# main.py
from manager import RobotManager
from utils import Robot

def main():
    # Create robot objects
    robot1 = Robot("Robo1", "X100")
    robot2 = Robot("Robo2", "Z500")
    
    # Create robot manager
    manager = RobotManager()
    
    # Add robots to manager
    manager.add_robot(robot1)
    manager.add_robot(robot2)
    
    # Display all robots
    manager.display_robots()
    
    # Move robots and display status
    robot1.move(5)
    robot2.move(10)
    print()
    manager.display_robots()

if __name__ == "__main__":
    main()
