# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 9a Activity 1b
# Date:         November 3, 2021

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
# Names:        Elayne Elphingstone
#               Reagan Wall
#               Logan Winship
#               Tyler Mayou & Zack Abbott
# Section:      472/572
# Assignment:   Lab 9a Activity 1a
# Date:         November 3, 2021

#open file and read file to single string for splitting into passports
inputTXT = open("./Lab9a_input.txt", "r+")
instring = inputTXT.read()
inputTXT.close()
#list will contain passports in order
passportlist = []

#seperating input string into passports and adding to list
for i in range(instring.count("\n\n")):
    passportlist.append(instring[:instring.index("\n\n")])
    instring = instring[instring.index("\n\n") + 2:]

#removing newline characters from every passport in the list
for i in range(len(passportlist)):
    for j in range(passportlist[i].count("\n")):
        passportlist[i] = passportlist[i][:passportlist[i].index("\n")] + " " + passportlist[i][passportlist[i].index("\n") + 1:]

#turning each passport in the list into a dictionary
for i in range(len(passportlist)):
    tempdict = {}
    for j in range(passportlist[i].count(":")):
        try:
            tempdict[passportlist[i][:passportlist[i].index(":")]] = passportlist[i][passportlist[i].index(":")+1:passportlist[i].index(" ")]
            passportlist[i] = passportlist[i][passportlist[i].index(" ") + 1:]
        except ValueError:
            tempdict[passportlist[i][:passportlist[i].index(":")]] = passportlist[i][passportlist[i].index(":")+1:]
    passportlist[i] = tempdict

for i in range(len(passportlist)):
    try:
        if not (1920 <= int(passportlist[i]["byr"]) <= 2005):
            int("string")
        if not (2011 <= int(passportlist[i]["iyr"]) <= 2021):
            int("string")
        if not (2021 <= int(passportlist[i]["eyr"]) <= 2031):
            int("string")
        height = passportlist[i]["hgt"]
        if height[-2:] == "cm":
            height = height[:-2]
            if not (150 < int(height) < 193):
                int("string")
        elif height[-2:] == "in":
            height = height[:-2]
            if not (59 < int(height) < 76):
                int("string")
        else:
            int("string")
        haircolor = str(passportlist[i]["hcl"])
        #"""
        if haircolor[0:1] == "#":
            if not (len(haircolor[1:]) == 6):
                int("string")
        else:
            int("string")
        #"""
        eyecolorlist = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not (passportlist[i]["ecl"] in eyecolorlist):
            int("string")
        if not (len(passportlist[i]["pid"]) == 9):
            int("string")
    except KeyError:
        passportlist[i] = None
    except ValueError:
        passportlist[i] = None
    except TypeError:
        print(passportlist[i]['hcl'])
        passportlist[i] = None

outputTXT = open("./Lab9a_Act1b_valid.txt", "w") 

count = 0
for item in passportlist:
    if item != None:
        count += 1
        outputTXT.write("pid:{} hcl:{} iyr:{} byr:{} ecl:{} hgt:{} eyr:{}\n".format(item["pid"],item["hcl"],item["iyr"],item["byr"],item["ecl"],item["hgt"],item["eyr"]))

outputTXT.close()

print("There are {} valid passports".format(count))
