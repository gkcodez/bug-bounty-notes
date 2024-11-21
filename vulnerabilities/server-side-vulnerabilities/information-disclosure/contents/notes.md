# ✍️ Notes

## What is information disclosure?
- Information disclosure also known as information leakage is when a website reveals sensitive information to users.

## Examples of sensitive information
- Revealing the names of hidden directories, their structure, and their contents via a `robots.txt` file or directory listing
- Access to source code files via backups.
- Explicitly mentioning database tables or column names in error messages.
- Exposing sensitive information such as credit card details.
- Hardcoding api keys, ip address, database credentials in the source code.
- Hinting at the existence or absence of resources, usernames via subtle differences in application behavior.

## How do information disclosure vulnerabilities
- Failure to remove internal content from public content.
- Insecure configuration of the website and related technologies.
- Flawed design and behavior of the application.

## Impact of information disclosure vulnerabilities
- Impact depends on the purpose of the website and context of vulnerability.
- Online shop leaking information of user's credit card details is severe.
- Leaking technical information, such as the directory structure or which third-party frameworks are being used, may have little to no direct impact.

## How to prevent information disclosure vulnerabilities
- Audit any code for potential information disclosure as part of your QA or build processes.
- Use generic error messages as much as possible. Don't provide attackers with clues about application behavior unnecessarily.
- Double-check that any debugging or diagnostic features are disabled in the production environment.
- Make sure you fully understand the configuration settings, and security implications, of any third-party technology that you implement.

## Testing for information disclosure
- Fuzzing
- Using burp scanner
- Using burp engagement tools
- Engineering infomative responses (Example: Error messages.)

## Common sources of information disclosures
- Files for web crawlers (robots.txt, security.txt, etc.)
- Directory listings
- Developer comments
- Error messages
- Debugging data
- User account pages
- Backup files
- Insecure configuration
- Version control history