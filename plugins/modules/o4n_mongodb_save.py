#!/usr/local/bin/python3

DOCUMENTATION = """
module: mongodb_save
version_added: 3.0
author: "Daiana Casas"
short_description: Guarda y/o actualiza documentos en una collection y database determinada.  
description:
    - Se conecta a MongoDB.
    - Genera un documento con la informacion que ingresa en el input.
    - Actualiza un documento con la informacion que ingresa en el input.
    - Verifica la existencia del device con la ip ingresada.
    - Manejo de errores en caso de inputs incorrectos.
    - v3:  agrego verificacion de existencias, actualizacion en ambas collections["master","lastversion"]
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
    status:
        description:
            - permite la actualizacion del documento perteneciente al equipo.
        requiered: False
        default: 'normal'
        choices: ['normal','update']     
    category:
        description:
            - nombre de la categoria de la informacion a guardar.
        requiered: False
        default: 'base'
    hostdevice: 
        description:
            - device's hostname
        requiered: True
    ipdevice: 
        description:
            - ip device
        requiered: True
    data:
        description:
            - informacion a guardar.
        requiered: True
"""

EXAMPLE = """
tasks:
    - name: Backup config device
      mongodb_save:
        hostname: 'localhost'
        port: '27017'
        collectionname: 'master'
        hostdevice: "{{host_device}}"
        ipdevice: "{{ip_device}}"
        data: "{{output.content.config}}"
      register: output
tasks:
    - name: Update backup config device
      mongodb_save:
        hostname: 'localhost'
        port: '27017'
        collectionname: 'master'
        status: 'upgrade'
        hostdevice: "{{host_device}}"
        ipdevice: "{{ip_device}}"
        data: "{{output.content.config}}"
tasks:
    - name: Update config device
      mongodb_save:
        hostname: 'localhost'
        port: '27017'
        collectionname: 'lastversion'
        status: update
        hostdevice: "{{host_device}}"
        ipdevice: "{{ip_device}}"
        data: "{{output2.content.config}}"
      register: output
 
"""

RETURN = """
msg: 
    description: En todos los casos retorna un JSON. Segun la opcion:
    
caso: actualizar device no existente
    {
            "info": "No se puede actualizar. No existe documento con el ip: 10.54.153.52",
            "time": "Fri Mar 13 17:05:24 2020"
        }
caso: guardar device nuevo
    {
            "category": "base",
            "info": "10.54.153.52-admin",
            "new_id": "5e6be7ea372efdf06aaf6513",
            "time": "Fri Mar 13 17:07:06 2020"
        }
caso: actualizar device existente SIN especificar : status = "normal"
    {
            "id": "{'$oid': '5e6be7ea372efdf06aaf6513'}",
            "info": "Ya existe un documento con el ip: 10.54.153.52 ",
            "time": "Fri Mar 13 17:08:14 2020"
        }
caso: actualizar device existente especificando: status = "update"
    {
            "time": "Fri Mar 13 17:23:18 2020",
            "update": "master",
            "update_id": "{'$oid': '5e6be7ea372efdf06aaf6513'}"
        
        }

"""

import time
from collections import OrderedDict
from ansible.module_utils.basic import *
from bson.json_util import dumps
from pymongo import MongoClient

if __name__ == "__main__":

    module = AnsibleModule(
        argument_spec=dict(
            hostname=dict(requiered=True),
            port=dict(requiered=True, type='int'),
            dbname=dict(requiered=False, default="test"),
            user=dict(requiered=False, default="admin"),
            password=dict(requiered=False,no_log=True),
            collectionname=dict(requiered=True, default="lastversion", choices=["master","lastversion"]),
            status=dict(requiered=False, default="normal", choices=["normal","update"]),
            category=dict(requiered=False, default="base", choices=["base"]),
            hostdevice=dict(required=True),
            ipdevice=dict(required=True),
            data=dict(requiered=True),
            )
    )
    hostname = module.params.get("hostname")
    port = module.params.get("port")
    namedb = module.params.get("dbname")
    user = module.params.get("user")
    password = module.params.get("password")
    collectionname = module.params.get("collectionname")
    status = module.params.get("status")
    category = module.params.get("category")
    input = module.params.get('data') # --> string with '
    new_data = OrderedDict()
    output = OrderedDict()

## Manipulo los datos para guardar en Mongo:
    try:
        new_data["hostname"] = module.params.get("hostdevice")
        new_data["ip"] = module.params.get("ipdevice")
        new_data["category"] = collectionname
        new_data["time"] = time.asctime(time.localtime())
        new_data["source"] = input
        output["time"] = new_data["time"]
    except Exception as error:
        msg = str(error)
        module.fail_json(msg=msg, content="No se puede guardar el input")
## Conexion mongo db: se establece la conexion en la 1er operacion:
    try:
## Conexion mongo db: se establece la conexion en la 1er operacion:
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
## Si es master collection:
    if access_client:
## Acceso a la coleccion "test" de la DB (si no existe ne Mongo, la crea): 'test'
        try:
            db = client[namedb]
            c = db[collectionname]
## Si existe ese documento:
        ##  POR IP:
            docObj = c.find_one({"ip": new_data["ip"]})
            docstr = dumps(docObj)
            doc = json.loads(docstr)
            fail = False
        except Exception as error:
            fail = True
            msg = "Error-> " + str(error)
        if not fail:
    ## Intento acceder al id, si exite uno:
            try:
                doc_id = str(doc["_id"])
    ## Actualizo el documento, ya sea en master o lastversion:
                if "update" in status.lower():
                    c.update_one(filter={'ip': new_data["ip"]}, update={'$set': {'source': new_data["source"], 'time': time.asctime(time.localtime())}})
                    output["update_id"] = doc_id
                    output["update"] = collectionname

    ## No puedo crear un nuevo doc con el mismo ip, ya sea en master o lastversion:
                else:
                    output["id"] = doc_id
                    output["update"] = collectionname
                    output["info"] = "Ya existe un documento con el ip: {} ".format(new_data["ip"])
    ## Si no existe ese ip,
            except Exception as error:
                e = "{}".format(error)
                if "'NoneType' object is not subscriptable" in e:
    ## e intento actualizar: error
                    if "update" in status.lower():
                        output["info"] = "No se puede actualizar. No existe documento con el ip: {}".format(new_data["ip"])
                    else:
                        r = c.insert_one(new_data)
                        output["new_id"] = str(r.inserted_id)
                        output["category"] = category
                        output["info"] = new_data["ip"] + "-" + new_data["hostname"]
            module.exit_json(status=True, content=output)
        else:
            module.fail_json(msg=msg, status=False)
