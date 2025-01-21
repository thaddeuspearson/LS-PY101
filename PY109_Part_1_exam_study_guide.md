# PY109 Part 1: Exam Study Guide

## [naming conventions](https://launchschool.com/books/python/read/variables#namingconventions)

### legal vs. idiomatic

> The concept of legal naming convention vs. idiomatic naming convention contrasts what _can_ be done, and what _should_ be done, from a pythonic standpoint. For example, the legal, idiomatic way to declare a non-constant variable is with `snake_case`. It is also legal to use `camelCase` in this instance, however, this would not be considered idiomatic.

### illegal vs. non-idiomatic

> The concept of illegal naming convention vs. non-idiomatic naming convention contrasts what _can_ be done, with what _shouldn't_ be done from a pythonic standpoint. For example, it is illegal to name a function beginning with a number, like `1st_name`. This will Raise a `SyntaxError`. An example of a legal, non-idiomatic function name would be `first_Name`, as no uppercase characters are idiomatically used in function definitions.

## [type coercion](https://launchschool.com/books/python/read/basic_ops#coercion): 

### explicit

> Explicit coercion occurs when a value is called with a built-in function in order to be interpreted as a specific type. An example of explicit coercion is using `int()` or `str()` on a value. This will explicitly tell the Python interpreter to treat the values passed to each of these as an integer or a string respectively.

### implicit

> Implicit coercion occurs when an expression or function call automatically converts an argument to a specific type in order to complete the intended operation. For example, any argument passed to the `print()` built in function will implicitly be converted to a string representation of the argument. In the case of expressions, such as adding an int to a float, the Python interpreter will attempt to implictly convert any operands to the necessary type in order for the operation to be able to complete. In the event the Python interpreter is unable to implicintly coerce a given value in an expression, such as trying to add an integer value to a string, it will raise a `TypeError`.

## [numbers](https://launchschool.com/books/python/read/data_types#numericvalues)

### integers
- Primitive date type
- The integer data type (`int`) represents integers, ex: the whole numbers (..., -3, -2, -1, 0, 1, 2, 3, ...).
- Integers do not have a fractional (or decimal) part.

### floats
- Primitive data type
- The floating point data type (`float`) represents floating point numbers, aka, the real numbers.
- Floating point numbers include integers and numbers with digits after the decimal point.

## [strings](https://launchschool.com/books/python/read/data_types#textsequences)

### string literals
- Primitive data type
- A string (`str`) is a text sequence of Unicode characters.
- Wrapped in single (`'`) or double (`"`) quotes. Multi-line strings use triple single(`'''`) or double (`"""`) quotes.
- Escape special characters with a backslash (`\`).
- Access the individual characters in a string with the `[]` indexing syntax

### f-strings
- formatted string literal that enable **string interpolation**
- `f'Blah {expression} blah.'`
- Python replaces the `{expression}` substring with the value of the expression inside the braces: it interpolates the expression's value.

### string methods

- [`capitalize`](https://www.w3schools.com/python/ref_string_capitalize.asp), [`swapcase`](https://www.w3schools.com/python/ref_string_swapcase.asp), [`upper`](https://www.w3schools.com/python/ref_string_upper.asp), [`lower`](https://www.w3schools.com/python/ref_string_lower.asp)

- [`isalpha`](https://www.w3schools.com/python/ref_string_isalpha.asp), [`isdigit`](https://www.w3schools.com/python/ref_string_isdigit.asp), [`isalnum`](https://www.w3schools.com/python/ref_string_isalnum.asp), [`islower`](https://www.w3schools.com/python/ref_string_islower.asp), [`isupper`](https://www.w3schools.com/python/ref_string_isupper.asp), [`isspace`](https://www.w3schools.com/python/ref_string_isspace.asp)

- [`strip`](https://www.w3schools.com/python/ref_string_strip.asp), [`rstrip`](https://www.w3schools.com/python/ref_string_rstrip.asp), [`lstrip`](https://www.w3schools.com/python/ref_string_lstrip.asp), [`replace`](https://www.w3schools.com/python/ref_string_replace.asp)

- [`split`](https://www.w3schools.com/python/ref_string_split.asp), [`find`](https://www.w3schools.com/python/ref_string_find.asp), [`rfind`](https://www.w3schools.com/python/ref_string_rfind.asp)

## [boolean](https://launchschool.com/books/python/read/data_types#booleanvalues) vs. [truthiness](https://launchschool.com/books/python/read/flow_control#truthiness)

### Booleans
- Primitive data type
- `True` or `False`
- Evaluate to `1` and `0` respectively

### Truthiness
- Arise in conditional expressions, such as `if` and `while` statements
- Falsey values: `False`, `None`, `0`, `''`,`[]`, `()`, `{}`, `set()`, `frozenset()`, and `range(0)`
- Everything else is truthy



## [`None`](https://launchschool.com/books/python/read/data_types#none)
- A way to express the absence of a value.

## [ranges](https://launchschool.com/books/python/read/data_types#sequences)
- A sequence of integers between two endpoints.
- With one argument, the range starts from 0 and ends just before the argument.
- With two arguments, the first argument is the starting point, while the second argument is one past the last number in the range.
- With three arguments, the 3rd argument is a step value.
- Ranges are homogenous; they always contain integers.
- immutable

## [lists](https://launchschool.com/books/python/read/intro_collections#whatsequences)
-
- Lists and tuples are heterogeneous; they may contain different kinds of objects, including other sequences
- mutable

### list methods 
1. [`len(list)`](), [`list.append()`](), [`list.pop()`](), [`list.reverse()`]()

## [dictionaries]()
### dictionary methods
1.  [`dict.keys()`](), [`dict.values()`](), [`dict.items()`](), [`dict.get()`]()

### slicing (strings, lists, tuples)

### operators

1.  [Arithmetic](): `+`, `-`, `*`, `/`, `//`, `%`, `**`

1.  [String operators](): `+`

1.  [List operators](): `+`

1.  [Comparison](): `==,` `!=`, `&lt;`, `&gt;`, `&lt;=`, `&gt;=`

1.  [Logical](): `and`, `or`, `not`

1.  [Identity](): `is`, `is not`

1.  [operator precedence]()

### mutability and immutability

### variables

1.  naming conventions

1.  initialization, assignment, and reassignment

1.  scope

1.  [`global`]() keyword

1.  variables as pointers

1.  variable shadowing

### conditionals and loops

1.  [`for`]()

1.  [`while`]()

### [`print()`]() and [`input()`]()

### exceptions (when they will occur and how to handle them)

### Functions:

1.  definitions and calls

1.  return values

1.  parameters vs. arguments

1.  nested functions

1.  output vs. return values, side effects

### expressions and statements

