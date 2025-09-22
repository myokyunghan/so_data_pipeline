from read_file import *
from insert_db import * 
import insert_file_list as ifl
import os 
import sys

def main(path_dir, tbl_schema, tbl_nm):
     print ("start main!")

     path = path_dir
     table_nm = tbl_nm

     file_list = os.listdir(path)
     file_list_xml = [file for file in file_list if file.endswith(".xml")]
     file_list_xml.sort(reverse=True, key=extract_num_from_nm)
     make_listfile(file_list_xml)
     

     for f in file_list_xml : 
          print("main : insert 대상 - ", path+f)
          g.insert_yn ='Y'

          while g.insert_yn =='Y':
               if ifl.insert_file_list[f] =='N':
                    xml_to_df = read_file(path+f, table_nm)
                    insert_db(xml_to_df, tbl_schema, table_nm, f)
               else :
                    break
    
def make_listfile(file_list_xml):
     
     print(os.getcwd())
     pwd = os.getcwd()
     insert_chk_file = f'{pwd}/insert_file_list.py'
     file_size = os.path.getsize(insert_chk_file) 
     print('File Size:', file_size, 'bytes')

     if file_size <= 0 :
          insert_file_list = {}
          for x in file_list_xml : 
               insert_file_list[x]='N'     
          f1 = open(insert_chk_file, "w")
          f1.write("%s = %s\n" % ("insert_file_list", insert_file_list))
          f1.close()

def extract_num_from_nm(file_nm):
     return int(file_nm.split('_')[0])          

if __name__ == "__main__":
     print(sys.argv)
     path_dir       = sys.argv[1]
     tbl_schema     = sys.argv[2]
     tbl_nm         = sys.argv[3]
     main(path_dir, tbl_schema, tbl_nm)
     # /Users/boysbeanxious/opt/anaconda3/bin/python /Users/boysbeanxious/github/so_data_pipeline/post_data_body_pipeline/main.py /Users/boysbeanxious/Downloads/stackoverflow.com/div_post/ public_for_2324 postsbody


