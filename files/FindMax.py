import csv
chr = csv.reader(open("chlorophyll.csv","rb"))
print "Starting..."
Max = 99999
Maxx = 0
Maxy = 0;
total = 0
for indexstart, row in enumerate(chr):
    for indexcell, cell in enumerate(row):
        if int(float(cell)) < Max and int(float(cell)):# != 99999:
            Max = int(float(cell))
            Maxx = indexcell
            Maxy = indexstart
            
           #print "ahh " + str(ahh) + "  ahhw " + str(ahhw)
print "Max: " + str(Max) + " X: " + str(Maxx) + " Y: " + str(Maxy)
print "DONE"
