#!/usr/bin/env python2
# let's see if I can get pandas to read in an Excel
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
print len(snl)
print "But if there are seevral worksheets, we have to take one and convert it into a dataframe"
print "In this case, we take the third one"
df = xl.parse(snl[2])
print df.head()
# the size attribute does not give an error, but it's unclear what it says.
# print df.size
# A more telling one perhaps is shape
print df.shape
print df.iloc[0,:]

print "Lessons:"
print "* pandas attempts to detect a header in the excel sheet, and will exclude it from data if positive"
