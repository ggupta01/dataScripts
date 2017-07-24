from pprint import pprint
import json,sys,logging
import pdb

#pdb.set_trace()
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

ancestor_count = 0

global_tag = '';
def filterJson(d_key,d_value,d_type="dict",list_nm=""):
        global global_tag , ancestor_count
        if d_type == "dict":
                for key, value in d_value.items():
                        #print key,"====",value
                        if type(value) == dict:
                                key = d_key+"/"+key if d_key != "" else key
                                filterJson(key,value,"dict",d_key)
                        elif type(value) == list:
                                filterJson(key,value,"list")
                        else:
                                # Here i will check the keywords and print their respective value
                                #print key+","+str(value) if d_key == "" else d_key+"/"+str(key)+","+str(value) if list_nm != "" else d_key+"/"+str(key)+","+str(value)
                                print key if d_key == "" else d_key+"/"+str(key) if list_nm != "" else d_key+"/"+str(key)

        elif d_type == "list":
                for eachItem in d_value:
                        if type(eachItem) == dict:
                                filterJson(d_key,eachItem)
                        elif type(eachItem) == list:
                                filterJson(d_key,eachItem,"list",d_key)
                        else:
                                print d_key                                                     # To print keys only.

#file = raw_input("file name? ")

with open("../20170718.json") as f:
        for line in f:
                jdata = json.loads(line)
                jdata_type = type(jdata)
                if jdata_type == list:
                        filterJson("",jdata,"list")
                elif jdata_type == dict:
                        filterJson("",jdata)
                else:
                        print jdata
