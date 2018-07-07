#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Simple Python Library for Communicating with Edit the Text.
#
# Made by edit/tikolu
#
# Use for NotEvil purposes only.

'''SETTI: Simplified Edit The Text Interface'''

try:
    import requests
except ImportError:
    print("Requests liblary not detected! Visit the SETTI wiki for information on how to install it.")
    exit()
try:
    import bs4
except ImportError:
    print("BeautifulSoup liblary not detected! Visit the SETTI wiki for information on how to install it.")
    exit()


def Save(page="", text="", printOutput=True):
    '''The Save command can be used to submit text to a page.'''
    requests.post("http://htwins.net/edit/" + page, data={'content': text})
    if printOutput:
        print(text)


def Read(page=""):
    '''The Read command can be used to get the contents of a page.'''
    r = requests.get("http://htwins.net/edit/raw/" + page, timeout=5, headers={'Cache-Control': 'nocache', 'Pragma': 'nocache'})
    r.encoding = "utf8"
    return r.text[:-2]


def GetIP(page=""):
    '''The GetIP command can be used to see what IP Address last edited a page.'''
    return (GetRawDict(page))["ipAddress"]


def Copy(page="", to="", printOutput=True):
    '''The Copy command can be used to copy the contents of a page to another page.'''
    Save(to, Read(page), False)
    if printOutput:
        print("Copied {} to {}.".format(page, to))


def ReadLine(page="", line=0, notFound=""):
    '''The ReadLine command can be used to get one line of a page.'''
    output = Read(page)
    try:
        return output.splitlines()[line]
    except IndexError:
        return notFound


def Append(page="", text="", sep="\n", printOutput=True):
    '''The Append command can be used to append text to an existing page's content.'''
    Save(page, '{}{}{}'.format(Read(page), sep, text), False)
    if printOutput:
        print("Appended {} to {}.".format(text, page))


def Export(page="", filename="page.txt", printOutput=True):
    '''The Export command can be used to Export a page into a file.'''
    f = open(filename, "w", encoding="utf-8")
    f.write(Read(page))
    f.close()
    if printOutput:
        print("{} has been exported to {}.".format(page, filename))


def GetRawDict(page=""):
    '''Returns a raw dict object of the specified page which includes details of the last edit.'''
    r = requests.get("http://htwins.net/edit/submit/" + page, timeout=5, headers={'Cache-Control': 'nocache', 'Pragma': 'nocache'})
    return r.json()


def GetTime(page=""):
    '''Returns the timestamp of the last edit of a page.'''
    return int((GetRawDict(page))["lastModified"])


def GetEditID(page=""):
    '''Returns the ID of the last edit of a page.'''
    return int((GetRawDict(page))["editId"])

    
if __name__ == '__main__':
    print("Great! Everything is working. Now you can import SETTI into your Python projects using 'import setti'.")
