from read_file import *
from insert_db import * 
import os 
import insert_file_list as ifl

def main():
     print ("start main!")

     path = "/Users/boysbeanxious/Downloads/article/divide_post/"
     table_nm = "postsbody"

     file_list = os.listdir(path)
     file_list_xml = [file for file in file_list if file.endswith(".xml")]
     file_list_xml.sort(reverse=True)
     # file_list_xml.sort()
     
     print("main : 전체파일 - ", file_list_xml)
     # insert_file_list = {}
     # for x in file_list_xml : 
     #      insert_file_list[x]='N'
     
     # print(insert_file_list['9_post.xml'])
          
     # file1 = open("/Users/boysbeanxious/github/post_data_pipeline/insert_file_list.py", "w")
     # file1.write("%s = %s\n" % ("insert_file_list", insert_file_list))
     # file1.close()
     

     for f in file_list_xml : 
          print("main : insert 대상 - ", path+f)
          g.insert_yn ='Y'
          # xml_to_df = read_file(path+f, table_nm)
          # print(xml_to_df.head(5))
          
          while g.insert_yn =='Y':
               if ifl.insert_file_list[f] =='N':
                    xml_to_df = read_file(path+f, table_nm)
                    insert_db(xml_to_df, table_nm, f)
               else :
                    break
    

if __name__ == "__main__":
     main()

