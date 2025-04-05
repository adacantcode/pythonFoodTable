# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
from pathlib import Path

greenColor = "#D0F0C0"
redColor = "#FF9377"
yellowColor = "#FCF75E"
greyColor = "#dddddd"

guildPeople = ["Acen.8513","Adaba.4635","Ajinka.9273","Ambroid.5087","Annael.1028","Arashid.7943","Ast.9853","Atheshy.8790","Ayiri.8214","Ayiri.8630","Ba nana.2340","beowulf.1783","Bersox.5138",
               "Beskyd.6143","Biordan.8453","Blackerczcz.8209","brii.1203","Cornellius.6901","Corruptor.2570","CryHeroCZ.1924","Damin.1203","Darkbeast.4613","Deisn.5034","dellamorte.3658","Draczeq.2078","Dreedo.6974","Eli Ska.3451","Ernedar.2937",
               "eSko.7630","exi.4032","Exitburn.6132","fidak.5094","Frost.6183","Gandalaaaf.1867","Godrox.7160","Golema.9674","HeTeD.6749","Hirani.5963","Charlie Hegemon.7638","Chatul.5947","jaktichu.6057","JamboCz.1329","jirkavili.5934",
               "JorMiSeK.3649","kaylinay.9415","Kikos.1205","Kiksyame.3861","Kraska.5241","Kriss.7514","LagnaR.6958","Laufres.4307","LemoNaj.3085","Linnie.8602","Lucius.2647","Ludanek.9057","Majlo.8346","Marketa.4385","marty.5306","Marwww.1824",
               "maxwus.4021","McCrowley.3940","Melina.2178","merklys.8741","Merzin.5012","milbob.9408","Morlinest.8531","MrHancl.3021","Muffi.1957","MyshCZ.1754","Narky.2190","Naxder.5102","Nikolas.7841","NixoCZ.6453","Nufichan.2967","OakShire.7086",
               "Orangebad.3107","Partysak.4806","paulie.5972","Paulie.9148","Pecar.1236","Pepan.2695","Petrovic.3765","Puly.7048","Quasha.4768","Quiteczko.5892","Raisier.4529","Ramundul.7864","Rize.2579","Rorschach.7406","Rouba.2047","roze.9715",
               "rykymary.5721","Sarlotka.1072","sedmi.8124","Settes.3960","Sherincal.4579","Sindroel.8604","SkipperCZ.6912","Skodak.8903","Spikeryno.9534","stafroncz.9651","Stefany.4160","StuartCZ.7365","Sunkam.1058","Sysel.1265","Tanus.5920",
               "Telrenth.2807","Tempest.8716","theMinarii.6158","tomekbobek.5106","Trauma.2037","Trivius.5097","VLK.4173","Vojta.4586","vopice.2075","VyzobanaSlunecnice.8076","Waggy.8327","wilimakar.9573","Wolfton.9501","Wolwerine.8064",
               "XanTiack.3714","Zagy.1250","Zajacik.1786","Zajda.6380","ZdenoMNM.9503","Zelvicka.2467","Zerochan.2704","MallwinCZ.7956"]

healingFoods = ["57100", "69105", "26529"]
powerFoods = ["57051", "69141", "17825", "57244", "57393", "57342", "57241", "57883"]
conceFoods = ["57299", "24797", "57302", "57205", "57178", "57341"]
allFoods = healingFoods + powerFoods + conceFoods
healingUtilities = ["25879"]
powerUtilities = ["9963", "34211", "33297"]
conceUtilities = ["38605"]
allUtilities = healingUtilities + powerUtilities + conceUtilities

