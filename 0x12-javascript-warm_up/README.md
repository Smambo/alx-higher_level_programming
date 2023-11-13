# Hey there!
## Follow me as I tackle tasks on JavaScript
## About:
JavaScript is a lightweight interpreted programming language. While it is mots well-known as the scripting language for web pages, many non-browser environments also use it, such as Node.js, Apache CouchDB and Adobe Acrobat. JavaScript's dynamic capabilities include runtime object construction, variable parameter lists, function variables, dynamic script creation, and source-code recovery (JavaScript functions store their source text and can be retrieved through `toString()`.

![image](https://github.com/Smambo/alx-higher_level_programming/assets/113464914/dbd04dbb-d947-41dc-8f83-e1ff1ce8ef92)


## Tasks:
### [0. First constant, first print](./0-javascript_is_amazing.js)
Write a script that prints “JavaScript is amazing”:

* You must create a constant variable called `myVar` with the value “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./0-javascript_is_amazing.js 
JavaScript is amazing
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ semistandard ./0-javascript_is_amazing.js 
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

### [1. 3 languages](./1-multi_languages.js)
Write a script that prints 3 lines:

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

### [2. Arguments](./2-arguments.js)
Write a script that prints a message depending of the number of arguments passed:

* If no arguments are passed to the script, print “No argument”
* If only one argument is passed to the script, print “Argument found”
* Otherwise, print “Arguments found”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./2-arguments.js 
No argument
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./2-arguments.js hello
Argument found
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./2-arguments.js hello there
Arguments found
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

Reference: [process.argv](https://nodejs.org/api/process.html#process_process_argv)
### [3. Value of my argument](./3-value_argument.js)
Write a script that prints the first argument passed to it:

* If no arguments are passed to the script, print “No argument”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `length`

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./3-value_argument.js 
No argument
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./3-value_argument.js Hello
Hello
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

### [4. Create a sentence](./4-concat.js)
Write a script that prints two arguments passed to it, in the following format: “ is ”

* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./4-concat.js c cool
c is cool
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./4-concat.js c
c is undefined
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./4-concat.js
undefined is undefined
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

### [5. An Integer](./5-to_integer.js)
Write a script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:

* If the argument can’t be converted to an integer, print “Not a number”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use `try/catch`

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./5-to_integer.js 89
My number: 89
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./5-to_integer.js "89"
My number: 89
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./5-to_integer.js 89.89
My number: 89
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./5-to_integer.js Hello
Not a number
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

### [6. Loop to languages](./6-multi_languages_loop.js)
Write a script that prints 3 lines: (like `1-multi_languages.js`) but by using an array of string and a loop

* The first line: “C is fun”
* The second line: “Python is cool”
* The third line: “JavaScript is amazing”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You are not allowed to use any `if/else` statement
* You can use only one `console.log`
* You must use a loop (`while`, `for`, etc.)

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

### [7. I love C](./7-multi_c.js)
Write a script that prints `x` times “C is fun”

* Where `x` is the first argument of the script
* If the first argument can’t be converted to an integer, print “Missing number of occurrences”
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You can use only two `console.log`
* You must use a loop (`while`, `for`, etc.)

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./7-multi_c.js 
Missing number of occurences
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./7-multi_c.js 2
C is fun
C is fun
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./7-multi_c.js 4
C is fun
C is fun
C is fun
C is fun
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./7-multi_c.js 3
C is fun
C is fun
C is fun
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

### [8. Square](./8-square.js)
Write a script that prints a square

* The first argument is the size of the square
* If the first argument can’t be converted to an integer, print “Missing size”
* You must use the character `X` to print the square
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`
* You must use a loop (`while`, `for`, etc.)

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./8-square.js 
Missing size
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./8-square.js Hello
Missing size
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./8-square.js 2
XX
XX
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./8-square.js 4
XXXX
XXXX
XXXX
XXXX
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./8-square.js -3
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

### [9. Add](./9-add.js)
Write a script that prints the addition of 2 integers

*    The first argument is the first integer
*    The second argument is the second integer
*    You have to define a function with this prototype: `function add(a, b)`
*    You must use `console.log(...)` to print all output
*    You are not allowed to use `var`

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./9-add.js 
NaN
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./9-add.js 1
NaN
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./9-add.js 1 7
8
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./9-add.js 13 89
102
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

### [10. Factorial](./10-factorial.js)
Write a script that computes and prints a factorial

*    The first argument is integer (argument can be cast as integer) used for computing the factorial
*    Factorial of `NaN` is `1`
*    You must do it recursively
*    You must use a function
*    You must use `console.log(...)` to print all output
*    You are not allowed to use `var`

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./10-factorial.js 
1
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./10-factorial.js 3
6
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./10-factorial.js 89
1.6507955160908452e+136
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$ ./10-factorial.js 333
Infinity
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x12-javascript-warm_up$
```

### [11. Second biggest!](./11-second_biggest.js)
Write a script that searches the second biggest integer in the list of arguments.

* You can assume all arguments can be converted to integer
* If no argument passed, print `0`
* If the number of arguments is 1, print `0`
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

### [12. Object](./12-object.js)
Update this script to replace the value `12` with `89`:

* You are not allowed to use `var`

```
smambo@lenovo-ubuntu:~/0x12$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

smambo@lenovo-ubuntu:~/0x12$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
smambo@lenovo-ubuntu:~/0x12$
```
### [13. Add file](./13-add.js)
Write a function that returns the addition of 2 integers.

* The function must be visible from outside
* The name of the function must be `add`
* You are not allowed to use `var`

