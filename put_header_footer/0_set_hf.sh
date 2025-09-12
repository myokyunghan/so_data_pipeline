#!/bin/zsh

path=$1
type=$2

echo $path
echo $type

for file in $path/*.xml
do	
	#echo $file
	head=`/usr/bin/sed -n '1p' $file`
	tail=`/usr/bin/sed -n '$p' $file`
	
	head_tag="<"${type}">"
	footer_tag="</"${type}">"
	echo $head_tag > head_tag.sh
	echo $footer_tag > footer.sh
	
	if [[ $head = *"xml"* ]]; then
		echo ""
	else
		echo "no header!!!"
		/usr/bin/perl -p -i -e '$.==1 and print `cat head_tag.sh`' `echo $file`
		/usr/bin/perl -p -i -e '$.==1 and print `cat header.sh`' `echo $file`
	fi

	if [[ $tail = *"$type"* ]]; then
		echo ""
	else
		echo "no footer!!!"
		echo ${tail_tag} >> $file  
	fi
done            
