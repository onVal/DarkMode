# DarkMode

Some apps I use don't yet transition to dark mode automatically. Also it seems to switch during improper times.

So this is a hacky python script that will be called in the morning and afternoon to toggle dark mode on macOS systems by using <code>launchd</code>.

Needs to be installed by running <code>./install.sh</code>

What it does:
- Changes todoist theme (via api call)
- Changes hyper theme (by editing .hyper.js file....this only works on my machine with my specific configuration)
- Changes system theme
