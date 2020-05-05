
What is this project about ?
------------

This web app is written in python and contains NoSQLi vulnerabilities. 

What types of vulnerabilities are there and how can I expose them ?
--------------------------

First vulnerability is authentication bypass and to simulate it to you need to modify network traffic. A suitable tool to modify traffic is burp broxy and I suggest you install it.

Simulating authentication bypass
-------------

1. First you have to setup burp proxy to intercept the network traffic.
2. Go to login page and for username enter 'admin' and for password enter any value you want. We are trying to simulate how a hacker can access the system without knowing the password.
3. Once request for authentication is intercepted, Modify post body as follows
[{"name":"username","value":"admin"},{"name":"password","value":{"$ne": null}}]
4. You should be redirected to profile page now
