#!/usr/bin/env python3

import os, subprocess
import json, requests
import darkdetect, todoist

def toggleTodoistTheme():

    with open("todoistCredentials.json", 'r') as f:
        payload = json.load(f)["payload"]
    
    print(payload)

    r = requests.post("https://todoist.com/oauth/access_token", data=payload)

    if r.status_code != 200:
        print("Error getting access token from todoist oauth server")
        quit()


    todoistToken = r.json()["access_token"]
    api = todoist.TodoistAPI(todoistToken)

    print(api.user)

    TODOIST_WHITE_THEME = 0
    TODOIST_DARK_THEME = 11

    if darkdetect.isDark():
        print("light theme is being set")
        api.user.update(theme=TODOIST_WHITE_THEME)
    else: 
        print("dark theme is being set")
        api.user.update(theme=TODOIST_DARK_THEME)

    api.commit()

def toggleSystemTheme():
    cmd = "osascript -e 'tell app \"System Events\" to tell appearance preferences to set dark mode to not dark mode'"
    os.system(cmd)

#toggles system dark mode
toggleTodoistTheme()
toggleSystemTheme()