my_str = "wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3"
stripped = my_str.strip("wlo1 Link encap:Ethernet HWaddr ")
print(stripped)
"or"
split = my_str.split()
output = split[4]
print(output)
