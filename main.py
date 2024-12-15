from missile import Missile
from guided_missile import GuidedMissile
from ballistic_missile import BallisticMissile

if __name__ == "__main__":
    missile = Missile("Standard Missile", 500)
    guided_missile = GuidedMissile("Tomahawk", 1600, "GPS")
    ballistic_missile = BallisticMissile("Trident II", 12000, "Nuclear")

    print(missile.describe())
    print(guided_missile.describe())
    print(ballistic_missile.describe())