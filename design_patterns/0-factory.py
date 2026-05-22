#!/usr/bin/env python3
"""Factory pattern — extending a registry."""


class Bus:
    """Represents a bus vehicle that travels on roads."""

    def mode(self):
        return "road"


class Train:
    """Represents a train vehicle that travels on rails."""

    def mode(self):
        return "rails"


class Bike:
    """Represents a bike vehicle that travels on dedicated lanes."""

    def mode(self):
        return "lane"


class Scooter:
    """Represents a scooter vehicle that travels on scooter lanes."""

    def mode(self):
        return "scooter_lane"


class VehicleFactory:
    """Centralizes vehicle creation via a registry,
    respecting Open/Closed Principle."""
    def __init__(self):
        self._registry = {}
        self._registry["bus"] = Bus
        self._registry["train"] = Train
        self._registry["bike"] = Bike

    def register_kind(self, name: str, cls):
        """Register a new vehicle type under the given name."""
        self._registry[name] = cls

    def create(self, kind: str):
        """Instantiate and return a vehicle by its registered name."""
        cls = self._registry.get(kind)
        if cls is None:
            raise ValueError(f"Unknown vehicle type: {kind}")
        return cls()


def main():
    factory = VehicleFactory()

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
