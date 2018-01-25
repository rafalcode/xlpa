#!/usr/bin/env python2
# assumes we shall work on  pathway.txt file which has been converted from Excel.
import sys, regex
import pandas as pd

argquan=len(sys.argv)
if argquan != 2:
   print "This script requires one argument"
   sys.exit(2)


d = pd.read_csv(sys.argv[1], sep='\t')
# d.values will render the meomoize data is arrays of arrays, etc.
# print d.shape # will give you the dimensions ... (12,12) in pathanalysis case
# print "Your tsv has dimension and size %i
# print d.size
# print "%s %s" % (d[0], d[4])
# print d.iloc[0][0]
# print d.iat[0,0]
# christ, finally this works


# OK, now able to grab col0 and col11
# print d.iloc[:,[0,11]]
# can convert this into a dict of list
RGX0=regex.compile(r'\/\/')
csz=len(d.iloc[:,11])
# print "Length on column 11 is %i" % csz
# for c in d.iloc[:,11]:
print "list of Pathways and implicated genes:"
for i in xrange(csz):
    lm=RGX0.split(d.iloc[i,11])
    lmsz=len(lm)
    print "%s(len=%i): " % (d.iloc[i,0], lmsz),
    for r in lm:
        print "%s " % r,
    print
