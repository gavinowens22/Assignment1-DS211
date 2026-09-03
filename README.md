# Assignment1-DS211
#Gavin Owens

# Car Inventory Assignment

#1. Purpose 
In this assignment I create code for car inventory database. I was given a CSV file and we then created Seller and Car objects.

#Car class
in the car class we had several attributes. this class was made to represent a single car. The attributes were

- manufacturer
- model
- year
- mileage
- engine
- transmission
- drivetrain
- mpg
- exterior color
- interior color
- accident or damage status
- price

  We then had Methods which included
  - paint which changed teh exterior color of the car
  - repair which replaced the engine,transmission, or drivetrain
  - reupholster which changed the interior color
  - drive which added miles to the current mileage
  - modify_price which changes the price based on a discount
 

  #Seller Class
  this represented a individual seller or a dealership

  the attributes included were

  -name
  -rating
  -inventory

  Methods:
  -buy: this added a car to the sellers inventory if it did not exist
  - sell: this would remove a car from the sellers inventory if it did exist
 
    
## CSV Data
The program reads Cars_Data.csv and creates Car objects from each row. Cars are then placed into the inventory of their corresponding Seller object.

## Limitations
The file was too big and I had trouble uploading it to GitHub also there were a lot of missing values in the file.



