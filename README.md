ip2dns.py

I'm da_667. I work for Cisco TALOS and I glued this script together with a boatload of help.

The purpose of this script is return a list of domains associated to an IP address in a nice, clean newline separated list, utilizing the openDNS API.

This script has an hard limitation that is governed by the openDNS api in that it can only accept 1,000 IP addresses at a time, so ensure that your input file contains no more than 1,000 IP addresses. I didn't make the rules, I just follow em.

usage:
./ip2dns.py -i [path/to/input/file] -o [/path/to/output/file] -t [your openDNS api token here]

This tool is being released under the MIT License. Cisco, OpenDNS, TALOS and/or any other Cisco owned or operated subsidiaries/organizations are in no way responsible for care, feeding, troubleshooting, or fire-breathing dragons that result from using this script. Really, I'm not going to be responsible for it either.

If you have questions/concerns or improvements to offer, reach out to me on twitter [at]da_667 or via e-mail deusexmachina667[at]gmail[dot]com. GL;HF.