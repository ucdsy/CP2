#!/usr/bin/env python

import sys
import subprocess
import os
from src import etl
import json
sys.path.insert(0, 'src')
from src import eda

def main(targets):
    eda_config = json.load(open('config/eda-params.json'))
    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)
        mydir = os.getcwd() # would be the MAIN folder
        mydir_tmp = mydir + "//src" # add the testA folder name
        mydir_new = os.chdir(mydir_tmp) # change the current working directory
        mydir = os.getcwd() #
        
        output=etl.run_cmd_shell(data_cfg['command'])
        return output   
    if 'eda' in targets:

        eda.generate_stats('test', **eda_config)
        
        
if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets=sys.argv[1:]
    main(targets)
    