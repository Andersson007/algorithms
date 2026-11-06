# Compiling a C program

```
gcc -std=cN -Wall -Wextra -Werror -g -ON -pedantic -o <output-filename> <file.c>
```

-std=cN     - C standard to use
-Wall       - enable most common warnings
-Wextra     - enable extra, less common warnings
-Werror     - treat all warnings as errors (stop compilation)
-g          - generate debugging info (for tools like gdb)
-ON         - optimization level (0-2)
-pedantic   - issue warnings strictly required by the C standard
