#!/usr/bin/python3
""" python task """
from urllib import request, parse
from sys import argv


if __name__ == "__main__":

    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email}).encode()
    # this will make the method "POST"
    req = request.Request(url=url, data=data)

    with request.urlopen(req) as f:
        print(f.read().decode('utf-8'))
