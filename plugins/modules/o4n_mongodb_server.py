#!/usr/local/bin/python3
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

DOCUMENTATION = """
---
module: o4n_mongodb_server
version_added: 1.0
author: "Daiana Casas"
short_description: Notifica el estado de la base de datos del servidor MongoDB
description: Responde el estado de la base de datos del servidor conforme lo hace el statusServer del mismo.
options:
    hostname:
        description: 
            - host del servidor
        requiered: True
    port:
        description:
            - puerto del servidor
        requiered: True  
        type: int
    dbname:
        description:
            - nombre de la base de datos a acceder
        requiered: False
        default: 'test'  
"""

EXAMPLES = """
- name: Server status
  o4n_mongodb_server:
    hostname: localhost
    port: 27017
    dbname: 'devices'
  register: server_out
"""

RETURN = """
msg: 
    description: En todos los casos retorna un JSON. (ejemplo truncado)
    "msg": {
        "$clusterTime": {
            "clusterTime": {
                "$timestamp": {
                    "i": 1,
                    "t": 1584383606
                }
            },
            "signature": {
                "hash": {
                    "$binary": "AAAAAAAAAAAAAAAAAAAAAAAAAAA=",
                    "$type": "00"
                },
                "keyId": 0
            }
        },
        "host": "ubuntu-vb",
        "localTime": {
            "$date": 1584383610348
        },
    }
"""

from pymongo import MongoClient
from bson.json_util import loads, dumps
import urllib.parse
from collections import OrderedDict
from ansible.module_utils.basic import *
from bson.codec_options import CodecOptions
import json


if __name__ == "__main__":

    module = AnsibleModule(
        argument_spec=dict(
            hostname=dict(requiered=True),
            port=dict(requiered=True),
            dbname=dict(requiered=True),
            user=dict(requiered=False),
            password=dict(requiered=False,no_log=True),

        )
    )
    hostname = module.params.get("hostname")
    port = int(module.params.get("port"))
    dbname = module.params.get("dbname")
    user = module.params.get("user")
    password = module.params.get("password")
    server_out = OrderedDict()
    mdb_msg = ""
    flag = False
    access_client = False
    access_db = False

    try:
    ## Conexion mongo db: se establece la conexion en la 1er operacion:
        client = MongoClient(
            host=hostname, 
            port=port, 
            username=user,
            password = password,
            authSource=dbname,
            connect=False, 
            tz_aware=False)
        access_client = True
    except Exception as error:
        mdb_msg = error
        module.fail_json(msg=error, content="Sin conexion a mongo DB")
    if access_client:
        try:
            db = client[dbname]
            codec_options = CodecOptions(document_class=dict, tz_aware=False)
            serverResult = db.command("serverStatus", codec_options=codec_options)
            status_param = dumps(serverResult)
            status_json = json.loads(status_param)
            server_out["status"] = status_json
        except Exception as error:
            server_out["status"] = error
            client.close()
            module.fail_json(msg=error)
        module.exit_json(status=True, server_out=server_out)
