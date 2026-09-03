import csv
from car import Car
from seller import Seller

sellers = {}

with open("Cars_Data.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        car = Car(
            row["manufacturer"],
            row["model"],
            row["year"],
            row["mileage"],
            row["engine"],
            row["transmission"],
            row["drivetrain"],
            row["mpg"],
            row["exterior_color"],
            row["interior_color"],
            row["accidents_or_damage"],
            row["price"]
        )

        seller_name = row["seller_name"]
        seller_rating = row["seller_rating"]

        if seller_name not in sellers:
            sellers[seller_name] = Seller(seller_name, seller_rating)

        sellers[seller_name].buy(car)


       
