## Python Networking #1
## Learning Objectives:
At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

* How to fetch internet resources with the Python package `urllib`
* How to decode `urllib` body response
* How to use the Python package `requests` #requestsiswaysimplerthanurllib
* How to make HTTP `GET` request
* How to make HTTP `POST`/`PUT`/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

## Tasks:
### [0. What's my status? #0](./0-hbtn_status.py)<br>
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`<br>

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x11-python-network_1$ ./0-hbtn_status.py | cat -e
Body response:$
	- type: <class 'bytes'>$
	- content: b'OK'$
	- utf8 content: OK$
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x11-python-network_1$
```

### [1. Response header value #0](./1-hbtn_header.py)<br>
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.<br>

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x11-python-network_1$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
fca4f321-9388-4332-b1b7-6be9e4073267
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x11-python-network_1$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
30d22f45-dcb4-4251-b737-084c98e57e93
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x11-python-network_1$
```

### [2. POST an email #0](./2-post_email.py)<br>
Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)<br>

```
root@ac05dbe003d0:/0x11# ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
root@ac05dbe003d0:/0x11#
```

### [3. Error code #0](./3-error_code.py)<br>
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).<br>

```
root@ac05dbe003d0:/0x11# ./3-error_code.py http://0.0.0.0:5000
Index
root@ac05dbe003d0:/0x11# ./3-error_code.py http://0.0.0.0:5000/status_401
Error code: 401
root@ac05dbe003d0:/0x11# ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
root@ac05dbe003d0:/0x11# ./3-error_code.py http://0.0.0.0:5000/status_500
Error code: 500
root@ac05dbe003d0:/0x11#
```

### [4. What's my status? #1](./4-hbtn_status.py)<br>
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`<br>

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x11-python-network_1$ ./4-hbtn_status.py | cat -e
Body response:$
	- type: <class 'str'>$
	- content: OK$
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x11-python-network_1$
```

### [5. Response header value #1](./5-hbtn_header.py)<br>
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header<br>

```
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x11-python-network_1$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
63a59fae-71bd-4765-9418-e078388c4821
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x11-python-network_1$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
10f7fc9f-512e-47a9-8b39-fffc01ebf711
smambo@lenovo-ubuntu:~/alx-higher_level_programming/0x11-python-network_1$ 
```

### [6. POST an email #1](./6-post_email.py)<br>
Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response<br>
### [7. Error code #1](./7-error_code.py)<br>
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.<br>
### [8. Search API](./8-json_api.py)<br>
Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.<br>
### [9. My Github!](./10-my_github.py)<br>
Write a Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://docs.github.com/en/rest/users?apiVersion=2022-11-28) to display your `id`<br>
