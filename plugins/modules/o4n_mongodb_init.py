#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals

DOCUMENTATION = """
---
module: o4n_mongodb_init
version_added: 1.0
author: "Daiana Casas"
short_description: Crea una coleccion en la base de datos y lo configura.
description:
    - Se conecta al servidor MongoDB
    - Dependiendo de la 'option' puede realizar distintas acciones sobre la base de datos especificada en la entrada.
        - crear un collection
        - eliminar un collection
        - eliminar todos los collections
        - ver todas las bases de datos con sus respectivos collections del servidor
        - ver todos los documentos de un collection
options:
    hostname:
        description:
            - host del servidor
        requiered: True
    port:
        description:
            - port del servidor
        requiered: True
    collectionname:
        description:
            - nombre del collection de la base de datos.
            - server, invoca al servidor.
            - name1, nombre del collection.
            - xallx, invoca a todos los collections.
        choices: ['server', <name>, 'xallx']
        requiered: True
    option:
        description:
            - Según su valor define la acción. Puede ser.
            - status, notifica la cantidad de documentos y sus contenidos
            - delete, elimina el/los collections invocados, según el collectionname
            - create, crea un collection con el nombre especificado en collecionname
        choices: ['status', 'delete', 'create']
        requiered: True
"""

EXAMPLES = """
- name: Server status - databases + collections
  o4n_mongodb_init:
    hostname: 'localhost'
    port: '27017'
    collectionname: 'server'
    option: 'status'
  register: content

- name: Create a collection on database test
  o4n_mongodb_init:
    hostname: 'localhost'
    port: '27017'
    collectionname: 'new_collection'
    option: 'create'
  register: content

- name: Delete a collection on database test
  o4n_mongodb_init:
    hostname: 'localhost'
    port: '27017'
    collectionname: 'new_collection'
    option: 'delete'
  register: content

- name: Collection info from database test
  o4n_mongodb_init:
    hostname: 'localhost'
    port: '27017'
    collectionname: 'new_collection'
    option: 'status'
  register: content
"""

RETURN = """
case1:
    description: Server status - databases + collections
    "msg": {
        "content": {
            "msg": {
                "admin": [
                    "system.version"
                ],
                "config": [
                    "system.sessions"
                ],
                "local": [
                    "startup_log"
                ],
                "test": [
                    "col1"
                ]
            },
            "status": true
        },
        "failed": false,
        "msg": true
    }
case2:
    description: Create a collection 'col2' on database test
    "msg": {
            "changed": false,
            "content": {
                "msg": "Creacion de la coleccion col2",
                "status": true
            },
            "failed": false,
            "msg": true
        }
case3:
    description: Delete a collection 'col2' on database test
    "msg": {
        "changed": false,
        "content": {
            "msg": "col2 eliminado",
            "status": true
        },
        "failed": false,
        "msg": true
    }
case4:
    description: Collection info 'col1' from database test
    "msg": {
        "changed": false,
        "content": {
            "msg": {
                "count_docs": 0,
                "list_docs": [],
                "name": "col1"
            },
            "status": true
        },
        "failed": false,
        "msg": true
    }
"""

from pymongo import MongoClient
from ansible.module_utils.basic import AnsibleModule
from bson.json_util import dumps
from bson.codec_options import CodecOptions
import json

if __name__ == "__main__":

    module = AnsibleModule(
        argument_spec=dict(
            hostname=dict(requiered=True),
            port=dict(requiered=True, type='int'),
            dbname=dict(requiered=False, default='devices'),
            user=dict(requiered=False, default="admin"),
            password=dict(requiered=False, no_log=True),
            collectionname=dict(requiered=True, default='lastversion'),
            option=dict(requiered=True),
        )
    )
    hostname = module.params.get("hostname")
    port = module.params.get("port")
    namedb = module.params.get("dbname")
    user = module.params.get("user")
    password = module.params.get("password")
    collection_name = module.params.get("collectionname")
    option = str(module.params.get("option")).lower()
    mdb_msg = ""
    flag = False
    access_client = False
    access_db = False
    try:
        # Conexion mongo db: se establece la conexion en la 1er operacion:
        # client = MongoClient(host=hostname,port=port, connect=False,tz_aware=False)
        client = MongoClient(
            host=hostname,
            port=port,
            username=user,
            password=password,
            authSource=namedb,
            connect=False,
            tz_aware=False
        )
        access_client = True
    except Exception as error:
        mdb_msg = error
        module.fail_json(msg=error, content="Sin conexion a mongo DB")
    if access_client:
        # Accedo a la base de datos:
        try:
            db = client[namedb]
            access_db = True
        except Exception as error:
            mdb_msg = error
            client.close()
        if access_db:
            flag = True
            if "create" in option:
                # Creacion de la coleccion de documentos:
                try:
                    db.create_collection(name=collection_name)
                    mdb_msg = "Creacion de la coleccion " + collection_name
                    flag = True
                except Exception as error:
                    em = str(error)
                    if "already exists" in em.lower():
                        exists = "Collection <" + collection_name + "> already exists."
                        list_col = [collection for collection in db.list_collection_names()]
                        mdb_msg = {"msg": exists, "db": namedb, "list_collections": list_col}
                    else:
                        mdb_msg = error
                        client.close()
            elif "delete" in option:
                try:
                    cflag = False
                    c_list = db.list_collection_names()
                    if collection_name.lower() == "xallx":
                        cflag = True
                        naflag = False
                        mdb_list = []
                    else:
                        naflag = True
                    for c in c_list:
                        if naflag:
                            if collection_name in c:
                                db.drop_collection(collection_name)
                                mdb_msg = collection_name + ": eliminado."
                                cflag = True
                                break
                        else:
                            db.drop_collection(c)
                            mdb_list.append(c + " eliminado")
                    if not cflag:
                        mdb_msg = collection_name + " not found."
                    if not naflag:
                        mdb_msg = mdb_list
                    flag = True
                except Exception as error:
                    mdb_msg = error
                    client.close()
            elif "status" in option:
                if "server" in collection_name:
                    try:
                        codec_options = CodecOptions(document_class=dict)
                        d = dict((db, [collection for collection in client[db].list_collection_names()]) for db in client.list_database_names())
                        mdb_msg = d
                        flag = True
                    except Exception as error:
                        mdb_msg = error
                        client.close()
                else:
                    try:
                        # Accedo a la coleccion:
                        c = db[collection_name]
                        docs = []
                        for a in c.find():
                            aux = dumps(a)
                            aux_json = json.loads(aux)
                            docs.append(aux_json)
                        # docs = [str(a) for a in c.find()]
                        qdocs = c.count_documents({})
                        mdb_msg = {"name_db": namedb, "name_collection": collection_name, "count_docs": qdocs, "list_docs": docs}
                    except Exception as error:
                        mdb_msg = error
                        client.close()
            else:
                mdb_msg = "Option: no válido"
        else:
            flag = False
        client.close()

    mdb_out = {"status": flag, "msg": mdb_msg}
    if flag:
        module.exit_json(msg=flag, content=mdb_out)
    else:
        module.fail_json(msg=mdb_msg)
