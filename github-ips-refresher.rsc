# Generated on Tue Sep 30 05:36:25 2025 UTC
file remove [find name~"^github.*ipv..rsc"]
/system script
remove [find name="github-ips-refresher"]
add dont-require-permissions=yes name=github-ips-refresher owner=admin policy=ftp,read,write,test source=":log info \"Download GitHub IP lists\";\r\
    \n\r\
    \n:log info \"Remove current GitHub IPs\";\r\
    \n/ip firewall address-list remove [find where list~\"^github.*\"];\r\
    \n/ipv6 firewall address-list remove [find where list~\"^github.*\"];\r\
    \n:log info \"Import newest GitHub IPs\";\r\"