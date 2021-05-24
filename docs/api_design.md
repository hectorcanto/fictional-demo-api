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
- Add the number of items of any given API query,
- Design specific non-REST endpoints for certain queries
- Provide a GraphQL endpoint where some operations can be done (like count or averaging)

For simplicity in this prototype we will provide the number of items of a given query, paginated, and with an `average`
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
    "perid"d: "6m"
  }
}
```


## API requests load

API will be highly queried through polling, since polling is expected to be more intense than updates, we 
need to enable mechanisms to cope with the load, we will consider:
- Allow HEAD calls to check if a resource has changed since last polling, this will reduce response time 
  and bandwith
  - We need to add Last-Modified header to our response headers
  - Cache needs to be aware of meaningful changes to key endpoints  

## Sales

Sales need to be queryable by model and time interval, so those fields should be indexed
A secondary endpoint should be available listing the sales of a model per month in a given range

## Vehicle Models

For production purposes the actual vehicles are secondary and efforts should be dedicated to the
Sales-Model-Parts relationship