# Python Senior Developer Exercise Plan

A useful exercise pattern for each task:

1. Solve it quickly.
2. Make it robust.
3. Add tests.
4. Benchmark it.
5. Explain the tradeoffs in writing.
6. Refactor it for readability.

## Questions to answer after finishing the tasks

- What is a closure?
- What is a decorator? Name common use cases.
- What is a higher-order function?
- What is function metadata? Name common metadata attributes.
- What is functools.wraps for?
- What is introspection?
- What is MRO? How it works in Python and why?
- What is the @property descriptor for?
- What are the __hash__ and __eq__ methods for?
- What are LEGB scoping rules? How does it affect variables inside functions?
- What is the __repr__ method for? How is it different from __str__?
- What are dataclasses for (frozen, non-frozen)? Benefits compared to regular classes?

## Tasks to solve for revision after finishing the tasks below

- Write a closure.
- Write a func using functools.partial.
- Use copy.copy and copy.deepcopy with nested DSs. Compare their values and determine if the underlying objects are the same.
- Write an example of using the @property descriptor.
- Create a diamond inheritance hierarchy and predict/verify the MRO.
- Write decorators for logging and caching that preserve the wrapped functions signature and metadata, then check its signature with the inspect module.
- Measure mem footprint of 100k objects with __slots__ vs w/o __slots__.
- Demonstrate objects equality vs identity.
- Create a set of objects with a custom __hash__ and __eq__ methods. Make an attribute used for __hash__ immutable.
- Write two samples of code that triggers LEGB scoping confusion; fix them.
- Write example of classes that use the __repr__ and __str__ methods.
- Write a dataclass and a frozen dataclass, call their __repr__ and __str__ methods.

## 1. Language Mechanics & Gotchas

* Write a function with a mutable default argument, observe the bug, and fix it two ways.
* Write a closure inside a loop that captures a variable incorrectly; fix it with a default argument and with `functools.partial`.
* Build a nested dict/list structure and demonstrate where `copy.copy` silently shares state vs `copy.deepcopy`.
* Implement a simplified `@property` from scratch using the descriptor protocol.
* Create a diamond inheritance hierarchy and predict/verify the MRO; override one method and trace the call chain.
* Write a decorator that preserves the wrapped function's signature and metadata using `functools.wraps`, then test it with `inspect.signature`.
* Write decorators for caching and logging, use functools.wraps and inspect.signature, print functions' matadata.
* Build a class that uses `__slots__` and measure the memory difference vs a regular class with 100k instances.
* Demonstrate identity vs equality: find cases where `is` gives `True` unexpectedly (int caching, string interning) and where `==` gives `True` but `is` does not.
* Create a set of objects with a custom `__hash__`/`__eq__`; demonstrate what breaks when a mutable field changes after insertion.
* Write code that triggers LEGB scoping confusion (`UnboundLocalError` from a variable that "exists"), then fix it.
- Use a frozen dataclass to create a class that is primarily data. Think of use casesof frozen and non-frozen dataclasses.

## 2. Iterators, Generators & Functional Patterns

- Write a generator that reads a 1GB+ file and yields parsed records without loading the file into memory.
- Implement `itertools.groupby` from scratch and handle the "must be pre-sorted" gotcha.
- Build a pipeline of three generators chained together (filter, transform, aggregate) and measure peak memory vs the equivalent list approach.
- Write a generator that supports `.send()` to dynamically change its behavior mid-iteration.
- Implement a lazy `flatten()` that handles arbitrarily nested iterables without recursion (use an explicit stack).
- Use `itertools.islice`, `chain`, and `tee` to solve a sliding-window aggregation without materializing the data.
- Build a custom iterable class that supports `__iter__` and `__next__`, then refactor it to a generator function and compare readability.
- Write a `@retry` decorator using a generator to control backoff timing, yielding delays between attempts.
- Implement a memory-efficient `unique_everseen()` that deduplicates an infinite stream using a set and a fallback for unhashable items.
- Compare `map`/`filter` vs list comprehensions vs generator expressions for the same task: measure readability, speed, and memory.

## 3. Concurrency & Parallelism