warriorConsumables = powerFoods + powerUtilities
berserkerConsumables = powerFoods + powerUtilities
dragonhunterConsumables = powerFoods + powerUtilities
spellbreakerConsumables = powerFoods + powerUtilities
scourgeConsumables = powerFoods + powerUtilities
reaperConsumables = powerFoods + powerUtilities
holosmithConsumables = powerFoods + powerUtilities
untamedConsumables = powerFoods + ["33297"]
chronomancerConsumables = conceFoods + conceUtilities
catalystConsumables = healingFoods + ["38605"]
harbingerConsumables = conceFoods + ["38522"] #38522 - magna sharpening stone
firebrandConsumables = healingFoods + healingUtilities
scrapperConsumables = healingFoods + healingUtilities

gwPictureURL = 'https://wiki.guildwars2.com/images/'
elitePictureURL = 'https://raw.githubusercontent.com/baaron4/GW2-Elite-Insights-Parser/refs/heads/master/GW2EICustomAssets/GW2WikiTango/'
emptyImage = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAAALXRFWHRDcmVhdGlvbiBUaW1lAMSNdCAyNyBixZllIDIwMjUgMTQ6MjM6NTggKzAxMDA0rhY1AAAAB3RJTUUH6QMbDRoiULJiyAAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAARnQU1BAACxjwv8YQUAAABwSURBVHjaY3iswgBE/5MC/xMPkgIhuhggFAn6YTpBmpE5hPWjKmbAFCJSJ1CAAZcEQZ1ImvHrxyHFQFgRbkNRNWMqxesdDM2o+vEHBDbNGPpxRQHVNZPvbPIDjPyoIj+RkJ88yc8YlGRJigoDSoohAMQkfR7W+0QRAAAAAElFTkSuQmCC"
otaznikImage="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAIAAAC0Ujn1AAAALHRFWHRDcmVhdGlvbiBUaW1lAHNvIDI5IGLFmWUgMjAyNSAxNjoyOToxNiArMDEwMHC24K8AAAAHdElNRQfpAx0PHxG0+nwpAAAACXBIWXMAAC4jAAAuIwF4pT92AAAABGdBTUEAALGPC/xhBQAAAQJJREFUeNrt1CEOgzAUBmAkAjHBERCISiQSiUD2AEiOwiE4AgLBIRBIxEQFggMgm4w/NJkYG+srNFkyniDQ9/haHhTnYS2ci/4PehzHPM/DMLytgRNcCiGO0k3TuK7rbAKDVVWZ08MweJ4HKE3Ttm3va9R1HUWR0vu+N6SLogCRZdnLuJQSg0hxzg1ptBX3d123TWH5SPm+b0iLNd6m0ArQcRwb0p9inmegoMuyPJN+ukmSoOmn0dM0qc8DR8yxX0ygsUbGGFy8XszxtZ5AY4/ADYJAx6XRaC5obBnNegKtdqbO34NGownq76G/FELpzg46SlOD8oD2GmKRttiQi/5degHvTt/2NX73oQAAAABJRU5ErkJggg=="

