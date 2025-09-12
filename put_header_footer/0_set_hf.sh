#!/bin/zsh

files=$(find ../divide_comment -name "*.xml") 

for file in ../divide_comment/*.xml
 do
	type="comments"
	echo $type
	
	head=`sed -n '1p' $file`
	tail=`sed -n '$p' $file`
	
	head_tag="<"${type}">"
	tail_tag="</"${type}">"
	echo $head_tag > head_tag.sh
	
	echo $file_nm
	echo " "			

	if [[ $head = *"xml"* ]]; then
		echo ""
	else
		echo "no header!!!"
		perl -p -i -e '$.==1 and print `cat head_tag.sh`' `echo $file`
		perl -p -i -e '$.==1 and print `cat header.sh`' `echo $file`
	fi

	if [[ $tail = *"$type"* ]]; then
		echo ""
	else
		echo "no footer!!!"
		echo ${tail_tag} >> $file  
	fi
done            
