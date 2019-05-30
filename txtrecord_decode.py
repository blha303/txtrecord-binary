#!/usr/bin/env python3
# txtrecord_decode.py output.png logo.example.com
import dns.resolver # pip3 install dnspython
import base64
import sys
q = dns.resolver.query(sys.argv[2],"TXT").response.answer[0]
enc = b"".join(line.split(b"}",1)[1] for line in sorted(_.strings[0] for _ in q))
with open(sys.argv[1],"wb") as f:
    f.write(base64.b64decode(enc))