foodNames = {
    '57299': ('Plate of Peppercorn-Spiced Poultry Aspic','4/4f/Plate_of_Peppercorn-Spiced_Poultry_Aspic.png'),
    '24797': ('Loaf of Candy Cactus Cornbread','b/b2/Loaf_of_Candy_Cactus_Cornbread.png'),
    '57302': ('Plate of Clove-Spiced Poultry Aspic','5/50/Plate_of_Clove-Spiced_Poultry_Aspic.png'),
    '57205': ('Plate of Sesame Poultry Aspic','6/64/Plate_of_Sesame_Poultry_Aspic.png'),
    '57178': ('Plate of Poultry Aspic with Mint Garnish','9/91/Plate_of_Poultry_Aspic_with_Mint_Garnish.png'),
    '57341': ('Plate of Poultry Aspic with Salsa Garnish','5/5b/Plate_of_Poultry_Aspic_with_Salsa_Garnish.png'),
    '57051': ('Peppercorn-Crusted Sous-Vide Steak','2/2e/Peppercorn-Crusted_Sous-Vide_Steak.png'),
    '69141': ('Mist Infused Peppercorn-Crusted Sous-Vide Steak','2/2e/Peppercorn-Crusted_Sous-Vide_Steak.png'),
    '17825': ('Bowl of Sweet and Spicy Butternut Squash Soup','d/df/Bowl_of_Sweet_and_Spicy_Butternut_Squash_Soup.png'),
    '57244': ('Cilantro Lime Sous-Vide Steak','6/65/Cilantro_Lime_Sous-Vide_Steak.png'),
    '57393': ('Mushroom Clove Sous-Vide Steak','b/ba/Mushroom_Clove_Sous-Vide_Steak.png'),
    '57342': ('Sous-Vide Steak with Mint-Parsley Sauce','9/99/Sous-Vide_Steak_with_Mint-Parsley_Sauce.png'),
    '57241': ('Soy-Sesame Sous Vide Steak','d/da/Soy-Sesame_Sous-Vide_Steak.png'),
    '57883': ('Plate of Spicy Moa Wings','f/ff/Plate_of_Spicy_Moa_Wings.png'),
    '57100': ('Bowl of Fruit Salad with Mint Garnish','4/47/Bowl_of_Fruit_Salad_with_Mint_Garnish.png'),
    '69105': ('Mist Infused Bowl of Fruit Salad with Mint Garnish','4/47/Bowl_of_Fruit_Salad_with_Mint_Garnish.png'),
    '26529': ('Delicious Rice Balls','5/5d/Delicious_Rice_Ball.png'),
    '46587': ('Malnourished', '6/67/Malnourished.png')
}

utilityNames = {
    '9963': ('Superior Sharpening Stone', '7/78/Superior_Sharpening_Stone.png'), #power
    '34211': ('Tin of Fruitcake','a/af/Tin_of_Fruitcake.png'), #power
    '25879': ('Bountiful Maintenance Oil', '5/5b/Master_Maintenance_Oil.png'), #heal
    '38605': ('Magnanimous Maintenance Oil', '5/53/Magnanimous_Maintenance_Oil.png'), #conce
    '33297': ('Writ of Masterful Strength', '2/2b/Writ_of_Masterful_Strength.png'), #power
    '9968': ('Master Maintenance Oil', '5/5b/Master_Maintenance_Oil.png'), #
    '46668': ('Diminished','7/71/Diminished.png'),
    '9283': ('Reinforced Armor', '8/83/Reinforced_Armor.png'),
    '38522': ('Magnanimous Sharpening Stone', 'a/aa/Magnanimous_Sharpening_Stone.png'),
    'xxxx': ('Potent Superior Sharpening Stone', '7/78/Superior_Sharpening_Stone.png'), #power
    'xxxy': ('Ogre Sharpening Stone', '7/78/Superior_Sharpening_Stone.png'), #power
    'xxxv': ('Mist-Infused Maintenance Oil', '5/5b/Master_Maintenance_Oil.png'), #heal
    'xxxz': ('Mist-Infused Sharpening Stone', '7/78/Superior_Sharpening_Stone.png') #power
}

allowedSpecs = {
    "Warrior": warriorConsumables,
    "Berserker": berserkerConsumables,
    "Dragonhunter": dragonhunterConsumables,
    "Spellbreaker": spellbreakerConsumables,
    "Scourge": scourgeConsumables,
    "Reaper": reaperConsumables,
    "Holosmith": holosmithConsumables,
    "Untamed": untamedConsumables,
    "Firebrand": firebrandConsumables,
    "Scrapper": scrapperConsumables,
    "Catalyst": catalystConsumables,
    "Harbinger": harbingerConsumables,
    "Chronomancer": chronomancerConsumables
}


