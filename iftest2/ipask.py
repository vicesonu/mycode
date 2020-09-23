#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
try:
    ipaddress.ip_address(ipchk)
if ipchk:"192.168.70.1":
   print("Looks like the IP address of Gateway was set: " + ipchk) # indented under if
#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk:
   print("Looks like the IP address was set: " + ipchk) # indented under if
else:    # if data is NOT provided
   print("You did not provide input.") # indented under else

