# Created : 2022 Jan 21
# This script reads the jsonl created from export of prodigy line by line, convert to xml
# and write each line of the jsonl file to an xml file with annotations


from xml.etree import ElementTree as et
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
import json 

json_file_path = '../data/annotations/prodigy_lips.jsonl'  #location of jsonl file ( prodigy export )
output_dir =  '../data/annotations/xml/'    #where you want to create the xml files 

L_lines = open(json_file_path,"r").read().split("\n")
L_lines = [k for k in L_lines if len(k)>0]   # remove any empty lines 

for str_json in L_lines  : 
    json_object = json.loads(str_json)
    fname = json_object["meta"]['file']
    xml_fname = fname.replace('.jpg','.xml')

    data = readfromstring(str_json)
    str_xml =  json2xml.Json2xml(data).to_xml()
    
    # write to an xml file
    #print(f'{output_dir}{xml_fname}')
    text_file = open(f'{output_dir}{xml_fname}', "w")
    text_file.write(str_xml)
    text_file.close()