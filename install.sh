#!/bin/bash


cp com.vlb.darkmode.plist ~/Library/LaunchAgents/
cp darkmode.py /usr/local/bin

launchctl load ~/Library/LaunchAgents/com.vlb.darkmode.plist
launchctl start com.vlb.darkmode.plist
