# ✍️ Notes

## SQL Injection

- Enter a single quote character `'` at the end of user input to check if it errors out.
- Enter another single quote character `''` to check that there are no errors.
- Add `'+OR+1=1--` at the end to retrieve all the data.
    - `--` is the comment character which comments out rest of the query.
- Send `'--` to bypass unprotected logins.
- Find the number of columns
    - Use union statements, for example.
        ```
        '+UNION+SELECT+NULL,NULL+FROM+dual--
        ```
    - Use order by statements
- Find database version