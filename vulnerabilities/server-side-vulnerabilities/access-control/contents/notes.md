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
- Administrative URL may be exposed in `robots.txt` file.
- Attacker can also bruteforce / fuzz the URL to find a sensitive functionality.


