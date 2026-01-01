#!/bin/zsh

# echo "=======================================================================" 
# echo "==================== Welcome to so_data_pipeline ======================"
# echo "=======================================================================" 

# current_path=`pwd`
# cd data_pipeline || {
#   echo "ERROR: Please execute the main.sh in the so_data_pipeline project: $dump_path" >&2
#   exit 0
# }

# echo ""
# echo "=======================================================================" 
# echo "=========== check if the path and file for dump exists ================"
# echo "======================================================================="

# #>>>>>>>>>>>>>>>>>>>>>> check if the path and file for dump exists
# echo -n "Input the absolute path of the dumpfile location: "
# read dump_path

# cd "$dump_path" || {
#   echo "ERROR: Path does not exists: $dump_path" >&2
#   exit 1
# }

# cnt=`find . -type f -name "*.xml" | wc -l`

# if [ $cnt -le 0 ]; then
#   echo "ERROR: Dumpfile does not exists"
#   exit 2
# fi

# file_list=`find . -type f -name "*.xml"`
# echo "Check the target xml file. These file will be inserted in the database tables"
# echo $file_list
# echo "If it is correct, press enter to continue"
# read dummy

# echo "=======================================================================" 
# echo "====================== check database setting ========================="
# echo "======================================================================="

# #>>>>>>>>>>>>>>>>>>>>>> check if the postgresql settings are correct


# echo -n "Input the location of database, 1 for local 2 for server: "
# read answer

# if [ $answer -eq 1 ]; then
#     ps -ef | grep postgres | grep -v grep >/dev/null 2>&1
#     if [ $? -ne 0 ]; then
#     echo "ERROR: Postgresql server is not running. Please start the postgresql server first." >&2
#     exit 3
#     fi

#     if ! psql -lqt >/dev/null 2>&1; then
#       echo "ERROR: Cannot connect to postgresql server. Please check your postgresql settings." >&2
#       exit 4
#     fi
# fi

# if [ ! -e "$current_path/data_pipeline/pg_config.py" ]; then
#   echo "ERROR: PostgreSQL configuration file does not exists: $current_path/data_pipeline/pg_config.py" >&2
#   exit 5
# fi

# echo -n "Input the table schema of postgresql: "
# read tbl_schema

dump_path="/Users/boysbeanxious/tmp"
current_path="/Users/boysbeanxious/github/so_data_pipeline"

find /Users/boysbeanxious/tmp -maxdepth 1 -type f -name "*.xml" | while IFS= read -r file
do
    filenm=$(basename "$file")
    type="${filenm:l}"     
    type="${type%.xml}"   
    new_dir=$dump_path/div_file/$type

    # echo "=======================================================================" 
    # echo "====================== 1. Divide the dump data ========================"
    # echo "=======================================================================" 
    # mkdir -p $new_dir
    # cp $file $new_dir
    # zsh ./div_file/div_dump.sh $new_dir $filenm && \rm $new_dir/$filenm
    # echo ""
    # echo "=======================================================================" 
    # echo "===================== 2. Set header and footer ========================"
    # echo "======================================================================="
    # echo "Execute set_header_footer ..., type: $type"
    # zsh ./hf/set_header_footer.sh $new_dir $type

    echo ""
    echo "=======================================================================" 
    echo "======================= 3. Insert to Database ========================="
    echo "======================================================================="
    echo "Insert $type dump file to Database ..."
    venv_so_data_pipeline/bin/python data_pipeline/main.py $new_dir public_for_2324 $type

done
