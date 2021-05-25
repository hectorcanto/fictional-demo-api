# API design and domain

In this document we will reflect the main characteristics of the API:
- REST endpoints
- load handling and caching
- caching

## REST endpoints

We will need endpoints that allows us to check sales per model in a given amount of time, something like
- model/{id}/sales?since=XX&until=YY, being XX and YY some sort of date or datetime 

The sale itself and the date itself is not that important, they need to predict the production they need have
according to the future sales, so they will need something like the sales per month (or any other interval) or the
average in a given amount of time.

It is important to notice that REST is about simplicity, lack of state, and agnosticism to the consumer, so we need to
leverage that with the needs of our users.

To give that information we can:
- Add the number of items of any given API query (`count` metadata in the response)
- Design specific non-REST endpoints for certain queries
- Provide a GraphQL endpoint where some operations can be done (like count and/or averaging)
- Provide a less detailed version of the data (`skip` query param)

For simplicity in this prototype we will provide the number of items of a given query, and with an `average`
query parameter that will provide the given computation for a period of time (day, week, month, year). This will provide
the target information without blocking the most straightforward information.

Having extra information in the queries, apart from objects, pushes us towards a more complex structured response,
so we will use a standard like `JSON:API` for it.

An example of the given idea so far:

POST model/{model_id}/sales?since=2018&average=month

```json
{
  "links": {
    "self": "localhos:8000/model/1/sales?since2018&average=month",
    "next": "localhos:8000/model/1/sales?since2018&average=month?page=1",
    "last": "localhos:8000/model/1/sales?since2018&average=month?page=19"
  },
  "data": [
    {
      "type": "sales",
      "id": "1",
      "attributes": {
        "created_at" : 155523123512,
        "office_id": 1
      }
    }
    ],
  "meta": {
    "count": 1000,
    "average": 24.39,
    "period": "6m"
  }
}
```

### Sales per model service

After the protoype phase, we can extract out the `model/pk/sales` endpoint and provide the same information but
without hitting the database using some sort of materialization, either in a PosgreSQL Materialized View or in
an auxiliary DB like Redis or DynamoDB.

Materialization will depend on consumers demands and update behaviour, and could be done either by a backend to backend
communication, a separated sync mechanism or a database trigger.

## API requests load

API will be highly queried through polling, since polling is expected to be more intense than updates, we 
need to enable mechanisms to cope with the load, we will consider:
- Allow HEAD calls to check if a resource has changed since last polling, this will increase the number of calls but 
  it will reduce mean response time and overall bandwidth
  - We need to add Last-Modified header to our response headers, using the existing model timestamps (updated_at)
  - Cache needs to be aware of meaningful changes to key endpoints  
  
### GraphQL approach

Alternatively, we could use a GraphQL approach, and extract the information depending on the consumer needs by
using the full querying power of GraphQL

### Caching approach

If we expect queries hitting the same data over and over, adding a cache is good, especially knowing that
the implementation cost is very low, as the framework gives us the means.

For the Sales per Model caching, we may need to build a separate cache table, but it is worth it as a step
before extracting out the endpoint to another service. A good caching design here, may save us an extra
service, which is desirable in early stages.

## Sales

Sales need to be queryable by model and time interval, so those fields should be indexed. By default, FK will be
indexed and `created_at` is already specified. 

A secondary endpoint could be made available listing the sales of a model per month in a given range

## Vehicle Models

For production purposes the actual vehicles are secondary and efforts should be dedicated to the
Sales-Model-Parts relationship