## Password Based
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