from missile import Missile

class BallisticMissile(Missile):
    """
    A class to represent a ballistic missile, inheriting from Missile.
    """
    def __init__(self, name, range_km, warhead_type):
        super().__init__(name, range_km)
        self.warhead_type = warhead_type

    def describe(self):
        """
        Describes the ballistic missile with additional information.
        """
        return f"Ballistic Missile: {self.name}, Range: {self.range_km} km, Warhead Type: {self.warhead_type}."
