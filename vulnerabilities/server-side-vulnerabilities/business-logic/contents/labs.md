# 🧪 Labs

## Portswigger

1.  [Excessive trust in client-side controls](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-excessive-trust-in-client-side-controls)
    - Login as `wiener`.
    - Intercept the request to add the `leather jacket` product to cart.
    - Change the price to `1` and forward the request.
    - Place order with the modified price.

2.  [High-level logic vulnerability](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-high-level)
    - Login as `wiener`.
    - Intercept the request to add the `leather jacket` product to cart.
    - Add a few other products in negative quantity to bring the price below 100.
    - Place order with the modified price.

3.  [Inconsistent security controls](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-security-controls)
    - Register and login as attacker.
    - Change email to a dontwannacry email.
    - Delete `carlos`.

4.  [Flawed enforcement of business rules](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-flawed-enforcement-of-business-rules)
    - Signup for newsletter and get `SIGNUP30` coupon.
    - Use `NEWCUST5` and `SIGNUP30` coupon alternatively and buy `leather jacket`.

5.  [Low-level logic flaw](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-low-level)
    - Login as `wiener`.
    - Intercept the request to add the `leather jacket` product to cart.
    - Repeat the add request `64247` times for the `leather jacket product`.
    - Add another product manually until the negative value becomes positive and below 100.
    - Place order with modified price.

6.  [Inconsistent handling of exceptional input](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-inconsistent-handling-of-exceptional-input)
    - Register for a test account with attacker's username and email.
    - Send a registration request with exceptionally large email address length (Example: 500 characters).
    - Confirm the email and login to this account.
    - Notice that the email gets truncated to 256 characters.
    - Signup with the below email which has the 256 character is just after `@dontwannacry.com`.
        ```
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@dontwannacry.com.exploit-0ade001f04694727ebab715a015a0081.exploit-server.net
        ```
    - Access the admin panel and delete `carlos`

7.  [Weak isolation on dual-use endpoint](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-weak-isolation-on-dual-use-endpoint)
    - Login as `wiener`
    - Change the password and send the request to repeater
    - Using the request in repeater change the password again but change the username to `administrator` and remove the current password parameter.
    - Login as administrator and delete the user `carlos`.

8.  [Insufficient workflow validation](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-insufficient-workflow-validation)
    - Order a product with low price.
    - Add the `leather jacket` to cart and send the order confirmation directly without placing the order.

9.  [Authentication bypass via flawed state machine](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-flawed-state-machine)
    - Navigate to `/admin` endpoint and send the request to repeater.
    - Login as `wiener` and intercept the request. 
    - Replace the `role-selector` request with admin request.
    - Access the admin panel and delete `carlos`

10. [Infinite money logic flaw](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-infinite-money)
    - Login as `wiener`
    - Signup to newsletter and get `SIGNUP30` coupon.
    - Buy a gift card and apply the coupon and place order.
    - Redeem the gift card to get 3 dollar more.
    - Repeat the endpoint below in same order to get more money.
        ```
        POST /cart
        POST /cart/coupon
        POST /cart/checkout
        GET /cart/order-confirmation?order-confirmed=true
        POST /gift-card
        ```
    - Use session and macro functionalities in settings to send requests in order.
    - Use intruder to repeat the same requests multiple times. Null payloads is enough here.

11. [Authentication bypass via encryption oracle](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-authentication-bypass-via-encryption-oracle)

12. [Bypassing access controls using email address parsing discrepancies](https://portswigger.net/web-security/logic-flaws/examples/lab-logic-flaws-bypassing-access-controls-using-email-address-parsing-discrepancies)
