# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 18:22:13 2021

@author: jjosh
"""

import seaborn as sns
import matplotlib.pyplot as plt



import csv
import pandas as pd
countries={"ad":"Andorra",
"ae":"United Arab Emirates",
"af":"Afghanistan",
"al":"Albania",
"am":"Armenia",
"ao":"Angola",
"aq":"Antarctica",
"ar":"Argentina",
"at":"Austria",
"au":"Australia",
"az":"Azerbaijan",
"ba":"Bosnia and Herzegovina",
"bd":"Bangladesh",
"be":"Belgium",
"bf":"Burkina Faso",
"bg":"Bulgaria",
"bh":"Bahrain",
"bi":"Burundi",
"bj":"Benin",
"bn":"Brunei Darussalam",
"bo":"Bolivia, Plurinational State of",
"br":"Brazil",
"bt":"Bhutan",
"bw":"Botswana",
"by":"Belarus",
"bz":"Belize",
"ca":"Canada",
"cd":"Congo, the Democratic Republic of the",
"cf":"Central African Republic",
"cg":"Congo",
"ch":"Switzerland",
"ci":"Cote d’Ivoire",
"cl":"Chile",
"cm":"Cameroon",
"cn":"China",
"co":"Colombia",
"cr":"Costa Rica",
"cu":"Cuba",
"cv":"Cape Verde",
"cy":"Cyprus",
"cz":"Czech Republic",
"de":"Germany",
"dj":"Djibouti",
"dk":"Denmark",
"do":"Dominican Republic",
"dz":"Algeria",
"ec":"Ecuador",
"ee":"Estonia",
"eg":"Egypt",
"eh":"Western Sahara",
"er":"Eritrea",
"es":"Spain",
"et":"Ethiopia",
"fi":"Finland",
"fr":"France",
"ga":"Gabon",
"gb":"United Kingdom",
"ge":"Georgia",
"gf":"French Guiana",
"gh":"Ghana",
"gl":"Greenland",
"gm":"Gambia",
"gn":"Guinea",
"gq":"Equatorial Guinea",
"gr":"Greece",
"gt":"Guatemala",
"gu":"Guam",
"gw":"Guinea-Bissau",
"gy":"Guyana",
"hk":"Hong Kong",
"hn":"Honduras",
"hr":"Croatia",
"ht":"Haiti",
"hu":"Hungary",
"id":"Indonesia",
"ie":"Ireland",
"il":"Israel",
"in":"India",
"iq":"Iraq",
"ir":"Iran, Islamic Republic of",
"is":"Iceland",
"it":"Italy",
"jm":"Jamaica",
"jo":"Jordan",
"jp":"Japan",
"ke":"Kenya",
"kg":"Kyrgyzstan",
"kh":"Cambodia",
"kp":"Korea, Democratic People’s Republic of",
"kr":"Korea, Republic of",
"kw":"Kuwait",
"kz":"Kazakhstan",
"la":"Lao People’s Democratic Republic",
"lb":"Lebanon",
"li":"Liechtenstein",
"lk":"Sri Lanka",
"lr":"Liberia",
"ls":"Lesotho",
"lt":"Lithuania",
"lu":"Luxembourg",
"lv":"Latvia",
"ly":"Libyan Arab Jamahiriya",
"ma":"Morocco",
"mc":"Monaco",
"md":"Moldova, Republic of",
"me":"Montenegro",
"mg":"Madagascar",
"mk":"Macedonia, the former Yugoslav Republic of",
"ml":"Mali",
"mm":"Myanmar",
"mn":"Mongolia",
"mo":"Macao",
"mr":"Mauritania",
"mt":"Malta",
"mu":"Mauritius",
"mv":"Maldives",
"mw":"Malawi",
"mx":"Mexico",
"my":"Malaysia",
"mz":"Mozambique",
"na":"Namibia",
"ne":"Niger",
"ng":"Nigeria",
"ni":"Nicaragua",
"nl":"Netherlands",
"no":"Norway",
"np":"Nepal",
"nz":"New Zealand",
"om":"Oman",
"pa":"Panama",
"pe":"Peru",
"pg":"Papua New Guinea",
"ph":"Philippines",
"pk":"Pakistan",
"pl":"Poland",
"pr":"Puerto Rico",
"ps":"Palestine, State of",
"pt":"Portugal",
"py":"Paraguay",
"re":"Reunion",
"ro":"Romania",
"rs":"Serbia",
"ru":"Russian Federation",
"rw":"Rwanda",
"sa":"Saudi Arabia",
"sc":"Seychelles",
"sd":"Sudan",
"se":"Sweden",
"sg":"Singapore",
"sh":"Saint Helena, Ascension and Tristan da Cunha",
"si":"Slovenia",
"sk":"Slovakia",
"sl":"Sierra Leone",
"sm":"San Marino",
"sn":"Senegal",
"so":"Somalia",
"sr":"Suriname",
"st":"Sao Tome and Principe",
"sv":"El Salvador",
"sy":"Syrian Arab Republic",
"sz":"Swaziland",
"td":"Chad",
"tg":"Togo",
"th":"Thailand",
"tj":"Tajikistan",
"tl":"Timor-Leste",
"tm":"Turkmenistan",
"tn":"Tunisia",
"tr":"Turkey",
"tw":"Taiwan (Republic of China)",
"tz":"Tanzania, United Republic of",
"ua":"Ukraine",
"ug":"Uganda",
"us":"United States",
"uy":"Uruguay",
"uz":"Uzbekistan",
"va":"Holy See (Vatican City State)",
"ve":"Venezuela, Bolivarian Republic of",
"vn":"Viet Nam",
"ye":"Yemen",
"yt":"Mayotte",
"za":"South Africa",
"zm":"Zambia",
"zw":"Zimbabwe"}
lines = csv.reader(open('outputnb.csv'))
dataset = list(lines)
n=0
b=0
nd=0
for i in range(len(dataset)):
    dataset[i] = [(x) for x in dataset[i]]
print(i)
df = pd.DataFrame(dataset, columns =['date', 'open','high','low','close','adclose','vol','company','exe','country'])
#print(df.exe)
a_list =df.country
a_set = set(a_list)
number_of_unique_values = len(a_set)
print(number_of_unique_values)
res = {}



for coun in a_set:
# print(coun)
# print(set(df.company[df[df.country == coun].index.tolist()].tolist()))
    res[coun] = len(set(df.company[df[df.country == coun].index.tolist()].tolist()))



print (res)
#sns.swarmplot(x=df.exe.apply(lambda x: (x)),y=df.country.apply(lambda x: (x)))
import pylab
i=0
def get_key(val):
    for key, value in countries.items():
        if val == value:
            return key

    return 0
dict={}
for idx in (res.keys()):
#print("r ",i," ",idx)
    y = res.get(idx)
    if(get_key(idx)!=0):
        x=get_key(idx)
        dict[x]=y




print(dict)





import pygal

# create a world map
worldmap = pygal.maps.world.World()

# set the title of the map
worldmap.title = 'Countries'
# adding the countries



worldmap.add('Number of companies in Nasdaq, NSE and BSE', dict)

# save into the file
worldmap.render_to_file('country12.svg')

print("Success")