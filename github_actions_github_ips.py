from datetime import datetime, UTC
import requests
import json
import re

# https://blog.markhatton.co.uk/2011/03/15/regular-expressions-for-ip-addresses-cidr-ranges-and-hostnames/
ipv4AddressRegex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
ipv4CidrRegex = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\/(3[0-2]|[1-2][0-9]|[0-9]))$"
ipv6AddressRegex = r"^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*"
ipv6CidrRegex = r"^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*(\/(12[0-8]|1[0-1][0-9]|[1-9][0-9]|[0-9]))$"

today = datetime.now(UTC).strftime("%c") + " UTC"

githubIpURL = "https://api.github.com/meta"

githubIps = json.loads(requests.get(githubIpURL).content)

addressLists = []

def generateRefresherRsc(lists):
    print(lists)

    writer = open("github-ips-refresher.rsc", "w")
    writer.write('# Generated on ' + today)

    #file remove [find name~"^github.*ipv..rsc"]
    writer.write('\nfile remove [find name~"^github.*ipv..rsc"]')

    writer.write('\n/system script')
    writer.write('\nadd dont-require-permissions=yes name=github-ips-refresher owner=admin policy=ftp,read,write,test source=":log info \\"Download GitHub IP lists\\";\\r\\')
    for list in lists:
        writer.write('    \n\\n/tool fetch url=\\"https://raw.githubusercontent.com/GForceIndustries/mikrotik-github-ips/refs/heads/main/' + list + '.rsc\\" mode=https dst-path=' + list + '.rsc;\\r\\')
    writer.write('    \n\\n\\r\\')

    writer.write('\"')
    writer.close()

def generateListRsc(ipList, listName):
    writer = open(listName + ".rsc", "w")
    writer.write("# Generated on " + today)

    if "v6" in listName:
        writer.write("\n/ipv6 firewall address-list")
    else:
        writer.write("\n/ip firewall address-list")
    
    for ip in ipList:
        writer.write("\nadd list=" + listName + " address=" + ip)
    
    writer.close()

def main():
    githubIpsJson = json.loads(requests.get(githubIpURL).content)

    githubJsonKeys = githubIpsJson.keys()

    for githubJsonKey in githubJsonKeys:
        if not githubJsonKey == "domains" and not githubJsonKey == "verifiable_password_authentication":
            ipv4s = []
            ipv6s = []
            for jsonValue in githubIpsJson[githubJsonKey]:
                if re.match(ipv4AddressRegex, jsonValue) or re.match(ipv4CidrRegex, jsonValue):
                    ipv4s.append(jsonValue)
                elif re.match(ipv6AddressRegex, jsonValue) or re.match(ipv6CidrRegex, jsonValue):
                    ipv6s.append(jsonValue)
            if len(ipv4s) > 0:
                addressList = "github-" + githubJsonKey + "-ips-ipv4"
                generateListRsc(ipv4s, addressList)
                addressLists.append(addressList)
            if len(ipv6s) > 0:
                addressList = "github-" + githubJsonKey + "-ips-ipv6"
                generateListRsc(ipv6s, addressList)
                addressLists.append(addressList)
            
    generateRefresherRsc(addressLists)

if __name__ == "__main__":
    main()
