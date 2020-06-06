# Network Client Scanner
A Client Scanner built using Python, used to *show* a list of ***Clients' IP Address & MAC Address*** connected to a network!

## Requirements
- Python Interpreter (version 2.7.xx or higher)
- Python Modules, ***Scapy*** and ***PyFiglet*** and one Windows Library,  ***Npcap***

  > For installation of theses modules, see *installation* section

## Installation
- For Installation of above mentioned Python Modules - 
    > For Linux Environment :

    - Open bash terminal and execute these commands step by step :

    ```bash
    pip3 install scapy  #for SCAPY module
    pip3 install pyfiglet  #for PyFiglet Module
    ```
    > For Windows Environment : 
    
     - You need to download and install this module from: 
       
         <https://nmap.org/npcap/dist/npcap-0.9992.exe>
- After Installation of Required Dependencies, Follow following Steps as they are Same for both Environments(Linux and Windows) : 

```bash
git clone https://github.com/Shivam4747/NetworkClient-Scanner.git

cd NetworkClient-Scanner/

python Network_Client_Scanner.py --target <subnet>
```

## Usage

```bash
# Prints a HELP message for how to use the script
  
python Network_Client_Scanner.py --help
```
> Output :
```bash
usage: python Network_Client_Scanner [optional arguments] required arguments

optional arguments:
  -h, --help            show this help message and exit

Required Arguments:
  -t TARGET_IP, --target TARGET_IP
                        Specify Target IP in CIDR Notation
```

## Example
```bash
python .\Network_Client_Scanner.py --target 192.168.42.0/24
```
> Output :

```shell
[*] Scanning all Clients connected to the subnet '192.168.42.0/24' ...

Clients' IP Addresses                   Clients' MAC Addresses
--------------------------------------------------------------

192.168.42.129                           7a:34:ec:ea:c0:45
192.168.98.126                           00:ff:dd:6f:d2:12
192.168.139.41                           12:54:a2:53:b5:2a
192.168.1.1                              24:3a:aa:f1:3a:4e

[+] Done!
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## HIT Counter
[![HitCount](http://hits.dwyl.com/Shivam4747/NetworkClient-Scanner.svg)](http://hits.dwyl.comShivam4747/NetworkClient-Scanner)
