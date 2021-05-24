
Framework selection
===================

We need to choose a Python framework for a quick prototype and reasonable evolution

* Status: 
  * proposed - 2021-05-23
  * accepted - 2021-05-24
    
* Author(s): Hecotr Canto
* Deciders: CitNOW

* Related documments:
  *  Software Developer Brief(../docs/dev_brief.pdf), Colin Hamilton, 2020-12-11


Context and Problem Statement
-----------------------------

We need to choose a series of libraries to build our API
The prototype has to function and be demoed
Testing is also important, so a testable design is advisable.

Decision
---------
## Decision Drivers

* Knowledge of the stack
* Implementation velocity
* Reusability
* Demo factor

## Considered Options

* FastAPI + Flask + SQL Alchemy
* Django + Rest Framework

## Decision Outcome

We've chosen Django plus Rest Framework because it allows us fast prototyping and reusage of existing code.
We take SQL out of the picture, thanks to the ORM, and provide complete CRUD endpoins with RestFramework
With good tactics we may transform it to something more flexible like other frameworks.

Although we wanted to try out FastAPI and Marshmallow, we rather leave that for another ocassion where the time
is not an issue.

### Pros and expected benefits

<> (Can be a list or a group of sections or a combination. Always list them.)

* ORM provides high abstraction while allowing raw queries
* Compatibility with REST and GraphQL
* Good Integration with SQL, NoSQL and AWS
* Many good plugins for anything
* Well-know framework with good docs and support
* Async support
 
### Cons and potential risks

* Coupling between Views and Models
* A bit difficult to work with DDD
* Extra work for reusability

## Possible improvements

* Use a Repository pattern wrapping the ORM
* Avoid relying on Django apps, to avoid coupling with the framework
* Use Marshmallow for API Validation and Serialization, less coupling and compatibility with other frameworks (FastAPI, Flask ...)