specImages = {
    'Warrior': 'Warrior_tango_icon_20px.png',
    'Berserker': 'Berserker_tango_icon_20px.png',
    'Spellbreaker': 'Spellbreaker_tango_icon_20px.png',
    'Bladesworn': 'Bladesworn_tango_icon_20px.png',
    'Guardian': 'Guardian_tango_icon_20px.png',
    'Dragonhunter': 'Dragonhunter_tango_icon_20px.png',
    'Firebrand': 'Firebrand_tango_icon_20px.png',
    'Willbender': 'Willbender_tango_icon_20px.png',
    'Necromancer': 'Necromancer_tango_icon_20px.png',
    'Scourge': 'Scourge_tango_icon_20px.png',
    'Reaper': 'Reaper_tango_icon_20px.png',
    'Harbinger': 'Harbinger_tango_icon_20px.png',
    'Engineer': 'Engineer_tango_icon_20px.png',
    'Holosmith': 'Holosmith_tango_icon_20px.png',
    'Scrapper': 'Scrapper_tango_icon_20px.png',
    'Mechanist': 'Mechanist_tango_icon_20px.png',
    'Ranger': 'Ranger_tango_icon_20px.png',
    'Untamed': 'Untamed_tango_icon_20px.png',
    'Soulbeast': 'Soulbeast_tango_icon_20px.png',
    'Druid': 'Druid_tango_icon_20px.png',
    'Elementalist': 'Elementalist_tango_icon_20px.png',
    'Catalyst': 'Catalyst_tango_icon_20px.png',
    'Tempest': 'Tempest_tango_icon_20px.png',
    'Weaver': 'Weaver_tango_icon_20px.png',
    'Mesmer': 'Mesmer_tango_icon_20px.png',
    'Chronomancer': 'Chronomancer_tango_icon_20px.png',
    'Mirage': 'Mirage_tango_icon_20px.png',
    'Virtuoso': 'Virtuoso_tango_icon_20px.png',
    'Revenant': 'Revenant_tango_icon_20px.png',
    'Renegade': 'Renegade_tango_icon_20px.png',
    'Herald': 'Herald_tango_icon_20px.png',
    'Vindicator': 'Vindicator_tango_icon_20px.png',
    'Thief': 'Thief_tango_icon_20px.png',
    'Deadeye': 'Deadeye_tango_icon_20px.png',
    'Specter': 'Specter_tango_icon_20px.png',
    'Daredevil': 'Daredevil_tango_icon_20px.png'
}

#load a whole folder
directory = Path("alllogs")
mainDict = {}
numberOfFiles = 0
fightDict = {}

try:
    with open("skills.txt", "r", encoding="utf-8") as file:
        consumablesDictionary = json.load(file)  # json se všemi consumables a jejich obrázky id: [název, img]
except:
    print ("File not found")

try:
    with open("foodimages.txt", "r", encoding="utf-8") as file:
        allFoodImagesDictionary = json.load(file)  # json se všemi consumables a jejich obrázky id: [název, img]
except:
    print("File not found")

try:
    with open("utilityimages.txt", "r", encoding="utf-8") as file:
        allUtilityImagesDictionary = json.load(file)  # json se všemi consumables a jejich obrázky id: [název, img]
except:
    print("File not found")

