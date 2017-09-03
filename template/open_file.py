# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 08:49:46 2017

@author: Administrator
"""

import sys
import pandas as pd



if __name__ == '__main__':
    first_name = sys.argv[1]
    second_name = sys.argv[2]
    

    
    try:
        file_name = first_name        
        data = pd.read_csv(first_name)    

        
       
    
    except:
    
        print ("File not exists. or something error")
    
    
    else:
        print (data.hours_length.describe())
        

        data.to_csv(second_name,index=False)