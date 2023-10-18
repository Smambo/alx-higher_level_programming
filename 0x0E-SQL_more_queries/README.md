# Hey there!
## Follow me as I tackle more tasks on SQL databases
## About:
Storing data in your application (in memory) has the obvious shortcoming that, whatever the technology you’re using, your data dies when your server stops. Some programming languages and/or frameworks take it even further by being stateless, which, in the case of an HTTP server, means your data dies at the end of an HTTP request. Whether the technology you’re using is stateless or stateful, you will need to persist your data somewhere. That’s what databases are for.

![sql_databases](https://github.com/Smambo/alx-higher_level_programming/assets/113464914/bf993e25-c57c-4ec1-8d4d-3d3ad740e2da)


## Tasks:
### [0.My privileges!](./0-privileges.sql)
Write a script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in `localhost`).

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo "CREATE USER 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" | mysql -hlocalhost -uroot -p
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `user_0d_1`@`localhost`
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ABORT_EXEMPT,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,FLUSH_OPTIMIZER_COSTS,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [1.Root user](./1-create_user.sql)
Write a script that creates the MySQL server user `user_0d_1`.
* `user_0d_1` should have all privileges on your MySQL server
* The `user_0d_1` password should be set to `user_0d_1_pwd`
* If the user `user_0d_1` already exists, your script should not fail

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 1-create_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `user_0d_1`@`localhost`
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ABORT_EXEMPT,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,FLUSH_OPTIMIZER_COSTS,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [2.Read user](./2-create_read_user.sql)
Write a script that creates the database `hbtn_0d_2` and the user `user_0d_2`.
* `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
* The `user_0d_2` password should be set to `user_0d_2_pwd`
* If the database `hbtn_0d_2` already exists, your script should not fail
* If the user `user_0d_2` already exists, your script should not fail

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password: 
Grants for user_0d_1@localhost
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `user_0d_1`@`localhost`
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ABORT_EXEMPT,AUDIT_ADMIN,AUTHENTICATION_POLICY_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,FLUSH_OPTIMIZER_COSTS,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,GROUP_REPLICATION_STREAM,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PASSWORDLESS_USER_ADMIN,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`
Grants for user_0d_2@localhost
GRANT USAGE ON *.* TO `user_0d_2`@`localhost`
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [3.Always a name](./3-force_name.sql)
Write a script that creates the table `force_name` on your MySQL server.
* `force_name` description:
  * `id` INT
  * `name` VARCHAR(256) can’t be null
