#!/usr/bin/python3
import re
import subprocess
from subprocess import Popen, PIPE

a = subprocess.Popen("zpool status", stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)

data, err = a.communicate()

raiddisks = re.findall(r"\b(sd+[a-z])\b", data.decode())


def zfs_send(source, remoteip, destination):
    zfssendstatus = " "
    try:
	cmd = "zfs send {} | ssh {} zfs recv {}".format(source, remoteip, destination)
	if source and remoteip and destination:
		data = subprocess.Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
		out, err = data.communicate()
		if not out and not err:
			zfssendstatus = "success"
		elif err:
			zfssendstatus = "Failed"
	else:
		zfssendstatus = "Failed"
    except:
	zfssendstatus = "unexpected err"
    return zfssendstatus

print(raiddisks)
