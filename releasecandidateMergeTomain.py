import subprocess

DEBUG = False

versionfilepath = "version.data"

gitmergecommand = "git merge"
gitswitchbranch = "git switch"
gitgetbranchcommand = "git rev-parse --abbrev-ref HEAD"

branchtype = "release"
sourcebranchname = "main"
destinationbranchname: str

startbranchname = subprocess.getoutput(gitgetbranchcommand)

if not startbranchname.startswith(branchtype):
    version: str
    versionfile = open(versionfilepath, "r")
    version = versionfile.readline()
    versionfile.close()

    destinationbranchname = f"{branchtype}_{version}"
else:
    destinationbranchname = startbranchname

output_gitswitchbranchcommand = f"{gitswitchbranch} {sourcebranchname}"
print(output_gitswitchbranchcommand) if DEBUG else None
subprocess.call(output_gitswitchbranchcommand) if not DEBUG else None

output_gitmergecommand = f"{gitmergecommand} {destinationbranchname}"
print(output_gitmergecommand) if DEBUG else None
subprocess.call(output_gitmergecommand) if not DEBUG else None


