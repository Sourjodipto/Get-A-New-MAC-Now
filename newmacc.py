#!/usr/bin/python3

import subprocess
import argparse


program = argparse.ArgumentParser(description="Get a new MAC now! Don't forget to use sudo.")
program.add_argument("-i", "--interface", dest="interface", help = "Enter your network interface")
program.add_argument("-m", "--mac", dest="mac",  help = "Enter your desired MAC")
args = program.parse_args()

def change(interface, mac):
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", mac])
	subprocess.call(["ifconfig", interface, "up"])

change(args.interface, args.mac)

print("We have kept out promise and there goes your new MAC! The address is " + args.mac)
