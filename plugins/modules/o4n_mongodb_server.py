#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


from __future__ import print_function, unicode_literals
#from typing_extensions import Required

DOCUMENTATION = """
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

EXAMPLE = """
tasks:
    - name: Server status
      o4n_mongodb_server:
        hostname: localhost
        port: 27017
        dbname: 'devices'
      register: server_out
"""

RETURN = """
{
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
    "asserts": {
        "msg": 0,
        "regular": 0,
        "rollovers": 0,
        "user": 14,
        "warning": 0
    },
    "connections": {
        "active": 1,
        "available": 51195,
        "current": 5,
        "totalCreated": 5
    },
    "electionMetrics": {
        "averageCatchUpOps": 0.0,
        "catchUpTakeover": {
            "called": 0,
            "successful": 0
        },
        "electionTimeout": {
            "called": 1,
            "successful": 1
        },
        "freezeTimeout": {
            "called": 0,
            "successful": 0
        },
        "numCatchUps": 0,
        "numCatchUpsAlreadyCaughtUp": 0,
        "numCatchUpsFailedWithError": 0,
        "numCatchUpsFailedWithNewTerm": 0,
        "numCatchUpsFailedWithReplSetAbortPrimaryCatchUpCmd": 0,
        "numCatchUpsSkipped": 1,
        "numCatchUpsSucceeded": 0,
        "numCatchUpsTimedOut": 0,
        "numStepDownsCausedByHigherTerm": 0,
        "priorityTakeover": {
            "called": 0,
            "successful": 0
        },
        "stepUpCmd": {
            "called": 0,
            "successful": 0
        }
    },
    "extra_info": {
        "input_blocks": 72632,
        "involuntary_context_switches": 478,
        "maximum_resident_set_kb": 118660,
        "note": "fields vary by platform",
        "output_blocks": 1200,
        "page_faults": 294,
        "page_reclaims": 21497,
        "system_time_us": 214745,
        "user_time_us": 1004980,
        "voluntary_context_switches": 1681
    },
    "flowControl": {
        "enabled": true,
        "isLagged": false,
        "isLaggedCount": 0,
        "isLaggedTimeMicros": 0,
        "locksPerOp": 0.0,
        "sustainerRate": 0,
        "targetRateLimit": 1000000000,
        "timeAcquiringMicros": 8
    },
    "freeMonitoring": {
        "state": "undecided"
    },
    "globalLock": {
        "activeClients": {
            "readers": 0,
            "total": 0,
            "writers": 0
        },
        "currentQueue": {
            "readers": 0,
            "total": 0,
            "writers": 0
        },
        "totalTime": 16152000
    },
    "host": "ubuntu-vb",
    "localTime": {
        "$date": 1584383610348
    },
    "locks": {
        "Collection": {
            "acquireCount": {
                "W": 1,
                "r": 63,
                "w": 4
            }
        },
        "Database": {
            "acquireCount": {
                "W": 11,
                "r": 108,
                "w": 10
            }
        },
        "Global": {
            "acquireCount": {
                "W": 3,
                "r": 140,
                "w": 24
            }
        },
        "Mutex": {
            "acquireCount": {
                "r": 130
            }
        },
        "ParallelBatchWriterMode": {
            "acquireCount": {
                "W": 1,
                "r": 61
            }
        },
        "ReplicationStateTransition": {
            "acquireCount": {
                "W": 2,
                "w": 167
            },
            "acquireWaitCount": {
                "w": 1
            },
            "timeAcquiringMicros": {
                "w": 40
            }
        },
        "oplog": {
            "acquireCount": {
                "r": 52,
                "w": 1
            }
        }
    },
    "logicalSessionRecordCache": {
        "activeSessionsCount": 1,
        "lastSessionsCollectionJobCursorsClosed": 0,
        "lastSessionsCollectionJobDurationMillis": 1027,
        "lastSessionsCollectionJobEntriesEnded": 0,
        "lastSessionsCollectionJobEntriesRefreshed": 0,
        "lastSessionsCollectionJobTimestamp": {
            "$date": 1584383595389
        },
        "lastTransactionReaperJobDurationMillis": 1026,
        "lastTransactionReaperJobEntriesCleanedUp": 0,
        "lastTransactionReaperJobTimestamp": {
            "$date": 1584383595390
        },
        "sessionCatalogSize": 0,
        "sessionsCollectionJobCount": 1,
        "transactionReaperJobCount": 1
    },
    "mem": {
        "bits": 64,
        "resident": 115,
        "supported": true,
        "virtual": 1830
    },
    "metrics": {
        "commands": {
            "<UNKNOWN>": 0,
            "_addShard": {
                "failed": 0,
                "total": 0
            },
            "_cloneCatalogData": {
                "failed": 0,
                "total": 0
            },
            "_cloneCollectionOptionsFromPrimaryShard": {
                "failed": 0,
                "total": 0
            },
            "_configsvrAddShard": {
                "failed": 0,
                "total": 0
            },
            "_configsvrAddShardToZone": {
                "failed": 0,
                "total": 0
            },
            "_configsvrBalancerStart": {
                "failed": 0,
                "total": 0
            },
            "_configsvrBalancerStatus": {
                "failed": 0,
                "total": 0
            },
            "_configsvrBalancerStop": {
                "failed": 0,
                "total": 0
            },
            "_configsvrCommitChunkMerge": {
                "failed": 0,
                "total": 0
            },
            "_configsvrCommitChunkMigration": {
                "failed": 0,
                "total": 0
            },
            "_configsvrCommitChunkSplit": {
                "failed": 0,
                "total": 0
            },
            "_configsvrCommitMovePrimary": {
                "failed": 0,
                "total": 0
            },
            "_configsvrCreateCollection": {
                "failed": 0,
                "total": 0
            },
            "_configsvrCreateDatabase": {
                "failed": 0,
                "total": 0
            },
            "_configsvrDropCollection": {
                "failed": 0,
                "total": 0
            },
            "_configsvrDropDatabase": {
                "failed": 0,
                "total": 0
            },
            "_configsvrEnableSharding": {
                "failed": 0,
                "total": 0
            },
            "_configsvrMoveChunk": {
                "failed": 0,
                "total": 0
            },
            "_configsvrMovePrimary": {
                "failed": 0,
                "total": 0
            },
            "_configsvrRemoveShard": {
                "failed": 0,
                "total": 0
            },
            "_configsvrRemoveShardFromZone": {
                "failed": 0,
                "total": 0
            },
            "_configsvrShardCollection": {
                "failed": 0,
                "total": 0
            },
            "_configsvrUpdateZoneKeyRange": {
                "failed": 0,
                "total": 0
            },
            "_flushDatabaseCacheUpdates": {
                "failed": 0,
                "total": 0
            },
            "_flushRoutingTableCacheUpdates": {
                "failed": 0,
                "total": 0
            },
            "_getNextSessionMods": {
                "failed": 0,
                "total": 0
            },
            "_getUserCacheGeneration": {
                "failed": 0,
                "total": 0
            },
            "_isSelf": {
                "failed": 0,
                "total": 0
            },
            "_mergeAuthzCollections": {
                "failed": 0,
                "total": 0
            },
            "_migrateClone": {
                "failed": 0,
                "total": 0
            },
            "_movePrimary": {
                "failed": 0,
                "total": 0
            },
            "_recvChunkAbort": {
                "failed": 0,
                "total": 0
            },
            "_recvChunkCommit": {
                "failed": 0,
                "total": 0
            },
            "_recvChunkStart": {
                "failed": 0,
                "total": 0
            },
            "_recvChunkStatus": {
                "failed": 0,
                "total": 0
            },
            "_shardsvrShardCollection": {
                "failed": 0,
                "total": 0
            },
            "_transferMods": {
                "failed": 0,
                "total": 0
            },
            "abortTransaction": {
                "failed": 0,
                "total": 0
            },
            "aggregate": {
                "failed": 0,
                "total": 0
            },
            "appendOplogNote": {
                "failed": 0,
                "total": 0
            },
            "applyOps": {
                "failed": 0,
                "total": 0
            },
            "authenticate": {
                "failed": 0,
                "total": 0
            },
            "availableQueryOptions": {
                "failed": 0,
                "total": 0
            },
            "buildInfo": {
                "failed": 0,
                "total": 0
            },
            "checkShardingIndex": {
                "failed": 0,
                "total": 0
            },
            "cleanupOrphaned": {
                "failed": 0,
                "total": 0
            },
            "cloneCollection": {
                "failed": 0,
                "total": 0
            },
            "cloneCollectionAsCapped": {
                "failed": 0,
                "total": 0
            },
            "collMod": {
                "failed": 0,
                "total": 0
            },
            "collStats": {
                "failed": 0,
                "total": 0
            },
            "commitTransaction": {
                "failed": 0,
                "total": 0
            },
            "compact": {
                "failed": 0,
                "total": 0
            },
            "connPoolStats": {
                "failed": 0,
                "total": 0
            },
            "connPoolSync": {
                "failed": 0,
                "total": 0
            },
            "connectionStatus": {
                "failed": 0,
                "total": 0
            },
            "convertToCapped": {
                "failed": 0,
                "total": 0
            },
            "coordinateCommitTransaction": {
                "failed": 0,
                "total": 0
            },
            "count": {
                "failed": 0,
                "total": 0
            },
            "create": {
                "failed": 0,
                "total": 0
            },
            "createIndexes": {
                "failed": 0,
                "total": 0
            },
            "createRole": {
                "failed": 0,
                "total": 0
            },
            "createUser": {
                "failed": 0,
                "total": 0
            },
            "currentOp": {
                "failed": 0,
                "total": 0
            },
            "dataSize": {
                "failed": 0,
                "total": 0
            },
            "dbHash": {
                "failed": 0,
                "total": 0
            },
            "dbStats": {
                "failed": 0,
                "total": 0
            },
            "delete": {
                "failed": 0,
                "total": 0
            },
            "distinct": {
                "failed": 0,
                "total": 0
            },
            "driverOIDTest": {
                "failed": 0,
                "total": 0
            },
            "drop": {
                "failed": 0,
                "total": 0
            },
            "dropAllRolesFromDatabase": {
                "failed": 0,
                "total": 0
            },
            "dropAllUsersFromDatabase": {
                "failed": 0,
                "total": 0
            },
            "dropConnections": {
                "failed": 0,
                "total": 0
            },
            "dropDatabase": {
                "failed": 0,
                "total": 0
            },
            "dropIndexes": {
                "failed": 0,
                "total": 0
            },
            "dropRole": {
                "failed": 0,
                "total": 0
            },
            "dropUser": {
                "failed": 0,
                "total": 0
            },
            "endSessions": {
                "failed": 0,
                "total": 0
            },
            "explain": {
                "failed": 0,
                "total": 0
            },
            "features": {
                "failed": 0,
                "total": 0
            },
            "filemd5": {
                "failed": 0,
                "total": 0
            },
            "find": {
                "failed": 0,
                "total": 8
            },
            "findAndModify": {
                "failed": 0,
                "total": 0
            },
            "flushRouterConfig": {
                "failed": 0,
                "total": 0
            },
            "fsync": {
                "failed": 0,
                "total": 0
            },
            "fsyncUnlock": {
                "failed": 0,
                "total": 0
            },
            "geoSearch": {
                "failed": 0,
                "total": 0
            },
            "getCmdLineOpts": {
                "failed": 0,
                "total": 0
            },
            "getDatabaseVersion": {
                "failed": 0,
                "total": 0
            },
            "getDiagnosticData": {
                "failed": 0,
                "total": 0
            },
            "getFreeMonitoringStatus": {
                "failed": 0,
                "total": 0
            },
            "getLastError": {
                "failed": 0,
                "total": 0
            },
            "getLog": {
                "failed": 0,
                "total": 0
            },
            "getMore": {
                "failed": 0,
                "total": 0
            },
            "getParameter": {
                "failed": 0,
                "total": 0
            },
            "getShardMap": {
                "failed": 0,
                "total": 0
            },
            "getShardVersion": {
                "failed": 0,
                "total": 0
            },
            "getnonce": {
                "failed": 0,
                "total": 0
            },
            "grantPrivilegesToRole": {
                "failed": 0,
                "total": 0
            },
            "grantRolesToRole": {
                "failed": 0,
                "total": 0
            },
            "grantRolesToUser": {
                "failed": 0,
                "total": 0
            },
            "hostInfo": {
                "failed": 0,
                "total": 0
            },
            "insert": {
                "failed": 0,
                "total": 0
            },
            "invalidateUserCache": {
                "failed": 0,
                "total": 0
            },
            "isMaster": {
                "failed": 0,
                "total": 8
            },
            "killAllSessions": {
                "failed": 0,
                "total": 0
            },
            "killAllSessionsByPattern": {
                "failed": 0,
                "total": 0
            },
            "killCursors": {
                "failed": 0,
                "total": 0
            },
            "killOp": {
                "failed": 0,
                "total": 0
            },
            "killSessions": {
                "failed": 0,
                "total": 0
            },
            "listCollections": {
                "failed": 0,
                "total": 0
            },
            "listCommands": {
                "failed": 0,
                "total": 0
            },
            "listDatabases": {
                "failed": 0,
                "total": 0
            },
            "listIndexes": {
                "failed": 0,
                "total": 2
            },
            "lockInfo": {
                "failed": 0,
                "total": 0
            },
            "logRotate": {
                "failed": 0,
                "total": 0
            },
            "logout": {
                "failed": 0,
                "total": 0
            },
            "mapReduce": {
                "failed": 0,
                "total": 0
            },
            "mapreduce": {
                "shardedfinish": {
                    "failed": 0,
                    "total": 0
                }
            },
            "mergeChunks": {
                "failed": 0,
                "total": 0
            },
            "moveChunk": {
                "failed": 0,
                "total": 0
            },
            "ping": {
                "failed": 0,
                "total": 0
            },
            "planCacheClear": {
                "failed": 0,
                "total": 0
            },
            "planCacheClearFilters": {
                "failed": 0,
                "total": 0
            },
            "planCacheListFilters": {
                "failed": 0,
                "total": 0
            },
            "planCacheListPlans": {
                "failed": 0,
                "total": 0
            },
            "planCacheListQueryShapes": {
                "failed": 0,
                "total": 0
            },
            "planCacheSetFilter": {
                "failed": 0,
                "total": 0
            },
            "prepareTransaction": {
                "failed": 0,
                "total": 0
            },
            "profile": {
                "failed": 0,
                "total": 0
            },
            "reIndex": {
                "failed": 0,
                "total": 0
            },
            "refreshSessions": {
                "failed": 0,
                "total": 0
            },
            "renameCollection": {
                "failed": 0,
                "total": 0
            },
            "repairCursor": {
                "failed": 0,
                "total": 0
            },
            "repairDatabase": {
                "failed": 0,
                "total": 0
            },
            "replSetAbortPrimaryCatchUp": {
                "failed": 0,
                "total": 0
            },
            "replSetFreeze": {
                "failed": 0,
                "total": 0
            },
            "replSetGetConfig": {
                "failed": 0,
                "total": 0
            },
            "replSetGetRBID": {
                "failed": 0,
                "total": 0
            },
            "replSetGetStatus": {
                "failed": 0,
                "total": 0
            },
            "replSetHeartbeat": {
                "failed": 0,
                "total": 0
            },
            "replSetInitiate": {
                "failed": 0,
                "total": 0
            },
            "replSetMaintenance": {
                "failed": 0,
                "total": 0
            },
            "replSetReconfig": {
                "failed": 0,
                "total": 0
            },
            "replSetRequestVotes": {
                "failed": 0,
                "total": 0
            },
            "replSetResizeOplog": {
                "failed": 0,
                "total": 0
            },
            "replSetStepDown": {
                "failed": 0,
                "total": 0
            },
            "replSetStepDownWithForce": {
                "failed": 0,
                "total": 0
            },
            "replSetStepUp": {
                "failed": 0,
                "total": 0
            },
            "replSetSyncFrom": {
                "failed": 0,
                "total": 0
            },
            "replSetUpdatePosition": {
                "failed": 0,
                "total": 0
            },
            "resetError": {
                "failed": 0,
                "total": 0
            },
            "revokePrivilegesFromRole": {
                "failed": 0,
                "total": 0
            },
            "revokeRolesFromRole": {
                "failed": 0,
                "total": 0
            },
            "revokeRolesFromUser": {
                "failed": 0,
                "total": 0
            },
            "rolesInfo": {
                "failed": 0,
                "total": 0
            },
            "saslContinue": {
                "failed": 0,
                "total": 0
            },
            "saslStart": {
                "failed": 0,
                "total": 0
            },
            "serverStatus": {
                "failed": 0,
                "total": 1
            },
            "setFeatureCompatibilityVersion": {
                "failed": 0,
                "total": 0
            },
            "setFreeMonitoring": {
                "failed": 0,
                "total": 0
            },
            "setIndexCommitQuorum": {
                "failed": 0,
                "total": 0
            },
            "setParameter": {
                "failed": 0,
                "total": 0
            },
            "setShardVersion": {
                "failed": 0,
                "total": 0
            },
            "shardConnPoolStats": {
                "failed": 0,
                "total": 0
            },
            "shardingState": {
                "failed": 0,
                "total": 0
            },
            "shutdown": {
                "failed": 0,
                "total": 0
            },
            "splitChunk": {
                "failed": 0,
                "total": 0
            },
            "splitVector": {
                "failed": 0,
                "total": 0
            },
            "startRecordingTraffic": {
                "failed": 0,
                "total": 0
            },
            "startSession": {
                "failed": 0,
                "total": 0
            },
            "stopRecordingTraffic": {
                "failed": 0,
                "total": 0
            },
            "top": {
                "failed": 0,
                "total": 0
            },
            "touch": {
                "failed": 0,
                "total": 0
            },
            "unsetSharding": {
                "failed": 0,
                "total": 0
            },
            "update": {
                "failed": 0,
                "total": 0
            },
            "updateRole": {
                "failed": 0,
                "total": 0
            },
            "updateUser": {
                "failed": 0,
                "total": 0
            },
            "usersInfo": {
                "failed": 0,
                "total": 0
            },
            "validate": {
                "failed": 0,
                "total": 0
            },
            "voteCommitIndexBuild": {
                "failed": 0,
                "total": 0
            },
            "waitForFailPoint": {
                "failed": 0,
                "total": 0
            },
            "whatsmyuri": {
                "failed": 0,
                "total": 0
            }
        },
        "cursor": {
            "open": {
                "noTimeout": 0,
                "pinned": 0,
                "total": 0
            },
            "timedOut": 0
        },
        "document": {
            "deleted": 0,
            "inserted": 0,
            "returned": 10,
            "updated": 0
        },
        "getLastError": {
            "wtime": {
                "num": 0,
                "totalMillis": 0
            },
            "wtimeouts": 0
        },
        "operation": {
            "scanAndOrder": 3,
            "writeConflicts": 0
        },
        "query": {
            "planCacheTotalSizeEstimateBytes": 0,
            "updateOneOpStyleBroadcastWithExactIDCount": 0
        },
        "queryExecutor": {
            "scanned": 0,
            "scannedObjects": 10
        },
        "record": {
            "moves": 0
        },
        "repl": {
            "apply": {
                "attemptsToBecomeSecondary": 1,
                "batchSize": 3,
                "batches": {
                    "num": 1,
                    "totalMillis": 18
                },
                "ops": 3
            },
            "buffer": {
                "count": 0,
                "maxSizeBytes": 268435456,
                "sizeBytes": 0
            },
            "executor": {
                "networkInterface": "DEPRECATED: getDiagnosticString is deprecated in NetworkInterfaceTL",
                "pool": {
                    "inProgressCount": 0
                },
                "queues": {
                    "networkInProgress": 0,
                    "sleepers": 0
                },
                "shuttingDown": false,
                "unsignaledEvents": 0
            },
            "initialSync": {
                "completed": 0,
                "failedAttempts": 0,
                "failures": 0
            },
            "network": {
                "bytes": 0,
                "getmores": {
                    "num": 0,
                    "totalMillis": 0
                },
                "notMasterLegacyUnacknowledgedWrites": 0,
                "notMasterUnacknowledgedWrites": 0,
                "ops": 0,
                "readersCreated": 0
            },
            "stepDown": {
                "userOperationsKilled": 0,
                "userOperationsRunning": 0
            }
        },
        "ttl": {
            "deletedDocuments": 0,
            "passes": 0
        }
    },
    "network": {
        "bytesIn": 2014,
        "bytesOut": 5370,
        "compression": {
            "snappy": {
                "compressor": {
                    "bytesIn": 2034,
                    "bytesOut": 1638
                },
                "decompressor": {
                    "bytesIn": 1638,
                    "bytesOut": 2034
                }
            },
            "zlib": {
                "compressor": {
                    "bytesIn": 0,
                    "bytesOut": 0
                },
                "decompressor": {
                    "bytesIn": 0,
                    "bytesOut": 0
                }
            },
            "zstd": {
                "compressor": {
                    "bytesIn": 0,
                    "bytesOut": 0
                },
                "decompressor": {
                    "bytesIn": 0,
                    "bytesOut": 0
                }
            }
        },
        "numRequests": 9,
        "physicalBytesIn": 2044,
        "physicalBytesOut": 4998,
        "serviceExecutorTaskStats": {
            "executor": "passthrough",
            "threadsRunning": 5
        }
    },
    "ok": 1.0,
    "opLatencies": {
        "commands": {
            "latency": 362,
            "ops": 8
        },
        "reads": {
            "latency": 0,
            "ops": 0
        },
        "transactions": {
            "latency": 0,
            "ops": 0
        },
        "writes": {
            "latency": 0,
            "ops": 0
        }
    },
    "opReadConcernCounters": {
        "available": 0,
        "linearizable": 0,
        "local": 0,
        "majority": 0,
        "none": 8,
        "snapshot": 0
    },
    "opcounters": {
        "command": 11,
        "delete": 0,
        "getmore": 0,
        "insert": 0,
        "query": 8,
        "update": 0
    },
    "opcountersRepl": {
        "command": 0,
        "delete": 0,
        "getmore": 0,
        "insert": 0,
        "query": 0,
        "update": 0
    },
    "operationTime": {
        "$timestamp": {
            "i": 1,
            "t": 1584383606
        }
    },
    "oplogTruncation": {
        "processingMethod": "sampling",
        "totalTimeProcessingMicros": 1294,
        "totalTimeTruncatingMicros": 0,
        "truncateCount": 0
    },
    "pid": 4074,
    "process": "mongod",
    "repl": {
        "electionId": {
            "$oid": "7fffffff0000000000000027"
        },
        "hosts": [
            "127.0.0.1:27017"
        ],
        "ismaster": true,
        "lastWrite": {
            "lastWriteDate": {
                "$date": 1584383606000
            },
            "majorityOpTime": {
                "t": 39,
                "ts": {
                    "$timestamp": {
                        "i": 1,
                        "t": 1584383606
                    }
                }
            },
            "majorityWriteDate": {
                "$date": 1584383606000
            },
            "opTime": {
                "t": 39,
                "ts": {
                    "$timestamp": {
                        "i": 1,
                        "t": 1584383606
                    }
                }
            }
        },
        "me": "127.0.0.1:27017",
        "primary": "127.0.0.1:27017",
        "rbid": 1,
        "secondary": false,
        "setName": "rs0",
        "setVersion": 1
    },
    "storageEngine": {
        "backupCursorOpen": false,
        "dropPendingIdents": 0,
        "name": "wiredTiger",
        "oldestRequiredTimestampForCrashRecovery": {
            "$timestamp": {
                "i": 0,
                "t": 0
            }
        },
        "persistent": true,
        "readOnly": false,
        "supportsCommittedReads": true,
        "supportsPendingDrops": true,
        "supportsSnapshotReadConcern": true
    },
    "tcmalloc": {
        "generic": {
            "current_allocated_bytes": 99523376,
            "heap_size": 113229824
        },
        "tcmalloc": {
            "aggressive_memory_decommit": 0,
            "central_cache_free_bytes": 238176,
            "current_total_thread_cache_bytes": 871216,
            "formattedString": "------------------------------------------------\nMALLOC:       99523952 (   94.9 MiB) Bytes in use by application\nMALLOC: +     12488704 (   11.9 MiB) Bytes in page heap freelist\nMALLOC: +       238176 (    0.2 MiB) Bytes in central cache freelist\nMALLOC: +       108352 (    0.1 MiB) Bytes in transfer cache freelist\nMALLOC: +       870640 (    0.8 MiB) Bytes in thread cache freelists\nMALLOC: +      2883584 (    2.8 MiB) Bytes in malloc metadata\nMALLOC:   ------------\nMALLOC: =    116113408 (  110.7 MiB) Actual memory used (physical + swap)\nMALLOC: +            0 (    0.0 MiB) Bytes released to OS (aka unmapped)\nMALLOC:   ------------\nMALLOC: =    116113408 (  110.7 MiB) Virtual address space used\nMALLOC:\nMALLOC:            711              Spans in use\nMALLOC:             65              Thread heaps in use\nMALLOC:           4096              Tcmalloc page size\n------------------------------------------------\nCall ReleaseFreeMemory() to release freelist memory to the OS (via madvise()).\nBytes released to the OS take up virtual address space but no physical memory.\n",
            "max_total_thread_cache_bytes": 516947968,
            "pageheap_commit_count": 66,
            "pageheap_committed_bytes": 113229824,
            "pageheap_decommit_count": 0,
            "pageheap_free_bytes": 12488704,
            "pageheap_reserve_count": 66,
            "pageheap_scavenge_count": 0,
            "pageheap_total_commit_bytes": 113229824,
            "pageheap_total_decommit_bytes": 0,
            "pageheap_total_reserve_bytes": 113229824,
            "pageheap_unmapped_bytes": 0,
            "spinlock_total_delay_ns": 0,
            "thread_cache_free_bytes": 871216,
            "total_free_bytes": 1217744,
            "transfer_cache_free_bytes": 108352
        }
    },
    "trafficRecording": {
        "running": false
    },
    "transactions": {
        "currentActive": 0,
        "currentInactive": 0,
        "currentOpen": 0,
        "currentPrepared": 0,
        "retriedCommandsCount": 0,
        "retriedStatementsCount": 0,
        "totalAborted": 0,
        "totalCommitted": 0,
        "totalPrepared": 0,
        "totalPreparedThenAborted": 0,
        "totalPreparedThenCommitted": 0,
        "totalStarted": 0,
        "transactionsCollectionWriteCount": 0
    },
    "transportSecurity": {
        "1.0": 0,
        "1.1": 0,
        "1.2": 0,
        "1.3": 0,
        "unknown": 0
    },
    "twoPhaseCommitCoordinator": {
        "currentInSteps": {
            "deletingCoordinatorDoc": 0,
            "waitingForDecisionAcks": 0,
            "waitingForVotes": 0,
            "writingDecision": 0,
            "writingParticipantList": 0
        },
        "totalAbortedTwoPhaseCommit": 0,
        "totalCommittedTwoPhaseCommit": 0,
        "totalCreated": 0,
        "totalStartedTwoPhaseCommit": 0
    },
    "uptime": 16.0,
    "uptimeEstimate": 16,
    "uptimeMillis": 16185,
    "version": "4.2.2",
    "wiredTiger": {
        "async": {
            "current work queue length": 0,
            "maximum work queue length": 0,
            "number of allocation state races": 0,
            "number of flush calls": 0,
            "number of operation slots viewed for allocation": 0,
            "number of times operation allocation failed": 0,
            "number of times worker found no work": 0,
            "total allocations": 0,
            "total compact calls": 0,
            "total insert calls": 0,
            "total remove calls": 0,
            "total search calls": 0,
            "total update calls": 0
        },
        "block-manager": {
            "blocks pre-loaded": 56,
            "blocks read": 50,
            "blocks written": 13,
            "bytes read": 282624,
            "bytes written": 102400,
            "bytes written for checkpoint": 102400,
            "mapped blocks read": 0,
            "mapped bytes read": 0
        },
        "cache": {
            "application threads page read from disk to cache count": 13,
            "application threads page read from disk to cache time (usecs)": 5577,
            "application threads page write from cache to disk count": 0,
            "application threads page write from cache to disk time (usecs)": 0,
            "bytes belonging to page images in the cache": 461190,
            "bytes belonging to the cache overflow table in the cache": 182,
            "bytes currently in the cache": 514773,
            "bytes dirty in the cache cumulative": 404742,
            "bytes not belonging to page images in the cache": 53583,
            "bytes read into cache": 427028,
            "bytes written from cache": 145416,
            "cache overflow cursor application thread wait time (usecs)": 0,
            "cache overflow cursor internal thread wait time (usecs)": 0,
            "cache overflow score": 0,
            "cache overflow table entries": 0,
            "cache overflow table insert calls": 0,
            "cache overflow table max on-disk size": 0,
            "cache overflow table on-disk size": 0,
            "cache overflow table remove calls": 0,
            "checkpoint blocked page eviction": 0,
            "eviction calls to get a page": 6,
            "eviction calls to get a page found queue empty": 6,
            "eviction calls to get a page found queue empty after locking": 0,
            "eviction currently operating in aggressive mode": 0,
            "eviction empty score": 0,
            "eviction passes of a file": 0,
            "eviction server candidate queue empty when topping up": 0,
            "eviction server candidate queue not empty when topping up": 0,
            "eviction server evicting pages": 0,
            "eviction server slept, because we did not make progress with eviction": 0,
            "eviction server unable to reach eviction goal": 0,
            "eviction server waiting for a leaf page": 41,
            "eviction state": 128,
            "eviction walk target pages histogram - 0-9": 0,
            "eviction walk target pages histogram - 10-31": 0,
            "eviction walk target pages histogram - 128 and higher": 0,
            "eviction walk target pages histogram - 32-63": 0,
            "eviction walk target pages histogram - 64-128": 0,
            "eviction walk target strategy both clean and dirty pages": 0,
            "eviction walk target strategy only clean pages": 0,
            "eviction walk target strategy only dirty pages": 0,
            "eviction walks abandoned": 0,
            "eviction walks gave up because they restarted their walk twice": 0,
            "eviction walks gave up because they saw too many pages and found no candidates": 0,
            "eviction walks gave up because they saw too many pages and found too few candidates": 0,
            "eviction walks reached end of tree": 0,
            "eviction walks started from root of tree": 0,
            "eviction walks started from saved location in tree": 0,
            "eviction worker thread active": 4,
            "eviction worker thread created": 0,
            "eviction worker thread evicting pages": 0,
            "eviction worker thread removed": 0,
            "eviction worker thread stable number": 0,
            "files with active eviction walks": 0,
            "files with new eviction walks started": 0,
            "force re-tuning of eviction workers once in a while": 0,
            "forced eviction - pages evicted that were clean count": 0,
            "forced eviction - pages evicted that were clean time (usecs)": 0,
            "forced eviction - pages evicted that were dirty count": 0,
            "forced eviction - pages evicted that were dirty time (usecs)": 0,
            "forced eviction - pages selected because of too many deleted items count": 0,
            "forced eviction - pages selected count": 0,
            "forced eviction - pages selected unable to be evicted count": 0,
            "forced eviction - pages selected unable to be evicted time": 0,
            "hazard pointer blocked page eviction": 0,
            "hazard pointer check calls": 0,
            "hazard pointer check entries walked": 0,
            "hazard pointer maximum array length": 0,
            "in-memory page passed criteria to be split": 0,
            "in-memory page splits": 0,
            "internal pages evicted": 0,
            "internal pages queued for eviction": 0,
            "internal pages seen by eviction walk": 0,
            "internal pages seen by eviction walk that are already queued": 0,
            "internal pages split during eviction": 0,
            "leaf pages split during eviction": 0,
            "maximum bytes configured": 1530920960.0,
            "maximum page size at eviction": 0,
            "modified pages evicted": 0,
            "modified pages evicted by application threads": 0,
            "operations timed out waiting for space in cache": 0,
            "overflow pages read into cache": 0,
            "page split during eviction deepened the tree": 0,
            "page written requiring cache overflow records": 0,
            "pages currently held in the cache": 37,
            "pages evicted by application threads": 0,
            "pages queued for eviction": 0,
            "pages queued for eviction post lru sorting": 0,
            "pages queued for urgent eviction": 0,
            "pages queued for urgent eviction during walk": 0,
            "pages read into cache": 31,
            "pages read into cache after truncate": 2,
            "pages read into cache after truncate in prepare state": 0,
            "pages read into cache requiring cache overflow entries": 0,
            "pages read into cache requiring cache overflow for checkpoint": 0,
            "pages read into cache skipping older cache overflow entries": 0,
            "pages read into cache with skipped cache overflow entries needed later": 0,
            "pages read into cache with skipped cache overflow entries needed later by checkpoint": 0,
            "pages requested from the cache": 636,
            "pages seen by eviction walk": 0,
            "pages seen by eviction walk that are already queued": 0,
            "pages selected for eviction unable to be evicted": 0,
            "pages selected for eviction unable to be evicted as the parent page has overflow items": 0,
            "pages selected for eviction unable to be evicted because of active children on an internal page": 0,
            "pages selected for eviction unable to be evicted because of failure in reconciliation": 0,
            "pages selected for eviction unable to be evicted due to newer modifications on a clean page": 0,
            "pages walked for eviction": 0,
            "pages written from cache": 7,
            "pages written requiring in-memory restoration": 0,
            "percentage overhead": 8,
            "tracked bytes belonging to internal pages in the cache": 7877,
            "tracked bytes belonging to leaf pages in the cache": 506896,
            "tracked dirty bytes in the cache": 282602,
            "tracked dirty pages in the cache": 9,
            "unmodified pages evicted": 0
        },
        "capacity": {
            "background fsync file handles considered": 0,
            "background fsync file handles synced": 0,
            "background fsync time (msecs)": 0,
            "bytes read": 204800,
            "bytes written for checkpoint": 58614,
            "bytes written for eviction": 0,
            "bytes written for log": 831792000,
            "bytes written total": 831850614,
            "threshold to call fsync": 0,
            "time waiting due to total capacity (usecs)": 0,
            "time waiting during checkpoint (usecs)": 0,
            "time waiting during eviction (usecs)": 0,
            "time waiting during logging (usecs)": 0,
            "time waiting during read (usecs)": 0
        },
        "concurrentTransactions": {
            "read": {
                "available": 127,
                "out": 1,
                "totalTickets": 128
            },
            "write": {
                "available": 128,
                "out": 0,
                "totalTickets": 128
            }
        },
        "connection": {
            "auto adjusting condition resets": 17,
            "auto adjusting condition wait calls": 128,
            "detected system time went backwards": 0,
            "files currently open": 21,
            "memory allocations": 6491,
            "memory frees": 5103,
            "memory re-allocations": 507,
            "pthread mutex condition wait calls": 293,
            "pthread mutex shared lock read-lock calls": 835,
            "pthread mutex shared lock write-lock calls": 192,
            "total fsync I/Os": 22,
            "total read I/Os": 918,
            "total write I/Os": 26
        },
        "cursor": {
            "cached cursor count": 30,
            "cursor bulk loaded cursor insert calls": 0,
            "cursor close calls that result in cache": 68,
            "cursor create calls": 202,
            "cursor insert calls": 19,
            "cursor insert key and value bytes": 9214,
            "cursor modify calls": 0,
            "cursor modify key and value bytes affected": 0,
            "cursor modify value bytes modified": 0,
            "cursor next calls": 352,
            "cursor operation restarted": 0,
            "cursor prev calls": 11,
            "cursor remove calls": 1,
            "cursor remove key bytes removed": 22,
            "cursor reserve calls": 0,
            "cursor reset calls": 661,
            "cursor search calls": 556,
            "cursor search near calls": 18,
            "cursor sweep buckets": 12,
            "cursor sweep cursors closed": 0,
            "cursor sweep cursors examined": 0,
            "cursor sweeps": 2,
            "cursor truncate calls": 0,
            "cursor update calls": 0,
            "cursor update key and value bytes": 0,
            "cursor update value size change": 0,
            "cursors reused from cache": 36,
            "open cursor count": 25
        },
        "data-handle": {
            "connection data handle size": 432,
            "connection data handles currently active": 34,
            "connection sweep candidate became referenced": 0,
            "connection sweep dhandles closed": 0,
            "connection sweep dhandles removed from hash list": 2,
            "connection sweep time-of-death sets": 32,
            "connection sweeps": 1,
            "session dhandles swept": 0,
            "session sweep attempts": 50
        },
        "lock": {
            "checkpoint lock acquisitions": 1,
            "checkpoint lock application thread wait time (usecs)": 0,
            "checkpoint lock internal thread wait time (usecs)": 0,
            "dhandle lock application thread time waiting (usecs)": 0,
            "dhandle lock internal thread time waiting (usecs)": 0,
            "dhandle read lock acquisitions": 84,
            "dhandle write lock acquisitions": 38,
            "durable timestamp queue lock application thread time waiting (usecs)": 0,
            "durable timestamp queue lock internal thread time waiting (usecs)": 0,
            "durable timestamp queue read lock acquisitions": 0,
            "durable timestamp queue write lock acquisitions": 4,
            "metadata lock acquisitions": 1,
            "metadata lock application thread wait time (usecs)": 0,
            "metadata lock internal thread wait time (usecs)": 0,
            "read timestamp queue lock application thread time waiting (usecs)": 0,
            "read timestamp queue lock internal thread time waiting (usecs)": 0,
            "read timestamp queue read lock acquisitions": 0,
            "read timestamp queue write lock acquisitions": 5,
            "schema lock acquisitions": 37,
            "schema lock application thread wait time (usecs)": 0,
            "schema lock internal thread wait time (usecs)": 0,
            "table lock application thread time waiting for the table lock (usecs)": 0,
            "table lock internal thread time waiting for the table lock (usecs)": 0,
            "table read lock acquisitions": 0,
            "table write lock acquisitions": 33,
            "txn global lock application thread time waiting (usecs)": 0,
            "txn global lock internal thread time waiting (usecs)": 0,
            "txn global read lock acquisitions": 19,
            "txn global write lock acquisitions": 19
        },
        "log": {
            "busy returns attempting to switch slots": 0,
            "force archive time sleeping (usecs)": 0,
            "log bytes of payload data": 2648,
            "log bytes written": 4096,
            "log files manually zero-filled": 0,
            "log flush operations": 153,
            "log force write operations": 178,
            "log force write operations skipped": 174,
            "log records compressed": 2,
            "log records not compressed": 2,
            "log records too small to compress": 6,
            "log release advances write LSN": 3,
            "log scan operations": 4,
            "log scan records requiring two reads": 9,
            "log server thread advances write LSN": 4,
            "log server thread write LSN walk skipped": 1015,
            "log sync operations": 7,
            "log sync time duration (usecs)": 55514,
            "log sync_dir operations": 1,
            "log sync_dir time duration (usecs)": 2388,
            "log write operations": 10,
            "logging bytes consolidated": 3584,
            "maximum log file size": 104857600,
            "number of pre-allocated log files to create": 2,
            "pre-allocated log files not ready and missed": 1,
            "pre-allocated log files prepared": 2,
            "pre-allocated log files used": 0,
            "records processed by log scan": 20,
            "slot close lost race": 0,
            "slot close unbuffered waits": 0,
            "slot closures": 7,
            "slot join atomic update races": 0,
            "slot join calls atomic updates raced": 0,
            "slot join calls did not yield": 10,
            "slot join calls found active slot closed": 0,
            "slot join calls slept": 0,
            "slot join calls yielded": 0,
            "slot join found active slot closed": 0,
            "slot joins yield time (usecs)": 0,
            "slot transitions unable to find free slot": 0,
            "slot unbuffered writes": 0,
            "total in-memory size of compressed records": 2724,
            "total log buffer size": 33554432,
            "total size of compressed records": 2161,
            "written slots coalesced": 0,
            "yields waiting for previous log file close": 0
        },
        "perf": {
            "file system read latency histogram (bucket 1) - 10-49ms": 0,
            "file system read latency histogram (bucket 2) - 50-99ms": 0,
            "file system read latency histogram (bucket 3) - 100-249ms": 0,
            "file system read latency histogram (bucket 4) - 250-499ms": 0,
            "file system read latency histogram (bucket 5) - 500-999ms": 0,
            "file system read latency histogram (bucket 6) - 1000ms+": 0,
            "file system write latency histogram (bucket 1) - 10-49ms": 0,
            "file system write latency histogram (bucket 2) - 50-99ms": 0,
            "file system write latency histogram (bucket 3) - 100-249ms": 0,
            "file system write latency histogram (bucket 4) - 250-499ms": 0,
            "file system write latency histogram (bucket 5) - 500-999ms": 0,
            "file system write latency histogram (bucket 6) - 1000ms+": 0,
            "operation read latency histogram (bucket 1) - 100-249us": 1,
            "operation read latency histogram (bucket 2) - 250-499us": 0,
            "operation read latency histogram (bucket 3) - 500-999us": 0,
            "operation read latency histogram (bucket 4) - 1000-9999us": 0,
            "operation read latency histogram (bucket 5) - 10000us+": 0,
            "operation write latency histogram (bucket 1) - 100-249us": 0,
            "operation write latency histogram (bucket 2) - 250-499us": 2,
            "operation write latency histogram (bucket 3) - 500-999us": 2,
            "operation write latency histogram (bucket 4) - 1000-9999us": 0,
            "operation write latency histogram (bucket 5) - 10000us+": 0
        },
        "reconciliation": {
            "fast-path pages deleted": 0,
            "page reconciliation calls": 7,
            "page reconciliation calls for eviction": 0,
            "pages deleted": 0,
            "split bytes currently awaiting free": 0,
            "split objects currently awaiting free": 0
        },
        "session": {
            "open session count": 21,
            "session query timestamp calls": 0,
            "table alter failed calls": 0,
            "table alter successful calls": 0,
            "table alter unchanged and skipped": 0,
            "table compact failed calls": 0,
            "table compact successful calls": 0,
            "table create failed calls": 0,
            "table create successful calls": 1,
            "table drop failed calls": 0,
            "table drop successful calls": 0,
            "table import failed calls": 0,
            "table import successful calls": 0,
            "table rebalance failed calls": 0,
            "table rebalance successful calls": 0,
            "table rename failed calls": 0,
            "table rename successful calls": 0,
            "table salvage failed calls": 0,
            "table salvage successful calls": 0,
            "table truncate failed calls": 0,
            "table truncate successful calls": 0,
            "table verify failed calls": 0,
            "table verify successful calls": 0
        },
        "snapshot-window-settings": {
            "cache pressure percentage threshold": 95,
            "current available snapshots window size in seconds": 5,
            "current cache pressure percentage": 0,
            "latest majority snapshot timestamp available": "Mar 16 15:33:26:1",
            "max target available snapshots window size in seconds": 5,
            "oldest majority snapshot timestamp available": "Mar 16 15:33:21:1",
            "target available snapshots window size in seconds": 5,
            "total number of SnapshotTooOld errors": 0
        },
        "thread-state": {
            "active filesystem fsync calls": 0,
            "active filesystem read calls": 0,
            "active filesystem write calls": 0
        },
        "thread-yield": {
            "application thread time evicting (usecs)": 0,
            "application thread time waiting for cache (usecs)": 0,
            "connection close blocked waiting for transaction state stabilization": 0,
            "connection close yielded for lsm manager shutdown": 0,
            "data handle lock yielded": 0,
            "get reference for page index and slot time sleeping (usecs)": 0,
            "log server sync yielded for log write": 0,
            "page access yielded due to prepare state change": 0,
            "page acquire busy blocked": 0,
            "page acquire eviction blocked": 0,
            "page acquire locked blocked": 0,
            "page acquire read blocked": 0,
            "page acquire time sleeping (usecs)": 0,
            "page delete rollback time sleeping for state change (usecs)": 0,
            "page reconciliation yielded due to child modification": 0
        },
        "transaction": {
            "Number of prepared updates": 0,
            "Number of prepared updates added to cache overflow": 0,
            "durable timestamp queue entries walked": 2,
            "durable timestamp queue insert to empty": 2,
            "durable timestamp queue inserts to head": 2,
            "durable timestamp queue inserts total": 4,
            "durable timestamp queue length": 1,
            "number of named snapshots created": 0,
            "number of named snapshots dropped": 0,
            "prepared transactions": 0,
            "prepared transactions committed": 0,
            "prepared transactions currently active": 0,
            "prepared transactions rolled back": 0,
            "query timestamp calls": 53,
            "read timestamp queue entries walked": 3,
            "read timestamp queue insert to empty": 2,
            "read timestamp queue inserts to head": 3,
            "read timestamp queue inserts total": 5,
            "read timestamp queue length": 1,
            "rollback to stable calls": 0,
            "rollback to stable updates aborted": 0,
            "rollback to stable updates removed from cache overflow": 0,
            "set timestamp calls": 6,
            "set timestamp durable calls": 0,
            "set timestamp durable updates": 0,
            "set timestamp oldest calls": 3,
            "set timestamp oldest updates": 3,
            "set timestamp stable calls": 3,
            "set timestamp stable updates": 3,
            "transaction begins": 75,
            "transaction checkpoint currently running": 0,
            "transaction checkpoint generation": 2,
            "transaction checkpoint max time (msecs)": 29,
            "transaction checkpoint min time (msecs)": 29,
            "transaction checkpoint most recent time (msecs)": 29,
            "transaction checkpoint scrub dirty target": 0,
            "transaction checkpoint scrub time (msecs)": 0,
            "transaction checkpoint total time (msecs)": 29,
            "transaction checkpoints": 1,
            "transaction checkpoints skipped because database was clean": 0,
            "transaction failures due to cache overflow": 0,
            "transaction fsync calls for checkpoint after allocating the transaction ID": 1,
            "transaction fsync duration for checkpoint after allocating the transaction ID (usecs)": 7736,
            "transaction range of IDs currently pinned": 0,
            "transaction range of IDs currently pinned by a checkpoint": 0,
            "transaction range of IDs currently pinned by named snapshots": 0,
            "transaction range of timestamps currently pinned": 21474836480.0,
            "transaction range of timestamps pinned by a checkpoint": 6804875772088549377,
            "transaction range of timestamps pinned by the oldest active read timestamp": 0,
            "transaction range of timestamps pinned by the oldest timestamp": 21474836480.0,
            "transaction read timestamp of the oldest active reader": 0,
            "transaction sync calls": 0,
            "transactions committed": 7,
            "transactions rolled back": 68,
            "update conflicts": 0
        },
        "uri": "statistics:"
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