- Write a thread-safe counter using `threading.Lock`, then rewrite it with `queue.Queue`, and compare.
- Write a script that downloads 20 URLs concurrently with `concurrent.futures.ThreadPoolExecutor` and handles individual failures without crashing.
- Use `multiprocessing.Pool` to parallelize a CPU-bound task (e.g., hashing large files) and measure speedup vs threads.
- Build an `asyncio` task that fetches multiple endpoints with `asyncio.gather`, with per-task timeouts via `asyncio.wait_for`.
- Write an async function that accidentally blocks the event loop (e.g., `time.sleep` instead of `asyncio.sleep`), detect it, and fix it.
- Implement a producer-consumer pipeline using `queue.Queue` with a poison pill for clean shutdown.
- Add a `asyncio.Semaphore`-based rate limiter to concurrent async calls (e.g., max 5 in flight).
- Write a script that spawns a subprocess, enforces a timeout with `subprocess.run(timeout=...)`, and captures stdout/stderr separately.
- Reproduce a race condition with two threads incrementing a shared variable, then fix it with a lock and verify correctness.
- Build a timeout decorator that wraps any synchronous function using `concurrent.futures` and raises after N seconds.

## 4. Files, Streams & OS

- Process a multi-GB log file line-by-line, extract error counts per hour, using constant memory.
- Write an atomic file update: write to a temp file, `fsync`, then `os.replace` to the target path.
- Build a directory watcher using `os.scandir` polling (or `watchdog`) that reacts to new files within 1 second.
- Safely extract a ZIP archive, checking for path traversal attacks (`../` in member names) before extracting.
- Detect a file's encoding using `chardet` (or heuristics), read it, and re-encode it as UTF-8.
- Write a recursive directory diff tool using `pathlib` that reports added, removed, and modified files by hash.
- Create a temp directory with `tempfile.TemporaryDirectory` as a context manager and demonstrate cleanup on exception.
- Build a script that tails a growing log file in real time (like `tail -f`) using `seek` and polling.
- Use `pathlib` to normalize, resolve, and compare file paths across platforms; demonstrate where string path manipulation would break.
- Implement file locking with `fcntl.flock` (Unix) to prevent concurrent writes; test with two processes.

## 5. Data Parsing & Transformation

- Read a CSV with inconsistent quoting and missing columns; normalize it to a clean schema using the `csv` module.
- Deep-diff two JSON files and produce a human-readable report of additions, deletions, and changes.
- Write a regex that extracts structured fields from messy log lines; then demonstrate catastrophic backtracking with a bad pattern and fix it.
- Serialize a Python object with datetime fields and custom types to JSON using a custom `JSONEncoder` subclass.
- Parse timestamps from three different formats in the same dataset into a consistent UTC `datetime`.
- Validate incoming JSON against a schema using `jsonschema` and produce clear error messages for violations.
- Convert a deeply nested JSON API response into a flat list of dicts suitable for CSV export.
- Stream-process a newline-delimited JSON (NDJSON) file, transforming each record and writing results without loading all data.
- Build a robust parser for a key-value config format that handles comments, blank lines, quoted values, and type coercion.
- Handle Unicode normalization: demonstrate how visually identical strings can fail equality checks, fix with `unicodedata.normalize`.

## 6. Error Handling & Resilience

- Implement an HTTP retry wrapper with exponential backoff, jitter, and a max-retries cap.
- Build a custom context manager using `contextlib.contextmanager` that acquires/releases a resource and logs on failure.
- Write a checkpoint/resume system: a long batch job saves progress to disk and resumes from the last checkpoint on restart.
- Chain exceptions correctly using `raise ... from ...` and demonstrate how naked `raise` and `raise X` differ in stack trace output.
- Build a custom exception hierarchy for a domain (e.g., `ValidationError`, `NotFoundError`) and show structured `except` handling.
- Write an idempotent script that creates resources if missing and skips if already present, safe to rerun.
- Implement a circuit breaker: track failure count, open the circuit after N failures, half-open after a timeout, close on success.
- Handle partial failures in batch processing: process all items, collect errors, report at the end instead of failing fast.
- Write timezone-aware datetime handling: convert between timezones, serialize to ISO 8601, and handle DST edge cases.
- Build structured logging using `logging` with JSON output, contextual fields, and log level filtering.

## 7. Testing & Mocking

