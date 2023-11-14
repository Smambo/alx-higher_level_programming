# Hey there!
## Follow me as I tackle tasks on JavaScript objects, scopes and closures
## Tasks:
### [0. Rectangle #0](./0-rectangle.js)
Write an empty class `Rectangle` that defines a rectangle:
* You must use the `class` notation for defining your class

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ cat 0-main.js
#!/usr/bin/node
const Rectangle = require('./0-rectangle');

const r1 = new Rectangle();
console.log(r1);
console.log(r1.constructor);
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./0-main.js 
Rectangle {}
[class Rectangle]
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

### [1. Rectangle #1](./1-rectangle.js)
Write a class `Rectangle` that defines a rectangle:
* You must use the `class` notation for defining your class
* The constructor must take 2 arguments `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ cat 1-main.js
#!/usr/bin/node
const Rectangle = require('./1-rectangle');

const r1 = new Rectangle(2, 3);
console.log(r1);
console.log(r1.width);
console.log(r1.height);

const r2 = new Rectangle(2, -3);
console.log(r2);
console.log(r2.width);
console.log(r2.height);

const r3 = new Rectangle(2);
console.log(r3);
console.log(r3.width);
console.log(r3.height);

smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$ ./1-main.js 
Rectangle { width: 2, height: 3 }
2
3
Rectangle { width: 2, height: -3 }
2
-3
Rectangle { width: 2, height: undefined }
2
undefined
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x13-javascript_objects_scopes_closures$
```

### [2. Rectangle #2](./2-rectangle.js)
Write a class `Rectangle` that defines a rectangle:
* You must use the `class` notation for defining your class
* The constructor must take 2 arguments `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object

### [3. Rectangle #3](./3-rectangle.js)
Write a class `Rectangle` that defines a rectangle:
* You must use the `class` notation for defining your class
* The constructor must take 2 arguments: `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
* Create an instance method called `print()` that prints the rectangle using the character `X`

### [4. Rectangle #4](./4-rectangle.js)
Write a class `Rectangle` that defines a rectangle:
* You must use the `class` notation for defining your class
* The constructor must take 2 arguments: `w` and `h`
* Initialize the instance attribute `width` with the value of `w`
* Initialize the instance attribute `height` with the value of `h`
* If w or h is equal to 0 or not a positive integer, create an empty object
* Create an instance method called `print()` that prints the rectangle using the character `X`
* Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
* Create an instance method called `double()` that multiples the `width` and the `height` of the rectangle by 2

### [5. Square #0](./5-square.js)
Write a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:
* You must use the `class` notation for defining your class and `extends`
* The constructor must take 1 argument: `size`
* The constructor of `Rectangle` must be called (by using `super()`)

### [6. Square #1](./6-square.js)
Write a class `Square` that defines a square and inherits from `Square` of `5-square.js`:
* You must use the `class` notation for defining your class and `extends`
* Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
  * If `c` is `undefined`, use the character `X`

### [7. Occurrences](./7-occurrences.js)
Write a function that returns the number of occurrences in a list:
* Prototype: `exports.nbOccurences = function (list, searchElement)`

### [8. Esrever](./8-esrever.js)
Write a function that returns the reversed version of a list:
* Prototype: `exports.esrever = function (list)`
* You are not allow to use the built-in method `reverse`

### [9. Log me](./9-logme.js)
Write a function that prints the number of arguments already printed and the new argument value. (see example below)
* Prototype: `exports.logMe = function (item)`
* Output format: `<number arguments already printed>: <current argument value>`

```
smambo@lenovo-ubuntu:~/0x13$ cat 9-main.js
#!/usr/bin/node
const logMe = require('./9-logme').logMe;

logMe("Hello");
logMe("Best");
logMe("School");

smambo@lenovo-ubuntu:~/0x13$ ./9-main.js
0: Hello
1: Best
2: School
smambo@lenovo-ubuntu:~/0x13$ 
```

### [10. Number conversion](./10-converter.js)
Write a function that converts a number from base 10 to another base passed as argument:
*    Prototype: `exports.converter = function (base)`
*    You are not allowed to import any file
*    You are not allowed to declare any new variable (`var`, `let`, etc..)

