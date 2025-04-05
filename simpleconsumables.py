# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
from pathlib import Path
import sys

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
               "XanTiack.3714","Zagy.1250","Zajacik.1786","Zajda.6380","ZdenoMNM.9503","Zelvicka.2467","Zerochan.2704"]

healingFoods = ["57100", "69105", "26529"]
powerFoods = ["57051", "69141", "17825", "57244", "57393", "57342", "57241", "57883"]
conceFoods = ["57299", "24797", "57302", "57205", "57178", "57341"]
allFoods = healingFoods + powerFoods + conceFoods
healingUtilities = ["25879", "9283"]
powerUtilities = ["9963", "34211", "33297", "9283"]
conceUtilities = ["38605", "9283"]
allUtilities = healingUtilities + powerUtilities + conceUtilities

warriorConsumables = powerFoods + powerUtilities
berserkerConsumables = powerFoods + powerUtilities
dragonhunterConsumables = powerFoods + powerUtilities
spellbreakerConsumables = powerFoods + powerUtilities
scourgeConsumables = powerFoods + powerUtilities
reaperConsumables = powerFoods + powerUtilities
holosmithConsumables = powerFoods + powerUtilities
untamedConsumables = powerFoods + ["33297", "9283"]
chronomancerConsumables = conceFoods + conceUtilities
catalystConsumables = healingFoods + ["38605", "9283"]
harbingerConsumables = conceFoods + ["38522", "9283"] #38522 - magna sharpening stone
firebrandConsumables = healingFoods + healingUtilities
scrapperConsumables = healingFoods + healingUtilities

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

gwPictureURL = 'https://wiki.guildwars2.com/images/'
elitePictureURL = 'https://raw.githubusercontent.com/baaron4/GW2-Elite-Insights-Parser/refs/heads/master/GW2EICustomAssets/GW2WikiTango/'
emptyImage = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAIAAAAC64paAAAALXRFWHRDcmVhdGlvbiBUaW1lAMSNdCAyNyBixZllIDIwMjUgMTQ6MjM6NTggKzAxMDA0rhY1AAAAB3RJTUUH6QMbDRoiULJiyAAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAARnQU1BAACxjwv8YQUAAABwSURBVHjaY3iswgBE/5MC/xMPkgIhuhggFAn6YTpBmpE5hPWjKmbAFCJSJ1CAAZcEQZ1ImvHrxyHFQFgRbkNRNWMqxesdDM2o+vEHBDbNGPpxRQHVNZPvbPIDjPyoIj+RkJ88yc8YlGRJigoDSoohAMQkfR7W+0QRAAAAAElFTkSuQmCC"
otaznikImage="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAIAAAC0Ujn1AAAALHRFWHRDcmVhdGlvbiBUaW1lAHNvIDI5IGLFmWUgMjAyNSAxNjoyOToxNiArMDEwMHC24K8AAAAHdElNRQfpAx0PHxG0+nwpAAAACXBIWXMAAC4jAAAuIwF4pT92AAAABGdBTUEAALGPC/xhBQAAAQJJREFUeNrt1CEOgzAUBmAkAjHBERCISiQSiUD2AEiOwiE4AgLBIRBIxEQFggMgm4w/NJkYG+srNFkyniDQ9/haHhTnYS2ci/4PehzHPM/DMLytgRNcCiGO0k3TuK7rbAKDVVWZ08MweJ4HKE3Ttm3va9R1HUWR0vu+N6SLogCRZdnLuJQSg0hxzg1ptBX3d123TWH5SPm+b0iLNd6m0ArQcRwb0p9inmegoMuyPJN+ukmSoOmn0dM0qc8DR8yxX0ygsUbGGFy8XszxtZ5AY4/ADYJAx6XRaC5obBnNegKtdqbO34NGownq76G/FELpzg46SlOD8oD2GmKRttiQi/5degHvTt/2NX73oQAAAABJRU5ErkJggg=="

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
mainDict = {} #slovník {player : {timestart : (buffid, buffid, buffid) } }
numberOfFiles = 0
fightDict = {} #seznam fightů - id: timestart

