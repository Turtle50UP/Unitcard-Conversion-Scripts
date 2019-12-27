import csv

labels = [
    "Name",
    "CC",
    "Level",
    "Skill",
    "Affection",
    "Cost Reduction",
    "Note",
    "Nickname"
]

def modifyFilename(filename, string):
    # modifies filename to include string after filename but before extension
    # assumes provided string for filename has an extension
    index = filename.rfind(".")
    return filename[:index] + "_" + string + filename[index:]

def changeExtension(filename, extension):
    index = filename.rfind(".")
    return filename[:index] + "." + extension

def csvToUCV2(filename):
    # takes a csv of data to populate unitcards, outputs a .txt file of unitcards
    # must be formatted exactly like example csv, including header
    with open(filename, 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        newFilename = changeExtension(modifyFilename(filename, "unitcardV2"), "txt")
        with open(newFilename, 'w', encoding='utf8') as unitcardfile:
            lines = []
            for row in csvreader:
                line = ("{{UnitcardV2"+
                        (("|name=" + row[0]) if row[0] else '') +
                        (("|cc=" + row[1]) if row[1] else '') +
                        (("|level=" + row[2]) if row[2] else '') +
                        (("|Skill=" + row[3]) if row[3] else '') +
                        (("|aff=" + row[4]) if row[4] else '') +
                        (("|CR=" + row[5]) if row[5] else '') +
                        (("|note=" + row[6]) if row[6] else '') +
                        (("|nickname=" + row[7]) if row[7] else '') +
                        "}}\n")
                lines.append(line)
            lines.append("{{clr}}")
            unitcardfile.writelines(lines)
    return newFilename

def ucv2ToCsv(filename):
    # takes .txt of a block of formatted unitcards, returns a csv with filled categories based on provided unitcards
    with open(filename, 'r', encoding="utf8") as ucv2file:
        lines = ucv2file.readlines()[:-1]
        newFilename = changeExtension(modifyFilename(filename, "csv"), "csv")
        with open(newFilename, 'w', encoding="utf8", newline="") as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            rows = []
            rows.append(labels)
            for line in lines:
                elems = line[2:-3].split('|')[1:]
                index = 0
                curRow = ["", "", "", "", "", "", "", ""]
                for i in range(len(labels)):
                    if index >= len(elems):
                        break
                    elem = elems[index]
                    if "name=" in elem and "nickname=" not in elem:
                        curRow[0] = elem.split("name=")[-1]
                    elif "cc=" in elem:
                        curRow[1] = elem.split("cc=")[-1]
                    elif "level=" in elem:
                        curRow[2] = elem.split("level=")[-1]
                    elif "Skill=" in elem:
                        curRow[3] = elem.split("Skill=")[-1]
                    elif "aff=" in elem:
                        curRow[4] = elem.split("aff=")[-1]
                    elif "CR=" in elem:
                        curRow[5] = elem.split("CR=")[-1]
                    elif "note=" in elem:
                        curRow[6] = elem.split("note=")[-1]
                    elif "nickname=" in elem:
                        curRow[7] = elem.split("nickname=")[-1]
                    index += 1
                for j in range(len(curRow)):
                    curRow[j].strip()
                rows.append(curRow)
            csvwriter.writerows(rows)
    return newFilename

def unitlistToCsv(filename):
    # takes .txt of Kkentaro's unitlist, returns .txt file of unitcards
    with open(filename, 'r', encoding="utf8") as ulfile:
        lines = ulfile.readlines()[1:-1]
        newFilename = changeExtension(modifyFilename(filename, "csv"), "csv")
        with open(newFilename, 'w', encoding="utf8", newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=',')
            rows = []
            rows.append(labels)
            for line in lines:
                elems = line[2:-3].split('|')[1:]
                index = 0
                curRow = ["", "", "", "", "", "", "", ""]
                for i in range(len(labels)):
                    if index >= len(elems):
                        break
                    elem = elems[index]
                    if "name=" in elem:
                        curRow[0] = elem.split("name=")[-1].strip()
                    elif "rank=" in elem:
                        curRow[1] = elem.split("rank=")[-1].strip()
                        if len(curRow[1]) == 0:
                            curRow[1] = "base"
                    elif "level=" in elem:
                        curRow[2] = elem.split("level=")[-1].strip()
                        if len(curRow[2]) == 0:
                            curRow[2] = "1"
                    elif "skill=" in elem or "saw=" in elem:
                        if "skill=" in elem and len(curRow[3]) == 0:
                            curRow[3] = elem.split("skill=")[-1].strip()
                            if len(curRow[3]) == 0:
                                curRow[3] = "1"
                        elif "saw=" in elem:
                            curRow[3] = "SAW"
                    elif "cr=" in elem:
                        curRow[5] = elem.split("cr=")[-1].strip()
                        if len(curRow[5]) == 0:
                            curRow[5] = "0"
                    elif "alias=" in elem:
                        curRow[7] = elem.split("alias=")[-1].strip()
                    index += 1
                rows.append(curRow)
            csvwriter.writerows(rows)
    return newFilename

def csvToUnitlist(filename):
    # takes .txt of unitcards, returns .txt file of Kkentaro's unitlist
    #TODO
    return

def unitlistToUCV2(filename):
    return csvToUCV2(unitlistToCsv(filename))