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
[0. What's my status? #0](./0-hbtn_status.py)<br>
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`<br>
[1. Response header value #0](./1-hbtn_header.py)<br>
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.<br>
[2. POST an email #0](./2-post_email.py)<br>
Write a Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`)<br>
[3. Error code #0](./3-error_code.py)<br>
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`).<br>
[4. What's my status? #1](./4-hbtn_status.py)<br>
Write a Python script that fetches `https://alx-intranet.hbtn.io/status`<br>
[5. Response header value #1](./5-hbtn_header.py)<br>
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header<br>
[6. POST an email #1](./6-post_email.py)<br>
Write a Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response<br>
[7. Error code #1](./7-error_code.py)<br>
Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.<br>
[8. Search API](./8-json_api.py)<br>
Write a Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter.<br>
[9. My Github!](./10-my_github.py)<br>
Write a Python script that takes your GitHub credentials (username and password) and uses the [GitHub API](https://docs.github.com/en/rest/users?apiVersion=2022-11-28) to display your `id`<br>
