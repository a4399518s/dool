from websocket import create_connection
import json

def websocket(message):
    ws = create_connection("ws://192.168.10.102:2345/rpc/v0")
    # ws = websocket.create_connection("ws://192.168.10.102:2345/rpc/v0")
    ws.send(message)
    return ws.recv()

def lotusMinerSectorsList():
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "Filecoin.SectorsList",
        "params": [],
        "meta": {
        }
    }
    res = websocket(json.dumps(data))
    res_json = json.loads(res)
    res_json_list = res_json["result"]
    res_list = list(map(lotusMinerSectorsInfo,res_json_list))
    return res_list

def lotusMinerSectorsInfo(i):
    data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "Filecoin.SectorsStatus",
        "params": [
            i,
            True
        ],
        "meta": {
        }
    }
    res = websocket(json.dumps(data))
    res_json = json.loads(res)
    return res_json["result"]

class  dstat_plugin(dstat):
     """
     Total Number of processes on this system.
     """
     def  __init__( self ):
         self .name    =  'filecoin-sectors-status'
         self .type  =  'd'
         self .width  =  4
         self .scale  =  10
         self .vars    =  ( 'total' ,'work')
 
     def  extract( self ): 
         self .val[ 'total' ]  =  len (glob.glob( '/proc/[0-9]*' ))
         self .val[ 'work' ]  =  len (glob.glob( '/proc/[0-9]*' ))
         self .val[ 'ccc' ]  =  "cc"