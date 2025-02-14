# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2025 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

class GET:

    @staticmethod
    def Format(string,type):
        if type == "post":
            string = string.replace("_","")
            first = string.split("activity-")
            second = first[1].rsplit("-",1)[0].lstrip().rstrip()
            count_char = second.count("-")
            if count_char >= 1:
                second = second.rsplit("-",count_char)[0]
        elif type == "comment":
            count = string.count("fsd_comment%3A%28")
            first = string.split("fsd_comment%3A%28",count)
            second = first[count].rsplit("%2Curn",1)[0].lstrip().rstrip()
            count_char = second.count("-")
            if count_char >= 1:
                second = second.replace("-","")
        else:
            first = string.split("activity:",1)
            second = first[1].rsplit("/",1)[0].lstrip().rstrip()
            count_char = second.count("-")
            if count_char >= 1:
                second = second.split("-",count_char)[0]
        binary = bin(int(second)).replace("0b","")
        return binary