# Read-only networking commands; no host settings are changed.
hostname
ipconfig /all
arp -a
netstat -an
netstat -r
route print
ping -n 4 127.0.0.1
# For the assigned lab host/domain, also use:
# tracert TARGET_IP
# pathping TARGET_IP
# nslookup TARGET_DOMAIN
# nbtstat -a TARGET_HOSTNAME
