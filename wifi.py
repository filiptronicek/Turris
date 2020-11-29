# This script will light up the first 7 lights and will show the number of connected clients in binary, so the limit is 128 clients.

import subprocess

result = subprocess.run(["bash", "wifi.sh"], stdout=subprocess.PIPE).stdout.decode("utf-8")

leds = [ 'wan', 'lan1', 'lan2', 'lan3', 'lan4', 'lan5', 'wifi' ]

blockLen = len(leds)
blocks = []

subprocess.run(["rainbow", "all", "disable"]) # Reset state of all LEDs
subprocess.run(["rainbow", "all", "blue"]) # Set all to blue color
subprocess.run(["rainbow", "pwr", "green"]) # Set pwr to green
subprocess.run(["rainbow", "pwr", "enable"]) # Enable pwr

for i in range(blockLen):
    blocks.append(pow(2, i))

clients = int(result.replace("\n", ""))

for idx, block in enumerate(reversed(blocks)):
    if (clients / block) >= 1:
        clients -= block
        subprocess.run(["rainbow", leds[len(leds) - idx - 1], "enable"])
        print(str(leds[len(leds) - idx - 1]) + ": enable")
