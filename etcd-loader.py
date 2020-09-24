#!/usr/bin/python3
#
# PJ Waskiewicz
# 9/24/2020

import json
import etcd3

# etcd cluster targets, TODO - move into config file?
host = "10.10.1.2"
port = 2379

client = etcd3.client(host=host, port=port)

key = client.get('/foo/baz/booze')

print(key)

client.close()