for file_path in directory.iterdir():
    if file_path.is_file():
        with open(file_path, "r") as file:
            numberOfFiles += 1
            data = json.load(file)
            timeStart = str(data['timeStart']) #each log has a unique starting time of the fight
            timeStart = timeStart[:-4]
            timeStart = timeStart.replace(" ","-")
            fightDict[numberOfFiles] = timeStart
            print (fightDict)

            for player in data["players"]:
                if not (str(player['account']).startswith("Non Squad Player")): # and str(player['account']) in guildPeople:
                    account = str(player['account'])
                    profession = str(player['profession'])
                    buffUptimes = player['buffUptimes']  #načtu všechny buffy, které hráč měl

                    foodId = "0"
                    foodUptime = 0
                    foodImage = emptyImage
                    utilityId= "0"
                    utilityUptime = 0
                    utilityImage = emptyImage
                    bkgColorFood = "#ffffff"
                    bkgColorUtility = "#ffffff"

                    for buff in buffUptimes: #projdu všechny buffy
                        buffId = str(buff['id'])
                        #je tento food buffid v povoleném seznamu pro danou profesi?
                        if profession in allowedSpecs and buffId in allowedSpecs[profession] and buffId in foodNames:
                            foodUptime = buff['buffData'][0].get('uptime', None)
                            foodId = buffId
                            bkgColorFood = greenColor
                        #buff je v jídlech, ale ne pro tuto profesi
                        elif profession in allowedSpecs and buffId in allFoods and buffId in foodNames and buffId not in allowedSpecs[profession]:
                            foodUptime = buff['buffData'][0].get('uptime', None)
                            foodId = buffId
                            bkgColorFood = redColor
                        #je tento utility buffid v povoleném seznamu pro danou profesi?
                        elif profession in allowedSpecs and buffId in allowedSpecs[profession] and buffId in utilityNames:
                            utilityUptime = buff['buffData'][0].get('uptime', None)
                            utilityId = buffId
                            bkgColorUtility = greenColor
                        #buff je v utilitách, ale ne pro tuto profesi
                        elif profession in allowedSpecs and buffId in allUtilities and buffId in utilityNames and buffId not in allowedSpecs[profession]:
                            utilityUptime = buff['buffData'][0].get('uptime', None)
                            utilityId = buffId
                            bkgColorUtility = redColor
                        elif profession not in allowedSpecs:
                            foodUptime = 0
                            foodId = "none"
                            utilityUptime = 0
                            utilityId = "none"
                            bkgColorUtility = greyColor
                            bkgColorFood = greyColor
                        else:
                            pass

                    if foodUptime > 99:
                        foodUptime = 100
                    if foodUptime == 0 and bkgColorFood != greyColor:
                        bkgColorFood = redColor
                    if utilityUptime > 99:
                        utilityUptime = 100
                    if utilityUptime == 0 and bkgColorUtility != greyColor:
                        bkgColorUtility = redColor

                    #žlutá - buff je správný, ale uptime je krátký
                    if bkgColorFood == greenColor and foodUptime < 95:
                        bkgColorFood = yellowColor
                    if bkgColorUtility == greenColor and utilityUptime < 95:
                        bkgColorUtility = yellowColor

                    specImage = elitePictureURL+specImages[profession]

                    #najdeme obrázek pro jídlo
                    try:
                        foodImage = gwPictureURL+foodNames[foodId][1]
                    except:
                        try:
                            foodImage = consumablesDictionary.get(foodId)[1]
                        except:
                            foodImage = otaznikImage

                    try:
                        foodText = foodNames[foodId][0]
                    except:
                        foodText = "???"

                    #najdeme obrázek pro utilitu
                    try:
                        utilityImage = gwPictureURL+utilityNames[utilityId][1]
                    except:
                        if utilityId in consumablesDictionary:
                            utilityImage = consumablesDictionary[utilityId][1]
                        else:
                            utilityImage = otaznikImage

                    try:
                        utilityText = utilityNames[utilityId][0]
                    except:
                        utilityText = "???"

                    #hráč ještě ve slovníku není, založíme mu proto prázdný slovník
                    if account not in mainDict:
                        mainDict[account] = {}

                    #vložíme slovník pro kombinaci hráč + čas
                    mainDict[account][timeStart] = {'profession': profession, 'food': foodId, 'fooduptime': foodUptime, 'foodcolor': bkgColorFood, 'foodimage': foodImage, 'utility': utilityId, 'utilityuptime': utilityUptime, 'utilitycolor': bkgColorUtility, 'utilityimage': utilityImage}

