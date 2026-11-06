# C Good Practices

* Name all global consts with macros
* Use puts() instead of printf() if possible
* Abstract nested loops in functions if they are necessary
* Declare all vars at the block start for compatibility with C89
* Large number of local vars is a sign of bad design
* Make vars as local as you can (including in loop bodies)
* Always cast types explicitly
* Assign NULL val to pointers that are not initialized yet
* Return NULL from functions returning an address in case of errors
* int func(int array[static 10]) good for compiler to know that it's static
* Always use size_t when dealing with arrays as the sizes are machine dependent
* Use bitshifts instead of multiplication/division for performance

* const int* x: to protect the data we point to
* int const* x: to protect the pointer
* int const* const x: to protect both
* const helps the compiler to find bugs and to optimize code
* Put "const" wherever you can function arguments and arrays

* Always separate program logic from input/output operations
* Always comment your code

* Global vars in other .c files: use "extern" to declare them
* Use "#ifndef ..." to avoid compile time errors
* Preprocessor is evel: don't use its directives whenever possible
* Less code in functions: easier to debug and test

* Naming: is_ boolean, `_cnt` counters, `_msecs` for measurement units
* For global consts use "const static NAME", not #define
* Declare all "public" functions in a .h file
* Error handling: reference error codes from a file and return via a passed pointer
  * Or use callback - a function pointer passed to a function as an argument
