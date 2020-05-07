#!/usr/bin/env python3

import os, subprocess
import json, requests
import darkdetect, todoist

def toggleTodoistTheme():

    with open("/usr/local/bin/darkmode/todoistCredentials.json", 'r') as f:
        payload = json.load(f)["payload"]

    r = requests.post("https://todoist.com/oauth/access_token", data=payload)

    if r.status_code != 200:
        print("Error getting access token from todoist oauth server")
        quit()

    todoistToken = r.json()["access_token"]
    api = todoist.TodoistAPI(todoistToken)

    TODOIST_LIGHT_THEME = 0
    TODOIST_DARK_THEME = 11

    api.user.update(theme=TODOIST_LIGHT_THEME if darkdetect.isDark() else TODOIST_DARK_THEME)

    api.commit()

def toggleSystemTheme():
    cmd = """
    osascript -e 'tell app "System Events" to tell appearance preferences to set dark mode to not dark mode'
    """
    os.system(cmd)

def toggleHyperTheme():
    setLightCmd =  "sed -i '' -e '/hyper-one-light/ s://::g' $(echo $HOME)/.hyper.js"
    setDarkCmd =   "sed -i '' -e '/hyper-one-light/ s:^://:g' $(echo $HOME)/.hyper.js"

    os.system(setLightCmd if darkdetect.isDark() else setDarkCmd)

#toggles system dark mode
toggleTodoistTheme()
toggleHyperTheme()
toggleSystemTheme()
