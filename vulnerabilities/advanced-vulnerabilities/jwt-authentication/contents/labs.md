# 🧪 Labs

## Portswigger

1.  [JWT authentication bypass via unverified signature](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-unverified-signature)
    - Login as `wiener`.
    - Change the user id value in the parameter and in JWT Token payload from `wiener` to `administrator`.
    - Navigate to admin panel after changing the JWT token payload from `wiener` to `administrator`.
    - Delete the user `carlos` after changing the JWT token payload `wiener` to `administrator`.

2.  [JWT authentication bypass via flawed signature verification](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-flawed-signature-verification)
    - Login as `wiener`.
    - Change the alg in JWT Token payload to `none`.
    - Remove the signature but leave the trailing dot.
    - Delete the user `carlos` using the delete request.

3.  [JWT authentication bypass via weak signing key](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-weak-signing-key)
    - Send the request with JWT token to the Repeater Tab.
    - Get the JWT token and bruteforce it using hashcat with the below command.
        ```
        hashcat -a 0 -m 16500 <JWT_TOKEN> <WORDLIST>
        ```
    - Switch to JWT Editor tab and Generate a New Symmetric Key using the identified secret.
    - Switch to JSON Web Token tab inside Repeater tab.
    - Change the payload value as required and Click on Sign.
    - In the new window select the previously generated symmetric key.
    - Delete the user `carlos` using the delete request with modified JWT.

4.  [JWT authentication bypass via jwk header injection](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jwk-header-injection)
    - Send the request with JWT token to the Repeater Tab.
    - Switch to JWT Editor tab and Generate a RSA Key.
    - Switch to JSON Web Token tab inside Repeater tab.
    - Change the payload value as required and Click on Attack.
    - In the new window select the previously generated RSA key.
    - Delete the user `carlos` using the delete request with modified JWT.


5.  [JWT authentication bypass via jku header injection](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-jku-header-injection)

6.  [JWT authentication bypass via kid header path traversal](https://portswigger.net/web-security/jwt/lab-jwt-authentication-bypass-via-kid-header-path-traversal)

7.  [JWT authentication bypass via algorithm confusion](https://portswigger.net/web-security/jwt/algorithm-confusion/lab-jwt-authentication-bypass-via-algorithm-confusion)

8.  [JWT authentication bypass via algorithm confusion with no exposed key](https://portswigger.net/web-security/jwt/algorithm-confusion/lab-jwt-authentication-bypass-via-algorithm-confusion-with-no-exposed-key)
