# Authentication

## What is authentication?
- Process of verifying the identity of a user or client.

## Types of authentication
- Something `you know`, such as password or security question (Knowledge factors).
- Something `you have`, such as mobile phone or security token (Possession factors).
- Something `you are or do`, such as biometrics or patterns of behavior (Inherence factors).

## Difference between authentication and authorization?
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
    - Locking the account when there are too many login attempts.
    - Blocking remote ip address when there are too many login attempts.
- Both approaches are vulnerable if implemented using flawed logic.
- If failed attempts resets after successful login, then the attacker login to own account after every few attempts to make the locking the account approach virtually useless.