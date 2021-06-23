echo "Installing Password Manager"
cd ~
mkdir complete
cd complete
git clone https://github.com/sarvartojikulov/password_manager.git .
echo "---> Installed"
cd ~
echo "alias passman='~/complete/.custom_bash_commands.sh'">>.bashrc
source .bashrc
echo "instlled succesfully"