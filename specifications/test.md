# Test

## Description
This class represents a test @ Codecool, containing the name of the test, 
a random mentor who is the admin of the test, the participating students,
the knowledge needed to pass the test, and the lists of the students who failed and passed the test.

# Parent class
None

## Attributes

* ```name```
  * data type: string
  * description: stores the name of the test
* ```admin```
  * data type: object 
  * description: a single mentor object, randomly selected from the CodecoolClass
* ```participants```
   * data type: list (containing Student objects)
   * description: stores the students participanting in the test
* ```knowledge_to_pass```
  * data type: integer
  * description: stores the value of the knowledge level needed to pass the test
* ```result```
  * data type: dictionary (string key, integer value)
  * description: stores the number of the passed and failed students 
* ```passed_students```
  * data type: list (containing Student objects)
  * description: stores the students who passed the test
* ```failed_students```
  * data type: list (containing Student objects)
  * description: stores the students who failed the test

## Class methods

### ```organize_test```

Creates a ```Test``` object having some data from the locally generated CodecoolClass object.

#### Arguments

* ```name```
  * data_type: string
  * description: holds the name of the test
* ```cc_class```
  * data_type: object
  * description: a generated CodecoolClass object


#### Return value

```Test``` object

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```grade_test```

Sets the result, passed_students and failed_students attributes of the object.

#### Arguments
* ```knowledge_to_pass```
  * data_type: integer
  * description: holds the value of the knowledge level needed to pass the test

#### Return value
None

### ```check_admin_satisfaction```

Prints the mentors response based on the number of failed students compared to all the participants.

#### Arguments
None

#### Return value
None

### ```failers_repeat```

The failed students repeat the test. Sets the lists of the failed and passed students accordingly.

#### Arguments
None

#### Return value
None