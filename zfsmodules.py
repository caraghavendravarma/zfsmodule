#!/usr/bin/python3
import re
import subprocess
from subprocess import Popen, PIPE

a = subprocess.Popen("zpool status", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)

data, err = a.communicate()

raiddisks = re.findall(r"\b(sd+[a-z])\b", data.decode())

print(raiddisks)
