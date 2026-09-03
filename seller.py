class Seller:
  def __init__(self,name,rating):
    self.name = name
    self.rating = rating
    self.inventory = []

  def buy(self,car):
      if car not in self.inventory:
            self.inventory.append(car)

  def sell(self,car):
      if car in self.inventory:
        self.inventory.remove(car)
 
