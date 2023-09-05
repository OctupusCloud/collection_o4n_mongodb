#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

DOCUMENTATION = """
---
module: o4n_mongodb_delete
version_added: 1.0
author: "Daiana Casas"
short_description: Elimina un/todos documentos en un collection y database determinada.  
description:
    - Se conecta al servidor MongoDB.
    - Según el dato de entrada va a buscarlo dentro de la collection y database especificada.
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
        default: 'lastversion'
        choices: ['lastversion','master']      
    delete_with: 
        description:
            - type of data information device to search and eliminate.
        requiered: True
        choices: ['ip','id','hostname','all']
    delete_this:
        description:
            - ip,id,hostname device. This is not required on delete_with ='all' option.
        requiered: False
"""

EXAMPLES = """
- name: Delete with ip config device
  o4n_mongodb_delete:
    hostname: 'localhost'
    port: '27017'
    collectionname: 'master'
    delete_with: 'ip'
    delete_this: "{{ip_device}}"
  register: output

- name: Delete with document's id 
  o4n_mongodb_delete:
    hostname: 'localhost'
    port: '27017'
    collectionname: 'master'
    delete_with: 'id'
    delete_this: "{{id_device}}"

- name: Delete with hostname device
  mongodb_save:
    hostname: 'localhost'
    port: '27017'
    collectionname: 'lastversion'
    delete_with: 'hostname'
    delete_this: "{{host_device}}"
  register: output

- name: Delete all documents on 'lastversion' collection.
  mongodb_save:
    hostname: 'localhost'
    port: '27017'
    collectionname: 'lastversion'
    delete_with: 'all'
  register: output
"""

RETURN = """
case1: 
    description: Delete with id/ip/hostname device
    "content": {
        "deleted": {
            "_id": {
                "$oid": "5e9f415a11ae7508ca552dbc"
            },
            "testlast": 4.0
        }
    }
case2:
    description: Delete all documents on TestCollection
    "content": {
            "deleted": "all documents of TestCollection"
        }
"""

from pymongo import MongoClient
from bson.json_util import loads,dumps
from bson.objectid import ObjectId
from collections import OrderedDict
from ansible.module_utils.basic import *
import json

if __name__ == "__main__":

    module = AnsibleModule(
        argument_spec=dict(
            hostname=dict(requiered=True),
            port=dict(requiered=True),
            dbname=dict(requiered=True),
            user=dict(requiered=False, default="admin"),
            password=dict(requiered=False,no_log=True),
            collectionname=dict(requiered=True),
            delete_with=dict(requiered=True,default="id",choices=["ip","id","hostname","all"]),
            delete_this=dict(requiered=False),
        )
    )
    hostname = module.params.get("hostname")
    port = int(module.params.get("port"))
    namedb = module.params.get("dbname")
    user = module.params.get("user")
    password = module.params.get("password")
    collectionname = module.params.get("collectionname")
    option = module.params.get("delete_with")# --> string with '
    value = module.params.get("delete_this")
    delete_out = OrderedDict()

    access_client = False
    if option != "all":
        if not len(value):
            msg = "Error MongoDb"
            module.fail_json(msg=msg, content="ERROR: no hay informacion para realizar la eliminacion. Ver 'delete_this': empty")            

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
        msg = str(error)
        module.fail_json(msg=msg, content="Sin conexion con mongo DB")
## Accedo a la database y collection correspondientes
    if access_client:
        try:
            db = client[namedb]
            c = db[collectionname]
            
## Procedo a la eliminacion del doc:
            if option == "ip":
                docObj = c.find_one_and_delete({"ip": value})
            elif option == "id":
                docObj = c.find_one_and_delete({"_id": ObjectId(value)})
            elif option == "hostname":
                docObj = c.find_one_and_delete({"hostname": value})
            elif option == "all":
                c.drop()
                db.create_collection(name=collectionname)
            if option == 'all':
                out = {"deleted": "all documents of " + collectionname}
            else:
                docstr = dumps(docObj)
                doc=json.loads(docstr)
                if isinstance(doc,dict):
                    out = {"deleted": doc }
                else: 
                    msg = "Error-> Document on Collection doesn't exist" 
                    module.fail_json(msg=msg, content="No se encuentra el doc {} :{}".format(option,value))
            fail = False
        except Exception as error:
            fail = True
            msg = "Error-> " + str(error)
            module.fail_json(msg=msg, content="Error en la busqueda del doc {} :{}".format(option,value))
    if not fail:
        module.exit_json(status=True, content=out)