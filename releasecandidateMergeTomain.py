import subprocess #bibliotek för att köra konsol komandon och hantera dess output

#Sant: Om den ska printa commandon till consolen
#Falsk: Om den ska utföra commandon
DEBUG = False

versionfilepath = "version.data" #versions data filen

gitmergecommand = "git merge" #kommandot för git merge
gitswitchbranch = "git switch" #kommandot för git switch (byta branch)
gitgetbranchcommand = "git rev-parse --abbrev-ref HEAD" #kommandot för att få endast namnet på nuvarande branch (avancerat)

branchtype = "release" #prefixet för alla release branch
sourcebranchname = "main" #namnet på branchen som det ska mergas till
destinationbranchname: str #variabel för namnet på branchen som ska mergas

startbranchname = subprocess.getoutput(gitgetbranchcommand) #namnet på nuvarande branch

#kollar om nuvarande branch inte är en release branch
if not startbranchname.startswith(branchtype): #om det inte är en release branch
    version: str #variabel för versionsnummer
    versionfile = open(versionfilepath, "r") #öppna versionsfilen
    version = versionfile.readline() #spara rad 1 ur versionfilen till versions variabeln 
    versionfile.close() #stäng versionsfilen

    destinationbranchname = f"{branchtype}_{version}" #sätt destinations branch namnet
else: #om det är en release branch
    destinationbranchname = startbranchname #sätt destinations branch namnet

output_gitswitchbranchcommand = f"{gitswitchbranch} {sourcebranchname}" #kommandot för att byta till main branchen
print(output_gitswitchbranchcommand) if DEBUG else None
subprocess.call(output_gitswitchbranchcommand) if not DEBUG else None

output_gitmergecommand = f"{gitmergecommand} {destinationbranchname}" #kommandot för att merga main branchen med release branchen
print(output_gitmergecommand) if DEBUG else None
subprocess.call(output_gitmergecommand) if not DEBUG else None


