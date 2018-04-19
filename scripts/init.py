import requests
import re
from urlparse import urljoin
import os
from os import popen
import urllib

basic_url = os.environ['BASICURL'] = 'http://fileserver-service:8000/scripts/'

text = requests.get(basic_url).text
lire = re.compile(r'<li>.*?>(.*?)<.*')
list = [lire.search(x).groups()[0] for x in text.splitlines() if lire.search(x)]

for script_file in list:
    if ".py" in script_file:
        print("Download File: %s" % script_file)
        script_file = script_file.replace("\n", "")
        server_url = urljoin(basic_url, script_file)
        file_target = os.path.join("/scripts/", os.path.basename(script_file))
        print("server_url: %s" % server_url)
        print("file_target: %s" % file_target)
        urllib.urlretrieve(server_url, file_target)
    print("File downloaded: %s" % script_file)

print( "All scripts downloaded!")
popen("fwatchdog")
