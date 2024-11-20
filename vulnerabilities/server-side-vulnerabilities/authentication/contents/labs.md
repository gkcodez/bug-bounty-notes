# 🧪 Labs

## Portswigger
1. [Username enumeration via different responses](https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses)
   - Fuzz the username using the username list provided in the lab.
   - Get valid username from the request with `Incorrect password` instead of `Incorrect username` in the response body.
   - Fuzz the password using password list provided in the lab.
   - Get valid username and password combination from the request which results in 302 status code.


2.  [2FA simple bypass](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-simple-bypass)
       - Enter the username and password for `wiener`.
       - Enter the 2FA from the email.
       - Note down the url for my account page.
       - Log out and login as `carlos`.
       - Navigate to the url for my account page.


3.  [Password reset broken logic](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-broken-logic)
      - Generate a password reset token for `wiener`.
      - Using this token reset the password for `carlos`.
      - Reset the password for `carlos`.


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
   - Login as `wiener`.
   - Send the request to repeater.
   - Use the request to trigger a mfa code to `carlos`.
   - Change the cookie from `verify=wiener` to `verify=carlos`.
   - Use burp intruder to bruteforce the login code in mfa page.
   - Note: Use below command in FFUF to bruteforce the login code.
      ```
      ffuf -w mfa_wordlist.txt:FUZZ -u "https://0a3a00620456a0f483f6e1a8004b00a5.web-security-academy.net/login2" -mc 302 -b "session=c4lf8n8fnIhAOUlR05tCTqtnK2ykkrV8; verify=carlos" -H "Referer: https://0a3a00620456a0f483f6e1a8004b00a5.web-security-academy.net/login2" -X POST -d mfa-code=FUZZ
      ```

9.  [Brute-forcing a stay-logged-in cookie](https://portswigger.net/web-security/authentication/other-mechanisms/lab-brute-forcing-a-stay-logged-in-cookie)

10. [Offline password cracking](https://portswigger.net/web-security/authentication/other-mechanisms/lab-offline-password-cracking)

11. [Password reset poisoning via middleware](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-reset-poisoning-via-middleware)

12. [Password brute-force via password change](https://portswigger.net/web-security/authentication/other-mechanisms/lab-password-brute-force-via-password-change)

13. [Broken brute-force protection, multiple credentials per request](https://portswigger.net/web-security/authentication/password-based/lab-broken-brute-force-protection-multiple-credentials-per-request)
       - Sign in with username as `carlos` and `test`.
       - Intercept the sign in request.
       - Change the password from `test` to an array of all the values in the password list provided in the lab.
       - Send the request.

14. [2FA bypass using a brute-force attack](https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-bypass-using-a-brute-force-attack)
