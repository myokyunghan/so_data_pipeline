from import_file import *
import column_map as cm


def read_file(file_nm, table_nm) : 
    
    xtree = et.parse(file_nm)
    xroot = xtree.getroot()
    
    arr=[]
    for node in xroot: 
        arr.extend(list(node.attrib.keys()))
    arr = list(set(arr))

    tot_arr = []
    for node in xroot: 
        tmp_arr = [node.attrib.get(column) if node is not np.nan else None for column in arr]
        tot_arr.append(tmp_arr)

    table_df = pd.DataFrame(tot_arr, columns =arr)    
    table_df_org_col = [x for x in cm.col_map[table_nm].keys()]
    table_df_col = table_df.columns
    intersection = list(set(table_df_org_col) & set(table_df_col))
    table_df = table_df[intersection]

    return table_df

    
    
