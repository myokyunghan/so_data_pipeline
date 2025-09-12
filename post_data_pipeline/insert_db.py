import gloabl_var as g
import column_map as cm
import gloabl_var as g
import insert_file_list as ifl
from import_file import *

def target_setting(dataset, tbl_schema, table_nm, f):
    print("target_setting : insert_yn - ",g.insert_yn)
    print("target_setting : db 입력 최종 목표 - ", dataset.shape)

    Id_df = dataset[['Id']].copy()
    Id_df['Id'] = Id_df['Id'].astype('int')
    min_id = Id_df['Id'].min()
    max_id = Id_df['Id'].max()
    
    conn = psycopg2.connect(dbname  =   config.db_config['dbname'], 
                            user    =   config.db_config['user'], 
                            password=   config.db_config['password'], 
                            host    =   config.db_config['host'], 
                            port    =   config.db_config['port'])
    cur = conn.cursor()
    print("@@")
    print("chk_query", f"select Id from {tbl_schema}.{table_nm} where Id between {str(min_id)} and {str(max_id)}")
    cur.execute(f"select Id from {tbl_schema}.{table_nm} where Id between {str(min_id)} and {str(max_id)}")
    print("@@")
    inserted_data = cur.fetchall()
    cur.close()
    conn.close()
    
    inserted_id = pd.DataFrame(inserted_data, columns = ['Id_chk'])
    inserted_id['Id_chk'] = inserted_id['Id_chk'].astype('object')
    inserted_id['Id_chk'] = inserted_id['Id_chk'].astype('str')
    inserted_id_chk = pd.merge(dataset, inserted_id, left_on = 'Id', right_on = 'Id_chk', how='left')
    inserted_id_chk = inserted_id_chk[inserted_id_chk['Id_chk'].isna()].drop(columns = ['Id_chk'])
    inserted_id_chk_copy = inserted_id_chk.copy()

    print("target_setting : 데이터셋 사이즈 - ", dataset.shape)
    print("target_setting : 앞으로 입력해야할 데이터 사이즈 - ", inserted_id_chk.shape[0])

    if inserted_id_chk.shape[0] == 0 :
        g.insert_yn='N'
        ifl.insert_file_list[f] = 'Y'   

        pwd = os.getcwd()     
        file1 = open(f"{pwd}/insert_file_list.py", "w")
        file1.write("%s = %s\n" % ("insert_file_list", ifl.insert_file_list))
        file1.close()
        
        print("target_setting : 데이터 입력종료 - ", g.insert_yn)

    inserted_id_chk['idx'] = inserted_id_chk.index/2500
    inserted_id_chk['idx'] = inserted_id_chk['idx'].astype('int')
    loop_list = list(inserted_id_chk['idx'].unique())
    loop_list.sort(reverse=True)
    return inserted_id_chk, inserted_id_chk_copy, loop_list


def insert_db(dataset,tbl_schema, table_nm, f):
    while g.insert_yn =='Y':
        try:
            bak_datset = dataset.copy()
            conn = None
            col_str = set_col_str(dataset,table_nm)
            dataset, dataset_copy, loop_list = target_setting(dataset, tbl_schema, table_nm, f)
            
            print("insert_db : 앞으로 입력해야할 데이터 사이즈 - ", dataset.shape)
            print("insert_db : 앞으로 수행할 루프횟수 - ", len(loop_list))
    
            engine = sa.create_engine(f"postgresql://{config.db_config['user']}:{config.db_config['password']}@{config.db_config['host']}:{config.db_config['port']}/{config.db_config['dbname']}", client_encoding='utf8')
            conn = engine.raw_connection()
            cursor = conn.cursor()
            for i in loop_list:
                sql = f'INSERT INTO {tbl_schema}.'+table_nm+'(' + col_str+')  VALUES %s'
                tuples = [tuple(x) for x in dataset_copy.loc[dataset['idx']==i, :].to_numpy()]

                print("insert_db : 루프번호 - ", i)
                print("insert_db : 튜플 사이즈 - ", len(tuples))

                psycopg2.extras.execute_values(cursor, sql, tuples, template=None, page_size=1000)
                conn.commit()

        except Exception as e:
            print('Error : ', e)
        else:
            print("insert_db : else - ")
        finally:
            print("insert_db : finally - ")
            if g.insert_yn =='Y':
                insert_db(bak_datset, tbl_schema, table_nm, f)
            if conn:
                conn.commit()
                print("insert_db : finally - ","남아있는 커넥션 제거") 
                cursor.close()
                conn.close()
    print("insert_db : 데이터 입력종료 - ", g.insert_yn)



def set_col_str(dataset, table_nm):
    d_c = dataset.columns
    print("set_col_str : 입력받은 데이터셋의 컬럼정보 - ",d_c)
    print("set_col_str : 입력받은 데이터셋과 맵핑되는 DB의 컬럼정보 - ",", ".join([cm.col_map[table_nm][x] for x in d_c]))
    return ", ".join([cm.col_map[table_nm][x] for x in d_c])
    
