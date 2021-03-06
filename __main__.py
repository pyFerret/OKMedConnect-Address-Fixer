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

regex_address = r"Street name:\s{0,}(.+?)\n" \
                r"House number:\s{0,}(.+?)\n" \
                r"City:\s{0,}(.+?)\n" \
                r"State:\s{0,}(.+?)\n" \
                r"Postal code:\s{0,}(.+?)\n" \
                r"Country:.+?\""
subst_address = "\\g<2> \\g<1>, \\g<3>, \\g<4> \\g<5>\""

regex_bridges = r"\"?Bridges(.*?),"
subst_bridges = "Bridges Health,"

name, ext = os.path.splitext(process_file)

oldFile = open(process_file, "r")
newFile = open(name + "_FORMATTED" + ext, "w")

write = re.sub(regex_address, subst_address, oldFile.read(), 0)
write = re.sub(regex_bridges, subst_bridges, write, 0)

newFile.write(write)

end_time = time.time()
print("executed in", end_time - start_time, "seconds!")
