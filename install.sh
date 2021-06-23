echo "Installing Password Manager"
cd ~
mkdir pmanager
cd pmanager
git clone https://github.com/sarvartojikulov/password_manager.git .
echo "---> Installed"
cd ~
echo "alias passman='~/pmanager/.custom_bash_commands.sh'">>.bashrc
source .bashrc
echo "instlled succesfully"