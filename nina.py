#!/usr/bin/env python

from urllib.parse import urlencode
from urllib.request import Request, urlopen
import re
from datetime import datetime
import json
from collections import namedtuple

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

url = 'https://warnung.bund.de/bbk.mowas/gefahrendurchsagen.json'
now = datetime.now()#.strftime('%Y-%m-%d %H:%M:%S')

request = Request(url)
json_string = urlopen(request).read().decode('utf-8')

# warnungen_dict=json.loads(json_string)  # behaves like a dict 
warnungen=json2obj(json_string)           # behaves like an object

for warnung in warnungen:
    ort=warnung.info[0].area[0].geocode[0].valueName
    if ort in ["Dortmund", "Bochum", "Hamm", "Herdecke" ]:
        print("=========================%s=================================" % ort )
        print( "%s %s severity=%s" % (warnung.msgType, warnung.sent, warnung.info[0].severity ))
        print( "%s" % warnung.info[0].headline )
        print( "%s" % warnung.info[0].description )
        print( "%s" % warnung.info[0].instruction )
        # import pdb; pdb.set_trace()



# https://schilling-bontkirchen.de/category/meine-notizzettel/

# <?php
# $url = file_get_contents('https://warnung.bund.de/bbk.mowas/gefahrendurchsagen.json');
 
# $json = json_decode($url);
# $z = 0;
# foreach ($json as $idx => $inhalt){
# $m1 = $inhalt->info[0]->headline;
# $m2 = $inhalt->info[0]->description;
#         foreach ($inhalt->info[0]->area as $id2 => $in2){
#                 if ($in2->geocode[0]->value=='059130000000'){
#                     $z++;
#                     print('{"data": { "head": "'.$m1.'"}}');                
#                     shell_exec('/teams.sh "'.$m1.'" "'.$m2.'"');
#                 } 
#        }
# }
# if ($z==0){
# print('{"data": { "head": "keine Gefahrenmeldung"}}');
# }
# ?>
