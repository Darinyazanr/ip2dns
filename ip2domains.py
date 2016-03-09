#!/usr/bin/python

import argparse
import textwrap
from urllib2 import Request, urlopen
import json


parser = argparse.ArgumentParser(
    formatter_class=argparse.RawDescriptionHelpFormatter,
    description=textwrap.dedent('''
                    ip2domains.py
                Brought to you by:
                    @da_667
                With Special Thanks from:
                    Kappa
                    WiK
                    Shadghost
                ---------------------
Given a list of IP addresses, return IP addresses from OpenDNS investigate api.
As you might expect this request an API key. Batteries sold separately.
Usage: ip2domains.py -i <infile> -o <outfile> -t [token here]
'''))

#Infile, outfile, and token arguments via ArgParse are all required.

parser.add_argument('-i', dest="infile", required=True, help="file containing a list of IP addresses, one per line.")
parser.add_argument('-o', dest="outfile", required=True, help="The name of the file to output a list of domains to.")
parser.add_argument('-t', dest="token", required=True, help="Your OpenDNS API token.")
args = parser.parse_args()


# latest_domains

headers = {
  'Authorization': 'Bearer ' + args.token,
  'User-Agent' : 'TALOS_OpenDNS_powertools'
}

#send a request to the api. If the response code is 200, print out a header plus the output and write the same data to a file.
with open(args.infile, 'r') as fin:
    for line in fin.readlines():
        request = Request('https://investigate.api.opendns.com/dnsdb/ip/a/%s.json' % line.strip(), headers=headers)
        response = urlopen(request)
        response_body = response.read()
        response_code = response.getcode()
        if response_code == 200:
            json_data = json.loads(response_body)
            head = 'domains for %s:' % line.strip()
            print head
            with open(args.outfile, 'a') as fout:
                fout.write(head + '\n')
                fout.close()
            for item in json_data['rrs']:
                print item['rr']
                with open(args.outfile, 'a') as fout:
                    fout.write(item['rr'])
                    fout.write('\n')
                    fout.close()
            print ''
            with open(args.outfile, 'a') as fout:
                fout.write('\n')
                fout.close()
        else:
            print "Failed with code %s" % response_body.code
fin.close()
exit()