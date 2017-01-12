# CodecoolClass

## Description
This class represents a real class @ Codecool, containing mentors and students working at the class.

## Parent class
None

## Attributes

* ```location```
  * data type: string
  * description: stores the city where the the class started
* ```year```
  * data type: integer
  * description: stores the year when the class started
* ```mentors```
   * data type: list (containing Mentor objects)
   * description: stores the mentors of the class
* ```students```
  * data type: list (containing Student objects)
  * description: stores the students of the class

## Class methods

### ```generate_local```

Creates a ```CodecoolClass``` object having some real-life data from the implementer students' real class.

#### Arguments
None

#### Return value

```CodecoolClass``` object

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```find_student_by_full_name```

Gives back a student with the same full name as the argument from ```students```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the student to be found

#### Return value
```Student``` object

### ```find_mentor_by_full_name```

Gives back a mentor with the same full name as the argument from ```mentors```

#### Arguments
* ```full_name```
  * data_type: string
  * description: holds the full name of the mentor to be found

#### Return value
```Mentor``` object

### ```get_student_all_energy```
Reads the list of ```students``` and sums their energy level

#### Arguments
None

#### Return value
```over_all_energy``` integer value

### ```get_student_all_knowledge```

Reads the list of ```students``` and sums their energy level

#### Arguments
None

#### Return value
```overall_knowledge``` integer value

### ```get_student_gender_for_print```
Decides on the given student's gender and gives back the desired pronoun for printing purposes

#### Arguments
```student``` object
```form``` decider on the type of pronoun

#### Return value
```pronoun``` string