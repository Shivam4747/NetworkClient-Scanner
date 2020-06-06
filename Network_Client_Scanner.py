#!/usr/bin/env python

import scapy.all
import argparse
import sys
from pyfiglet import Figlet


def get_arguments():
    parser = argparse.ArgumentParser(prog='python Network_Client_Scanner', usage='%(prog)s [optional arguments] '
                                                                                 'required arguments')
    req_arg = parser.add_argument_group("Required Arguments")
    req_arg.add_argument("-t", "--target", dest="target_ip", help="Specify Target IP in CIDR Notation", required=True)
    options = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    return options


def client_scanner(target_ip):

    req_packet = scapy.all.ARP(pdst=target_ip)
    broad_packet = scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")
    broad_req = broad_packet / req_packet
    (answered_packets, unanswered_packets) = scapy.all.srp(broad_req, timeout=2, verbose=False)

    return answered_packets


def info_packets(answered_packets_list):
    clients_data = []

    for info in answered_packets_list:
        client_data_dict = {"IP" : info[1].psrc, "MAC" : info[1].hwsrc}
        clients_data.append(client_data_dict)

    return clients_data


def main_result(clients_data):

    # print("[*] Scanning All Clients on the subnet " + "\'" + target_ip + "\'" + " ...\n")
    print("Clients\' IP Addresses\t\t\tClients\' MAC Addresses")
    print("--------------------------------------------------------------\n")
    for info in clients_data:
        print(info["IP"] + "\t\t\t\t " + info["MAC"] + "\n")

    print("\n[+] Done!")


def render_text():
    print("\n\n----------------------Client Scanner Script made by----------------------\n")
    f = Figlet(font='slant')
    print(f.renderText('shIVam') + "\t\t\t\t\tv1.0\n\n\n")


def main():

    render_text()
    options = get_arguments()
    print("[*] Scanning all Clients connected to the subnet " + "\'" + options.target_ip + "\'" + " ...\n")
    answered_packets_list = client_scanner(options.target_ip)
    clients_data = info_packets(answered_packets_list)
    main_result(clients_data)


if __name__ == '__main__':
    main()
