## Password based
### [Username enumeration via different responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses)

- Fuzz the username using the username list provided in the lab.
- Get valid username from the request with `Incorrect password` instead of `Incorrect username` in the response body.
- Fuzz the password using password list provided in the lab.
- Get valid username and password combination from the request which results in 302 status code.

### [Username enumeration via subtly different responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-subtly-different-responses)

- Fuzz the username using the username list provided in the lab.
- Get valid username from the request with `Incorrect username or password` instead of `Incorrect username or password.` in the response body. Note the `.` at the end.
- Fuzz the password using password list provided in the lab.
- Get valid username and password combination from the request which results in 302 status code.

### [Username enumeration via response timing](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-response-timing)

- Fuzz the username using the username list provided in the lab.
- Get valid username from the request with highest response time.
- Fuzz the password using password list provided in the lab.
- Get valid username and password combination from the request which results in 302 status code.


### [Broken brute-force protection, IP block](https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block)

- Generate the username list and password list by alternating the known attackers credentials and the unknown victim's credentials.
- Fuzz the username and password using generated lists.
- Get valid username and password combination from the request which results in 302 status code.