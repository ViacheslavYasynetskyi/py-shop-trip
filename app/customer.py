from app.car import Car
from app.shop import Shop
from app.fuel_price import FuelPrice

import datetime


class Customer:
    def __init__(self, data_customer: dict) -> None:
        self.name = data_customer["name"]
        self.products = data_customer["product_cart"]
        self.location = data_customer["location"]
        self.money = data_customer["money"]

    def distance_to_shop(self, shop: Shop) -> float:
        distance = ((shop.location[0] - self.location[0]) ** 2
                    + (shop.location[1] - self.location[1]) ** 2) ** 0.5
        return distance

    def cost_trip(self, shop: Shop, car: Car, data: FuelPrice) -> float:
        cost = (self.distance_to_shop(shop)
                * car.fuel_consumption / 100
                * data.fuel_price)
        return round(cost, 2)

    def full_cost(self, shop: Shop, car: Car, data: FuelPrice) -> float:
        cost_full = self.cost_trip(shop, car, data) * 2
        for food in self.products:
            cost_full += self.products[food] * shop.product[food]
        return cost_full

    def shopping(self, shop: Shop, car: Car, data: FuelPrice) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location
        date_of_purchase = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
        print(f"Date: {date_of_purchase}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought:")
        sum_prices = 0
        for food, count in self.products.items():
            sum_prices += self.products[food] * shop.product[food]
            print(f"{count} {food}s for {sum_prices} dollars")
        print(f"Total cost is {self.full_cost(shop, car, data)} dollars")
        print("See you again!")
        print(f"{self.name} rides home")
        self.money -= self.full_cost(shop, car, data)
        print(f"{self.name} now has {self.money} dollars")