for file_path in directory.iterdir():
    if file_path.is_file():
        with open(file_path, "r") as file: #otevřeme log
            numberOfFiles += 1
            print (f"Log {str(numberOfFiles)}")
            data = json.load(file) #natáhneme data z logu
            timeStart = str(data['timeStart']) #each log has a unique starting time of the fight
            timeStart = timeStart[:-4]
            timeStart = timeStart.replace(" ","-")
            fightDict[numberOfFiles] = timeStart #ukládám pořadové číslo fightu a jeho timestamp

            #u každého hráče jednoduše načtu consumables
            for player in data["players"]:
                if not (str(player['account']).startswith("Non Squad Player")): #není-li hráč roamer
                    account = str(player['account'])
                    profession = str(player['profession'])
                    try:
                        consumables = player['consumables']
                    except:
                        consumables = {}

                    #vyrobím si z toho čistý seznam idů consumables
                    idList = [profession]
                    for index, consumable in enumerate(consumables):
                        if consumable['id'] not in idList and consumable['id'] != 17681:
                            idList.append(consumable['id'])

                    #hráč ještě ve slovníku není, založíme mu proto prázdný slovník
                    if account not in mainDict:
                        mainDict[account] = {}

                    #vložíme slovník pro kombinaci hráč + čas
                    mainDict[account][timeStart] = idList

#print (mainDict)

with open("jsondump.txt", "w") as dumpfile:
    json.dump(mainDict, dumpfile, indent=4)

with open("skills.txt", "r", encoding="utf-8") as file:
    consumablesDictionary = json.load(file)  # Load JSON into a Python dictionary

#start the HTML file
html_content = """<!DOCTYPE html>
<html>
<head>
    <title>Player List</title>
    <style>
        table {border-collapse: collapse; width: 50%%; table-layout: fixed;}
        th, td {border: 3px solid black; padding: 0px; text-align: left; width: 100%; white-space: nowrap;}
        th {background-color: #f2f2f2;}
        td img {display: inline-block;}
        
        tr:hover {
            background-color: #f2f2f2; /* Light gray on hover */
        }
        .highlight td {
            filter: brightness(0.8);
        }
        
        td.highlight {
            filter: brightness(0.8);
    </style>
</head>
<body>
<table id="myTable">
<tr>
    <th>Player</th>"""

for i in range(1, numberOfFiles+1):
    html_content += f"""<th>{fightDict[i]}</th>"""

html_content += """</tr>"""

for player in mainDict:
    html_content += f"""<tr>"""
    html_content += f"""<td>{player}</td>"""
    for i in range(1, numberOfFiles+1):
        fight = fightDict[i]
        if fight in mainDict[player]: #hráč byl v tomto fightu
            html_content += f"""<td>"""
            for index, consumable in enumerate(mainDict[player][fight]):
                id = str(consumable)
                if index == 0:
                    image = elitePictureURL+specImages[str(id)]
                    title = str(id)
                    if title in allowedSpecs:
                        bgcolor = greenColor
                        profession = title
                    else:
                        bgcolor = redColor
                        profession = title
                    html_content += f"""<img src="{image}" title="{title}"  width="20px" height="20px" style="padding: 5px; padding-right: 15px; spacing: 0px; background-color: {bgcolor}"> """
                else:
                    try:
                        image = consumablesDictionary.get(id)[1]
                        title = consumablesDictionary.get(id)[0]
                        if profession in allowedSpecs and id in allowedSpecs[profession]:
                            bgcolor = greenColor
                        else:
                            bgcolor = redColor
                    except:
                        image = otaznikImage
                        title = ""
                        bgcolor = greyColor
                    html_content += f"""<img src="{image}" title="{title}"  width="20px" height="20px" style="padding: 5px; spacing=0px; background-color: {bgcolor}">"""

            html_content += f"""</td>"""
        else:
            html_content += f"""<td>-</td>"""

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
    with open("consumables.html", "w") as file:
        file.write(html_content)
    print("HTML file written successfully!")
except Exception as e:
    print(f"Error writing HTML file: {e}")
