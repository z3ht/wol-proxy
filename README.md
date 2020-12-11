# wol-proxy
Very simple tool for receiving proxy Wake-on-Lan (WoL) packets across networks and initializing an intra-network wakeup 

This tool allows for keeping a high power device on extreme low power mode and a much smaller device (like a raspberry pi) on and waiting for a wakeup packet to turn on the high power device only when it is needed so power can be saved.

#### Installation
   1) Portforward a port of your choice from your router to the low power device (likely a raspberry pi)
   2) Must have the `wakeonlan` apt package installed and working on the low power device
   3) Run the `server.py` script on your low power device with the open port
   4) The target (high power) device must have WoL properly configured and be in a hibernation state (check out my [dotfiles](https://github.com/z3ht/dotfiles) repository for a script that does this automatically)

#### Usage
   - Install netcat
   - Send requests with `echo "<password>" | nc -u <router ip> <port#>`
