# ✍️ Notes

## What is access control?
- **Authentication:** Confirms the user is who they say they are.
- **Session management:** Identifies if the subsequent requests are made by the same user.
- **Access control:** Determines whether a user is allowed to perform an action.

## Types of access controls
- **Vertical access controls:** Different types of users have different application functions.
  - Example: Admin, Moderator, etc.
- **Horizontal access controls:** Different users have access to subset of resources of the same type.
  - Example: User1, User2, etc.

## Broken access control

### Vertical previlege escalation
- Non-administrative user gains access to administrative functions.

#### Unprotected functionality
- Sensitive information might be exposed in `robots.txt` file.
- Attacker can also bruteforce / fuzz the URL to find a sensitive functionality.
- Sometimes, sensitive information might be available in an unpredictable URL (Security by obscurity).
- This would fail if the URL is exposed in any of the javascript files.

#### Parameter-based access control methods
- Some applications capture user access rights or role at login and store it in an user controlled location.
  - Hidden field
  - Cookie
  - Query string parameter
- Attacker can modify these values and access administrative functions.

#### Broken access control resulting from platform misconfiguration
- Some applications enforce access controls at the platform layer by restricting access to specific URLs and HTTP methods based on the user's role.
  ```
  DENY: POST, /admin/deleteUser, managers
  ```
- Some applications allow user to override the URL in the original request, such as `X-Original-URL` and `X-Rewrite-URL`.

#### Broken access control resulting from URL-matching discrepancies
- Casing based. `/ADMIN/DELETEUSER` and `/admin/deleteUser` treated differently. 
- Extension based. `/admin/deleteUser.anything` and `/admin/deleteUser` treated differently.
- Trailing slash. `/admin/deleteUser` and `/admin/deleteUser/` treated differently.

### Horizontal previlege escalation
- User is able to gain access to resources belonging to another user, instead of their own resources of the same type.
- If id is predictable change it and check if the data from other user can be accessed.
- For unpredictable ids, find a place where the user id of another is exposed, such as blog post author, comments, etc.
- Check the responses of redirects, eventhough the page redirected, it might still contain the information.

### Horizontal to vertical previlege escalation
- Often, a horizontal privilege escalation attack can be turned into a vertical privilege escalation, by compromising a more privileged user.
- Change the id of the normal user to admin user.
- Check if the functionalities related to a high previleged user are exposed.

### Insecure Direct Object References
- Subcategory of access control vulnerabilities.
- Attacker modifies the user controlled input to obtain unauthorized access.

### Access control vulnerabilities in multi-step processes
- Many websites implement important functions over a series of steps.
- First few steps may have access control implemented correctly but not in the later steps.
- An attacker can gain unauthorized access to the function by skipping the first few steps and directly submitting the request for the later step with the required parameters.

### Referer-based access control
- Some websites only check if the referer matches that of the admin.
- An attacker can change the session id and send the request which has referer same as that of the admin. 
