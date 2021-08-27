"""
Examples of the standard 'platform' module.
"""
import platform

print(f"The attributes and methods of platform are {dir(platform)} \n")

print(f"The system is {platform.system()}")
print(f"The uname is {platform.uname()}")
print(f"The release is {platform.release()} \n")


print(f"The python version is {platform.python_version()}")
