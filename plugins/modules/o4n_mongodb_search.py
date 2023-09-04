#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


from __future__ import print_function, unicode_literals


DOCUMENTATION = """
module: o4n_mongodb_search
version_added: 1.0
author: "Daiana Casas"
short_description: Busca documentos en una collection y database determinada. 
description:
    - Se conecta a MongoDB
    - Busca un documento con la informacion que ingresa en la ipdevice.
    
options:
    hostname:
        description: 
            - host del servidor
        requiered: True
    port:
        description:
            - port del servidor
        requiered: True  
        type: int
    dbname:
        description:
            - database name
        requiered: False
        default: 'test'    
    collectionname:
        description: 
            - nombre de la collection. Debe existir en la db.
        requiered: True            
    category:
        description:
            - nombre de la categoria de la informacion a guardar.
        requiered: False
        default: 'base'
    device:
        description:
            - informacion a guardar.
        requiered: True            
"""

EXAMPLE = """
tasks:
    - name: Search objects in a Data Base by IP
      o4n_mongodb_search:
        hostname: 'localhost'
        port: '27017'
        dbname: 'dbase'
        collectionname: 'server'
        search: '10.1.1.1'
      register: content

tasks:
    - name: Search objects in a Data Base by username
      o4n_mongodb_search:
        hostname: 'localhost'
        port: '27017'
        dbname: 'dbase'
        collectionname: 'server'
        search: 'nepal'
      register: content
"""

RETURN = """
msg: 
    description: En todos los casos retorna un JSON.
    "msg": {
        "salida": {
            "changed": false,
            "failed": false,
            "find": true,
            "sout": {
                "_id": {
                    "$oid": "601341474e7c093407c5da92"
                },
                "category": "master",
                "hostname": "o4n_SW_DATA_CENTER",
                "ip": "10.54.154.157",
                "source": "...content..."
            }
        }    
    }
"""

from pymongo import MongoClient
from bson.json_util import loads,dumps
from collections import OrderedDict
from ansible.module_utils.basic import *
from bson.objectid import ObjectId
import urllib.parse
import json


if __name__ == "__main__":

    module = AnsibleModule(
        argument_spec=dict(
            hostname=dict(requiered=True),
            port=dict(requiered=True, type='int'),
            dbname=dict(requiered=False, default="test"),
            user=dict(requiered=False),
            password=dict(requiered=False,no_log=True),
            collectionname=dict(requiered=True),
            category=dict(requiered=False, default="base"),
            search=dict(requiered=True, type='dict'),
            )
    )
    hostname = module.params.get("hostname")
    port = module.params.get("port")
    namedb = module.params.get("dbname")
    user = module.params.get("user")
    password = module.params.get("password")
    collectionname = module.params.get("collectionname")
    category = module.params.get("category")
    search = module.params.get("search")
    #search_param_parser = search_param.replace("'",'"')
    #search = json.loads(search_param_parser)
    sout = OrderedDict()

    access_client = False
    access_col = False

    find = False

## Conexion mongo db: se establece la conexion en la 1er operacion:
    try:
        #client = MongoClient(host=hostname, port=port, connect=False, tz_aware=False)
        client = MongoClient(
            host=hostname, 
            port=port, 
            username=user,
            password = password,
            authSource=namedb,
            connect=False, 
            tz_aware=False
        )
        access_client = True
    except Exception as error:
        mdb_msg = error
        module.fail_json(msg=error, content="Sin conexion a mongo DB")
## Accedo al db y coleccion:
    if access_client:
        try:
            db = client[namedb]
            c = db[collectionname]
            access_col = True
        except Exception as error:
            sout["status"] = error
            client.close()
            module.fail_json(msg=error, find=False)
    if access_col:
## ingreso a las keys:
##      POR IP:
        try:
            sip = search["ip"]
            docObj = c.find_one({"ip": sip})
            fail = False
        except Exception as error:
            fail = True
##      POR HOSTNAME:
        if fail:
            try:
                shost = search["username"]
                docObj = c.find_one({"username": shost})
                docstr = dumps(docObj)
                if docObj:
                    doc = json.loads(docstr)
                    module.exit_json(status=True,find=True, sout=doc)
                else:
                    module.exit_json(status=True,find=False, sout=docObj)
            except Exception as error:
                module.fail_json(msg="Key word error", content="El key word no existe en el doc de MongoDB", find=False)
        else:
            if docObj:
                docstr = dumps(docObj)
                doc = json.loads(docstr)
                module.exit_json(status=True,find=True, sout=doc)
            else:
                module.exit_json(status=True,find=False, sout=docObj)