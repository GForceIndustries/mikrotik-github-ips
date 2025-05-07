# Generated on Wed May  7 19:38:19 2025 UTC
file remove [find name~"^github.*ipv..rsc"]
/system script
remove [find name="github-ips-refresher"]
add dont-require-permissions=yes name=github-ips-refresher owner=admin policy=ftp,read,write,test source=":log info \"Download GitHub IP lists\";\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-hooks-ips-ipv4.rsc\" mode=https dst-path=github-hooks-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-hooks-ips-ipv6.rsc\" mode=https dst-path=github-hooks-ips-ipv6.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-web-ips-ipv4.rsc\" mode=https dst-path=github-web-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-web-ips-ipv6.rsc\" mode=https dst-path=github-web-ips-ipv6.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-api-ips-ipv4.rsc\" mode=https dst-path=github-api-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-api-ips-ipv6.rsc\" mode=https dst-path=github-api-ips-ipv6.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-git-ips-ipv4.rsc\" mode=https dst-path=github-git-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-git-ips-ipv6.rsc\" mode=https dst-path=github-git-ips-ipv6.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-github_enterprise_importer-ips-ipv4.rsc\" mode=https dst-path=github-github_enterprise_importer-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-github_enterprise_importer-ips-ipv6.rsc\" mode=https dst-path=github-github_enterprise_importer-ips-ipv6.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-packages-ips-ipv4.rsc\" mode=https dst-path=github-packages-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-pages-ips-ipv4.rsc\" mode=https dst-path=github-pages-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-pages-ips-ipv6.rsc\" mode=https dst-path=github-pages-ips-ipv6.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-importer-ips-ipv4.rsc\" mode=https dst-path=github-importer-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-actions-ips-ipv4.rsc\" mode=https dst-path=github-actions-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-actions-ips-ipv6.rsc\" mode=https dst-path=github-actions-ips-ipv6.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-actions_macos-ips-ipv4.rsc\" mode=https dst-path=github-actions_macos-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-codespaces-ips-ipv4.rsc\" mode=https dst-path=github-codespaces-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-dependabot-ips-ipv4.rsc\" mode=https dst-path=github-dependabot-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-copilot-ips-ipv4.rsc\" mode=https dst-path=github-copilot-ips-ipv4.rsc;\r\
    \n/tool fetch url=\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/github-copilot-ips-ipv6.rsc\" mode=https dst-path=github-copilot-ips-ipv6.rsc;"
