from datetime import datetime, UTC
import requests
import json

today = datetime.now(UTC).strftime("%c") + " UTC"

githubIpURL = "https://api.github.com/meta"

githubIps = json.loads(requests.get(githubIpURL).content)

listsToGenerate = ["hooks", "web", "api", "git", "github_enterprise_importer", "packages", "pages", "importer", "actions", "actions_macos", "codespaces", "dependabot", "copilot"]

def generateRsc(prefixList, serviceName, ipVersion):
    fileName = "github-" + serviceName + "-ips-" + ipVersion + ".rsc"
    listName = "github-" + serviceName + "-ips-ip" + ipVersion

    writer = open(fileName, "w")
    writer.write("# Generated on " + today)

    if "v6" in fileName:
        writer.write("\n/ipv6 firewall address-list")
    else:
        writer.write("\n/ip firewall address-list")
    
    for prefix in prefixList:
        writer.write("\nadd list=" + listName + " address=" + prefix)

    writer.close()

def main():
    for listToGenerate in listsToGenerate:

        ipv4s = []
        ipv6s = []

        for prefix in githubIps[listToGenerate]:
            if "." in prefix:
                ipv4s.append(prefix)
            else:
                ipv6s.append(prefix)
            
        if len(ipv4s) > 0:
            #fileName = "github-" + listToGenerate + "-ips-v4.rsc"
            generateRsc(ipv4s, listToGenerate, "v4")
        if len(ipv6s) > 0:
            #fileName = "github-" + listToGenerate + "-ips-v6.rsc"
            generateRsc(ipv6s, listToGenerate, "v6")

if __name__ == "__main__":
    main()
