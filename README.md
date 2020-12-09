# wol-proxy
Very simple tool for receiving proxy Wake-on-Lan (WoL) packets accross networks and initializing an intra-network wakeup 

This tool allows for keeping a high power device on extreme low power mode and a much smaller device (like a raspberry pi) on and waiting for a wakeup packet to turn on the high power device only when it is needed so power can be saved.

#### Installation
   1) Portforward a port of your choice from your router to the target device (likely a raspberry pi)
   2) Must have the `wakeonlan` apt package installed and working
   3) Run the `server.py` script on your server with the open port
   4) The target (high power) device must have WoL properly configured and be in a hibernation state

#### Usage
   - Install netcat
   - Send requests with `echo "<password>" | nc -u <router ip> <port#>`
