from __future__ import print_function
import python_jsonschema_objects as pjs
import os
import errno
import json
import uuid
from random import randrange, randint
from DatetimeClass import DatetimeClass
import argparse
import jsonschema
from datetime import datetime

class CTRDataGenerator(object): 
    MAX_DTC_instance = 1
    curr_DTC_instance = 0
    datetime = None
    
    def __new__(cls,*args):
        if cls.curr_DTC_instance <= cls.MAX_DTC_instance:
            cls.curr_DTC_instance += 1
        if cls.curr_DTC_instance == 1:
            cls.datetime = DatetimeClass(args[2], args[3], args[4])
        return super().__new__(cls)
    
    def __init__(self, schemafile, size, startdate, enddate, timeformat, outputfile):
        self.schema = self.readJsonSchema(schemafile)
        self.size = size
        self.outputfile = outputfile
        self.timeformat = timeformat
    
    def readJsonSchema(self, filename):
        if os.path.exists(filename):
            try:
                with open(filename,'r') as f:
                    schema = json.load(f)
            except IOError:
                print("File " + filename + "could not be read")
                
        else:
            raise FileNotFoundError("File " + filename + " not found or insufficient access permission")
        return schema

    def generate(self):
        builder = pjs.ObjectBuilder(self.schema)
        ns = builder.build_classes()
        CTR = ns.CtrSchema
        i = 0
        CTRList = {}
        CTRList['ctrs'] = []
        while (i<self.size):
            seed=randint(0,100)
            ct = CTRDataGenerator.datetime.generate_random_datetime(seed)
            CTR_i = CTR(id=uuid.uuid4().hex, click_percent=randrange(0,100), click_time=ct.strftime(self.timeformat))
            s_ctr_i = '{"id":"'+ str(CTR_i.id) +'","click_percent":'+ str(CTR_i.click_percent) +',"click_time":"' + CTR_i.click_time + '"}'
            CTRList['ctrs'].append(json.loads(s_ctr_i))
            i = i+1
        
        
        outfile = self.outputfile
        if not os.path.exists(os.path.dirname(outfile)):
            try:
                os.makedirs(os.path.dirname(outfile))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        try:
            with open(outfile, "w") as f:
                json.dump(CTRList, f, indent=4, separators=(',',': '), sort_keys=True)
            f.close()    
        except IOError:
            print("File " + outfile + "could not be written")

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description = 'Parameters to generate CTR data <schemafile> <size> <startdate> <enddate> <timeformat> <outputfile>')
    parser.add_argument('schemafile', help='Relative path of the JSON schema file', nargs='?', const=1, default='..\\schema\\CTR_Schema.json')
    parser.add_argument('size', help='Size of the dataset (to be generated)', nargs='?', const=1, default=10, type=int)
    parser.add_argument('startdate', help='Start date range (for timestamps to be generated)', nargs='?', const=1, default='1/1/2008 1:30 PM')
    parser.add_argument('enddate', help='End date range (for timestamps to be generated)', nargs='?', const=1, default='1/1/2009 4:50 AM')
    parser.add_argument('timeformat', help='Datetime format to be generated e.g. \'1/1/2008 1:30 PM\', \'%m/%d/%Y %I:%M %p\' (see datetime class for more formats)', nargs='?', const=1, default='%m/%d/%Y %I:%M %p')
    parser.add_argument('outputfile', help='Relative path of the output JSON datafile', nargs='?', const=1, default='..\\data\\gen_data.json')
    args = parser.parse_args()  
    
    data_genr = CTRDataGenerator(args.schemafile,args.size,args.startdate,args.enddate,args.timeformat,args.outputfile)
    
    data_genr.generate()
    