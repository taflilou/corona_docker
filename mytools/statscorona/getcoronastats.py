#!/usr/bin/python
# Get number of people infected by Coronavirus in France

import re
import argparse
import requests
from bs4 import BeautifulSoup

# TODO
# Put coutry name in parameter: done
# Faire une fonction pr retourner la liste de tous les pays possibles: done

URL = "https://www.worldometers.info/coronavirus/"

# countryname="turkey"

def coronastats(countryname):
        country_name = ''.join([countryname,"/"])
        mywebpage = requests.get(URL)
        mytree = BeautifulSoup(mywebpage.content, 'html.parser')
        nbr_france = mytree.find(href="".join(["country/",country_name])).find_next("td").text
        resultat = "There are {} people infected by Coronavirus in {} \n".format(nbr_france, countryname)
        # print(resultat)
        return resultat

def getcountrylist():
        countryname_list=[]
        mywebpage = requests.get(URL)
        mytree = BeautifulSoup(mywebpage.content, 'html.parser')
        countrynames = mytree.find_all("a", class_="mt_a")
        for countrytag in countrynames:
            countryname_list.append(countrytag["href"])
#        for c in countryname_list:
#            print(c.split('/')[1])
        # return(str(country) for country in countryname_list)
        return("\n".join([str(country).split('/')[1] for country in countryname_list]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("option", help='OPTIONS: getcountrylist || countryname', type=str)
    args = parser.parse_args()
    if (args.option == "getcountrylist"):
        getcountrylist()
    else:
        countryname = args.option
        coronastats(countryname)
