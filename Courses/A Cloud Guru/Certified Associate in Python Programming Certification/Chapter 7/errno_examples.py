import errno
import os

try:
    f = open("fake.txt")
except OSError as err:
    if err.errno == errno.ENOENT:
        print("File not found")
        print(f"{err.errno}, ({errno.errorcode[err.errno]}), {os.strerror(err.errno)}")
    elif err.errno == errno.EACCES:
        print("Bad permissions")
