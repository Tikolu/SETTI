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
    r = requests.get("http://htwins.net/edit/raw/" + page)
    r.encoding = "utf8"
    read = r.text
    return read


def GetIP(page=""):
    '''The GetIP command can be used to see what IP Address last edited a page.'''
    r = requests.get("http://htwins.net/edit/" + page)
    read = r.text
    return bs4.BeautifulSoup(read, 'html.parser').find(id='ip').string


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


def Append(page="", text="", printOutput=True):
    '''The Append command can be used to append text to an existing page's content.'''
    Save(page, Read(page) + "\n" + text, False)
    if printOutput:
        print("Appended {} to {}.".format(text, page))

def Export(page="", filename="page.txt", printOutput=True):
    '''The Export command can be used to Export a page into a file.'''
    f = open(filename, "w", encoding="utf-8")
    f.write(Read(page))
    f.close()
    if printOutput:
        print("{} has been exported to {}.".format(page, filename))


if __name__ == '__main__':
    print("Great! Everything is working. Now you can import SETTI into your Python projects by using 'import setti'.")
