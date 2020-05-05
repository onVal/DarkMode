# DarkMode

Some apps I use don't yet transition to dark mode automatically. Also I don't like the default time the system makes the switch.

So this is a hacky python script that will be called in the morning and afternoon to toggle dark mode on macOS systems by using <code>launchd</code>.

Needs to be installed by running <code>./install.sh</code>

The <code>install.sh</code> script will just copy <code>darkmode.py</code> to <code>/usr/local/bin</code> and the plist file into <code>~/Library/LaunchAgents</code> and then start the launchd service. 

What it does:
- Changes todoist theme (via api call)
- Changes hyper theme (by editing .hyper.js file....this only works on my machine with my specific configuration)
- Changes system theme