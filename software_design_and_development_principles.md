# Final Software Design Principles

## Most relevant

1. **KISS** (Keep It Simple, Stupid)
2. **DRY** (Don't Repeat Yourself)
3. **YAGNI** (You Aren't Gonna Need It)
4. **SOLID** (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion)
5. **Separation of Concerns** (SoC)
6. **Composition over Inheritance**
7. **Fail Fast**
8. **Law of Demeter** (LoD)
9. **Principle of Least Astonishment** (POLA)
10. **Convention over Configuration** (CoC)
11. **Occam's Razor**

## Still very relevant

12. **Principle of Least Privilege** (PoLP)
13. **Inversion of Control** (IoC)
14. **Atomic Commits**

---

## Principle Details

### 1. KISS (Keep It Simple, Stupid)

- Favor the simplest solution that works; complexity is a cost, not a feature.
- Avoid clever tricks, deep abstractions, etc. when a straightforward approach will do the job.
- Simple code is easier to read, test, debug, and maintaint.

**Problem:** A developer writes a config parser that uses metaprogramming, dynamic dispatch, and a plugin registry to load a YAML file with five keys.

**Applying KISS:** Replace it with a plain function that reads the file and returns a dataclass/struct. The five-key config doesn't need an extensible architecture — a 15-line function is easier to understand and maintain.

---

### 2. DRY (Don't Repeat Yourself)

- Every entity in the project (logic, code, configuration, documentation) should have a single representation in the system.

**Problem:** Validation rules for a user's email are copy-pasted into the registration endpoint, the profile-update endpoint, and the admin panel. A new requirement (allow `+` aliases) is fixed in one place but missed in the other two.

**Applying DRY:** Extract the validation into a single `validate_email()` function and call it from all three locations. One fix, one place, consistent behavior.

---

### 3. YAGNI (You Aren't Gonna Need It)

- Don't add features or change anything until there's a concrete present need.
- Speculative code adds maintenance burden and is often wrong when the real requirement arrives.

**Problem:** A team builds a notification service that supports email, SMS, push, Slack, and carrier pigeon — but the product only sends emails today. The SMS and push modules sit untouched for two years, then need a full rewrite when the real requirements emerge.

**Applying YAGNI:** Build only the email sender. When SMS is actually needed, implement it then — with real requirements, real test cases, and the knowledge you'll have at that point.

---

### 4. SOLID

#### Single Responsibility Principle (SRP)
- A class/module should have only one reason to change.
- If a change in business rules and a change in persistence logic both force you to edit the same class, it has too many responsibilities.

**Problem:** A `Report` class fetches data from the database, applies business calculations, and formats the output as PDF. A change to the PDF layout risks breaking the calculation logic.

**Applying SRP:** Split into `ReportDataFetcher`, `ReportCalculator`, and `PdfRenderer`. Each changes for exactly one reason.

#### Open/Closed Principle (OCP)
- Software entities should be open for extension but closed for modification.
- Add new behavior by adding new code (new classes, new implementations), not by editing existing, tested code.

**Problem:** A `PaymentProcessor` uses a growing `if/elif` chain to handle credit cards, PayPal, crypto, etc. Every new payment method requires editing the core processor, risking regressions.

**Applying OCP:** Define a `PaymentMethod` interface. Each payment type implements it. The processor iterates over registered implementations — adding a new one requires zero changes to existing code.

#### Liskov Substitution Principle (LSP)
- Subtypes must be substitutable for their base types without altering program correctness.
- If a function works with a base class, it must work with any derived class without surprises.

**Problem:** `Rectangle` has `set_width()` and `set_height()`. `Square` extends `Rectangle` and overrides both so they always set both dimensions. Code that sets width to 5 and height to 10 and expects area = 50 gets 100 instead.

**Applying LSP:** Don't make `Square` a subtype of `Rectangle`. Model them as siblings implementing a common `Shape` interface with an `area()` method, preserving expected behavior.

#### Interface Segregation Principle (ISP)
- Clients should not be forced to depend on methods they don't use.
- Prefer many small, focused interfaces over one large, general-purpose one.

**Problem:** A `Worker` interface has `work()`, `eat()`, and `sleep()`. A `Robot` class is forced to implement `eat()` and `sleep()` with empty stubs or exceptions.

**Applying ISP:** Split into `Workable`, `Feedable`, and `Sleepable`. `Robot` implements only `Workable`. No stubs, no lying interfaces.

#### Dependency Inversion Principle (DIP)
- High-level modules should not depend on low-level modules; both should depend on abstractions.
- Abstractions should not depend on details; details should depend on abstractions.

**Problem:** A `UserService` directly instantiates `MySQLUserRepository`. Switching to PostgreSQL or writing unit tests with an in-memory store requires rewriting `UserService`.

**Applying DIP:** `UserService` depends on a `UserRepository` interface. `MySQLUserRepository` implements it. The database choice is injected at construction time — swapping or mocking is trivial.

---

### 5. Separation of Concerns (SoC)

- Divide a system into distinct sections, each addressing a separate concern (e.g., presentation, business logic, data access).
- Changes to one concern should not ripple into unrelated parts of the system.
- Enables independent development, testing, and evolution of each layer.

**Problem:** A web controller contains SQL queries, HTML template logic, authentication checks, and business calculations in a single 500-line function.

**Applying SoC:** Split into layers: a controller handles HTTP, a service layer holds business logic, a repository handles data access, and templates handle presentation. Each can be tested and modified independently.

---

### 6. Composition over Inheritance

- Build behavior by combining small, focused objects rather than extending deep class hierarchies.
- Inheritance creates tight coupling and fragile base-class problems; composition is more flexible.
- "Has-a" relationships are usually more accurate than "is-a" relationships.

**Problem:** A game has `Character → Warrior → FlyingWarrior → FlyingFireWarrior`. Adding a non-flying fire character means duplicating the fire logic or creating a parallel hierarchy.

**Applying Composition:** Give `Character` fields like `attack_strategy` and `movement_strategy`. A fire-breathing ground warrior gets `FireAttack` + `WalkMovement`. A flying ice mage gets `IceAttack` + `FlyMovement`. Mix and match freely, no hierarchy explosion.

---

### 7. Fail Fast

- Detect and report errors as close to their source as possible.
- Don't let invalid state propagate silently through the system only to cause a confusing failure later.
- Validate inputs at the boundary; crash loudly on invariant violations.

**Problem:** A function receives `None` for a required parameter, silently stores it, and 200 lines later a `NoneType has no attribute 'name'` traceback appears in an unrelated module. Debugging takes hours.

**Applying Fail Fast:** Add a check at the top: `if user is None: raise ValueError("user is required")`. The error now points directly at the caller that passed bad data.

---

### 8. Law of Demeter (LoD)

- An object should only talk to its immediate collaborators, not reach through them to their internals.
- Avoid long chains like `order.customer.address.city.zip_code`.
- Reduces coupling — if the internal structure changes, only the immediate owner needs updating.

**Problem:** A shipping module accesses `order.customer.address.city` directly. When `Address` is refactored to split into `shipping_address` and `billing_address`, every caller across the codebase breaks.

**Applying LoD:** `Order` exposes `order.shipping_city()`. The shipping module calls that. When the address model changes, only `Order` is updated — callers are unaffected.

---

### 9. Principle of Least Astonishment (POLA)

- Software should behave the way users and other developers would reasonably expect.
- Names, APIs, and behaviors should match their conventional meaning.
- Surprises cause bugs; predictability enables productivity.

**Problem:** A method called `get_users()` silently deletes inactive users from the database before returning the list. Callers expecting a read-only query are unknowingly mutating data.

**Applying POLA:** `get_users()` only reads. If cleanup is needed, create a separate `purge_inactive_users()` with a name that signals its side effect.

---

### 10. Convention over Configuration (CoC)

- Provide sensible defaults so that developers only need to specify unconventional aspects.
- Reduces boilerplate and decision fatigue for standard cases.
- The convention should be overridable when needed, but the default should cover 80%+ of use cases.

**Problem:** A web framework requires 200 lines of XML to map a `UserController` to `/users`, specify the view directory, declare the model binding, and configure the serializer — all of which follow the same predictable pattern.

**Applying CoC:** The framework maps `UserController` to `/users` automatically, looks for templates in `views/users/`, and binds the `User` model by name. Zero config for the common case; override only when the convention doesn't fit.

---

### 11. Occam's Razor

- When multiple solutions work, prefer the one with the fewest assumptions and moving parts.
- Complexity must justify itself — simpler explanations and designs are more likely correct.
- Applies to debugging (simplest hypothesis first) and architecture (simplest design that meets requirements).

**Problem:** A service intermittently returns stale data. The team suspects a distributed cache race condition and begins designing a cache-invalidation protocol with versioned keys and pub/sub.

**Applying Occam's Razor:** Check the simple things first. The TTL was set to 24 hours instead of 5 minutes due to a config typo. Fix the config, problem solved — no new infrastructure needed.

---

### 12. Principle of Least Privilege (PoLP)

- Grant only the minimum permissions necessary for a component to do its job.
- Applies to users, services, API tokens, database roles, and file system access.
- Limits the blast radius when something goes wrong or is compromised.

**Problem:** A microservice that only reads product data uses a database connection string with full admin privileges. A SQL injection vulnerability lets an attacker drop tables.

**Applying PoLP:** The service connects with a read-only database role. Even if exploited, the attacker cannot modify or delete data.

---

### 13. Inversion of Control (IoC)

Inversion of Control (IoC) means: Instead of your code controlling when and how other components are called, an external framework or component controls that flow.

- Without IoC: Your code creates and calls everything it needs.
- With IoC: You provide the components or rules, and a framework decides when to call them.

Simple example: In a web framework, you don't write main() that waits for HTTP requests and calls your functions.
You simply define a function like handleRequest(), and the framework calls it when a request arrives.
In short: “Don’t call us; we’ll call you.”

---

### 14. Atomic Commits

- Each commit should contain exactly one logical change — a single bug fix, a single feature, or a single refactor.
- Don't mix unrelated changes (e.g., a feature + a style fix + a rename) in the same commit.
- Makes `git bisect`, `revert`, `cherry-pick`, and code review dramatically easier.

**Problem:** A developer commits a bug fix, a variable rename, and an unrelated import cleanup in one commit. The rename introduces a regression. Reverting the commit also loses the bug fix. `git bisect` points to a large diff that's hard to reason about.

**Applying Atomic Commits:** Three separate commits: one for the bug fix, one for the rename, one for the cleanup. The regression is isolated to the rename commit — revert it cleanly, keep the bug fix, and review each change on its own merits.
