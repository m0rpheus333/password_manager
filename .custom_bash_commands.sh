#!/bin/bash

# To get Pythpn to work in GitBash use winpty command
#source https://medium.com/@presh_onyee/getting-python-shell-to-work-on-git-bash-windows-mac-linux-5fdfc49409e4
winpty python ~/complete/main.py
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
    winpty python ~/complete/add.py $title $username
elif [[ $1 == "copy" ]]
then
    winpty python ~/complete/copy.py $title
elif [[ $1 == "edit" ]]
then
    winpty python ~/complete/edit.py $title
else
	echo "Info: "
	echo "      passman add:        Neue Titel und Username hinzufügen."
	echo " "
	echo "                    -title: Flag, um den Title zu identifizieren"
	echo "                    -username: Flag, um den Username zu identifizieren"
	echo "---> Beispiel: passman add -title Facebook -username Karl1990"
	echo " "
	echo " "
	echo "      passman copy:       Passwort mit Titel kopieren"
	echo " "
	echo "              -title: Flag, um den Title zu identifizieren"
	echo "---> Beispiel: passman copy -title Facebook"
fi



