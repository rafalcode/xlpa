#!/usr/bin/env python2
# let's see if I can get pandas to read in an Excel
import sys
import pandas as pd

argquan=len(sys.argv)
if argquan != 2:
   print "This script requires one argument"
   sys.exit(2)

# refer to arguments with sys.argv[1] etc.

# xl = pd.ExcelFile(sys.argv[1])
xl = pd.read_excel(sys.argv[1], dtype=object)
snl=xl.sheet_names
df = xl.parse(snl[0])
print df.head()
