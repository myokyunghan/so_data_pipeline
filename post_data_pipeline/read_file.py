from import_file import *
import column_map as cm


def read_file(file_nm, table_nm) : 
    # xtree = et.parse("../xmldump/99_post.xml")
    xtree = et.parse(file_nm)
    xroot = xtree.getroot()
    '''
    xml 내용을 arr에 저장
    '''
    arr=[]
    # xml의 node를 대상으로
    for node in xroot: 
        # 노드의 key 값을 arr리스트에 붙여넣기     
        arr.extend(list(node.attrib.keys()))
    # 중복을 제거하여 xml의 컬럼 정보를 arr 배열에 저장
    arr = list(set(arr))

    '''
    arr을 dataframe 형태로 변경
    '''
    df = pd.DataFrame()
    tot_arr = []
    # xml의 node를 대상으로
    for node in xroot: 
        # 이전 셀에서 만든 컬럼정보를 기반으로 데이터프레임의 한 행을 tmp_arr에 저장     
        tmp_arr = [node.attrib.get(column) if node is not np.NaN else None for column in arr]
        # tmp_arr을 tot_arr에 append
        tot_arr.append(tmp_arr)

    table_df = pd.DataFrame(tot_arr, columns =arr)

    print("read_file : 데이터프레임 컬럼 - ", table_df.columns)
    
    
    table_df_org_col = [x for x in cm.col_map[table_nm].keys()]
    table_df_col = table_df.columns
    intersection = list(set(table_df_org_col) & set(table_df_col))
    table_df = table_df[intersection]

    return table_df

    
    
