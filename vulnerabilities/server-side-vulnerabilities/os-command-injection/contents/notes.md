# ✍️ Notes

## What is OS command injection?
- Also called shell injection.
- Allows attacker to execute operating system commands on the server running the application.
- Often the attacker can leverage a os command injection vulnerability to fully compromise the application and data.

## Injecting os commands
- In a shopping application endpoint like the one below, change a parameter value into a command.
  ```
    https://insecure-website.com/stockStatus?productID=381&storeID=29
  ```
- For example, here change the product id parameter value from `381` to `& echo hacked &`
- Trailing & is to separate the injected command from what follows it.