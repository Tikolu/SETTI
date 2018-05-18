# NotEvil Edit The Text Bot
#
# Made by edit/tikolu
#
# Use for NotEvil purposes only.


import html
try:
    import requests
except ImportError:
    print("Requests liblary not detected! Visit the Netta-B wiki for information on how to install it.")
    exit()

def Save(page="", text="", printOutput=True):
    requests.post("http://htwins.net/edit/" + page, data={'content': text})
    if printOutput:
        print(text)

def Read(page=""):
    r = requests.get("http://htwins.net/edit/" + page)
    r.encoding = "utf8"
    read = r.text
    r = ((read.split('<textarea rows="20" cols="100" name="content">'))[1].split('</textarea>')[0])
    return html.unescape(r)
    

def GetIP(page=""):
    r = requests.get("http://htwins.net/edit/" + page)
    read = r.text
    return((read.split('<dd id="ip">'))[1].split('</dd>')[0])

def Copy(page="", to="", printOutput=True):
    Save(to, Read(page), False)
    if printOutput:
        print("Copied {} to {}.".format(page, to))

def ReadLine(page="", line=0, notFound=""):
    output = Read(page)
    try:
        return output.splitlines()[line]
    except IndexError:
        return notFound

def Append(page="", text="", printOutput=True):
    Save(page, Read(page) + "\n" + text, False)
    if printOutput:
        print("Appended {} to {}.".format(text, page))
      
if "__main__" == __name__:
    print("Great! Everything is working. Now you can import Netta-B into your Python projects by using 'import nettaB'.")