# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

from Core.Utils import Colors
from Core import Start
from time import sleep
import datetime
import os

class CREATE:

    @staticmethod
    def Create_Timeline(name):
        date = datetime.datetime.now()
        f = open(name,"w")
        f.write("----------------------------------------------\n")
        f.write("| Created with LinkdTime                     |\n")
        f.write("| Link: https://github.com/Lucksi/LinkdTime  |\n")
        f.write("| Date: {}           |\n".format(date))
        f.write("----------------------------------------------\n\n")
        f.close()

    @staticmethod
    def Write_Timeline(users,conversion,ordinated,types,titles,reader,timel_name,fixed_earliest,fixed_latest,timezone):
        j = 1
        f = open(timel_name,"a")
        f.write("Earliest Event: {} {} Latest Event: {} {}\n\n".format(str(fixed_earliest),timezone,str(fixed_latest),timezone))
        for element in ordinated:
            f.write("Number° {}\r\n".format(str(j)))
            orig_index = conversion.index(element)
            f.write("Element Title: {}\r\n".format(titles[orig_index]))
            if users[orig_index] != "":
                f.write("Author: {}\r\n".format(users[orig_index]))
            f.write("Type: {}\r\n".format(types[orig_index]))
            if types[orig_index] == "Profile-Picture" or type[orig_index] == "Company-Logo":
                f.write("Added on date: {} {}\r\n".format(element,timezone))
            else:
                f.write("Posted on date: {} {}\r\n".format(element,timezone))
            f.write("Url: {}\r\n\n".format(reader[orig_index].lstrip().rstrip()))
            j = j + 1
        f.close()
        print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Timeline Saved on: {}".format(Colors.Color.GREEN + str(timel_name)))
    
    @staticmethod
    def Timeline(path,timel_name,auto,timezone):
        timel_name = "Timelines/{}".format(timel_name)
        CREATE.Create_Timeline(timel_name)
        users = []
        conversion = []
        ordinated = []
        types = []
        titles = []
        earliest = ""
        t_i = 1
        if os.path.isfile(path):
            f = open(path,"r",newline=None)
            reader = f.readlines()
            f.close()
            num = len(reader)
            for element in reader:
                print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Url: {}".format(Colors.Color.GREEN + element.replace("\n","")))
                if auto == 0:
                    title = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Timeline-Element title" + "\n\n" + Colors.Color.PURPLE2 + "[-Timeline-]" + Colors.Color.WHITE + "-->"))
                    while title == "" or title == " ":
                        title = str(input(Colors.Color.GREEN + "\n[+]" + Colors.Color.WHITE + "Insert Timeline-Element title" + "\n\n" + Colors.Color.PURPLE2 + "[-Timeline-]" + Colors.Color.WHITE + "-->"))
                else:
                    title = "Element n°{}".format(t_i)
                    t_i = t_i + 1
                titles.append(title)
                Start.MAIN.Scan(element,"True",users,conversion,types,timezone)
                sleep(1)
            fixed_earliest = min(conversion)
            fixed_latest = max(conversion)
            temp = conversion.copy()
            for i in range(num):
                earliest = min(temp)
                ordinated.append(earliest)
                temp.remove(earliest)
            print(Colors.Color.BLUE + "\n[I]" + Colors.Color.WHITE + "Creating Timeline\n")
            sleep(2)
            print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Earliest Event: {} {}  Latest Event: {} {}\n".format(Colors.Color.GREEN + str(fixed_earliest), Colors.Color.WHITE + timezone + Colors.Color.WHITE,Colors.Color.GREEN + str(fixed_latest),Colors.Color.WHITE + timezone))
            j = 1
            for element in ordinated:
                print(Colors.Color.BLUE + "[I]" + Colors.Color.WHITE + "Number° {}".format(Colors.Color.GREEN + str(j)))
                orig_index = conversion.index(element)
                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE +  "Element Title: {}".format(Colors.Color.GREEN + titles[orig_index]))
                if users[orig_index] != "":
                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Author: {}".format(Colors.Color.GREEN + users[orig_index]))
                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE +  "Type: {}".format(Colors.Color.GREEN + types[orig_index]))
                if types[orig_index] == "Profile-Picture" or type[orig_index] == "Company-Logo":
                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Added on date: {} {}".format(Colors.Color.GREEN + element + Colors.Color.WHITE,timezone))
                else:
                    print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Posted on date: {} {}".format(Colors.Color.GREEN + element + Colors.Color.WHITE,timezone))
                print(Colors.Color.GREEN + "[+]" + Colors.Color.WHITE + "Url: {}\n".format(Colors.Color.GREEN + reader[orig_index].lstrip().rstrip()))
                j = j + 1
            CREATE.Write_Timeline(users,conversion,ordinated,types,titles,reader,timel_name,fixed_earliest,fixed_latest,timezone)
        else:
            print(Colors.Color.RED + "[!]" + Colors.Color.WHITE + "File: {} not found".format(Colors.Color.GREEN + path + Colors.Color.WHITE)) 