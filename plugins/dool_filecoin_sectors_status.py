
from websocket import create_connection
import json
class  dstat_plugin(dstat):
     """
     Total Number of processes on this system.
     """
     def  __init__( self ):
         self .id = 'filecoin-sectors-status'
         self .type  =  's'

         self .name    =  'filecoin-sectors-status'
         self .nick  = ( 'SectorID', 'State')
         self .width  =  5
         self .scale  =  1000
         self .vars    =  ( 'total' ,'work')
 
     def  extract( self ): 
         self .data = self.lotusMinerSectorsList()
         self .vars = list(map(lambda e:e["SectorID"],self.data))
         self .name = []
         for name in self.vars:
             self .name.append('sectors' + str(name) + ' state')

         self .val = {}
         list(map(lambda e:self .val.setdefault(e["SectorID"],[str(e["SectorID"]),e["State"]]),self.data))

     def websocket(self,message):
         ws = create_connection("ws://192.168.10.102:2345/rpc/v0")
         # ws = websocket.create_connection("ws://192.168.10.102:2345/rpc/v0")
         ws.send(message)
         return ws.recv()

     def lotusMinerSectorsList(self):
        data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "Filecoin.SectorsList",
            "params": [],
            "meta": {
            }
        }
        res = self.websocket(json.dumps(data))
        res_json = json.loads(res)
        res_json_list = res_json["result"]
        res_list = list(map(self.lotusMinerSectorsInfo,res_json_list))
        return res_list

     def lotusMinerSectorsInfo(self,i):
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
         res = self.websocket(json.dumps(data))
         res_json = json.loads(res)
         return res_json["result"]
