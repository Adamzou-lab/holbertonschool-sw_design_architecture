#!/usr/bin/env python3
"""Decorator pattern — adding a new wrapper."""


class Beverage:
    """Base class for all beverages."""

    def cost(self):
        raise NotImplementedError

    def description(self):
        raise NotImplementedError


class Coffee(Beverage):
    """Concrete beverage: a plain coffee."""

    def cost(self):
        return 50

    def description(self):
        return "Coffee"


class MilkDecorator(Beverage):
    """Wraps a beverage and adds milk (+10)."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 10

    def description(self):
        return self._inner.description() + " + milk"


class SugarDecorator(Beverage):
    """Wraps a beverage and adds sugar (+5)."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 5

    def description(self):
        return self._inner.description() + " + sugar"


class CaramelDecorator(Beverage):
    """Wraps a beverage and adds caramel (+15)."""

    def __init__(self, inner):
        self._inner = inner

    def cost(self):
        return self._inner.cost() + 15

    def description(self):
        return self._inner.description() + " + caramel"


def main():
    milk = MilkDecorator(Coffee())
    print(milk.description(), milk.cost())

    sugar_milk = MilkDecorator(SugarDecorator(Coffee()))
    print(sugar_milk.description(), sugar_milk.cost())

    caramel = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print(caramel.description(), caramel.cost())


if __name__ == "__main__":
    main()