#start the HTML file
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Player List</title>
    <style>
        table {border-collapse: collapse; width: 50%%;}
        th, td {border: 1px solid black; padding: 4px; text-align: left; }
        th {background-color: #f2f2f2;}
    </style>
    
    <style>
        table {
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid black;
            padding: 4px;
            text-align: left;
        }
        tr:hover {
            background-color: #f2f2f2; /* Light gray on hover */
        }
        .highlight td {
            filter: brightness(0.8);
        }
        
        td.highlight {
            filter: brightness(0.8);
}

    </style>
</head>
<body>
<table id="myTable">
<tr>
    <th>Player</th>"""

for i in range(1, numberOfFiles+1):
    html_content += f"""<th>{fightDict[i]}</th>"""

html_content += """</tr>"""

#sortedDict = dict(sorted(mainDict.items()))
sortedDict = mainDict

for player in sortedDict:
    html_content += f"""<tr>"""
    html_content += f"""<td style="background-color: #fefefe;">{player}</td>"""
    for i in range(1, numberOfFiles+1):
        fight = fightDict[i]
        if fight in sortedDict[player]:
            food = sortedDict[player][fight]['food']
            foodImage = sortedDict[player][fight]['foodimage']
            utility = sortedDict[player][fight]['utility']
            utilityImage = sortedDict[player][fight]['utilityimage']
            prof = sortedDict[player][fight]['profession']

            if prof == "none":
                profImage = emptyImage
            else:
                profImage = elitePictureURL + specImages[prof]

            html_content += f"""<td bgcolor={sortedDict[player][fight]['foodcolor']}><img src="{foodImage}" width="20px" height="20px"> - {sortedDict[player][fight]['fooduptime']} <img src="{profImage}" align="right"></td>"""
        else:
            html_content += f"""<td style="background-color: #fefefe;">-</td>"""

    html_content += f"""</tr>"""

    html_content += f"""<tr>"""
    html_content += f"""<td style="border-bottom:3pt solid black; background-color: #fefefe;"></td>"""
    for i in range(1, numberOfFiles + 1):
        fight = fightDict[i]
        if fight in sortedDict[player]:
            food = sortedDict[player][fight]['food']
            foodImage = sortedDict[player][fight]['foodimage']
            utility = sortedDict[player][fight]['utility']
            utilityImage = sortedDict[player][fight]['utilityimage']
            prof = sortedDict[player][fight]['profession']

            if prof == "none":
                profImage = emptyImage
            else:
                profImage = elitePictureURL + specImages[prof]

            html_content += f"""<td bgcolor={sortedDict[player][fight]['utilitycolor']} style="border-bottom:3pt solid black;"><img src="{utilityImage}" width="20px" height="20px"> - {sortedDict[player][fight]['utilityuptime']}</td>"""
        else:
            html_content += f"""<td style="border-bottom:3pt solid black; background-color: #fefefe;">-</td>"""

    html_content += f"""</tr>"""

#konec HTML
html_content = html_content + """
    </table>
    
    
<script>
    document.addEventListener("DOMContentLoaded", function () {
        let table = document.getElementById("myTable");
    
        table.addEventListener("click", function (e) {
            let cell = e.target; 
    
            if (cell.tagName === "TH") {
                // Highlight column when clicking header
                let columnIndex = cell.cellIndex; // Get column index
    
                // Toggle column highlight
                let rows = table.getElementsByTagName("tr");
                let isHighlighted = rows[1].cells[columnIndex].classList.contains("highlight"); // Check if already highlighted
                
                for (let row of rows) {
                    let targetCell = row.cells[columnIndex];
                    if (targetCell) {
                        targetCell.classList.toggle("highlight", !isHighlighted);
                    }
                }
            } 
            
            else if (cell.tagName === "TD") {
                // Highlight row when clicking a <td>
                let clickedRow = cell.closest("tr");
                clickedRow.classList.toggle("highlight");
            }
        });
    });
</script>
    
</body>
</html>
"""

try:
    with open("players02042025.html", "w") as file:
        file.write(html_content)
    print("HTML file written successfully!")
except Exception as e:
    print(f"Error writing HTML file: {e}")

with open("jsondump.txt", "w") as jfile:
    json.dump(mainDict, jfile, indent=4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