* The database name will be passed as an argument of the `mysql` command
* If the table `force_name` already exists, your script should not fail

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO force_name (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id	name
89	Best School
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO force_name (id) VALUES (333);' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1364 (HY000) at line 1: Field 'name' doesn't have a default value
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM force_name;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id	name
89	Best School
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [4.ID can't be null](./4-never_empty.sql)
Write a script that creates the table `id_not_null` on your MySQL server.
* `id_not_null` description:
  * `id` INT with the default value 1
  * `name` VARCHAR(256)
* The database name will be passed as an argument of the `mysql` command
* If the table `id_not_null` already exists, your script should not fail

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO id_not_null (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id	name
89	Best School
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO id_not_null (name) VALUES ("Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM id_not_null;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id	name
89	Best School
1	Best
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [5.Unique ID](./5-unique_id.sql)
Write a script that creates the table `unique_id` on your MySQL server.
* `unique_id` description:
  * `id` INT with the default value `1` and must be unique
  * `name` VARCHAR(256)
* The database name will be passed as an argument of the `mysql` command
* If the table `unique_id` already exists, your script should not fail

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best School");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id	name
89	Best School
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO unique_id (id, name) VALUES (89, "Best");' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
ERROR 1062 (23000) at line 1: Duplicate entry '89' for key 'unique_id.id'
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM unique_id;' | mysql -hlocalhost -uroot -p hbtn_0d_2
Enter password: 
id	name
89	Best School
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [6.States table](./6-states.sql)
Write a script that creates the database `hbtn_0d_usa` and the table `states` (in the database `hbtn_0d_usa`) on your MySQL server.
* `states` description:
  * `id` INT unique, auto generated, can’t be null and is a primary key
  * `name` VARCHAR(256) can’t be null
* If the database `hbtn_0d_usa` already exists, your script should not fail
* If the table `states` already exists, your script should not fail

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 6-states.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id	name
1	California
2	Arizona
3	Texas
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [7.Cities table](./7-cities.sql)
Write a script that creates the database `hbtn_0d_usa` and the table `cities` (in the database `hbtn_0d_usa`) on your MySQL server.
* `cities` description:
  * `id` INT unique, auto generated, can’t be null and is a primary key
  * `state_id` INT, can’t be null and must be a `FOREIGN KEY` that references to `id` of the `states` table
  * `name` VARCHAR(256) can’t be null
* If the database `hbtn_0d_usa` already exists, your script should not fail
* If the table `cities` already exists, your script should not fail

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 7-cities.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO cities (state_id, name) VALUES (1, "San Francisco");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id	state_id	name
1	1	San Francisco
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'INSERT INTO cities (state_id, name) VALUES (10, "Paris");' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
ERROR 1452 (23000) at line 1: Cannot add or update a child row: a foreign key constraint fails (`hbtn_0d_usa`.`cities`, CONSTRAINT `cities_ibfk_1` FOREIGN KEY (`state_id`) REFERENCES `states` (`id`))
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id	state_id	name
1	1	San Francisco
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [8.Cities of California](./8-cities_of_california_subquery.sql)
Write a script that lists all the cities of California that can be found in the database `hbtn_0d_usa`.
* The `states` table contains only one record where `name` = `California` (but the `id` can be different, as per the example)
* Results must be sorted in ascending order by `cities.id`
* You are not allowed to use the `JOIN` keyword
* The database name will be passed as an argument of the `mysql` command

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM states;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id	name
1	California
2	Arizona
3	Texas
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# echo 'SELECT * FROM cities;' | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id	state_id	name
1	1	San Francisco
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
Enter password: 
id	name
1	San Francisco
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# 
```

### [9.Cities by States](./9-cities_by_state_join.sql)
Write a script that lists all cities contained in the database `hbtn_0d_usa`.
* Each record should display: `cities.id` - `cities.name` - `states.name`
* Results must be sorted in ascending order by `cities.id`
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

```

```

### [10.Genre ID by show](./10-genre_id_by_show.sql)
Write a script that lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.
* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
* Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title	genre_id
Breaking Bad	1
Breaking Bad	6
Breaking Bad	7
Breaking Bad	8
Dexter	1
Dexter	2
Dexter	6
Dexter	7
Dexter	8
Game of Thrones	1
Game of Thrones	3
Game of Thrones	4
House	1
House	2
New Girl	5
Silicon Valley	5
The Big Bang Theory	5
The Last Man on Earth	1
The Last Man on Earth	5
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [11.Genre ID for all shows](./11-genre_id_all_shows.sql)
Write a script that lists all shows contained in the database `hbtn_0d_tvshows`.
* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
* Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
* If a show doesn’t have a genre, display `NULL`
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title	genre_id
Better Call Saul	NULL
Breaking Bad	1
Breaking Bad	6
Breaking Bad	7
Breaking Bad	8
Dexter	1
Dexter	2
Dexter	6
Dexter	7
Dexter	8
Game of Thrones	1
Game of Thrones	3
Game of Thrones	4
Homeland	NULL
House	1
House	2
New Girl	5
Silicon Valley	5
The Big Bang Theory	5
The Last Man on Earth	1
The Last Man on Earth	5
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [12.No genre](./12-no_genre.sql)
Write a script that lists all shows contained in `hbtn_0d_tvshows` without a genre linked.
* Each record should display: `tv_shows.title` - `tv_show_genres.genre_id`
* Results must be sorted in ascending order by `tv_shows.title` and `tv_show_genres.genre_id`
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
title	genre_id
Better Call Saul	NULL
Homeland	NULL
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [13.Number of shows by genre](./13-count_shows_by_genre.sql)
Write a script that lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.
* Each record should display: `<TV Show genre>` - `<Number of shows linked to this genre>`
* First column must be called `genre`
* Second column must be called `number_of_shows`
* Don’t display a genre that doesn’t have any shows linked
* Results must be sorted in descending order by the number of shows linked
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

```
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries# cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
Enter password: 
genre	number_shows
Drama	5
Comedy	4
Mystery	2
Crime	2
Suspense	2
Thriller	2
Adventure	1
Fantasy	1
root@51d49543472e:/alx-higher_level_programming/0x0E-SQL_more_queries#
```

### [14.My genres](./14-my_genres.sql)
Write a script that uses the `hbtn_0d_tvshows` database to lists all genres of the show `Dexter`.
* The `tv_shows` table contains only one record where `title` = `Dexter` (but the `id` can be different)
* Each record should display: `tv_genres.name`
* Results must be sorted in ascending order by the genre name
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

```

```

### [15.Only Comedy](./15-comedy_only.sql)
Write a script that lists all Comedy shows in the database `hbtn_0d_tvshows`.
* The `tv_genres` table contains only one record where `name` = `Comedy` (but the `id` can be different)
* Each record should display: `tv_shows.title`
* Results must be sorted in ascending order by the show title
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

```

```

### [16.List shows and genres](./16-shows_by_genre.sql)
Write a script that lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.
* If a show doesn’t have a genre, display NULL in the genre column
* Each record should display: `tv_shows.title` - `tv_genres.name`
* Results must be sorted in ascending order by the show title and genre name
* You can use only one `SELECT` statement
* The database name will be passed as an argument of the `mysql` command

```

```
