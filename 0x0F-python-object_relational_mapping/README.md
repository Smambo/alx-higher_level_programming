# Hey there!
## Follow me as I tackle tasks on Object-relational mapping (ORM) in Python
## About:
An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code. ORMs provide a high-level abstraction upon a relational database that allows a developer to write Python code instead of SQL to create, read, update and delete data and schemas in their database.
![image](https://github.com/Smambo/alx-higher_level_programming/assets/113464914/8069a6aa-c972-43ba-bda6-91076384def2)


## Tasks:
### [0. Get all states](./0-select_states.py)
Write a script that lists all `states` from the database `hbtn_0e_0_usa`:

* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 0-select_states.sql | mysql -uroot -p
Enter password: 
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [1. Filter states](./1-filter_states.py)
Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:

* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 0-select_states.sql 
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 0-select_states.sql | mysql -uroot -p
Enter password: 
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
(9, 'New York')
(10, 'Nevada')
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [2. Filter states by user input](./2-my_filter_states.py)
Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.

* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* You must use `format` to create the SQL query with the user input
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 0-select_states.sql 
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 0-select_states.sql | mysql -uroot -p
Enter password: 
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
(7, 'Arizona')
(12, 'Arizona')
(17, 'Arizona')
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [3. SQL Injection...](./3-my_safe_filter_states.py)
Write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!

* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (safe from MySQL injection)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 0-select_states.sql 
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 0-select_states.sql | mysql -uroot -p
Enter password: 
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./3-my_safe_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [4. Cities by states](./4-cities_by_state.py)
Write a script that lists all `cities` from the database `hbtn_0e_4_usa`

* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `cities.id`
* You can use only `execute()` once
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 4-cities_by_state.sql 
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./4-cities_by_state.py root root hbtn_0e_4_usa
(1, 'San Francisco', 'California')
(2, 'San Jose', 'California')
(3, 'Los Angeles', 'California')
(4, 'Fremont', 'California')
(5, 'Livermore', 'California')
(6, 'Page', 'Arizona')
(7, 'Phoenix', 'Arizona')
(8, 'Dallas', 'Texas')
(9, 'Houston', 'Texas')
(10, 'Austin', 'Texas')
(11, 'New York', 'New York')
(12, 'Las Vegas', 'Nevada')
(13, 'Reno', 'Nevada')
(14, 'Henderson', 'Nevada')
(15, 'Carson City', 'Nevada')
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [5. All cities by state](./5-filter_cities.py)
Write a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`

* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` (SQL injection free!)
* You must use the module `MySQLdb` (`import MySQLdb`)
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `cities.id`
* You can use only `execute()` once
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 4-cities_by_state.sql 
-- Create states table in hbtn_0e_4_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_4_usa;
USE hbtn_0e_4_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 4-cities_by_state.sql | mysql -uroot -p
Enter password: 
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./5-filter_cities.py root root hbtn_0e_4_usa Texas
Dallas, Houston, Austin, Dallas, Houston, Austin
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./5-filter_cities.py root root hbtn_0e_4_usa Hawaii

(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [6. First state model](./model_state.py)
Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:

* `State` class:
  * inherits from `Base` [Tips](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html)
  * links to the MySQL table `states`
  * class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  * class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null
* You must use the module `SQLAlchemy`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* *WARNING:* all classes who inherit from `Base` *must* be imported before calling `Base.metadata.create_all(engine)`

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 6-model_state.sql
-- Create database hbtn_0e_6_usa
CREATE DATABASE IF NOT EXISTS hbtn_0e_6_usa;
USE hbtn_0e_6_usa;
SHOW CREATE TABLE states;
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 6-model_state.sql | mysql -uroot -p
Enter password: 
ERROR 1146 (42S02) at line 4: Table 'hbtn_0e_6_usa.states' doesn't exist
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 6-model_state.py
#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./6-model_state.py root root hbtn_0e_6_usa
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 6-model_state.sql | mysql -uroot -p
Enter password: 
Table	Create Table
states	CREATE TABLE `states` (\n  `id` int NOT NULL AUTO_INCREMENT,\n  `name` varchar(128) NOT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [7. All states via SQLAlchemy](./7-model_state_fetch_all.py)
Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`

*    Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
*    You must use the module `SQLAlchemy`
*    You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
*    Your script should connect to a MySQL server running on `localhost` at port `3306`
*    Results must be sorted in ascending order by `states.id`
*    Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 7-model_state_fetch_all.sql
-- Insert states
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 7-model_state_fetch_all.sql | mysql -uroot -p hbtn_0e_6_usa
Enter password: 
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [8. First state](./8-model_state_fetch_first.py)
Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`

* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* The state you display must be the first in `states.id`
* You are not allowed to fetch all states from the database before displaying the result
* If the table `states` is empty, print `Nothing` followed by a new line
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
1: California
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# 
```

### [9. Contains 'a'](./9-model_state_filter_a.py)
Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`

* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `states.id`
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./9-model_state_filter_a.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
5: Nevada
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [10. Get a state](./10-model_state_my_get.py)
Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`

* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name to search` (SQL injection free)
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* You can assume you have one record with the state name to search
* Results must display the `states.id`
* If no state has the name you searched for, display `Not found`
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
3
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./10-model_state_my_get.py root root hbtn_0e_6_usa Illinois
Not found
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [11. Add a new state](./11-model_state_insert.py)
Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`

* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Print the new `states.id` after creation
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./11-model_state_insert.py root root hbtn_0e_6_usa
6
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: Arizona
3: Texas
4: New York
5: Nevada
6: Louisiana
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [12. Update a state](./12-model_state_update_id_2.py)
Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`

* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Change the name of the `State` where `id = 2` to `New Mexico`
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./12-model_state_update_id_2.py root root hbtn_0e_6_usa
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
1: California
2: New Mexico
3: Texas
4: New York
5: Nevada
6: Louisiana
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [13. Delete states](./13-model_state_delete_a.py)
Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`

* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./13-model_state_delete_a.py root root hbtn_0e_6_usa
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
2: New Mexico
4: New York
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

### [14. Cities in state](./14-model_city_fetch_by_state.py)
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.

* `City` class:
  * inherits from `Base` (imported from `model_state`)
  * links to the MySQL table `cities`
  * class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  * class attribute `name` that represents a column of a string of 128 characters and can’t be null
  * class attribute `state_id` that represents a column of an integer, can’t be null and is a foreign key to `states.id`
* You must use the module `SQLAlchemy`

Next, write a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:

* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
* You must use the module `SQLAlchemy`
* You must import `State` and `Base` from `model_state` - `from model_state import Base, State`
* Your script should connect to a MySQL server running on `localhost` at port `3306`
* Results must be sorted in ascending order by `cities.id`
* Results must be display as they are in the example below (`<state name>: (<city id>) <city name>`)
* Your code should not be executed when imported

```
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 14-model_city_fetch_by_state.sql
-- Create database hbtn_0e_14_usa, tables states and cities + some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_14_usa;
USE hbtn_0e_14_usa;

CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

CREATE TABLE IF NOT EXISTS cities ( 
    id INT NOT NULL AUTO_INCREMENT, 
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
INSERT INTO cities (state_id, name) VALUES (1, "San Francisco"), (1, "San Jose"), (1, "Los Angeles"), (1, "Fremont"), (1, "Livermore");
INSERT INTO cities (state_id, name) VALUES (2, "Page"), (2, "Phoenix");
INSERT INTO cities (state_id, name) VALUES (3, "Dallas"), (3, "Houston"), (3, "Austin");
INSERT INTO cities (state_id, name) VALUES (4, "New York");
INSERT INTO cities (state_id, name) VALUES (5, "Las Vegas"), (5, "Reno"), (5, "Henderson"), (5, "Carson City");
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping# cat 14-model_city_fetch_by_state.sql | mysql -uroot -p
Enter password: 
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
California: (1) San Francisco
California: (2) San Jose
California: (3) Los Angeles
California: (4) Fremont
California: (5) Livermore
Arizona: (6) Page
Arizona: (7) Phoenix
Texas: (8) Dallas
Texas: (9) Houston
Texas: (10) Austin
New York: (11) New York
Nevada: (12) Las Vegas
Nevada: (13) Reno
Nevada: (14) Henderson
Nevada: (15) Carson City
(venv) root@35318dc49ca3:/alx-higher_level_programming/0x0F-python-object_relational_mapping#
```

