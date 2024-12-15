# test.py
import unittest
from utils import Robot
from manager import RobotManager
from utils import reset_robot_position, check_robot_status, find_robot_by_name

class TestRobot(unittest.TestCase):
    def setUp(self):
        # Set up robot objects for testing
        self.robot1 = Robot("Robo1", "X100")
        self.robot2 = Robot("Robo2", "Z500")
        self.robot3 = Robot("Robo3", "X100")
        self.manager = RobotManager()

    def test_robot_initialization(self):
        # Test robot initialization
        self.assertEqual(self.robot1.name, "Robo1")
        self.assertEqual(self.robot1.model, "X100")
        self.assertEqual(self.robot1.position, 0)

    def test_robot_move(self):
        # Test robot move functionality
        self.robot1.move(10)
        self.assertEqual(self.robot1.position, 10)
        self.robot1.move(-5)
        self.assertEqual(self.robot1.position, 5)

    def test_robot_speak(self):
        # Test robot speak functionality
        with self.assertLogs() as log:
            self.robot1.speak("Test Message")
        self.assertIn("Robo1 says: Test Message", log.output)

    def test_manager_add_robot(self):
        # Test adding robots to the manager
        self.manager.add_robot(self.robot1)
        self.manager.add_robot(self.robot2)
        self.assertEqual(len(self.manager.robots), 2)
    
    def test_manager_remove_robot(self):
        # Test removing robots from the manager
        self.manager.add_robot(self.robot1)
        self.manager.remove_robot("Robo1")
        self.assertEqual(len(self.manager.robots), 0)
        self.manager.remove_robot("NonExistentRobot")
        self.assertEqual(len(self.manager.robots), 0)
    
    def test_get_robots_by_model(self):
        # Test retrieving robots by model
        self.manager.add_robot(self.robot1)
        self.manager.add_robot(self.robot2)
        self.manager.add_robot(self.robot3)
        
        x100_robots = self.manager.get_robots_by_model("X100")
        self.assertEqual(len(x100_robots), 2)
        self.assertIn(self.robot1, x100_robots)
        self.assertIn(self.robot3, x100_robots)

    def test_manager_display_robots(self):
        # Test the display function
        self.manager.add_robot(self.robot1)
        self.manager.add_robot(self.robot2)
        with self.assertLogs() as log:
            self.manager.display_robots()
        self.assertIn("List of Robots:", log.output)
        self.assertIn("Robo1", log.output)

    def test_robot_utils(self):
        # Test utils functions
        reset_robot_position(self.robot1)
        self.assertEqual(self.robot1.position, 0)
        
        status = check_robot_status(self.robot1)
        self.assertEqual(status, "Robot Robo1 (Model: X100) is currently at position 0.")
        
        found_robot = find_robot_by_name("Robo1", self.manager.robots)
        self.assertEqual(found_robot, self.robot1)

if __name__ == "__main__":
    unittest.main()
