# wol-proxy
Very simple tool for receiving proxy wol packets sent by netcat (or any other UDP/TCP packet sending tool) and initializing a wakeup


#### Installation
   1) Portforward a port of your choice from the router to the target device (likely a raspberry pi).
   2) Must have the `wakeonlan` apt package installed and working
