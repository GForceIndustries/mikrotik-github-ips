/system script
add dont-require-permissions=yes name=github-ips owner=admin policy=ftp,read,write,test source="file remove [find name=\"github-ips-refresher.rsc\"];\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-ips-refresher.rsc\" mode=https dst-path=github-ips-refresher.rsc;\r\
    \n/system script remove [find name=\"github-ips-refresher\"]\r\
    \n/import file-name=github-ips-refresher.rsc;\r\
    \n/system script run github-ips-refresher;"
/system scheduler
add interval=1d name=github-ips on-event=github-ips policy=ftp,read,write,test start-date=2025-04-23 start-time=06:45:00
