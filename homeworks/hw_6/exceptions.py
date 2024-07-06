"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __str__(self):
        return 'Low fuel exception'


class NotEnoughFuel(Exception):
    def __init__(self, fuel_on_board: float, fuel_need: float):
        self.foul_on_board = fuel_on_board
        self.fuel_need = fuel_need

    def __str__(self):
        return (f'Not enough fuel. On board: {self.foul_on_board}, '
                f'need: {self.fuel_need}')


class CargoOverload(Exception):
    def __init__(self, cargo_to_load: float, max_posible_cargo: float):
        self.cargo_to_load = cargo_to_load
        self.max_posible_cargo = max_posible_cargo

    def __str__(self):
        return (f'Cago overload: max possible cargo: {self.max_posible_cargo},'
                f'cargo to load: {self.cargo_to_load}')
