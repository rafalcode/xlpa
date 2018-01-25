#!/usr/bin/env python2
# will read an excel but will assume there is only one worksheet
import sys
import pandas as pd

argquan=len(sys.argv)
if argquan != 2:
   print "This script requires one argument"
   sys.exit(2)

# refer to arguments with sys.argv[1] etc.

xl = pd.ExcelFile(sys.argv[1])
# the following may work in some circumstance, but it does not have sheet_names method:
# xl = pd.read_excel(sys.argv[1], dtype=object)
snl=xl.sheet_names
snlsz=len(snl)
if snlsz >1:
    print "Sorry max. one worksheet in your spreadsheet is allowed"

df = xl.parse(snl[0])
print df.head()
# the size attribute does not give an error, but it's unclear what it says.
# print df.size
# A more telling one perhaps is shape
print df.shape
print df.iloc[0,:]
