import re
import time
import sys
import os

try:
    process_file = sys.argv[1]
except IndexError:
    print("No file path has been specified.\nWhich files would you like to process?")
    process_file = input()

start_time = time.time()

regex = r"Street name: (.+?)\nHouse number: (.+?)\nCity: (.+?)\nState: (.+?)\nPostal code: (.+?)\nCountry:.+?\""
subst = "\\g<2> \\g<1>, \\g<3>, \\g<4> \\g<5>\""

name, ext =os.path.splitext(process_file)

oldFile = open(process_file, "r")
newFile = open(name + "_FORMATTED" + ext, "w")

newFile.write(re.sub(regex, subst, oldFile.read(), 0, re.DOTALL))

end_time = time.time()
print("executed in", end_time - start_time, "seconds!")