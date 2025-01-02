# How the web works?

## DNS in detail
- DNS - Domain name system.
- DNS provides a simple way to communicate with the devices without having to remember complex numbers.
- Instead of `104.26.10.229` we just need to remember `tryhackme.com`.

## Domain hierarchy
- Root domain - .
- Top level domain - com, net, edu, org, etc.
- Second level domain - tryhackme, google, microsoft, etc

## Top level domain
- gTLD - Generic top level domain
- ccTLD - Country code top level domain
- Full list of TLD can be found [here](https://data.iana.org/TLD/tlds-alpha-by-domain.txt)

## Second level domain
- Limited to 63 characters + TLD.
- Can only use letters, numbers and hyphen.
- Cannot start with a hyphen.

### Subdomain
- Sits on the left hand side of the second level domain.
- Same restrictions in second level domain applies to subdomains.
- For example In `admin.tryhackme.com`, `admin` part is the subdomain.
- Multiple subdomains can be split with the period.
- Maximum character length of the whole domain including the subdomain should not be more than 253 characters.

## DNS Record Types
- A Record - Resolves to IPV4 addresses.
- AAAA Record - Resolves to IPV6 addresses.
- CNAME Record - Resolves to another subdomain. For example: `store.tryhackme.com` resolves to `shop.shopify.com`.
- MX Record - Handles email for a domain.
- TXT Record - Free text fields where any text data can be stored.

## Making a request

### What happens when you make a DNS request?
- Computer checks the local cache, if not present it makes request to the Recursive DNS Server.
- Recursive DNS Server is usually provided by ISP, you can also set your own Recursive DNS Server.
- Recursive DNS Server also has a local cache of recently looked up domains.
- If it is found, then the request is sent back to the computer and the request ends there.
- If it is NOT found, the request is forwarded to the root DNS servers.
- Root server is the DNS backbone of the internet.
- Root server forwards the request to the Top Level Domain Server (TLD Server).
- TLD Server holds records to find the correct authoritative server of the domain.
- Authoritative server is also known as Nameserver.
- The response is then sent back to the client requesting it.
- All DNS records come with a Time To Live (TTL) value in seconds after which you have to look it up again.
- Caching saves on making a DNS request everytime you communicate with the server.
