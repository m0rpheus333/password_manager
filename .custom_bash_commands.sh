#!/bin/bash
python ~/complete/main.py
ITER=0
for item in $@
do
    case $item in
        -title)
            index=$(expr $ITER + 2)
            title=${!index}
        ;;
        -username)
            index=$(expr $ITER + 2)
            username=${!index}
        ;;
    esac
    ITER=$(expr $ITER + 1)
done

if [[ $1 == "add" ]]
then
    python ~/complete/add.py $title $username
elif [[ $1 == "copy" ]]
then
    python ~/complete/copy.py $title
elif [[ $1 == "edit" ]]
then
    python ~/complete/edit.py $title
fi



