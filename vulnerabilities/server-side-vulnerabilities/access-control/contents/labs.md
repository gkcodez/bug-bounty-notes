# 🧪 Labs

## Portswigger

1. [Unprotected admin functionality](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality)
   - Navigate to `<LAB_URL>/robots.txt`.
   - Find the administrative panel URL in the disallow parameter.
   - Navigate to the administrative panel and delete the user `carlos`. 

2. [Unprotected admin functionality with unpredictable URL](https://portswigger.net/web-security/access-control/lab-unprotected-admin-functionality-with-unpredictable-url)
   - Search for `admin` in index.html.
   - Locate the administrative panel URL in a javascript function.
   - Navigate to the administrative panel and delete the user `carlos`.

3. [User role controlled by request parameter](https://portswigger.net/web-security/access-control/lab-user-role-controlled-by-request-parameter)
   - Login as `wiener`.
   - Change the `Admin` cookie value to `true`.
   - Navigate to the administrative panel and delete the user `carlos`.  
 
4. [User role can be modified in user profile](https://portswigger.net/web-security/access-control/lab-user-role-can-be-modified-in-user-profile)
   - Login as `wiener`.
   - Change the email and check the response for the parameters.
   - Add the `roleid` parameter in the request and set the value to `2`.
   - Navigate to the administrative panel and delete the user `carlos`. 
 
5. [User ID controlled by request parameter ](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter)
   - Login as `wiener`.
   - Change the user id from `wiener` to `carlos` is my account page request.
   - Get the API key from the response and submit.

6. [User ID controlled by request parameter, with unpredictable user IDs](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-unpredictable-user-ids)
   - Login as `wiener`.
   - Navigate to a blog post which has post author as `carlos`.
   - Get the user id by inspecting the page.
   - Change the user id from `wiener` to `carlos` is my account page request.
   - Get the API key from the response and submit.

7. [User ID controlled by request parameter with data leakage in redirect ](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-data-leakage-in-redirect)
   - Login as `wiener`.
   - Navigate to my account page of the user `carlos`.
   - Check the response even though it is redirected to login page.
   - Get the API key from the response and submit.

8. [User ID controlled by request parameter with password disclosure](https://portswigger.net/web-security/access-control/lab-user-id-controlled-by-request-parameter-with-password-disclosure)
   - Login as `wiener`.
   - Change the user id in the browser's address bar and navigate to my account page of the user `administrator`.
   - Inspect the page and get the password for `administrator`.
   - Navigate to the administrative panel and delete the user `carlos`.  

9.  [Insecure direct object references](https://portswigger.net/web-security/access-control/lab-insecure-direct-object-references)
    - Navigate to live chat
    - View transcript and send the request to repeater.
    - Change the transcript file name in the request from `1.txt` to `2.txt`.
    - Login as `carlos`.

10. [URL-based access control can be circumvented](https://portswigger.net/web-security/access-control/lab-url-based-access-control-can-be-circumvented)
    - Navigate to administrative panel.
    - Change the request url from `/admin` to `/`.
    - Add `X-Original-URL` request header with value as `/admin`.
    - Trigger request delete the user `carlos`.
    - Change the request URL from `/admin/delete?username=carlos` to `/?username=carlos`.
    - Add `X-Original-URL` request header with value as `/admin/delete`.
    - Forward the request and the user `carlos` should be deleted.

11. [Method-based access control can be circumvented](https://portswigger.net/web-security/access-control/lab-method-based-access-control-can-be-circumvented)
    - Login as administrator.
    - Navigate to administrative panel.
    - Promote user `carlos` to admin and forward the request to repeater.
    - Login as `wiener`.
    - Trigger the promote user request for `wiener` after changing the session id.
    - Note that the request gets an unauthorized error.
    - Change the request method to `GET` or `PUT` and add the username request parameter.
    - Forward the request and the user `wiener` should be promoted.

12. [Multi-step process with no access control on one step](https://portswigger.net/web-security/access-control/lab-multi-step-process-with-no-access-control-on-one-step)
    - Login as administrator.
    - Navigate to administrative panel.
    - Promote user `carlos` to admin.
    - Confirm the promotion and forward the request to repeater
    - Login as `wiener`.
    - Trigger the promote user confirmation request for `wiener` after changing the session id.

13. [Referer-based access control](https://portswigger.net/web-security/access-control/lab-referer-based-access-control)
    - Login as administrator.
    - Navigate to administrative panel.
    - Promote user `carlos` to admin and forward the request to repeater.
    - Login as `wiener`.
    - Trigger the promote user request for `wiener` after changing the session id.
    - Forward the request and the user `wiener` should be promoted.
