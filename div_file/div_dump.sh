#!/bin/zsh

file_path=$1
file=$2

today=`date`
echo $today
echo $file_path

echo "Dividing $file_path/$file ..."
cd $file_path
awk -v file="$file" '
BEGIN {
    print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>Start (" file ") <<<<<<<<<<<<<<<<<<<<<<<<<<<"
}
{
    a = int(NR/594839) "_" file
    print $0 > a
}
END {
    print "=>>>>>>>>>>>>>>>>>>>>>>>>>>>>End (" file ") <<<<<<<<<<<<<<<<<<<<<<<<<<<"
}
' "$file"

echo ""
today=`date`
echo $today
echo "$file divide end" 