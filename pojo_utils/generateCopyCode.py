# Writes statements to copy fields
#
# Call like:
#   python generateCopyCode.py source dest ../../try-dataflow/fieldsAndTypes.csv ","
#
# Suppose the fieldsAndTypes.csv file contains something like:
#   omit_bo, blabla...
#   omit_bo_status, blabla...
#   ...
#
# Then it produces output like:
#   dest.setOmit_bo(source.getOmit_bo());
#   dest.setOmit_bo_status(source.getOmit_bo_status());
#   ...
#

from sys import argv;

sourceVariable = argv[1]
destVariable = argv[2]

# The file may contain other data.
# Fields are separated by customizable field separator
fieldsFile = argv[3]

sep = argv[4]

def capitalizeFirstLetter(s) :
    if len(s) >= 0 :
        firstChar = s[0]
        firstChar = firstChar.upper()
        return firstChar + s[1:]

def getGetter(s) :
    return "get" + capitalizeFirstLetter(s)

def getSetter(s) :
    return "set" + capitalizeFirstLetter(s)

with open(fieldsFile, "rb") as f :
    lines = f.read().split('\n')
    lines = [line.strip() for line in lines]
    lines = [line for line in lines if (len(line) >= 1)]
    for line in lines :
        record = line.split(sep)
        field = record[0].strip()
        getter = getGetter(field)
        setter = getSetter(field)
        get = getGetter(field)
        print destVariable + "." + setter + "(" + sourceVariable + "." + getter + "());"




