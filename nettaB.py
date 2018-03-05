# NotEvil Edit The Text Bot
#
# Made by edit/tikolu
#
# Use for NotEvil purposes only.



import requests

def Save(page="", text="", printOutput=True):
    requests.post("http://htwins.net/edit/" + page, data={'content': text})
    if printOutput:
        print(text)

def Read(page=""):
    r = requests.get("http://htwins.net/edit/" + page)
    read = r.text
    return((read.split('<textarea rows="20" cols="100" name="content">'))[1].split('</textarea>')[0])

def IP(page=""):
    r = requests.get("http://htwins.net/edit/" + page)
    read = r.text
    return((read.split('<dd id="ip">'))[1].split('</dd>')[0])

def Copy(page="", to="", printOutput=True):
    Save(to, Read(page), False)
    if printOutput:
        print("Copied " + page + " to " + to + ".")
    
