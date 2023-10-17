# Hey there!
## Follow me as I tackle tasks on SQL databases.
## About:

Storing data in your application (in memory) has the obvious shortcoming that, whatever the technology you’re using, your data dies when your server stops. Some programming languages and/or frameworks take it even further by being stateless, which, in the case of an HTTP server, means your data dies at the end of an HTTP request. Whether the technology you’re using is stateless or stateful, you will need to persist your data somewhere. That’s what databases are for.

## Tasks:
### [0. List a database](./0-list_databases.sql)
Write a script that lists all databases of your MySQL server
```
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 0-list_databases.sql | mysql -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
sys
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction#
```
### [1. Create a database](./1-create_database_if_missing.sql)
Write a script that creates the database `hbtn_0c_0` in your MySQL server.
* If the database `hbtn_0c_0` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

```
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
hbtn_0c_0
information_schema
mysql
performance_schema
sys
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction#
```
### [2. Delete a database](./2-remove_database.sql)
Write a script that deletes the database `hbtn_0c_0` in your MySQL server.
* If the database `hbtn_0c_0` doesn’t exist, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

```
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
hbtn_0c_0
information_schema
mysql
performance_schema
sys
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
sys
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction#
```
### [3. List tables](./3-list_tables.sql)
Write a script that lists all the tables of a database in your MySQL server.

* The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)

```
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql
columns_priv
component
db
default_roles
engine_cost
func
general_log
global_grants
gtid_executed
help_category
help_keyword
help_relation
help_topic
innodb_index_stats
innodb_table_stats
password_history
plugin
procs_priv
proxies_priv
replication_asynchronous_connection_failover
replication_asynchronous_connection_failover_managed
replication_group_configuration_version
replication_group_member_actions
role_edges
server_cost
servers
slave_master_info
slave_relay_log_info
slave_worker_info
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction#
```

### [4. First table](./4-first_table.sql)
Write a script that creates a table called `first_table` in the current database in your MySQL server.
* `first_table` description:
  * `id` INT
  * `name` VARCHAR(256)
* The database name will be passed as an argument of the `mysql` command
* If the table `first_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

```
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction#
```
### [5. Full description](./5-full_table.sql)
Write a script that prints the full description of the table` first_table` from the database `hbtn_0c_0` in your MySQL server.
* The database name will be passed as an argument of the `mysql` command
* You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements

```
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table	Create Table
first_table	CREATE TABLE `first_table` (\n  `id` int DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction#
```
### [6. List all in table](./6-list_values.sql)
Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.
* All fields should be printed
* The database name will be passed as an argument of the `mysql` command

```
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction#
```
### [7. First add](./7-insert_value.sql)
Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.
* New row:
  * `id` = `89`
  * `name` = `Best School`
* The database name will be passed as an argument of the `mysql` command

```
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id	name
89	Best School
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction# cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id	name
89	Best School
89	Best School
89	Best School
root@51d49543472e:/alx-higher_level_programming/0x0D-SQL_introduction#
```
### [8. Count 89](./8-count_89.sql)
Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.
* The database name will be passed as an argument of the `mysql` command

```

```
### [9. Full creation](./9-full_creation.sql)
Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.
* `second_table` description:
  * `id` INT
  * `name` VARCHAR(256)
  * `score` INT
* The database name will be passed as an argument to the `mysql` command
* If the table `second_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` and `SHOW` statements
* Your script should create these records:
  * `id` = 1, `name` = “John”, `score` = 10
  * `id` = 2, `name` = “Alex”, `score` = 3
  * `id` = 3, `name` = “Bob”, `score` = 14
  * `id` = 4, `name` = “George”, `score` = 8

```

```
### [10. List by best](./10-top_score.sql)
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the `mysql` command

```

```
### [11. Select the best](./11-best_score.sql)
Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the `mysql` command

```

```
### [12. Cheating is bad](./12-no_cheating.sql)
Write a script that updates the score of Bob to `10` in the table `second_table`.
* You are not allowed to use Bob’s id value, only the `name` field
* The database name will be passed as an argument of the `mysql` command

```

```
### [13. Score too low](./13-change_class.sql)
Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* The database name will be passed as an argument of the `mysql` command

```

```
### [14. Average](./14-average.sql)
Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* The result column name should be `average`
* The database name will be passed as an argument of the `mysql` command

```

```

### [15. Number by score](./15-groups.sql)
Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* The result should display:
  * the `score`
  * the number of records for this `score` with the label `number`
* The list should be sorted by the number of records (descending)
* The database name will be passed as an argument to the `mysql` command

```

```
### [16. Say my name](./16-no_link.sql)
Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.
* Don’t list rows without a `name` value
* Results should display the score and the name (in this order)
* Records should be listed by descending score
* The database name will be passed as an argument to the `mysql` command

```

```
