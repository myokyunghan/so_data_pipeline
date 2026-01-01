#!/bin/zsh

path=$1
type=$2


cd hf

files=($path/*.xml)
total=${#files[@]}
count=0
bar_width=30

for file in $path/*.xml
do	
	head=`/usr/bin/sed -n '1p' $file`
	tail=`/usr/bin/sed -n '$p' $file`
	
	head_tag="<"${type}">"
	footer_tag="</"${type}">"
	echo $head_tag > head_tag.sh
	echo $footer_tag > footer.sh
	
	if [[ $head = *"xml"* ]]; then
		:
	else
		/usr/bin/perl -i -pe 'if ($.==1) { open F, "head_tag.sh"; print <F>; close F }' "$file"
		/usr/bin/perl -i -pe 'if ($.==1) { open F, "header.sh";   print <F>; close F }' "$file"

	fi

	if [[ $tail = *"$type"* ]]; then
		:
	else
		echo ${footer_tag} >> $file  
	fi

	((count++))
	percent=$((count * 100 / total))
	filled=$((count * bar_width / total))

	bar=${(l:$filled::#:)}

	printf "\r[%-*s] %3d%% (%d/%d)" \
		"$bar_width" "$bar" \
		"$percent" "$count" "$total"

	
done            
