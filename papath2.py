#!/usr/bin/env python2
# We concentrate here on genes (by which I mea we hash on them) assumes we shall work on  pathway.txt file which has been converted from Excel.
import sys, regex
from collections import defaultdict
import pandas as pd

argquan=len(sys.argv)
if argquan != 3:
    print "This script requires two arguments: 1 pathway tsv file 2 Target gene tsv"
    sys.exit(2)


d = pd.read_csv(sys.argv[1], sep='\t')

# OK, now able to grab col0 and col11
# print d.iloc[:,[0,11]]
# can convert this into a dict of list
RGX0=regex.compile(r'\/\/')
csz=len(d.iloc[:,11])
D=defaultdict(list)
# print "Length on column 11 is %i" % csz
# for c in d.iloc[:,11]:
print "list of Pathways and implicated genes:"
for i in xrange(csz):
    lm=RGX0.split(d.iloc[i,11])
    lmsz=len(lm)
    for r in lm:
        # append pathway to the hash for the gene
        D[r].append(d.iloc[i,0])

print "Sz of defdict = %i" % len(D)
for k in D.keys():
    print "%s(%i) " % (k, len(D[k])),
print

d2 = pd.read_csv(sys.argv[2], sep='\t')
c2sz=len(d2.iloc[:,2])
print c2sz
for i in xrange(c2sz):
    # if D[d2.iloc[i,1]] is None:
    # possibly a bit useless defdict never None.
    if len(D[d2.iloc[i,1]]) > 0:
        print "%s: " % d2.iloc[i,1],
        for j in D[d2.iloc[i,1]]:
            print "%s " % j,
        print

# print "samp value %s" % d2.iloc[15,1]
