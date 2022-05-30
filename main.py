import os, sys, lib

try:
    if os.getuid() != 0:
        lib.fail(lib.FAIL+"Run script as admin to continue with installation."+lib.ENDC)
except:
    lib.fail("Run script on linux to continue with installation.")

