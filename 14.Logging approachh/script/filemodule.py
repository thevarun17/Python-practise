import json

def extractInputData(filename):
    fvar = open(filename, 'r')
    data = fvar.readlines()
    fvar.close()
    return data
a= extractInputData('newcountries.txt')
print(a)




def processFiledata(fdata):
    countries = {}
    for x in fdata:
        countryname = x.split('#')[0]
        tempres = countries.get(countryname, "NA")

        if(tempres == "NA"):
            countries[countryname] = []
            countries[countryname].append(x.split('#')[1])
        else:
            countries[countryname].append(x.split('#')[1])

    return countries

#
def createOutputFile(jsondata):
    fvar = open ('filename')
    json.dump(jsondata,fvar)
    fvar.close()
    return "success"
