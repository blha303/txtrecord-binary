#!/usr/bin/env python3
# txtrecord_encode.py input.png logo.example.com
import base64
import sys
with open(sys.argv[1],"rb") as f:
    enc = base64.b64encode(f.read()).decode("utf-8")

# '%04d' and '247' may need to be updated for large files to ensure the line count doesn't push the length
# longer than 255 bytes
print("\n".join("%s. IN TXT '{%04d}%s'" % (sys.argv[2], n,s) for n,s in enumerate(wrap(enc,247))))