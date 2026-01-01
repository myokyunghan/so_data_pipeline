import json 
import os 
import sys

def open_status_file(tbl_nm):
     pwd = os.getcwd()
     status_file = f'{pwd}/data_pipeline/check_point/{tbl_nm}_status.json'
     with open(status_file) as f:
          status = json.load(f)
     return status

def save_status_file(status, tbl_nm):
     pwd = os.getcwd()
     status_file = f'{pwd}/data_pipeline/check_point/{tbl_nm}_status.json'
     with open(status_file, "w", encoding="utf-8") as f:
        json.dump(status, f, ensure_ascii=False, indent=2)
    
def draw_progress_bar(current, total, filename='', bar_length=30):
    percent = int(current * 100 / total)
    filled = int(current * bar_length / total)
    bar = "#" * filled + "-" * (bar_length - filled)
    sys.stdout.write(
        f"\r[{bar}] {percent:3d}% ({current}/{total})  {filename}"
    )
    sys.stdout.flush()