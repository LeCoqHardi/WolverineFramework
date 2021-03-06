<img src="assets/Banner.png">

# How to install/Uninstall
<b>Install</b> : Just copy this command to your terminal<br>
`cd ~ && git clone https://www.github.com/lecoqhardi/WolverineFramework && chmod +x WolverineFramework/wolverine && chmod +x WolverineFramework/Wolverine.sh && sudo mv WolverineFramework/wolverine /bin && sudo mv WolverineFramework /etc && clear && echo "Install Complete"`<br>
<b>Uninstall</b> : Just copy this command to your terminal<br>
`sudo rm -r /etc/WolverineFramework && sudo rm /bin/wolverine` <br>
If you want to uninstall all packages mentionned in "# Tools in the Framework", just type : <br>
<b>Debian/Ubuntu</b> : `sudo apt purge <package name>` <br>
<b> Arch </b>`sudo pacman -R <package name>` <br>
<b>Update</b> : Just copy this command to your terminal <br>
`cd /etc && sudo rm -r WolverineFramework && sudo git clone https://www.github.com/lecoqhardi/WolverineFramework.git && sudo mv /etc/WolverineFramework/wolverine /bin && cd ~ && clear && sudo chmod +x /bin/wolverine && echo "Update Complete"`


# WolverineFramework

WolverineFramework is a little and very complete Script allowing you to install and use basic Cybersecurity tools ! The Script is constantly updated, so don't forget to pull the Framework frequently by doing `cd /etc && sudo rm -r WolverineFramework && sudo git clone https://www.github.com/lecoqhardi/WolverineFramework.git && sudo mv /etc/WolverineFramework/wolverine /bin && cd ~ && clear && sudo chmod +x /bin/wolverine && echo "Update Complete"` !  (I advise you to run again /etc/WolverineFramework/Install.sh when there is an update with `bash /etc/WolverineFramework/Install_deb.sh` for Debian/Ubuntu users or `bash /etc/WolverineFramework/Install_arch.sh` for Arch users). 

# How it works ?

It's very simple, the main script "Wolverine.sh" asks you what you want to do and, depending on what you choose, it will run some "mini" script in the Script folder, in order to keep you from having to type complete commands lines.

# Tools in the Framework

  - ettercap-graphical → Man in the Middle tool
  - hping3 → DoS/DDoS tool
  - Medusa → Multi purpose Bruteforce tool
  - Patator → Multi purpose Bruteforce tool (Not available on ArchLinux)
  - Hydra → Multi purpose Bruteforce tool
  - Network Mapper (nmap) → Network and ports scanning tool
  - PostGreSQL → Essential database for Metasploit
  - Metasploit → Framework with a lot of Exploits
  - Phoneinfoga → Tool to get informations on Intenret from a Phone Number 
  - Wordpress Security Scanner (WPScan) → Tool to scan Wordpress Websites, to get all the extensions and so the vulnerabilities
  - MacChanger → Tool used to hide your real MAC Address behind a fake one
  - Arp-Scan → Tool using ARP to discover hosts inside a LAN

# How to use ?

First, I advise you to run the "Install.sh" script. This script installs every packet needed for the Framework (It'll install the packets above, if you have them, it'll do nothing), it'll also make the others script executable. Launch it with `bash /etc/WolverineFramework/Install_deb.sh` for Debian/Ubuntu users or `bash /etc/WolverineFramework/Install_arch.sh`for Arch users on your terminal.


Then launch it by just running `wolverine` in your terminal.

Enjoy !
 
# That's it !

Have fun with this little script, if you want to contact me, you can on Discord, Twitch or Twitter :

Discord : Théo#2226
Twitter : @LeCoqHardi__
Twitch : https://www.twitch.tv/LeCoqHardi

# Important Notes

- If you have the error "Unable to Locate package metasploit-framework", use this command -> "wget https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb && chmod +x msfinstall &&./msfinstall "
- Right now Patator isn't available on ArchLinux, when it is, i'll add it to the script Install_arch.sh
