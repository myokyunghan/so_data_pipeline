from read_file import *
from insert_db import * 
import os 
import sys

def main(path_dir, tbl_schema, tbl_nm):
     path = path_dir
     table_nm = tbl_nm

     file_list = os.listdir(path)
     file_list_xml = [file for file in file_list if file.endswith(".xml")]
     file_list_xml.sort(reverse=True, key=extract_num_from_nm)
     make_listfile(file_list_xml, tbl_nm)
     

     total = len(file_list_xml)

     for idx, f in enumerate(file_list_xml, start=1):
          g.insert_yn ='Y'
          ut.draw_progress_bar(idx, total, f)

          while g.insert_yn =='Y':
               status = ut.open_status_file(tbl_nm)
               if status[f] =='N':
                    xml_to_df = read_file(f'{path}/{f}', table_nm)
                    insert_db(xml_to_df, tbl_schema, table_nm, f)
               else :
                    break


def make_listfile(file_list_xml, tbl_nm):
     pwd = os.getcwd()
     status_file = f'{pwd}/data_pipeline/check_point/{tbl_nm}_status.json'

     if not os.path.exists(status_file) :
          ut.save_status_file({x : 'N' for x in file_list_xml}, tbl_nm )
          
def extract_num_from_nm(file_nm):
     return int(file_nm.split('_')[0])          

if __name__ == "__main__":
     print(sys.argv)
     path_dir       = sys.argv[1]
     tbl_schema     = sys.argv[2]
     tbl_nm         = sys.argv[3]
     main(path_dir, tbl_schema, tbl_nm)



