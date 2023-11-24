import os
import chardet

filename_eng="en/global.ini"
filename_ger="live/global.ini"

def getType(file):
    bytes = min(32, os.path.getsize(file))
    raw = open(file, 'rb').read(bytes)
    return chardet.detect(raw)

type_eng=getType(filename_eng)    
type_ger=getType(filename_ger)    

if(type_ger!=type_eng):
    print(f"Enc. eng: {type_eng['encoding']}\n"\
          f"Enc. ger: {type_ger['encoding']}")
    exit(1)
    