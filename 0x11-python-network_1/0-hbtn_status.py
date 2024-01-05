#!/usr/bin/python3
"""A script that
fetches https://intranet.hbtn.io/status.
"""


if __name__ == '__main__':
    import urllib.request
    
    url = 'https://intranet.hbtn.io/status'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    req = urllib.request.Request(url, headers=headers)
    
    with urllib.request.urlopen(req) as resp:
        content = resp.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
