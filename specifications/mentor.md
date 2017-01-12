# Mentor

## Description
This class represents a mentor @ Codecool, containing the first name, last name, year of birth, gender and nickname of the mentor.

## Parent class

Person

## Attributes

* ```first_name```
  * data type: string
  * description: stores the first name of the mentor
* ```last_name```
  * data type: string 
  * description: stores the last name of the mentor
* ```year_of_birth```
   * data type: integer
   * description: stores the date of birth of the mentor
* ```gender```
  * data type: string
  * description: stores the gender of the mentor
* ```nickname```
  * data type: string
  * description: stores the nickname of the mentor 

## Class methods

### ```create_by_csv```

Creates a list of ```Mentor``` objects having some data from the locally generated CodecoolClass object.

#### Arguments

* ```path```
  * data_type: string
  * description: holds the path to the csv file

#### Return value
list (containing Mentor objects) 
