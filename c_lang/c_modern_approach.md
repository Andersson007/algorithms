# C Moder Approach book

## Variables

* It's best to append the letter f to float "2150.48f", otherwise, it'll be interpreted as double.

* A macro definition defines a name for a constant and can contain expressions

```
#define INCHES_PER_POUND 166

#define SCALE_FACTOR (5.0f / 9.0f)
```

* `size_t` is the right type for sizes - it's a special unsigned int type that is
   guaranteed by the C standard to be able to hold the size of the largest possible objects in memory.
   The actual underlying type of `size_t` can change depending on the system architecture.
   When using `size_t`, the code remains portable.

   ```
   size_t num_of_elem = size_of(array) / size_of(array[i]);
   for (size_t i; i < num_of_elem; i++) {
   ```

## Formatted input and output

* Many professional C programmers avoid scanf, instead reading all data in character form using getchar()
  and converting it to numeric form later

## Data types

* Ranges of values for data types are machine dependent.
  * To determine specific ranges, one way is to check the `<limits.h>` header 
    which is a part of standard library: it defines the smallest and largest values of each type.

* Integer overflow happens when a result of an operation with two ints is too large to fit the input type:
  * If the ints are signed, the result is undefined
  * If the ints are unsigned, the result is defined

### Type conversion

Computers can do arithmetic ops only on operands of the same size.

* Implicit conversion: C allows mixing basic types in expression, but the compiler converts operands of different type
so that the hardware will be able to do arithmetic on them.
This is called "implicit conversion" which happens automatically.

* Explicit conversion: is done by a programmer by using the cast operator: (type-name) expression:

```
float f = 1.1f;
int i = (int) f;
```

* Advantages of type definitions (done via typedef): can make a program more understandable and easier to
  modify w/o changing all declarations

  ```
  typedef float Dollars;
  Dollars cash_in, cash_out;
  ```

* For greater portability, consider using typedef to define new names for integer types.
  The C lib inself uses typedef to create names for types that can vary from on C implementation
  to another (often have names with `_t`, e.g. `size_t`.

  In C99, the `<stdin.h>` header uses typedef to define names for integer types with a particular
  number of bits, e.g., `int32_t` is a signed int type with exactly 32 bits.
  Using these types is an effective way to make programs more portable.
