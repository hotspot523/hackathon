
'''
A. Change firewall - protocol - from tcp to udp
B. Change 3rd vnics- portgroup name to EXT_VLAN_201b
C. Change ospf- enabled = false to true
D. Update holddowntimer = holddowntimer +keepalivetimer
'''

import json, os
file = 'sample.json'
with open(file) as json_data:
    data = json.load(json_data)
    json_data.close()

    data['featureConfigs']['features'][2]['firewallRules']['firewallRules'][0]['application']['service'][0]['protocol'] = 'udp'


    data['vnics']['vnics'][0]['portgroupName'] = 'EXT_VLAN_201b'


    data['featureConfigs']['features'][5]['bgp']['redistribution']['rules']['rules'][0]['from']['ospf'] = 'true'


    timer = data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][0]['holdDownTimer'] + \
        data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][0]['keepAliveTimer']
    data['featureConfigs']['features'][5]['bgp']['bgpNeighbours']['bgpNeighbours'][0]['holdDownTimer'] = timer

os.remove(file)

with open(file, 'w') as json_data:
    json_data.seek(0)  # rewind
    json_data.write(json.dumps(data))
    json_data.truncate()