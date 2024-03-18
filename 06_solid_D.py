# Dependency inversion principle

# BAD solution
"""
class FXConverter:
    def convert(self, from_currency, to_currency, amount):
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")


class App:
    def start(self):
        converter = FXConverter()
        converter.convert("EUR", "USD", 100)


if __name__ == "__main__":
    app = App()
    app.start()
"""

# GOOD solution
from abc import ABC


class CurrencyConverter(ABC):
    def convert(self, from_currency, to_currency, amount):
        pass


class FXConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print("Converting currency using FX API")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.15


class AlphaConverter(CurrencyConverter):
    def convert(self, from_currency, to_currency, amount):
        print("Converting currency using Alpha API")
        print(f"{amount} {from_currency} = {amount * 1.2} {to_currency}")
        return amount * 1.2


class App:
    def __init__(self, converter):
        self.converter = converter

    def start(self):
        self.converter.convert("EUR", "USD", 100)


if __name__ == "__main__":
    converter = AlphaConverter()  # FXConverter()
    app = App(converter)
    app.start()
