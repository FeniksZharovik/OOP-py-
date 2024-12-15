class Missile:
    """
    A class to represent a generic missile.
    """
    def __init__(self, name, range_km):
        self.name = name
        self.range_km = range_km

    def describe(self):
        """
        Describes the missile.
        """
        return f"Missile: {self.name}, Range: {self.range_km} km."