- Write a parametrized test suite using `@pytest.mark.parametrize` that covers normal, edge, and error cases for a single function.
- Mock an HTTP API call using `unittest.mock.patch` and verify the function under test handles 200, 404, and timeout responses.
- Write tests for filesystem-interacting code using `tmp_path` fixture without touching the real filesystem.
- Build a `conftest.py` with reusable fixtures that set up and tear down test state without shared mutable state between tests.
- Test a function that depends on the current time by injecting a clock (dependency injection) instead of `mock.patch("time.time")`.
- Use `pytest.raises` with `match=` to verify exception types and messages, including chained exceptions.
- Write a test that detects a resource leak (unclosed file, unstopped thread) by checking state after the function returns.
- Test a retry function by mocking a dependency that fails N times then succeeds; verify the call count and final result.
- Identify and fix a flaky test caused by dict ordering, floating-point comparison, or test pollution.
- Use `hypothesis` (property-based testing) to find an edge case in a string processing function that unit tests missed.

## 8. Debugging & Performance

- Profile a slow function with `cProfile`, identify the bottleneck, optimize it, and verify the speedup with `timeit`.
- Benchmark two implementations of the same function using `timeit`, controlling for warmup, iterations, and garbage collection.
- Find and fix an accidental O(n^2) algorithm (e.g., repeated `in` checks on a list instead of a set).
- Use `sys.getsizeof` and `tracemalloc` to compare memory usage of a list of dicts vs a list of tuples vs a list of dataclasses.
- Build a manual LRU cache with `OrderedDict`, then compare behavior and performance with `functools.lru_cache`.
- Debug a memory leak caused by lingering references (e.g., appending to a module-level list); find it with `tracemalloc` or `objgraph`.
- Profile import time of a module using `python -X importtime` and reduce startup latency by deferring heavy imports.
- Identify and fix a performance issue caused by unnecessary deep copies in a hot loop.
- Write a microbenchmark that avoids common mistakes: measure the right thing, avoid dead-code elimination, use enough iterations.
- Compare generator vs list performance for a pipeline where only the first N results are needed — demonstrate short-circuit advantage.

## 9. Packaging & Environments

- Create a minimal installable package with `pyproject.toml`, `src/` layout, and a working `pip install -e .`.
- Debug a dependency conflict: two packages require different versions of the same dependency; resolve it.
- Build a CLI tool with `argparse` (subcommands, `--help`, type validation) and make it installable via `[project.scripts]`.
- Write a `pyproject.toml` with optional dependency groups (e.g., `[dev]`, `[test]`) and install them selectively.
- Create a virtual environment, reproduce a bug that only appears with specific dependency versions, and pin the fix.
- Package a project with both a library API and a CLI entry point; verify both work after install.
- Audit a project's dependencies for known vulnerabilities using `pip-audit` or `safety` and address findings.
- Debug a "module not found" error caused by module shadowing (your file named `json.py`, `email.py`, etc.).
- Write a `noxfile.py` or `tox.ini` that runs tests across Python 3.10, 3.11, and 3.12 and reports results.
- Compare `pip freeze`, `pip-tools compile`, and `uv lock`: generate a lockfile, delete the venv, and reproduce the exact environment.

## 10. Code Design & Refactoring

- Refactor a 100+ line function into smaller composable functions with clear inputs/outputs and no shared mutable state.
- Replace a dict-heavy data flow with `dataclasses` or `NamedTuple` — add type hints and compare readability.
- Extract tightly coupled code into a testable component by introducing dependency injection (pass dependencies as arguments).
- Identify and safely remove dead code from a module using coverage reports and `grep` to verify no callers.
- Redesign a function that takes 8+ boolean/config arguments to use a config dataclass or builder pattern.
- Write a plugin system using `importlib` and entry points that loads modules dynamically by name.
- Refactor code that mixes I/O and business logic into a pure-function core with an I/O shell.
- Create a configuration system that layers defaults, config file, environment variables, and CLI args (in precedence order).
- Take a class with poor naming (vague methods, single-letter variables) and rename everything to be self-documenting.
- Review a piece of code for maintainability: identify coupling, missing error handling, implicit assumptions, and unclear intent; then fix the top 3 issues.
