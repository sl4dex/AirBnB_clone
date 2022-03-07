# HBNB: an Airbnb clone
![hbnb](https://user-images.githubusercontent.com/22855312/156941892-2db52c11-c64d-4b63-a7ee-a0c5c2fcf295.png)
## Description
The idea of the project is to make a very similar program to that of [AirBnB](https://www.airbnb.com).  
What is AirBnB? It's an online marketplace for house, hotel, and hostel rentals. It does not own any  
of the listed properties, instead it just displays all available properties listed by vendors for guests to rent. 
<br /><br />
We achieve these functionalities with our custom command interpreter using the [cmd python library](https://docs.python.org/3/library/cmd.html)  
## Project Installation
`git clone https://github.com/sl4dex/AirBnB_clone`
### Project tree
```
AirBnB_clone
|
|-- models
|   |
|   |-- engine
|   |   |
|   |   |-- file_storage.py
|   |   `-- __init__.py
|   |
|   |-- amenity.py
|   |-- base_model.py
|   |-- city.py
|   |-- __init__.py
|   |-- place.py
|   |-- review.py
|   |-- state.py
|   `-- user.py
|
|-- tests
|   |
|   |-- test_models
|   |   |
|   |   |-- test_engine
|   |   |   |
|   |   |   |-- __init__.py
|   |   |   `-- test_file_storage.py
|   |   |
|   |   |-- __init__.py
|   |   |-- test_amenity.py
|   |   |-- test_base_model.py
|   |   |-- test_city.py
|   |   |-- test_place.py
|   |   |-- test_review.py
|   |   |-- test_state.py
|   |   `-- test_user.py
|   |
|   |-- __init__.py
|   `-- test_console.py
|
|-- AUTHORS
|-- console.py
|-- file.json
`-- README.md
```
### Class hierarchy (only subclasses and attributes)
```
BaseModel
|
|-- User(BaseModel)
|   |
|   |-- email
|   |-- password
|   |-- first_name
|   `-- last_name
|
|-- State(BaseModel)
|   |
|   |-- state_id
|   `-- name
|
|-- City(BaseModel)
|   |
|   `-- name
|
|-- Amenity(BaseModel)
|   |
|   `-- name
|
|-- Place(BaseModel)
|   |
|   |-- city_id
|   |-- user_id
|   |-- name
|   |-- description
|   |-- number_rooms
|   |-- number_bathrooms
|   |-- masx_guest
|   |-- price_by_night
|   |-- latitude
|   |-- longitude
|   `-- amenity_ids
|
|-- Review(BaseModel)
|   |
|   |-- place_id
|   |-- user_id
|   `-- text
|
|-- id
|-- created_at
`-- updated_at
```
## HBNB command interpreter
To start the hbnb console just execute the console.py file  
`./console.py` 
### Usage
You can check all available commands by typing `help`  
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) 
```
and exit the console by typing `quit`

### create: object creation
#### Syntax
create classname  
classname.create()  
#### Description
Creates a new instance of a class, saves it to the JSON file, and prints the id
#### Example
```
(hbnb) create BaseModel
660d0e7c-5834-4c40-a5e3-29feadc1fcbd
(hbnb) 
```
### destroy: object deletion
#### Syntax
destory classname id 
classname.destroy(id)  
#### Description
Deletes object with specified id, saves the changes to JSON file 
#### Example
```
(hbnb) destroy BaseModel 660d0e7c-5834-4c40-a5e3-29feadc1fcbd
(hbnb) 
```
### all, show: object listing
#### Syntax
all  
all classname  
classname.all()  
#### Description
prints all string representation of all instances based or not on the class name   
#### Example
```
(hbnb) all
[
  "[BaseModel] (7d53b2fc-b209-4400-ab78-e424a36153f0)
  <{'id': '7d53b2fc-b209-4400-ab78-e424a36153f0',
    'created_at': datetime.datetime(2022, 3, 4, 8, 52, 34, 314075),
    'updated_at': datetime.datetime(2022, 3, 4, 8, 52, 34, 314886)
  }>", 
  "[City] (62eb94be-4fbc-4236-a87f-b6899a34648e) 
  <{'state_id': '',
    'name': '',
    'id': '62eb94be-4fbc-4236-a87f-b6899a34648e',
    'created_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653498), 
    'updated_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653513)
  }>"
]
(hbnb) 
```
```
(hbnb) all City
[
  "[City] (62eb94be-4fbc-4236-a87f-b6899a34648e) 
  <{'state_id': '',
    'name': '',
    'id': '62eb94be-4fbc-4236-a87f-b6899a34648e',
    'created_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653498), 
    'updated_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653513)
  }>"
]  
```
#### Syntax  
show classname id  
classname.show(id)  
#### Description
prints the string representation of an instance with the specified id  
#### Example
```
(hbnb) show City 62eb94be-4fbc-4236-a87f-b6899a34648e
[
  "[City] (62eb94be-4fbc-4236-a87f-b6899a34648e) 
  <{'state_id': '',
    'name': '',
    'id': '62eb94be-4fbc-4236-a87f-b6899a34648e',
    'created_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653498), 
    'updated_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653513)
  }>"
]
(hbnb) 
```
### count: object counting
#### Syntax  
classname.count()  
#### Description
Retrieve the number of instances of a class
#### Example
```
(hbnb) BaseModel.count()
2
(hbnb) User.count()
0
(hbnb) 
```
### update: object modification
#### Syntax  
update classname id attrname attrvalue  
classname.update(id, attrname, attrvalue)  
update classname id {'attrname': "attrvalue" ...}  
classname.update(id, {'attrname': "attrvalue" ...})  
#### Description
Updates attribute/s of an instance with the specified id. You can update:  
- a single value specifying an attribute name and the new value
- a single or multiple values with a dictionary of attribute names and values as items
#### Example
```
(hbnb) show City 62eb94be-4fbc-4236-a87f-b6899a34648e
[
  "[City] (62eb94be-4fbc-4236-a87f-b6899a34648e) 
  <{'state_id': '',
    'name': '',
    'id': '62eb94be-4fbc-4236-a87f-b6899a34648e',
    'created_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653498), 
    'updated_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653513)
  }>"
]
(hbnb) update City 62eb94be-4fbc-4236-a87f-b6899a34648e name, Chicago
(hbnb) show City 62eb94be-4fbc-4236-a87f-b6899a34648e
[
  "[City] (62eb94be-4fbc-4236-a87f-b6899a34648e) 
  <{'state_id': '',
    'name': 'Chicago',
    'id': '62eb94be-4fbc-4236-a87f-b6899a34648e',
    'created_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653498), 
    'updated_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653513)
  }>"
]
```
```
(hbnb) update City 62eb94be-4fbc-4236-a87f-b6899a34648e {'name': "Seattle", 'state_id': "0300"}
(hbnb) show City 62eb94be-4fbc-4236-a87f-b6899a34648e
[
  "[City] (62eb94be-4fbc-4236-a87f-b6899a34648e) 
  <{'state_id': '0300',
    'name': 'Seattle',
    'id': '62eb94be-4fbc-4236-a87f-b6899a34648e',
    'created_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653498), 
    'updated_at': datetime.datetime(2022, 3, 6, 13, 55, 59, 653513)
  }>"
]
```
<br /><br /><br /><br />
_Developed by Ignacio Castellan & Salvador Diaz_
