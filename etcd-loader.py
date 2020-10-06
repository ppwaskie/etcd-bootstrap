#!/usr/bin/python3
#
# PJ Waskiewicz
# 9/24/2020

import json
import etcd3

# etcd cluster targets, TODO - move into config file?
host = "10.10.1.2"
port = 2379

# open the etcd target
client = etcd3.client(host=host, port=port)

# read in the json schema
with open("./input.json", "r") as f:
    data = json.load(f)

# Start at node1 for the key
# TODO: not scalable as deleting nodes will leave gaps, fix this later (maybe add count of current nodes in DB)
node_num = 1

# Load the etcd3 database
for host in data['hosts']:
    json_nodedata = json.dumps(host)
    node_key = "/hosts/node" + str(node_num)

    # Load the next node's record
    client.put(node_key, json_nodedata)
    node_num += 1

#    hostname = host.get('hostname')
#    print ('/hosts/' + hostname + '/hostname \t\t\t ===> ', hostname)
#    print ('/hosts/' + hostname + '/available \t\t\t ===> ', host.get('available'))
#    client.put('/hosts/' + hostname + '/hostname', hostname)
#    client.put('/hosts/' + hostname + '/available', host.get('available'))
#
#    # network config block
#    for network in host['network']:
#        print ('/hosts/' + hostname + '/network/ipaddr \t\t ===> ', network.get('ipaddr'))
#        print ('/hosts/' + hostname + '/network/gateway \t\t ===> ', network.get('gateway'))
#        print ('/hosts/' + hostname + '/network/netmask \t\t ===> ', network.get('netmask'))
#        client.put('/hosts/' + hostname + '/network/ipaddr', network.get('ipaddr'))
#        client.put('/hosts/' + hostname + '/network/gateway', network.get('gateway'))
#        client.put('/hosts/' + hostname + '/network/netmask', network.get('netmask'))
#
#        for ethernet in network['ethernet']:
#            print ('/hosts/' + hostname + '/network/ethernet/mtu \t ===> ', ethernet.get('mtu'))
#            print ('/hosts/' + hostname + '/network/ethernet/fc-mode \t ===> ', ethernet.get('fc-mode'))
#            client.put('/hosts/' + hostname + '/network/ethernet/mtu', ethernet.get('mtu'))
#            client.put('/hosts/' + hostname + '/network/ethernet/fc-mode', ethernet.get('fc-mode'))
#
#    # blinkstick config data block
#    for blinkstick in host['blinkstick']:
#        print ('/hosts/' + hostname + '/blinkstick/frontColor \t ===> ', blinkstick.get('frontColor'))
#        print ('/hosts/' + hostname + '/blinkstick/backColor \t ===> ', blinkstick.get('backColor'))
#        print ('/hosts/' + hostname + '/blinkstick/blinkRate \t ===> ', blinkstick.get('blinkRate'))
#        client.put('/hosts/' + hostname + '/blinkstick/frontColor', blinkstick.get('frontColor'))
#        client.put('/hosts/' + hostname + '/blinkstick/backColor', blinkstick.get('backColor'))
#        client.put('/hosts/' + hostname + '/blinkstick/blinkRate', blinkstick.get('blinkRate'))

# shutdown etcd3 connection
client.close()