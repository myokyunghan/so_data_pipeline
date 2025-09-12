#!/bin/zsh

path=$1
type=$2

echo $path
echo $type

for file in $path/*.xml
do	
	echo $file
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
		/usr/bin/perl -i -pe 'if ($.==1) { open F, "head_tag.sh"; print <F>; close F }' "$file"
		/usr/bin/perl -i -pe 'if ($.==1) { open F, "header.sh";   print <F>; close F }' "$file"

	fi

	if [[ $tail = *"$type"* ]]; then
		echo ""
	else
		echo "no footer!!!"
		echo ${footer_tag} >> $file  
	fi
done            
