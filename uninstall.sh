#!/bin/bash

launchctl unload ~/Library/LaunchAgents/com.vlb.darkmode.plist
rm ~/Library/LaunchAgents/com.vlb.darkmode.plist
rm -rf /usr/local/bin/darkmode
