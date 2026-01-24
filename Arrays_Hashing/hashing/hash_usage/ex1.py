names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countmap = {}
for name in names:
    if name not in countmap:
        countmap[name] = 1
    else:
        countmap[name] +=1