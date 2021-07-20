# Introduction
## DJANGO contactbook

The task is to create a simple address management app (contactbook). There should be a
super class “AddressEntry”, so the attributes can be defined only once. This class should
provide the following attributes:
● “gender” (Options should be selectable: “male”, “female”)
● “name” (String)
● “firstname” (String)
● “birthdate” (Date)
● “active” (Boolean, default=True)
Based on the super class there needs to be 2 different classes (objects) called “Person” and
“Contact”. These 2 objects would have additional attributes and methods, which are not the
same, so it makes sense to work with 2 own Classes (objects) inherit from “AddressEntry”,
which will be stored in the database. For history reasons it is mandatory that objects that get
deleted, are not deleted permanently, instead the attribute “active” should be set to False.
As this application is a microservice of an embedded whole project, a REST API should be
provided, and it is a closed system, so it needs to be protected - the endpoints are only
accessible for authenticated users.
TDD (Test-driven development) principles should be followed, so please make sure you do
provide right away unit tests for your code
Tasks
1. Setup a simple django project with the 3 classes mentioned “AddressEntry”, “Person”
and “Contact”
2. Provide for both objects “Person” and “Contact” the “CRUD” endpoints under
accessible under the url: “<project_url>/api/contacts” and
“<project_url>/api/persons”
a. Make sure the DELETE endpoint does set the “active” flag to FALSE instead of
deleting the object
b. Do only list the active objects for LIST endpoint
3. Provide an API LIST endpoint “<project_url>/api/addresses”, where a filter parameter
“is_older_than” is provided – the endpoint should return a list of all “Persons” and
“Contacts”, which are older than the given parameter
4. Nice to have: provide a client (python package), so we can easily use the REST API
with python


## Done

...

## Installation

```sh
pull source from github
open project in PyCharm
from PyCharm open requirements.txt file and install required packages
```


