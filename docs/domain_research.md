# Domain research

Before fully implementing the prototype and describe the architecture iterations we will walk through the stated
problem and try to extract some important information about the `domain`.

This analysis will help us to design our solution including models, REST endpoints and architecture.


## Domain objects

The development brief introduces several domain components:
- Sales
- Vehicles
- Regional Offices
- Vehicle models
- Parts of a vehicle
- Manufacturing facilities: the ones assembling vehicles
- Production facilities: the ones building parts

We can also infer that there will be several users:
- Salespeople, attached to a Regional Office
- Manufacturer overseers, in charge of the vehicle factories
- Productions overseers, in charge of part factories

The main feature demanded in the brief is that Sales information has to run quick from Offices to Factories, so
our implementation will focus on that.

### Sales and vehicle manufacturing

The most important information we have to handle is 'what vehicle Models we have to built according to the sales'.
So Sales will drive vehicle assembling, so the key domain objects are Sales per Model and period of time. Consequently,
we  need to know which parts belong to each model, that will shape our models and API Design.

We assume that the same type of Part can belong to more than a Model.
Individual parts are not considered here, we assume that the Production facilities keep their inventory and track their
stock on their own, we only keep Model-Part relation for them to query how many parts they have to build according to
the Sales of the models having those parts.

There are other domain objects that we are not creating here, as our service only cares about sales, so, domain concepts
like Factories or Stock are not considered here.

## Model drafts

From what gathered so far:

**Sale** model:
- id PK
- office_id FK
- model_id FK
- sale_time DT
- other info like sell price or buyer

**Office** model
- id PK
- address
- phone
- region
- other info related to the sell conditions

**Vehicle Model** model
- id
- name
- parts Many2Many rel
- vehicles One2Many rel

**PartType**
- id
- name

**PartsOfModel** intermediate table with the relations between parts types and models, that express the many
to many relationship
- id PK
- model_id FK
- part_id FK

**Vehicle**
- id PK (chassis number or VIN)
- sale FK (nullable)
- other info like build_time or factory of origin

Vehicle is a secondary domain object, but it is needed because it makes the match between a Sale and a Model

Legend:
PK: primary key
FK: Foreign Key
DT: Datetime or Timestamp

## Continuation

This is it for now regarding domain, we will take this information and use it for our API design, and our database
model implementation