# Design consistent hashing

To achieve horizontal scaling (to balance the load), it is important to distribute
requests/data efficiently and evenly across servers.
Consistent hashing is a commonly used technique to achieve this goal.

The re-hashing problem arises when you resize (add/remove instances, often automatically) your server pool.
Re-mapping should be limited and the mapping should stay consistent: clients are forwarded to right instances.

In production, consistent hashing is usually a part of the sharding/load-balancing system.

Real-world/open-source examples:
* HAProxy or Envoy: support consistent/hash-based load balancing.
  - Solve the problem: "I have N stateless backend servers, and I want requests with the same key to
    consistently go to the same server, while automatically adapting when servers are added/removed.”
