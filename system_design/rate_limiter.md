# Design a rate limiter

Server side, not client side.

API Gateway: Cloud microservices have become widely popular and rate limiting is usually
implemented within a component called API gateway. API gateway is a fully managed
service that supports rate limiting, SSL termination, authentication, IP whitelisting, servicing
static content, etc. API gateway is a middleware that stays in between you clinets and your API servers.

Alternatively to API gateway, a rate limiter can be implemented on the API server-side.

The basic idea of rate limiting algorithms is simple. At the high-level, we need a counter to
keep track of how many requests are sent from the same user, IP address, etc. If the counter is
larger than the limit, the request is dropped.

## High-level design

Store the counter in in-memory cache (e.g., in Redis) because it's fast compared to a conventional on-dics database.

1. The client sends a request to rate limiting middleware suche as API gateway
2. Rate limiting middleware fetches the counter from the corresponding bucket in Redis
   and checks if the limit is reached or not:
  * If the limit is reached, the request is rejected.
  * If the limit is not reached, the request is sent to API servers.
       Meanwhile, the system increments the counter and saves it back to Redis.

## Exceeding the rate limit

In case a request is rate limited, APIs return a HTTP response code 429 (too many requests) to the client.

Depending on the use cases, we may enqueue the rate-limited requests to be
processed later. For example, if some orders are rate limited due to system overload, we may
keep those orders to be processed later. In this case, such requests will be send to a message queue.

## Detailed design

* Rules are stored on the disk. Workers frequently pull rules from the disk and store them in the cache.
* When a client sends a request to the server, the request is sent to the rate limiter middleware first.
* Rate limiter middleware loads rules from the cache. It fetches counters and last request
timestamp from Redis cache. Based on the response, the rate limiter decides:
  * if the request is not rate limited, it is forwarded to API servers.
  * if the request is rate limited, the rate limiter returns 429 too many requests error to
    the client. In the meantime, the request is either dropped or forwarded to the queue.

## Rate limiter in a distributed environment

Building a rate limiter that works in a single server environment is not difficult.
However, scaling the system to support multiple servers and concurrent threads is a different story.

There are two challenges:
* Race condition: Redis has mechanisms for solving it
* Synchronization issue: Synchronization is another important factor to consider
  in a distributed environment. To support millions of users, one rate limiter server
  might not be enough to handle the traffic.
  When multiple rate limiter servers are used, synchronization is required.
  The solution for a stateless web tier is to use a centralized data store like Redis.

## Performance optimization

Multi-data center setup is crucial for a rate limiter because latency is high for users
located far away from the data center. Most cloud service providers build many edge server
locations around the world. Traffic is automatically routed to the closest edge server to reduce latency.

## Monitoring

After the rate limiter is put in place, it is important to gather analytics data to check whether
the rate limiter is effective. Primarily, we want to make sure:

* The rate limiting algorithm is effective: e.g, we notice our rate limiter becomes
  ineffective when there is a sudden increase in traffic like flash sales.
  In this scenario, we may replace the algorithm to support burst traffic.
* The rate limiting rules are effective: e.g, if rate limiting rules are too strict,
  many valid requests are dropped. In this case, we want to relax the rules a little bit
