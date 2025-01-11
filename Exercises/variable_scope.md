# Variable Scope Exercises
Exercises to reinforce scoping concepts in Python.

<br>

## Questions
1. What will the following code print and why? *Don't run it until you have tried to answer.*
    
    ```python
    num = 5

    def my_func():
        print(num)

    my_func()
    ```
    <details>
    <summary>Answer</summary>
    <br>
    The variable num is initialized to 5 in the global scope and is accessible within the scope of the my_func function. When my_func is called, it prints 5.
    </details>
<br>

2. What will the following code print and why? *Don't run it until you have tried to answer.*

    ```python
    num = 5

    def my_func():
        num = 10

    my_func()
    print(num)
    ```
    <details>
    <summary>Answer</summary>
    <br>
    The variable num is initialized to 5 in the global scope. When my_func is called, it initializes a local variable also called num *(which shadows the global variable num)* and sets it's value to 10. The print statement on the last line then prints 5, as the original global variable num is in scope.
    </details>
<br>

3. What will the following code print and why? *Don't run it until you have tried to answer.*

    ```python
    num = 5

    def my_func():
        global num
        num = 10

    my_func()
    print(num)
    ```
    <details>
    <summary>Answer</summary>
    <br>
    The variable num is initialized to 5 in the global scope. When my_func is called, it references the globally scoped variable num. it then and sets it's value to 10. The print statement on the last line then prints 10, as the original global variable num has been reassigned by my_func.
    </details>
<br>

4. What will the following code print and why? *Don't run it until you have tried to answer.*

    ```python
    def outer():
        outer_var = 'Hello'

        def inner():
            inner_var = 'World'
            print(outer_var, inner_var)

        inner()

    outer()
    ```
    <details>
    <summary>Answer</summary>
    <br>
    The outer func initializes outer_var and sets it's value to the string "Hello". It then defines a nested function, inner, and within it's scope initializes another variable called inner_var, and sets it's value to the string "World". When the function outer is executed, it also calls inner, which prints "Hello World" using outer_var *(which it has access to via the lexical scope)* and inner_var *(which is a local variable)*. 
    </details>
<br>
    
5. What will the following code print and why? *Don't run it until you have tried to answer.*

    ```python
    def my_func():
        num = 10

    my_func()
    print(num)
    ```
    <details>
    <summary>Answer</summary>
    <br>
    The print statement on the last line will throw a NameError, as the variable num is locally scoped to my_func, and after execution finishes, is not available in the global scope.
    </details>
<br>

6. What will the following code print and why? *Don't run it until you have tried to answer.*

    ```python
    def my_func():
        x = 15

        def inner_func1():
            x = 25
            print("Inner 1:", x)

        def inner_func2():
            print("Inner 2:", x)

        inner_func1()
        inner_func2()

    my_func()
    ```
    <details>
    <summary>Answer</summary>
    <br>
    Since inner_func1 and inner_func2 are both defined and executed within my_func, when my_func is executed, inner_func1 will print "Inner 1: 25" and inner_func_2 will print "Inner 2: 15". inner_func2 has access to x in lexical scope where x is defined as 15 in my_func. In inner_func1, x is a local variable that is shadowing x in lexical scope, and it is assigned to 25 within inner_func1's local scope.
    </details>
    <br>