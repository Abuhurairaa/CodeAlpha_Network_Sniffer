#!/usr/bin/env python

import scapy.all as scapy

def packet_callback(packet):
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        print(f"IP Source: {ip_src}, IP Destination: {ip_dst}")

        if packet.haslayer(scapy.TCP):
            tcp_src_port = packet[scapy.TCP].sport
            tcp_dst_port = packet[scapy.TCP].dport
            print(f"TCP Source Port: {tcp_src_port}, TCP Destination Port: {tcp_dst_port}")

        elif packet.haslayer(scapy.UDP):
            udp_src_port = packet[scapy.UDP].sport
            udp_dst_port = packet[scapy.UDP].dport
            print(f"UDP Source Port: {udp_src_port}, UDP Destination Port: {udp_dst_port}")

        elif packet.haslayer(scapy.ICMP):
            icmp_type = packet[scapy.ICMP].type
            icmp_code = packet[scapy.ICMP].code
            print(f"ICMP Type: {icmp_type}, ICMP Code: {icmp_code}")

# Replace 'eth0' with the appropriate network interface
network_interface = 'eth0'

scapy.sniff(iface=network_interface, store=False, prn=packet_callback)