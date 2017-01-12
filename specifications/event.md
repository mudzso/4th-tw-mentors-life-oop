# Event

## Description
This object represents a codecooler event. It can either be a party or meeting.

## Parent class
None

## Attributes

* ```event_name```
    * data type: string
    * description: stores the name of the event
* ```CCclass```
    * data type: object
    * description: stores the ```CodecoolClass``` object for further usage
* ```drink_alcohol```
    * data type: boolean
    * description: decides whether it is allowed to consume alcohol at the event or not
* ```location```
    * data type: string
    * description: stores the location at which the event is held
* ```date```
    * data type: string
    * description: stores the date of the event
 
## Class methods

### ```organize_event```
Creates an ```Event``` type objects

#### Arguments
* ```CCclass``` object

#### Return value
* ```Event``` 

## Instance methods

### ```get_drunk```
All hell breaks loose and everybody starts and proceeds to get drunk as dirt

#### Arguments
None

#### Return value
None