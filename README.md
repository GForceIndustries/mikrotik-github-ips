# GitHub IP Address Lists for MikroTik Firewalls

MikroTik firewall address lists for GitHub IP address ranges. Refreshed daily at 05:30 UTC. Configuration files are generated to create address lists for each of GitHub's services which can be used in firewall rules.

Developed and tested on RouterOS 7.18.2.

## Usage

Create a script to download the configuration files for the GitHub service(s) you use, remove any existing entries in the GitHub address lists, and import the new address list(s). Then, create a schedule to run the script at an appropriate time for your environment. You can either configure these manually, or download and import **github-ips-setup.rsc** to create them automatically. If you use the setup configuration provided, IP address lists for all of GitHub's services will be added to your router. Read on for a sample script and schedule if you want to configure these manually. If you create the script and schedule manually, they require ftp, read, write and test permissions. 

### Sample Script (Single Service)

```
/system script
add dont-require-permissions=yes name=github-ips owner=admin policy=ftp,read,write,test source=":log info \"Download GitHub IP lists\";\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-hooks-ips-ipv4.rsc\" mode=https dst-path=github-hooks-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-hooks-ips-ipv6.rsc\" mode=https dst-path=github-hooks-ips-ipv6.rsc;\r\
    \n\r\
    \n:log info \"Remove current GitHub IPs\";\r\
    \n/ip firewall address-list remove [find where list=\"github-hooks-ips-ipv4\"];\
    \n\r\
    \n/ipv6 firewall address-list remove [find where list=\"github-hooks-ips-ipv6\"];\r\
    \n:log info \"Import newest GitHub IPs\";\r\
    \n/import file-name=github-hooks-ips-ipv4.rsc;\r\
    \n/import file-name=github-hooks-ips-ipv6.rsc;"
```

### Sample Schedule

```
/system scheduler
add disabled=yes interval=1m name=github-ips on-event=github-ips policy=ftp,read,write,test start-date=2025-04-23 start-time=06:45:00
```

## Licence & Warranty

You are free to use the provided MikroTik configuration files to aid in maintaining your firewall configuration. You are free also to clone the repository and adapt the code that generates the daily files to suit your needs.

Configuration files are provided without warranty. While they are offered in good faith, no assurance is offered that they are appropriate for your environment and no liability will is accepted for any outcomes of their use. You are responsible for examining the configuration provided and ascertaining that it is suitable for your use case.

While the daily configuration files are generated using information provided by GitHub, they are 100% unofficial and are not endorsed or maintained by GitHub or Microsoft Corporation.

Thank you to [Mark Hatton](https://blog.markhatton.co.uk/2011/03/15/regular-expressions-for-ip-addresses-cidr-ranges-and-hostnames/) for publically documenting regular expressions for IPv4 and IPv6 addresses and CIDR ranges.
