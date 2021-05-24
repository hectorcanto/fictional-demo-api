# Process brieffing

## Intro

In this document I'll explain briefly the process I followed

## Steps

- First I read a few times the Dev Brief document, to really understand what is requesting
  - With the information gathered I produced a draft of models, to help me understand how the API and DB should be, as 
well as to see how to cut the system into simpler pieces.
  - Also, I produced a domain reference document that will drive the naming and structure of the code

- I did some research on RDS and Aurora, since Aurora is new for me. Other AWS elements I already knew

- Implement a first iteration of the models and their factories  
  - Test the models
  - I found some issue with the UUID PK and decide to replace it with plain Auto incremental integers
    since I could not found a solution quickly
- Implement and test a basic version of the API endpoints (pytest)
  - Make the cool ModelSales endpoint and add query_params
  - At this time I had spent plenty of time so I avoided setting up a docker-compose environment and do extra
    work on models, API features and testings
  -  Test and add errors to the ModelSales endpoint 
- Create a population command to have data to query
- Create a Postman collection to query the populated data and prepare the demo  
- Produce 2 architecture diagrams and play around with Diagrams
- Complete the documentation including
  - This document
  - General README
  - ADR example
