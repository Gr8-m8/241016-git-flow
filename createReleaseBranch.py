import subprocess

#Sant: Om den ska printa commandon till consolen
#Falsk: Om den ska utföra commandon
DEBUG = True

#Nycklar för användarinput
KEYS_INPUT_UPDATEMINOR = ["0.0.1", "minor", "-"]
KEYS_INPUT_UPDATE = ["0.1.0", "", "="]
KEYS_INPUT_UPDATEMAJOR = ["1.0.0", "major", "+"]

#Nycklar för versionstexts position
KEY_UPDATE = 2
KEY_UPDATEMINOR = 4
KEYS_UPDATEMAJOR = 0

versionfilepath = "version.data"

#kommand som används för relevanta git funktioner
gitbranchcommand = "git branch" #skapar ny git branch med argumentet branchnamn
gitpushcommand = "git origin push" #lägga up git ändringar på git repositoriet, origin argument branchnamn

#variabler för branshnamn
branchtype = "release" #branchnamn prefix
version: str #branchnamn versionsnummer

#öppna filen version.data och läs dess innehåll till versions variabeln
version_file = open(versionfilepath, "r")
version = version_file.readline()
version_file.close()

#läser användarinput om vilken storlek på uppdateringen
updatev = input("Update Scale:\n> ")
key = KEY_UPDATE
if updatev in KEYS_INPUT_UPDATE: # om input är i Nyckellistan for medelupdatering
    key = KEY_UPDATE
elif updatev in KEYS_INPUT_UPDATEMINOR: # om input är i Nyckellistan for mindre uppdatering
    key = KEY_UPDATEMINOR
elif updatev in KEYS_INPUT_UPDATEMAJOR: # om input är i Nyckellistan for större uppdatering
    key = KEYS_UPDATEMAJOR

version = f"{version[0:key]}{int(version[key])+1}{version[key+1:]}"
#ta versions text variabeln 'version': version
#ta index på numret i versionsnamnet som ska updateras: version[KEY_UPDATE]
#gör texten (som är ett nummer) till ett nummer  int(version[KEY_UPDATE])
#öka numret med 1 int(version[KEY_UPDATE])+1
#sätt det gamla värdet till det nya

#öppnar filen version.txt och skriv version variabeln till den
version_file = open(versionfilepath, "w")
version_file.write(version)
version_file.close()

#skapar branchnamn utifrån prefix och versionsvariabeln
branchname = f"{branchtype}_{version}"

#skapar kommand texten för print eller consol
output_newbranch = f"{gitbranchcommand} {branchname}"
output_pushbranch = f"{gitpushcommand} {branchname}"

if DEBUG: #om DEBUG läge printa
    print(output_newbranch)
    print(output_pushbranch)
else: #om inte DEBUG läge. subprocess.call funktionen skriver till consolen som om en användare skulle göra det
    subprocess.call(output_newbranch)
    subprocess.call(output_pushbranch)