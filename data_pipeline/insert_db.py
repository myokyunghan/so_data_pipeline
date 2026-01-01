import gloabl_var as g
import column_map as cm
import gloabl_var as g
from import_file import *

def target_setting(dataset, tbl_schema, table_nm, f):
    Id_df = dataset[['Id']].copy()
    Id_df['Id'] = Id_df['Id'].astype('int')
    min_id = Id_df['Id'].min()
    max_id = Id_df['Id'].max()


    conn = psycopg2.connect(dbname  =   pg_config.db_config['dbname'], 
                            user    =   pg_config.db_config['user'], 
                            password=   pg_config.db_config['password'], 
                            host    =   pg_config.db_config['host'], 
                            port    =   pg_config.db_config['port'])
    cur = conn.cursor()
    cur.execute(f"select Id from {tbl_schema}.{table_nm} where Id between {str(min_id)} and {str(max_id)}")
    
    inserted_data = cur.fetchall()
    cur.close()
    conn.close()

    inserted_id = pd.DataFrame(inserted_data, columns = ['Id_chk'])
    inserted_id['Id_chk'] = inserted_id['Id_chk'].astype('object')
    inserted_id['Id_chk'] = inserted_id['Id_chk'].astype('str')
    inserted_id_chk = pd.merge(dataset, inserted_id, left_on = 'Id', right_on = 'Id_chk', how='left')
    inserted_id_chk = inserted_id_chk[inserted_id_chk['Id_chk'].isna()].drop(columns = ['Id_chk'])
    inserted_id_chk_copy = inserted_id_chk.copy() 

    if inserted_id_chk.shape[0] == 0 :
        status = ut.open_status_file(table_nm)
        g.insert_yn='N'
        status[f] = 'Y'     
        ut.save_status_file(status, table_nm)

        
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
            
            engine = sa.create_engine(f"postgresql://{pg_config.db_config['user']}:{pg_config.db_config['password']}@{pg_config.db_config['host']}:{pg_config.db_config['port']}/{pg_config.db_config['dbname']}", client_encoding='utf8')
            conn = engine.raw_connection()
            cursor = conn.cursor()
            for i in loop_list:
                sql = f'INSERT INTO {tbl_schema}.'+table_nm+'(' + col_str+')  VALUES %s'
                tuples = [tuple(x) for x in dataset_copy.loc[dataset['idx']==i, :].to_numpy()]

                psycopg2.extras.execute_values(cursor, sql, tuples, template=None, page_size=1000)
                conn.commit()
                print(f"    where are you {i}")

        except Exception as e:
            print('Error : ', e)
        else:
            if g.insert_yn =='Y':
                insert_db(bak_datset, tbl_schema, table_nm, f)
        finally:
            if conn:
                conn.commit()
                cursor.close()
                conn.close()
    



def set_col_str(dataset, table_nm):
    d_c = dataset.columns
    return ", ".join([cm.col_map[table_nm][x] for x in d_c])
    
