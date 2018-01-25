#!/usr/bin/env python2
# let's see if I can get pandas to read in an Excel
import sys, regex
from collections import defaultdict
import pandas as pd

argquan=len(sys.argv)
if argquan != 3:
   print "This script requires two argument, query and target file"
   sys.exit(2)


d = pd.read_csv(sys.argv[1], sep='\t')
d2 = pd.read_csv(sys.argv[2], sep='\t')
# always hash the second argument following query - target convention
D2=defaultdict(list)
# d.values will render the meomoize data is arrays of arrays, etc.
# print d.shape # will give you the dimensions ... (12,12) in pathanalysis case
# print "Your tsv has dimension and size %i
# print d.size
# print "%s %s" % (d[0], d[4])
# print d.iloc[0][0]
# print d.iat[0,0]
# christ, finally this works

# OK, now able to grab col0 and col11
# print d.iloc[:,[1,2]]
d2sz=len(d2.iloc[:,1])
for i in xrange(d2sz):
    D2[d2.iloc[i,1]]=[]
    D2[d2.iloc[i,1]].append(d2.iloc[i,0])

D2sz=len(D2)
for k in D2.keys():
    ksz=len(D2[k])
    print "%s(%i): " % (k, ksz),
    for j in D2[k]:
        print "%s " % j,
    print
