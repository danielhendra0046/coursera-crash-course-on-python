## Practice Quiz: For Loops
* **Total points: 5**
* **Grade: 100%**

<br>

### Question 1
How are while loops and for loops different in Python?

* While loops can be used with all data types, for loops can only be used with numbers.
* For loops can be nested, but while loops can't.
* **While loops iterate while a condition is true, for loops iterate through a sequence of elements.**
* While loops can be interrupted using break, for loops using continue.

> We can use while loops when we want our code to execute repeatedly while a condition is true, and for loops when we want to execute a block of code for each element of a sequence.

```
def factorial(n):
    result = 1
    for x in range(1, n):
        result *= x
    return result

for n in range(0, 10):
    print(n, factorial(n+1))
```

Output:

```
0 1
1 1
2 2
3 6
4 24
5 120
6 720
7 5040
8 40320
9 362880
```