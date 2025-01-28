from scapy.all import rdpcap, sendp, IP
from tkinter import Tk, filedialog
import os

if os.name == "nt":
    interface = "Ethernet"
else:
    interface = "eth0"

def replicate_pcap(pcap_file, target_ip):
    packets = rdpcap(pcap_file)
    for packet in packets:
        if IP in packet:
            packet[IP].dst = target_ip
    sendp(packets, interface)

print("\033[2J\033[H", end="", flush=True)
print("\x1b[38;5;221m"+r"""
 ╔╗╔╔═╗╔╦╗  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ┬─┐┌─┐┌─┐┬  ┬┌─┐┌─┐┌┬┐┌─┐┬─┐
 ║║║║╣  ║   ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ├┬┘├┤ ├─┘│  ││  ├─┤ │ │ │├┬┘
 ╝╚╝╚═╝ ╩   ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ┴└─└─┘┴  ┴─┘┴└─┘┴ ┴ ┴ └─┘┴└─

                                          Creator: jts.codes/
 
  Select Packet Capture File to begin...
""")

try:
    pcap_file = filedialog.askopenfilename(title="SELECT PCAP FILE")
    target_ip = input("  Target IP Address: ")
    count = int(input("\n  Attack Count: "))
    for i in range(count):
        replicate_pcap(pcap_file, target_ip)
    input("\n  Process Completed! Press ENTER to exit...\n")
except Exception:
    input("\033[0;31m\n  Process Incomplete! Press ENTER to exit...\n")
