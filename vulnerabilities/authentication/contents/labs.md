## Portswigger
1. [Username enumeration via different responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses)
   - Fuzz the username using the username list provided in the lab.
   - Get valid username from the request with `Incorrect password` instead of `Incorrect username` in the response body.
   - Fuzz the password using password list provided in the lab.
   - Get valid username and password combination from the request which results in 302 status code.

2.  [2FA simple bypass](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-simple-bypass)

3.  [Password reset broken logic](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-broken-logic)

4. [Username enumeration via subtly different responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-subtly-different-responses)
   - Fuzz the username using the username list provided in the lab.
   - Get valid username from the request with `Incorrect username or password` instead of `Incorrect username or password.` in the response body. Note the `.` at the end.
   - Fuzz the password using password list provided in the lab.
   - Get valid username and password combination from the request which results in 302 status code.

5. [Username enumeration via response timing](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-response-timing)
   - Fuzz the username using the username list provided in the lab.
   - Get valid username from the request with highest response time.
   - Fuzz the password using password list provided in the lab.
   - Get valid username and password combination from the request which results in 302 status code.

6. [Broken brute-force protection, IP block](https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block)
   - Generate the username list and password list by alternating the known attackers credentials and the unknown victim's credentials.
   - Fuzz the username and password using generated lists.
   - Get valid username and password combination from the request which results in 302 status code.


7. [Username enumeration via account lock](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-account-lock)
   - Fuzz the username and find the username from the request with `too many attempts` in the response.
   - Fuzz the password and find the password using the request which does not have any error message in the response.
   - Login after the wait time is completed.

8.  [2FA broken logic](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-broken-logic)

9.  [Brute-forcing a stay-logged-in cookie](https://portswigger.net/web-security/authentication/other-mechanisms/lab-brute-forcing-a-stay-logged-in-cookie)

10. [Offline password cracking](https://portswigger.net/web-security/authentication/other-mechanisms/lab-offline-password-cracking)

11. [Password reset poisoning via middleware](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-poisoning-via-middleware)

12. [Password brute-force via password change](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-brute-force-via-password-change)

13. [Broken brute-force protection, multiple credentials per request](https://portswigger.net/web-security/authentication/password-based/lab-broken-brute-force-protection-multiple-credentials-per-request)

14. [2FA bypass using a brute-force attack](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-bypass-using-a-brute-force-attack)
