# ✍️ Notes

## What are JWTs?
- JSON web tokens (JWTs) are a standardized format for sending cryptographically signed JSON data between systems.
- Data is stored on the client side within the JWT itself. This makes it a popular choice for distributed websites.

## JWT format
- A JWT has 3 parts, each separated by a dot. 
  - Header
  - Payload
  - Signature
- The header and payload parts of a JWT are just base64url-encoded JSON objects.
- Header contains metadata about the token itself.
- Payload contains information about the user.
- The header and payload can be easily decoded by anyone with the access to the token.
- Security of the token relies heavily on the cryptographic signature.

## JWT signature
- Server generates the signature by hashing the header and payload.
- In some cases, the resulting hash is also encrypted.
- As the signature is derived from the header and payload, changing a single character in the token would result in mismatched signature.
- Without the server's secret signing key, it should not be possible to generate the correct signature.

## JWT vs JWS vs JWE
- JWT (JSON Web Token) - Format for representing information.
- JWS (JSON Web Signature) - Actual signature.
- JWE (JSON Web Encryption) - Similar to JWS, except that the contents are encrypted rather than encoded.
- When people use the term "JWT", they almost always mean a JWS token.

## What are JWT attacks?
- Sending modified JWTs to bypass authentication and access controls by impersonating another user who has already been authenticated.
- If an attacker is able to create their own valid tokens with arbitrary values, they may be able to escalate their own privileges or impersonate other users.

## How do JWT vulnerabilities arise?
- Signature of the JWT is not verified properly.
- Server's secret key is leaked.
- Signature can be guessed or brute-forced.

## Exploiting flawed JWT signature verification

### Accepting arbitrary signatures
- Unverified signature (Change the values in the payload.)
- Accepting tokens with no signature (Change the alg to `none` and remove signature.)

### Brute-forcing secret keys

#### Brute-forcing secret keys using hashcat

```
hashcat -a 0 -m 16500 <jwt> <wordlist>
```

## JWT header parameter injections
- According to JWS specification, only the `alg` parameter is mandatory.
- Other parameters are called JOSE parameters.
  - jwk (JSON Web Key) - Provides an embedded JSON object representing the key.
  - jku (JSON Web Key Set URL) - Provides a URL from which a server can fetch set of keys containing correct key.
  - kid (Key ID) - Provides an ID which the server uses to identify the correct key in case there are multiple keys.

### Injecting self-signed JWTs via the jwk parameter
