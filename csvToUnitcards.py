import csv

def modifyFilename(filename, string):
    # modifies filename to include string after filename but before extension
    # assumes provided string for filename has an extension
    index = filename.rfind(".")
    return filename[:index] + "_" + string + filename[index:]

def changeExtension(filename, extension):
    index = filename.rfind(".")
    return filename[:index] + "." + extension

def csvToUnitcard(filename):
    # takes a csv of data to populate unitcards, outputs a .txt file of unitcards
    # must be formatted exactly like example csv, including header
    with open(filename, 'r', encoding='utf8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)
        newFilename = changeExtension(modifyFilename(filename, "unitcardV2"), "txt")
        with open(newFilename, 'w', encoding='utf8') as unitcardfile:
            lines = []
            for row in csvreader:
                print(row)
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
    return

def unitcardToCsv(filename):
    # takes .txt of a block of formatted unitcards, returns a csv with filled categories based on provided unitcards
    #TODO
    return

def unitlistToUnitcard(filename):
    # takes .txt of Kkentaro's unitlist, returns .txt file of unitcards
    #TODO
    return

def unitcardToUnitlist(filename):
    # takes .txt of unitcards, returns .txt file of Kkentaro's unitlist
    #TODO
    return

def unitcardToUnitcardV2(filename):
    # takes .txt of Shiny's unitcards, returns .txt file of unitcards
    #TODO
    return

def unitcardV2ToUnitcard(filename):
    # takes .txt of unitcards, returns .txt file of Shiny's unitcards
    #TODO
    return

def unitlistToShinycard(filename):
    return unitcardV2ToUnitcard(unitlistToUnitcard(filename))

def shinycardToUnitlist(filename):
    return unitcardToUnitlist(unitcardToUnitcardV2(filename))