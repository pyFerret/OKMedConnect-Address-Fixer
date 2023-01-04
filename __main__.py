import re
import time
import sys
import os
from datetime import datetime

try:
    process_file = sys.argv[1]
except IndexError:
    print("No file path has been specified.\n"
          "Which files would you like to process?")
    process_file = input()

datecheck = True
try:
    file_date = sys.argv[2]
except IndexError:
    print("No date has been specified.\n"
          "What date would you like to input?")
    file_date = input()

while datecheck:
    try:
        match = re.search(r'\d{4}-\d{2}-\d{2}', file_date)
        date = datetime.strptime(match.group(), '%Y-%m-%d').date()
        datecheck = False
    except AttributeError:
        print("Invalid Date. Please use the format 'YYYY-MM-DD'")
        file_date = input()
    except ValueError:
        print("Invalid Date. Please use possible values")
        file_date = input()


start_time = time.time()

print("processing:", end=" ")

regex_address = r"Street name:\s{0,}(.+?)\n" \
                r"House number:\s{0,}(.+?)\n" \
                r"City:\s{0,}(.+?)\n" \
                r"State:\s{0,}(.+?)\n" \
                r"Postal code:\s{0,}(.+?)\n" \
                r"Country:.+?\""
subst_address = "\\g<2> \\g<1>, \\g<3>, \\g<4> \\g<5>\""
print("■", end="")

regex_bridges = r"\n\"?Bridges(.*?),"
subst_bridges = "\nBridges Health,"
print("■", end="")


regex_date = r"(.+)\n"
subst_date = "\\g<1>, " + str(date) + "\n"
print("■", end="")

regex_topline = r"\"Billing Responsibility\"," \
                r"UID," \
                r"\"First Name\"," \
                r"\"Last Name\"," \
                r"\"Date of Birth\"," \
                r"\"Date of Service\"," \
                r"\"Pickup Facility\"," \
                r"\"Pickup Address\"," \
                r"\"Destination Facility\"," \
                r"\"Destination Address\"," \
                r"\"Price Quoted\".{12}\n"
print("■", end="")

subst_topline = ""
print("■")

print("writing:", end=" ")

name, ext = os.path.splitext(process_file)
with open(process_file, "r") as oldFile, open(name + "_FORMATTED" + ext, "w") as newFile:
    print("■", end="")

    write = re.sub(regex_address, subst_address, oldFile.read(), 0)
    print("■", end="")
    write = re.sub(regex_bridges, subst_bridges, write, 0)
    print("■", end="")
    write = re.sub(regex_date, subst_date, write, 0)
    print("■", end="")
    write = re.sub(regex_topline, subst_topline, write, 0)
    print("■", end="")

    newFile.write(write)
    print("■")


end_time = time.time()
print("executed in", end_time - start_time, "seconds!")
