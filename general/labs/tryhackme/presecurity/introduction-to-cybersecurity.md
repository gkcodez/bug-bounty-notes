# Introduction to cybersecurity

## Offensive security introduction

### What is offensive security?
- Process of simulating and thinking like a hacker to find vulnerabilities in the system.

### Hacking your first machine
- Deploy the target machine.
- Run the following command in the command line inside the target machine.
  ```
  gobuster -u http://fakebank.thm -w wordlist.txt dir
  ```
- Notice the result contains an endpoint called `/bank-transfer`
- Navigate to this page and transfer $2000 to your account
- Return to the account page to find the answer above the balance

### Careers in cybersecurity
- Penetration tester - Tests products and technologies to find vulnerabilities
- Red teamer - Plays the role of an adversary and attacks the organization from enemy's perspective
- Security engineer - Designs, monitors and maintains security controls.

## Defensive security introduction

### What is defensive security?
- Preventing intrusions from occurring
- Detecting intrusions when they occur and responds properly
- Some tasks related to defensive security include:
  - Cybersecurity awareness
  - Documenting and managing assets
  - Updating and patching systems
  - Setting up preventative devices
  - Setting up logging and monitoring devices

### Areas of defensive security
  - Security operations center (SOC)
    - Monitors networks and systems to detect malicious cyber security events. 
  - Threat intelligence
    - Threat intelligence collects information to help the company prepare against potential adversaries. 
  - Digital forensics and incident response (DFIR)
    - Digital forensics involves analyzing evidence of an attack on a system
    - Incident response specifies the methodology to be followed to handle such case 
  - Malware analysis
    - Malware stands for malicious software
    - Malware analysis aims to learn about such malicious programs

  ### Practical example of defensive security
  - Find the malicious IP and block it
  - Malicious IP address can be identified from opensource databases such as AbuseIPDB

  
