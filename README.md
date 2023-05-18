# PPS
Privicy Protection system 3

This is a code for the PPS3.
-
## What is the PPS3?
The PPS3 is the third generation of a system, I'm developing to switch desktop or minimize applications, based on sensor input. (For now only door senors)

## How do I use it?
1. Enter your WIFi ssid and password in the client.cpp
2. Enter a ID in the client.cpp (can be any number)
3. Install the client.cpp script on a esp8266
4. Conect a limit switch to your esp8266
5. Attach the esp and switch to your door so that when the door is closed the swich is pressed and when it is opend the limit switch is unpressed
6. Edit the settings.json like this:

```
{
  "YOUR_ID": "ACTION ('s' for switch desktop and 'm' for minimize application)"
}
```

7. Start the server.py
