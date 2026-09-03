class Car:
  def __init__(self,manufacturer, model, year, mileage, engine, transmission, drivetrain, mpg, exterior_color, interior_color, accidents_or_damage, price):
      self.manufacturer = manufacturer
      self.model = model
      self.year = year
      self.mileage = mileage
      self.engine = engine
      self.transmission = transmission
      self.drivetrain = drivetrain
      self.mpg = mpg
      self.exterior_color = exterior_color
      self.interior_color = interior_color
      self.accidents_or_damage = accidents_or_damage
      self.price = price  
  def paint(self, exterior_color):
      self.exterior_color = exterior_color
  def repair(self, part, replacement):
      if part == "engine":
          self.engine = replacement
      if part == "transmission":
          self.transmission = replacement
      if part == "drivetrain":
          self.drivetrain = replacement
  def reupholster(self, interior_color):
      self.interior_color = interior_color
  def drive (self, miles):
      self.mileage = miles + self.mileage
  def modify_price (self, price):
      if price < 1: 
        new_price = self.price - (self.price * price)
        print(new_price)

        confirmation = input("Is this the correct amount? ")
        if confirmation == "yes":
          self.price = new_price
      else:
          self.price = price
          

    
    
          
  
