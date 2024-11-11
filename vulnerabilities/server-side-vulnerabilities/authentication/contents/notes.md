# ✍️ Notes

## What is authentication?
- Process of verifying the identity of a user or client.

## Types of authentication
- Something `you know`, such as password or security question (Knowledge factors).
- Something `you have`, such as mobile phone or security token (Possession factors).
- Something `you are or do`, such as biometrics or patterns of behavior (Inherence factors).

## Authentication vs authorization?
- Authentication is verifying that the user is who they claim to be. 
- Authorization involves whether the user is allowed to do something.

## How do authentication vulnerabilities rise?
 - Authentication mechanism is weak and fails to protect against bruteforce attacks.
 - Logic flaws or poor coding allows an attacker to bypass authentication entirely. This is also called as `broken authentication`.

 ## What is the impact of vulnerable authentication?
 - Impact of vulnerable authentication is severe.
 - An attacker can compromise the entire application if he gets access to high previleged accounts.

 ## Vulnerabilities in password-based login

### Bruteforce attacks

- Attacker uses a system of trail and error to guess valid login credentials.
- Typically automated using wordlists of usernames and passwords.
- Not always random guesses. Attacker should use logic and publicly available information to make a wordlist for more educated guesses.


#### Bruteforcing usernames
- Easy to guess if they conform to a recognizable pattern. 
- For example: `firstname.lastname@companyname.com`.
- Look for predictable usernames such as `admin` or `administrator`.
- Check for publicly available information.

#### Bruteforcing passwords
- High entropy passwords are difficult to crack with bruteforce alone.
- Users tend to crowbar passwords to fit into the policy. For example: Since `password` is not accepted, Users may try using `P@ssword`, `Password1!` or `P4$$word` instead.

#### Username enumeration
- Attacker observes changes in the following fields and tries to guess the valid username.
    - Status code
    - Error message
    - Response time

### Flawed bruteforce protection

- Two main methods to prevent bruteforcing
    - Blocking remote ip address when there are too many login attempts.
    - Locking the account when there are too many login attempts.

- Both approaches are vulnerable if implemented using flawed logic.

#### IP blocking
- If failed attempts gets reset after successful login, then the attacker login to own account after every few attempts to make the locking the account approach virtually useless.

#### Account locking
- If the account lock, does not throw any error while login with the right credentials, after account is locked out, the attacker can bruteforce the password and login after the wait time is over.


#### User rate limit
- Limits the number of requests that can be sent for an endpoint.
- Better than account locking as it is less prone to username enumeration.


> 💡 Try bypassing user rate limit by sending an array of passwords instead of a single password.


### HTTP basic authentication
- HTTP basic authentication is old but still used in websites due to its simplicity.

```
Authorization: Basic base64(username:password)
```

- It is not preferred due to the following reasons.
    - Sends the credentials with every request.
    - No bruteforce protection.
    - No CSRF protection. 