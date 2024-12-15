from .missile import Missile

class GuidedMissile(Missile):
    """
    A class to represent a guided missile, inheriting from Missile.
    """
    def __init__(self, name, range_km, guidance_system):
        super().__init__(name, range_km)
        self.guidance_system = guidance_system

    def describe(self):
        """
        Describes the guided missile with additional information.
        """
        return f"Guided Missile: {self.name}, Range: {self.range_km} km, Guidance System: {self.guidance_system}."