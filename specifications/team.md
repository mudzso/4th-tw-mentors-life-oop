# Team

## Description
This class represents a team @ Codecool, containing the name of the team and a list containing the members of the team.

## Parent class

None

## Attributes

* ```team_name```
  * data type: string
  * description: stores the name of the team
* ```team```
  * data type: list (containig Student objects)
  * description: stores the members of a team

## Class methods

### ```make_teams```

Creates a list of ```Team``` objects having some data from the locally generated CodecoolClass object.

#### Arguments

* ```n_of_members```
  * data_type: integer
  * description: the number of Student objects sorted into a Team object
* ```cc_class```
  * data_type: object
  * description: the locally created CodecoolClass object

#### Return value
list (containing Team objects) 

### ```team_knowledge_levels```

Returns a string containing the overall knowledge level of the given team.

#### Arguments

* ```Teams```
  * data_type: list
  * description: a list containing Team objects
* ```team_name```
  * data_type: string
  * description: the name of the team, we want to get the knowledge level of

#### Return value
string 

### ```do_assigment_with_random_teams```

Averages the knowledge level of the Team objects.

#### Arguments

* ```teams```
  * data_type: list
  * description: a list containing Team objects

#### Return value
None