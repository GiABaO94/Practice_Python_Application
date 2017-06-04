# Adding modules (same mean with libraries) to script

from sys import argv

# Unpack whatever in argv => assign it to all variables on the left 
"""
Fix Bug
Because Visual Studio can't catch agrument so we should choose Project -> Property -> Debug. Entering the value of agruments which appear in this code
"""
script, first , second = argv

# Writting code

print ("This is a ", script)
print ("This is the ", first)
print ("This is the ", second)