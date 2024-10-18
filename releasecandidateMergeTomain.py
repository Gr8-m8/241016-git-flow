import os
import subprocess

DEBUG = False

versionfilepath = "version.data"

gitmergecommand = "git merge"
gitswitchbranch = "git switch"
gitgetbranchcommand = "git rev-parse --abbrev-ref HEAD"

branchtype = "release"
destinationbranchname = "main"
currentbranchname = subprocess.getoutput(gitgetbranchcommand)

if not currentbranchname.startswith(branchtype):
    version: str
    versionfile = open(versionfilepath, "r")
    version = versionfile.readline()
    versionfile.close()

    output_gitswitchbranchcommand = f"{gitswitchbranch} {branchtype}_{version}"
    print(output_gitswitchbranchcommand) if DEBUG else None
    subprocess.call(output_gitswitchbranchcommand) if not DEBUG else None

output_gitmergecommand = f"{gitmergecommand} {destinationbranchname}"
print(output_gitmergecommand) if DEBUG else None
subprocess.call(output_gitmergecommand) if not DEBUG else None


