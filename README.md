# Hearthstone Firewall Switcher for Battlegrounds
Hearthstone firewall switcher is a simple application which helps you block and restore Hearthstone's access
to internet with a single button press -- this gives you more time to think and do stuff in tavern.

![demo](https://i.ibb.co/smszvnN/image.png)

## Installation
1. Download zip archive from [releases page](https://github.com/ucarno/hs-firewall/releases).
2. Extract `HSFirewall` directory wherever you want.
3. Done! Open `HSFirewall.exe` located in app directory.
4. Optionally create desktop link to executable.
5. Open program and select path to Hearthstone executable
(by default `C:\Program Files (x86)\Hearthstone\Hearthstone.exe`).

## Usage
1. A few seconds before fight, press green button, it should become red.
2. After ~5 seconds, press button again and game should reconnect you back to the tavern.

## How it works
This program works by maintaining Windows Defender firewall rule through `netsh advfirewall firewall` commands.

![disabled](https://i.ibb.co/cYZc0XZ/image.png)
![enabled](https://i.ibb.co/KKBhKp9/image.png)

## Building executable from source
* Create virtual environment and install necessary libs from `requirements.txt`.
* Build using command `pyinstaller --noconfirm --uac-admin --noconsole --name HSFirewall main.py`
