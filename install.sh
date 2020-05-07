#!/bin/bash
launchctl unload ~/Library/LaunchAgents/com.vlb.darkmode.plist
cp com.vlb.darkmode.plist ~/Library/LaunchAgents/

mkdir -p /usr/local/bin/darkmode
cp darkmode.py /usr/local/bin/darkmode
cp todoistCredentials.json /usr/local/bin/darkmode

launchctl load ~/Library/LaunchAgents/com.vlb.darkmode.plist
launchctl start com.vlb.darkmode.plist
