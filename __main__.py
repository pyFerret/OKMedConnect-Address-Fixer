import re
import time
import sys
import os
from datetime import datetime

try:
    process_file = sys.argv[1]
except IndexError:
    print("No file path has been specified.\nWhich files would you like to process?")
    process_file = input()

start_time = time.time()

regex_address = r"Street name:\s{0,}(.+?)\n" \
                r"House number:\s{0,}(.+?)\n" \
                r"City:\s{0,}(.+?)\n" \
                r"State:\s{0,}(.+?)\n" \
                r"Postal code:\s{0,}(.+?)\n" \
                r"Country:.+?\""
subst_address = "\\g<2> \\g<1>, \\g<3>, \\g<4> \\g<5>\""

regex_bridges = r"\n\"?Bridges(.*?),"
subst_bridges = "\nBridges Health,"

name, ext = os.path.splitext(process_file)

match = re.search(r'\d{4}-\d{2}-\d{2}', name)
date = datetime.strptime(match.group(), '%Y-%m-%d').date()

regex_date = r"(.+)\n"
subst_date = "\\g<1>, " + str(date) + "\n"

regex_topline = r"\"Billing Responsibility\"," \
                r"\"Name of Billing Responsibility\"," \
                r"UID," \
                r"\"First Name\"," \
                r"\"Last Name\"," \
                r"\"Date of Birth\"," \
                r"\"Date of Service\"," \
                r"\"Pickup Facility\"," \
                r"\"Pickup Address\"," \
                r"\"Destination Facility\"," \
                r"\"Destination Address\".{12}\n"
subst_topline = ""

oldFile = open(process_file, "r")
newFile = open(name + "_FORMATTED" + ext, "w")

write = re.sub(regex_address, subst_address, oldFile.read(), 0)
write = re.sub(regex_bridges, subst_bridges, write, 0)
write = re.sub(regex_date, subst_date, write, 0)
write = re.sub(regex_topline, subst_topline, write, 0)

newFile.write(write)

end_time = time.time()
print("executed in", end_time - start_time, "seconds!")
