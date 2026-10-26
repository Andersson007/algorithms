# System design interview

Questions:
* Describe a typical client-server request flow
* What allows scaling
* Types of scaling
* DB scaling: horizontal + sharding
* Caching
* CDN
* Reproduce the app chart (page 3)
* Web tier scaling
* Stateless web tier
* Supporting multiple DCs
* Using message queues
* Adding loggin, monitoring, automation
* Summarize how to scale your system to support millions of users


## Types of scaling

When we separate a web tier, database tier, and other tiers as separate servers,
this allows them to be scaled independently.

* Vertical scaling: add more power (CPU, RAM, disc, etc.) to your existing servers.
  - It doesn't have failover or redundancy.

* Horizontal scaling: you use load balancers and add more servers into your pool of resources.
  - Allows failover, redundancy, and often deployment without downtime.
  - This type is better for large scale apps.

* DB scaling: one primary (handles only write queries), many replicas to read from. Failover via replica-primary promotion.

## Other ways to improve performance

### Caching

* Adding caching to improve load/responce time:
  * A Cache is a temporary in-memory storage area that stores the results of expensive responses
    or frequently accessed data so that subsequent requests are serverd more quickly
    (for example, not to call database every time a new web page loads).
  * A cache tier is a temporary data store layer, much faster than the DB.
    Can be scaled independently.
    - If data exists in cache, read it from the cache,
    - otherwise, fetch it from the DB and save it to the cache.
    - Example: Memcache.

### CDN

Shifting static content like images, videos, audio recordings, etc. to the content delivery network (CDN).

* A CDN is a network of geographically distributed servers used to deliver static content.
  When a user visits a website, a CDN server that is closest to the user will deliver static content.

* CDN is a form of caching: if data isn't there, a CDN server gets it from origin servers and stores it locally.

* Content metadata can include TTL that describes how long the content should be cached.

## Web tier scaling

* Stateless web tier is when we move state (e.g. user session data) out of the web tier to persistent storage such as RDBMS or NoSQL.
  - Each web server in the cluster can then access the state data from the DB.
  - In the stateless architecture, request from users can be sent to any web server which will fetch state data from a shared
    datastore instead of holding it locally.

* Supporting multiple data centers: users are geo-routed by a load balancer to the closest datacenter based on the clients IP addresses.

* Using message queues. A message queue serves as in in-memory buffer:
  * Input services (aka "producers"/"publishers") put messages in the message queue.
  * Subscriber services take the messages from the queue and perform actions defined by the messages.
  * When the size of the queue gets large, you scal out subscribers by adding more servers.

## Adding logging, monitoring, automation

## Scaling databases

In addition to vertical and horizontal scaling with multiple primary and possibly replicas,
sharding separates large DBs into smaller, more easily managed parts called shards.
  * Each shard shares the same schema, but the actual data on each shard is unique to the shard.
  * E.g., each shard have the same table for users, but holds a unique set of entries based on user ID.
    Then a special hash function is used to find a corresponding shard.
    * User ID is a sharding ("partition") key.
    * You route queries between your shards based on your shard/partition key.
    * Though sharding has some serious drawbacks: first, it's significanly more complext than just storing everything in the same DB.

## Summary of how to scale your system to support millions of users:

- Split tiers into individual services
- Keep web tier stateless
- Build redundancy at every tier
- Cache data as much as you can
- Support multiple DCs
- Host static assets in CDN
- Scale your data tier
- Log and monitor your systems, use automation


