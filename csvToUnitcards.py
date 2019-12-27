def modifyFilename(filename, string):
    # modifies filename to include string after filename but before extension
    # assumes provided string for filename has an extension
    index = filename.rfind(".")
    return filename[:index] + "_" + "string" + filename[index:]

def csvToUnitcard(filename):
    # takes a csv of data to populate unitcards, outputs a .txt file of unitcards
    #TODO
    newFilename = modifyFilename(filename, "unitcardV2")
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