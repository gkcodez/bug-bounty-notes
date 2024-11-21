# 🧪 Labs

## Portswigger

1.  [Information disclosure in error messages](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-error-messages)
    - Navigate to a product details page.
    - Change the productId parameter value to an invalid value such as `test`.
    - Get the framework version at the end.

2.  [Information disclosure on debug page](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-on-debug-page)
    - Navigate to a home page.
    - Open chrome devtools and check the comment. 
    - Get the debug file path and get the secret key value from the table.

3.  [Source code disclosure via backup files](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-via-backup-files)
    - Navigate to `robots.txt`.
    - Open the backup folder and download the java file.
    - Check the file and get the key from the db configuration.

4.  [Authentication bypass via information disclosure](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-authentication-bypass)
    - Login as `wiener`.
    - Send the my account request to repeater.
    - Change the request method to `TRACE`.
    - Get the custom header name `X-Custom-Ip-Authorization` from the response.
    - Navigate to `/admin`.
    - Notice that it is available only to local users.
    - Add the custom header `X-Custom-Ip-Authorization: 127.0.0.1` and send the request.
    - Delete the user `carlos`.

5.  [Information disclosure in version control history](https://portswigger.net/web-security/information-disclosure/exploiting/lab-infoleak-in-version-control-history)
    - Create a new folder. Example: `Code`.
    - Switch to the `Code` directory.
    - Open the browser and navigate to `<LAB_URL>/.git` directory.
    - Download the directory using the below command.
        ```
        wget -r -R index.html "https://0a13004f03995d1b803f497100c900c9.web-security-academy.net/.git"
        ```
        - `-r` - Downloads recursively.
        - `-R` - Excludes file.
    - Open the folder in an editor like `vscode`.
    - Open the commit which has the admin password removed and get password.
    - Login as administrator.
